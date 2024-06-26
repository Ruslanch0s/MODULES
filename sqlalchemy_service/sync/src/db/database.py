from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from config import pg_cfg

engine = create_engine(pg_cfg.uri)
SessionLocal = sessionmaker(engine)

sync_engine = create_engine(
    url=pg_cfg.uri,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)

# async_engine = create_async_engine(
#     url=pg_cfg.uri,
#     echo=True,
# )

session_factory = sessionmaker(sync_engine)
# async_session_factory = async_sessionmaker(async_engine)
