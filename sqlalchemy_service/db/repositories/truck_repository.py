from db.database import async_session_factory
from db.models import TruckModel
from db.repositories.base_repository import BaseRepository


class TruckRepository(BaseRepository[TruckModel]):
    def __init__(self):
        super().__init__(model=TruckModel)

    def get_truck_by_marker_id_1(self, marker_id_1: str) -> TruckModel | None:
        with async_session_factory() as session:
            return session.query(self.model).filter(
                self.model.marker_id_1 == marker_id_1
            ).first()


truck_repository = TruckRepository()
