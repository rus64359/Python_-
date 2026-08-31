import pytest
from models import Student

# ──────────────────────────────────────────────────────────────
# CREATE — добавление студента
# ──────────────────────────────────────────────────────────────

class TestCreateStudent:

    def test_create_student_positive(self, db_session):
         """Позитивный: добавляем студента и проверяем, что он записан в БД."""
         student = Student( name="TEST_Ivan Petrov",
            email="test_ivan@example.com",
            group_name="A-101",
            note="Created by pytest",
         )
         db_session.add(student)
         db_session.commit()

# Перезачитываем из БД
         db_session.refresh(student)

         assert student.id is not None, "ID не присвоен — запись не сохранена"
         assert student.name == "TEST_Ivan Petrov"
         assert student.email == "test_ivan@example.com"

# Проверяем, что запись реально в БД
         found = (
            db_session.query(Student)
            .filter(Student.id == student.id)
            .one_or_none()
        )
         assert found is not None, "Запись не найдена в БД после commit"
         assert found.name == "TEST_Ivan Petrov"

    def test_create_student_negative_duplicate_email(self, db_session):
        """Негативный: два студента с одинаковым email — нарушение уникальности."""
        first = Student(
            name="TEST_Dup First",
            email="test_dup@example.com",
        )
        db_session.add(first)
        db_session.commit()

        second = Student(
            name="TEST_Dup Second",
            email="test_dup@example.com", # тот же email
        )
        db_session.add(second)

        with pytest.raises(Exception):
            db_session.commit()

        db_session.rollback() # откатываем проваленную транзакцию

# ──────────────────────────────────────────────────────────────
# UPDATE — изменение студента
# ──────────────────────────────────────────────────────────────

class TestUpdateStudent:

     def test_update_student_positive(self, db_session):
        """Позитивный: создаём студента, меняем name, проверяем обновление."""
        student = Student(
            name="TEST_Update Me",
            email="test_update@example.com",
            group_name="B-202",
        )
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)

        original_id = student.id

 # Меняем имя
        student.name = "TEST_Updated Name"
        db_session.commit()
        db_session.refresh(student)

        assert student.id == original_id
        assert student.name == "TEST_Updated Name"

# Проверяем через свежий запрос
        updated = (
            db_session.query(Student)
            .filter(Student.id == original_id)
            .one()
        )
        assert updated.name == "TEST_Updated Name"

     def test_update_student_negative_nonexistent(self, db_session):
        """Негативный: пытаемся обновить несуществующую запись."""
 # Пытаемся найти запись с несуществующим ID
        nonexistent = (
            db_session.query(Student)
            .filter(Student.id == 999999)
            .one_or_none()
        )
        assert nonexistent is None, "Запись с ID 999999 не должна существовать"

# ──────────────────────────────────────────────────────────────
# DELETE — удаление студента
# ──────────────────────────────────────────────────────────────

class TestDeleteStudent:

    def test_delete_student_positive(self, db_session):
        """Позитивный: создаём студента, удаляем, проверяем, что его нет."""
        student = Student(
            name="TEST_Delete Me",
            email="test_delete@example.com",
        )
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)

        deleted_id = student.id

 # Удаляем
        db_session.delete(student)
        db_session.commit()

 # Проверяем, что записи больше нет
        found = (
            db_session.query(Student)
            .filter(Student.id == deleted_id)
            .one_or_none()
        )
        assert found is None, "Запись всё ещё в БД после удаления"

    def test_delete_student_negative_already_deleted(self, db_session):
        """Негативный: пытаемся удалить уже удалённую запись."""
        student = Student(
            name="TEST_Twice Delete",
            email="test_twice@example.com",
        )
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)

 # Первое удаление
        db_session.delete(student)
        db_session.commit()

# Второе удаление того же объекта — не должно падать,
# но и не должно ничего удалить
        try:
            db_session.delete(student)
            db_session.commit()
        except Exception:
        # SQLAlchemy может выбросить исключение при повторном delete
            db_session.rollback()

 # Главное — записи нет в БД
        found = (
            db_session.query(Student)
            .filter(Student.name == "TEST_Twice Delete")
            .one_or_none()
        )
        assert found is None