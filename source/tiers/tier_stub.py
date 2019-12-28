from providers.common_provider import CommonProvider


class TierStub:

    name: str
    provider: CommonProvider

    def pre_action(self):
        pass

    def operate(self, operation: str):
        pass

    def post_action(self):
        pass
