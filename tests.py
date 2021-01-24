import pytest

import uuid
import model
import datetime

today = datetime.datetime.now()


@pytest.fixture
def todo_list():
    return model.TodoList.new(name="Some important list")


@pytest.fixture
def item_1(todo_list):
    item = model.ListItem.new(list_uid=todo_list.uid, title="Item 1", notes="Some note.", priority="High", due_at=today)

    return item


@pytest.fixture
def item_2(todo_list):
    item = model.ListItem.new(list_uid=todo_list.uid, title="Item 2", notes="Some note.", priority="Medium", due_at=today)

    return item


@pytest.fixture
def item_3(todo_list):
    item = model.ListItem.new(list_uid=todo_list.uid, title="Item 3", notes="Some note.", priority="Low", due_at=today)

    return item


def test_create_new_todo_list():
    my_list = model.TodoList.new(name="Some important list")

    assert isinstance(my_list.uid, uuid.UUID)
    assert my_list.name == "Some important list"


def test_add_new_item_to_list(todo_list, item_1):
    assert isinstance(item_1.uid, uuid.UUID)
    assert item_1.list_uid == todo_list.uid
    assert item_1.title == "Item 1"
    assert item_1.notes == "Some note."
    assert item_1.priority == "High"
    assert not item_1.completed
    assert item_1.due_at == today


def test_mark_item_completed(item_1):
    item_1.complete()

    assert item_1.completed


def test_items_sorted_by_priority(item_1, item_2, item_3):
    unsorted = [item_3, item_2, item_1]
    
    sorted(unsorted)

    assert unsorted == [item_1, item_2, item_3]