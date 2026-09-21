import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is required; set it in .env before starting FaceCue")
if not SECRET_KEY:
    raise RuntimeError("JWT_SECRET_KEY is required; set it in .env before starting FaceCue")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(
    DATABASE_URL,
    pool_size=10,          # base pool per worker process
    max_overflow=5,        # extra connections under burst load
    pool_timeout=30,       # seconds to wait for a connection before erroring
    pool_recycle=1800,     # recycle connections every 30 min (avoids stale conns)
    pool_pre_ping=True,    # checks connection liveness before use
    echo=False,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,   # avoids re-querying objects after commit
    autoflush=False,
)