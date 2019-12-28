import logging
from typing import List, Dict

from dict_convert import DictionaryConverter
from providers.common_provider import CommonProvider
from tiers.tier_stub import TierStub
from util import Util


class CommonTier(DictionaryConverter):

    name: str
    depends_on: List[str]

    stub_dict: Dict[str, TierStub] = {}

    def operate(self, provider: CommonProvider, operation):
        stub: TierStub = self.stub_dict.get(provider.name)
        if not stub:
            logging.info('gen stub')
            full_class_name = 'tiers.{0}.{1}_tier.{2}TierStub'.format(provider.name, self.name, self.name.capitalize())
            stub = Util.get_class(full_class_name)
            if not stub:
                raise Exception('Was unable to find stub: {0}'.format(full_class_name))
            stub.name = self.name
            stub.provider = provider
            self.stub_dict[provider.name] = stub
        stub.pre_action(stub)
        stub.operate(stub, operation)
        stub.post_action(stub)
