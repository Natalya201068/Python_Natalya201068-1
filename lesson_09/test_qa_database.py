from QAdataBase import QAdataBase
import pytest

db = QAdataBase("postgresql://postgres:3725@localhost:5432/QA")


@pytest.fixture
def test_data(db_session):
    title = "Painting"
    new_title = "Philosophy"

    db_session.add_all([title, new_title])
    db_session.commit()

    return {"title": title, "new_title": new_title}


def test_get_subjects():
    db_result = db.get_subjects()
    assert db_result is not None


def test_insert_subject():
    res1 = db.get_subjects()
    title = "Painting"
    db.insert_subject(title)
    res2 = db.get_subjects()
    db.delete_by_title(title)
    assert len(res2) - len(res1) == 1


def test_update_subject():
    title = "Painting"
    new_title = "Philosophy"
    result = db.update_subject(title, new_title)
    db.delete_by_title(new_title)
    assert result is not None
    assert result['subject_title'] == new_title


def test_delete_subject():
    title = "Painting"
    db.insert_subject(title)
    res1 = db.get_subject_by_title(title)
    assert any(s["subject_title"] == title for s in res1)
    db.delete(title)
    res2 = db.get_subject_by_title(title)
    assert not any(s["subject_title"] == title for s in res2)
