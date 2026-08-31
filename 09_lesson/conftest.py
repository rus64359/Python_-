import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Student

# ── Настройки подключения ─────────────────────────────────────
DB_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"

@pytest.fixture(scope="session")
def engine():
    """Создаёт движок SQLAlchemy (одно подключение на всю сессию тестов)."""
    eng = create_engine(DB_URL, echo=False)
    yield eng
    eng.dispose()

@pytest.fixture
def db_session(engine):
    """
    Создаёт свежую сессию для каждого теста.
    После теста откатывает незакоммиченные изменения и закрывает сессию.
    Дополнительно — удаляет все тестовые записи (name начинается с 'TEST_'),
    чтобы гарантировать чистоту даже если предыдущий запуск упал.
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

 # Очистка: удаляем все тестовые записи
    session.query(Student).filter(Student.name.like("TEST_%")).delete(
        synchronize_session=False
    )
    session.commit()
    session.close()