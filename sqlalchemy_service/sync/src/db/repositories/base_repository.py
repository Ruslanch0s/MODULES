from typing import TypeVar, Generic

from db.database import session_factory

TypeModel = TypeVar('TypeModel')


class BaseRepository(Generic[TypeModel]):
    def __init__(self, model: type(TypeModel)):
        self.model = model

    def get(self, id_: int) -> TypeModel | None:
        with session_factory() as session:
            return session.query(self.model).filter(
                self.model.id == id_).first()

    def get_all(self, offset: int = 0, limit: int = 10) -> list[TypeModel]:
        with session_factory() as session:
            return session.query(self.model).offset(offset).limit(limit).all()

    @staticmethod
    def create(obj_in: TypeModel) -> TypeModel:
        with session_factory() as session:
            session.add(obj_in)
            session.commit()
            session.refresh(obj_in)
            return obj_in

    @staticmethod
    def update(db_obj: TypeModel, obj_in: TypeModel) -> TypeModel:
        obj_data = obj_in.dict(exclude_unset=True)
        for key, value in obj_data.items():
            setattr(db_obj, key, value)

        with session_factory() as session:
            session.commit()
            session.refresh(db_obj)
            return db_obj

    def delete(self, id_: int) -> TypeModel:
        with session_factory() as session:
            obj = session.query(self.model).get(id_)
            session.delete(obj)
            session.commit()
            return obj
