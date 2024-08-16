from sqlalchemy.orm import Query


class Specification:
    def apply(self, query: Query):
        raise NotImplementedError(
            "Метод apply должен быть реализован в подклассе")


class DistinctSpecification(Specification):
    """Уникальные поля"""

    def __init__(self, column):
        self.column = column

    def apply(self, query: Query):
        return query.distinct(self.column)


class OrderBySpecification(Specification):
    def __init__(self, *columns):
        self.columns = columns

    def apply(self, query: Query):
        return query.order_by(*self.columns)


class FilterSpecification(Specification):
    """Example: FilterSpecification(User.age >= 18)"""

    def __init__(self, *conditions):
        self.conditions = conditions

    def apply(self, query: Query):
        return query.filter(*self.conditions)


class OrderBySpecification(Specification):
    """Example: OrderBySpecification(User.age.desc())"""

    def __init__(self, *columns):
        self.columns = columns

    def apply(self, query: Query):
        return query.order_by(*self.columns)


class LimitSpecification(Specification):
    def __init__(self, limit):
        self.limit = limit

    def apply(self, query: Query):
        return query.limit(self.limit)


class OffsetSpecification(Specification):
    def __init__(self, offset):
        self.offset = offset

    def apply(self, query: Query):
        return query.offset(self.offset)


class AndSpecification(Specification):
    def __init__(self, *specifications):
        self.specifications = specifications

    def apply(self, query: Query):
        for spec in self.specifications:
            query = spec.apply(query)
        return query
