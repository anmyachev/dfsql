from dataskillet.sql_parser.base import Statement

LOOKUP_ORDER_DIRECTIONS = {
    0: 'default',
    1: 'ASC',
    2: 'DESC'
}

LOOKUP_NULLS_SORT = {
    0: 'default',
    1: 'NULLS FIRST',
    2: 'NULLS LAST'
}


class OrderBy(Statement):
    def __init__(self, field, direction='default', nulls='default', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field = field
        self.direction = direction
        self.nulls = nulls

    def __str__(self):
        out_str = str(self.field)
        if self.direction != 'default':
            out_str += f' {self.direction}'
        if self.nulls != 'default':
            out_str += f' {self.nulls}'
        return out_str
