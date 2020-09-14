class Statement:
    def __init__(self, alias=None, raw=None):
        self.alias = alias
        self.raw = raw

    def maybe_add_alias(self, some_str):
        if self.alias:
            return f'{some_str} as {self.alias}'
        else:
            return some_str

    def __str__(self):
        return self.raw
