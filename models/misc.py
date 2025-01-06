from utils import loadenv

AUTOWELCOME_COLLECTION_ID = loadenv.autowelcome_collection_id
REMINDERS_COLLECTION_ID = loadenv.reminders_collection_id
STUDYROOMS_COLLECTION_ID = loadenv.studyrooms_collection_id
AUTORESPONSES_COLLECTION_ID = loadenv.autoresponses_collection_id

class AutoWelcome:
    def __init__(self, db_manager, server_id, welcome_channel_id, welcome_message, welcome_role_id=None, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.welcome_channel_id = welcome_channel_id
        self.welcome_message = welcome_message
        self.welcome_role_id = welcome_role_id
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["welcome_channel_id"],
            doc["welcome_message"],
            doc.get("welcome_role_id"),
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "welcome_channel_id": self.welcome_channel_id,
            "welcome_message": self.welcome_message,
            "welcome_role_id": self.welcome_role_id
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(AUTOWELCOME_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(AUTOWELCOME_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(AUTOWELCOME_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(AUTOWELCOME_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(AUTOWELCOME_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]


class Reminders:
    def __init__(self, db_manager, server_id, user_id, message, reminder_time, created_at, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.user_id = user_id
        self.message = message
        self.reminder_time = reminder_time
        self.created_at = created_at
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["user_id"],
            doc["message"],
            doc["reminder_time"],
            doc["created_at"],
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "user_id": self.user_id,
            "message": self.message,
            "reminder_time": self.reminder_time,
            "created_at": self.created_at
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(REMINDERS_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(REMINDERS_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(REMINDERS_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(REMINDERS_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(REMINDERS_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]


class AutoResponses:
    def __init__(self, db_manager, server_id, trigger, response, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.trigger = trigger
        self.response = response
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["trigger"],
            doc["response"],
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "trigger": self.trigger,
            "response": self.response
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(AUTORESPONSES_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(AUTORESPONSES_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(AUTORESPONSES_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(AUTORESPONSES_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(AUTORESPONSES_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]


class StudyRooms:
    def __init__(self, db_manager, server_id, room_name, channel_id, participants, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.room_name = room_name
        self.channel_id = channel_id
        self.participants = participants
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["room_name"],
            doc["channel_id"],
            doc["participants"],
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "room_name": self.room_name,
            "channel_id": self.channel_id,
            "participants": self.participants
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(STUDYROOMS_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(STUDYROOMS_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(STUDYROOMS_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(STUDYROOMS_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(STUDYROOMS_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]
