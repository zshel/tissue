import json
import logging
import os
from typing import List

from providers.common_provider import CommonProvider


class ProviderHelper:

    providers: List[CommonProvider] = []

    current_provider: CommonProvider = None

    def __init__(self, providers_dir: str):
        self.providers_dir = providers_dir

    def load_providers(self):
        directory = os.fsencode(self.providers_dir)
        for file in os.listdir(directory):
            logging.info(file)
            with open('{0}{1}{2}'.format(str(directory.decode('utf-8')),
                                         os.path.sep, str(file.decode('utf-8'))), 'r') as opened_file:
                provider: CommonProvider = CommonProvider(json.load(opened_file))
                self.providers.append(provider)

    def set_current_provider(self, provider_name):
        self.current_provider = self.get_provider(provider_name)

    def get_provider(self, provider_name) -> CommonProvider:
        for provider in self.providers:
            name = provider.name
            if not name or name != provider_name:
                continue
            return provider
        return None

