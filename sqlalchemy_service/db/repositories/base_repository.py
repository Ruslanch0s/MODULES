from typing import TypeVar, Generic, List, Type

from sqlalchemy import func
from sqlalchemy.future import select

from db.database import async_session_factory
from db.specifications import Specification, FilterSpecification, DistinctSpecification

TypeModel = TypeVar('TypeModel')


class BaseRepository(Generic[TypeModel]):
    def __init__(self, model: Type[TypeModel]):
        self.model = model

    @staticmethod
    def set_specs(query, specs: List[Specification] = None):
        if specs is not None:
            for spec in specs:
                query = spec.apply(query)
        return query

    async def get_some(
            self, fields: list = None, specs: list[Specification] = None
    ) -> list[TypeModel]:
        async with async_session_factory() as session:
            query = select(self.model) if fields is None else select(*fields)
            query = self.set_specs(query, specs)
            result = await session.execute(query)
            return result.scalars().all()

    async def count(self, specs: list[Specification] = None) -> int:
        async with async_session_factory() as session:
            # Применение спецификаций, только Filter
            subquery = self.set_specs(
                select(self.model), [spec for spec in specs if isinstance(
                    spec, (FilterSpecification, DistinctSpecification))]
            )
            query = select(func.count()).select_from(subquery)
            result = await session.execute(query)
            return result.scalar_one()

    async def create(self, obj_in: TypeModel) -> TypeModel:
        async with async_session_factory() as session:
            session.add(obj_in)
            await session.commit()
            await session.refresh(obj_in)
            return obj_in

    async def update(self, db_obj: TypeModel, obj_in: TypeModel) -> TypeModel:
        obj_data = obj_in.dict(exclude_unset=True)
        for key, value in obj_data.items():
            setattr(db_obj, key, value)

        async with async_session_factory() as session:
            await session.commit()
            await session.refresh(db_obj)
            return db_obj

    async def delete(self, id_: int) -> TypeModel:
        async with async_session_factory() as session:
            result = await session.execute(
                select(self.model).where(self.model.id == id_))
            obj = result.scalars().first()
            if obj:
                await session.delete(obj)
                await session.commit()
            return obj
