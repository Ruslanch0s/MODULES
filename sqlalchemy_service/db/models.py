import enum
import uuid

from sqlalchemy import Column, String, TIMESTAMP, Index, Boolean, \
    Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class TruckModel(Base):
    __tablename__ = 'trucks'
    __table_args__ = (
        Index('truck_markers_idx', 'marker_id_1', 'marker_id_2', unique=True),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    truck_num = Column(String(100), nullable=False, unique=True)
    marker_id_1 = Column(String(100), nullable=False, unique=True)
    marker_id_2 = Column(String(100), nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    transit_records = relationship("TransitRecordModel",
                                   back_populates="trucks")


class TransitRecordStatus(enum.Enum):
    success = "success"
    marker_1_missing = "marker 1 missing"
    marker_2_missing = "marker 2 missing"
    order_mixed = "order mixed"
    marker_1_not_exist = "marker 1 not exist"
    marker_2_not_exist = "marker 2 not exist"
    wait_2_tag = "wait 2 tag"


class TransitRecordModel(Base):
    __tablename__ = 'transit_records'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    truck_num = Column(String(100), ForeignKey('trucks.truck_num'),
                       nullable=True)
    marker_id_1 = Column(String(100), nullable=True)
    marker_id_2 = Column(String(100), nullable=True)
    place = Column(String(100), nullable=False)
    local_place = Column(String(100), nullable=True)
    read_time = Column(TIMESTAMP(timezone=True))
    status = Column(Enum(TransitRecordStatus))
    # detail = Column(String(256), nullable=True)
    used = Column(Boolean(), default=False)

    trucks = relationship("TruckModel", back_populates="transit_records")
