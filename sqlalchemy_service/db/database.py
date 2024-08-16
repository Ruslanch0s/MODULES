from sqlalchemy.ext.asyncio import async_sessionmaker, \
    create_async_engine

from config import pg_cfg

engine = create_async_engine(pg_cfg.uri)
async_engine = async_sessionmaker(
    url=pg_cfg.uri,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)
async_session_factory = async_sessionmaker(engine, expire_on_commit=False)
