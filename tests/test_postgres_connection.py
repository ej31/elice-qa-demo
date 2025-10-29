import os

import pytest
from dotenv import load_dotenv

load_dotenv()

_REQUIRED_KEYS = (
    "POSTGRES_HOST",
    "POSTGRES_PORT",
    "POSTGRES_USER",
    "POSTGRES_PASSWORD",
    "POSTGRES_DB",
)


def _get_connection_params():
    missing = [key for key in _REQUIRED_KEYS if not os.getenv(key)]
    if missing:
        pytest.skip(f"환경변수 부족으로 테스트를 건너뜁니다: {', '.join(missing)}")

    return {
        "host": os.environ["POSTGRES_HOST"],
        "port": int(os.environ["POSTGRES_PORT"]),
        "user": os.environ["POSTGRES_USER"],
        "password": os.environ["POSTGRES_PASSWORD"],
        "dbname": os.environ["POSTGRES_DB"],
    }


def test_postgres_select_one():
    psycopg2 = pytest.importorskip("psycopg2")
    params = _get_connection_params()

    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
            assert cur.fetchone() == (1,)
