import os
import json
from typing import List

from providers.common_provider import CommonProvider
from tiers.common_tier import CommonTier

OPERATION_RUN = 'run'
OPERATION_UPDATE = 'update'
OPERATION_DELETE = 'delete'


class TierHelper:

    tiers: List[CommonTier] = []

    def __init__(self, tiers_dir):
        self.tiers_dir = tiers_dir

    def load_tiers(self):
        directory = os.fsencode(self.tiers_dir)
        for file in os.listdir(directory):
            with open('{0}{1}{2}'.format(str(directory.decode('utf-8')),
                                         os.path.sep, str(file.decode('utf-8'))), 'r') as opened_file:
                tier: CommonTier = CommonTier(json.load(opened_file))
                self.tiers.append(tier)

    def tier_built(self, tier) -> bool:
        return False

    def tier_updated(self, tier) -> bool:
        return True

    def get_tier(self, tier_name: str) -> CommonTier:
        tier: CommonTier
        for tier in self.tiers:
            if not tier.name or tier.name != tier_name:
                continue
            return tier
        return None

    def operate_tier(self, tier_name: str, provider: CommonProvider, operation=OPERATION_RUN, update_dependencies=False, solo=False):
        tier = self.get_tier(tier_name)
        if tier.depends_on and not solo:
            for dependency_name in tier.depends_on:
                dependency = self.get_tier(dependency_name)
                if not self.tier_built(dependency):
                    self.operate_tier(dependency_name, provider, update_dependencies=update_dependencies)
                    continue
                if self.tier_built(dependency) and not update_dependencies:
                    continue
                if self.tier_built(dependency) and update_dependencies and not self.tier_updated(dependency):
                    self.operate_tier(dependency_name, provider, operation=self.OPERATION_UPDATE, update_dependencies=True)
                    continue
        tier.operate(provider, operation)