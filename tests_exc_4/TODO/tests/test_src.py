import pytest
from src import todos, add_todo, remove_todo, edit_todo, remove_all


def test_add_todo():
    add_todo("Go to bed")
    assert todos[-1] == "Go to bed"


def test_remove_todo():
    add_todo("Go to bed")
    remove_todo(0)
    assert "Go to bed" not in todos


def test_edit_todo():
    add_todo("Go to bed")
    edit_todo(0, "Get up from bed")
    assert todos[0] == "Get up from bed"


def test_remove_all():
    add_todo("Go to bed")
    add_todo("Tske a nap")
    remove_all()
    assert len(todos) == 0


def test_check_pos_no_todos():
    todos.clear()
    with pytest.raises(Exception, match="No more todos"):
        check_pos(0)


def test_check_pos_invalid_pos():
    with pytest.raises(Exception, match="No such item nb"):
        check_pos(10)

        