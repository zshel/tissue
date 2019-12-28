import logging
import os

from provider_helper import ProviderHelper
from tier_helper import TierHelper


logging.basicConfig(level=logging.DEBUG)
config_dir = '{0}{1}config'.format(os.path.dirname(os.getcwd()), os.path.sep)
logging.info(config_dir)
provider_dir = '{0}{1}providers'.format(config_dir, os.path.sep)
tier_dir = '{0}{1}tiers'.format(config_dir, os.path.sep)

provider_helper = ProviderHelper(provider_dir)
tier_helper = TierHelper(tier_dir)

provider_helper.load_providers()

provider_helper.set_current_provider('aws')

tier_helper.load_tiers()

tier_helper.operate_tier('function', provider_helper.current_provider, solo=True)
tier_helper.operate_tier('function', provider_helper.current_provider, solo=True)
