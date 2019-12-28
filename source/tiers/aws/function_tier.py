import logging

from providers.aws_provider import AwsProvider
from tiers.tier_stub import TierStub


class FunctionTierStub(TierStub):

    def pre_action(self):
        logging.info('[{0}] pre'.format(self.name))

    def operate(self, operation: str):
        logging.info('[{0}] operate: {1}'.format(self.name, operation))

    def post_action(self):
        logging.info('[{0}] post'.format(self.name))