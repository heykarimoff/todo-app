import uuid
import datetime

class TodoList:
    def __init__(self, uid: uuid.UUID, name: str) -> None:
        self.uid = uid
        self.name = name


    @classmethod
    def new(cls, name: str):
        uid = uuid.uuid4()
        return cls(uid=uid, name=name)


class ListItem:
    def __init__(self, uid: uuid.UUID, list_uid: uuid.UUID, title: str, notes: str = None, priority: str = None, completed: bool = False, due_at: datetime.datetime = None) -> None:
        self.uid = uid
        self.list_uid = list_uid
        self.title = title
        self.notes = notes
        self.priority = priority
        self.completed = completed
        self.due_at = due_at

    @classmethod
    def new(cls, **kwargs):
        uid = uuid.uuid4()
        return cls(uid=uid, **kwargs)

    def complete(self):
        self.completed = True
