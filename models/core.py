from appwrite.id import ID

from utils import loadenv

SERVER_COLLECTION_ID = loadenv.server_collection_id
USER_COLLECTION_ID = loadenv.user_collection_id
LEVELSYSTEM_COLLECTION_ID = loadenv.levelsystem_collection_id

class Server:
    def __init__(self, db_manager, server_id, name, owner_id, created_at, settings, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.name = name
        self.owner_id = owner_id
        self.created_at = created_at
        self.settings = settings
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["name"],
            doc["owner_id"],
            doc["created_at"],
            doc["settings"],
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "name": self.name,
            "owner_id": self.owner_id,
            "created_at": self.created_at,
            "settings": self.settings
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(SERVER_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            self.doc_id = ID.unique()
            created_doc = self.db_manager.create_document(SERVER_COLLECTION_ID, data, document_id=self.doc_id)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(SERVER_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(SERVER_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(SERVER_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]


class User:
    def __init__(self, db_manager, servers, user_id, username, created_at, profile, doc_id=None):
        self.db_manager = db_manager
        self.user_id = user_id
        self.username = username
        self.created_at = created_at
        self.profile = profile
        self.servers = servers
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["user_id"],
            doc["username"],
            doc["created_at"],
            doc["profile"],
            doc["servers"],
            doc["$id"]
        )

    def to_document(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "created_at": self.created_at,
            "profile": self.profile,
            'servers': self.servers
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(USER_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(USER_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(USER_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(USER_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(USER_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]


class LevelSystem:
    def __init__(self, db_manager, server_id, user_id, xp, level, last_updated, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.user_id = user_id
        self.xp = xp
        self.level = level
        self.last_updated = last_updated
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["user_id"],
            doc["xp"],
            doc["level"],
            doc["last_updated"],
        )