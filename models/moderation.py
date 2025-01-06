from utils import loadenv

MODERATION_COLLECTION_ID = loadenv.moderation_collection_id
LOGGING_COLLECTION_ID = loadenv.logging_collection_id

class Moderation:
    def __init__(self, db_manager, server_id, user_id, action, reason, timestamp, moderator_id, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.user_id = user_id
        self.action = action
        self.reason = reason
        self.timestamp = timestamp
        self.moderator_id = moderator_id
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["user_id"],
            doc["action"],
            doc["reason"],
            doc["timestamp"],
            doc["moderator_id"],
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "user_id": self.user_id,
            "action": self.action,
            "reason": self.reason,
            "timestamp": self.timestamp,
            "moderator_id": self.moderator_id
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(MODERATION_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(MODERATION_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(MODERATION_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(MODERATION_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(MODERATION_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]


class Logging:
    def __init__(self, db_manager, server_id, event_type, details, timestamp, user_id=None, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.event_type = event_type
        self.details = details
        self.timestamp = timestamp
        self.user_id = user_id
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["event_type"],
            doc["details"],
            doc["timestamp"],
            doc.get("user_id"),
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "event_type": self.event_type,
            "details": self.details,
            "timestamp": self.timestamp,
            "user_id": self.user_id
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(LOGGING_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(LOGGING_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(LOGGING_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(LOGGING_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(LOGGING_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]
