from sqlalchemy import desc

from db.models import TransitRecordModel
from db.repositories.base_repository import BaseRepository

from db.specifications import DistinctSpecification, OrderBySpecification, \
    FilterSpecification


class TransitRecordRepository(BaseRepository[TransitRecordModel]):
    def __init__(self):
        super().__init__(model=TransitRecordModel)

    async def get_unique_places(self) -> list[str]:
        return await self.get_some(
            fields=[self.model.place],
            specs=[
                DistinctSpecification(self.model.place),
                OrderBySpecification(desc(self.model.place))
            ])

    async def get_unique_local_places(self, place: str = None) \
            -> list[str | None]:
        return await self.get_some(
            fields=[self.model.local_place],
            specs=[
                DistinctSpecification(self.model.local_place),
                OrderBySpecification(
                    desc(self.model.local_place)
                ),
                FilterSpecification(
                    (self.model.place == place) if place else None
                )
            ])


transit_record_repository = TransitRecordRepository()
