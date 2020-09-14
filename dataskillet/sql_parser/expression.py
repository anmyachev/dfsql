from dataskillet.sql_parser.base import Statement


class Expression(Statement):
    def __init__(self, value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.value = value

    def __str__(self):
        return self.maybe_add_alias(str(self.value))


class Star(Expression):
    def __init__(self, *args, **kwargs):
        super().__init__(value='*', *args, **kwargs)

    def __str__(self):
        # Can't alias a star
        return self.value
