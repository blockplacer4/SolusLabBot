from utils import loadenv

REACTIONROLES_COLLECTION_ID = loadenv.reactionroles_collection_id
ROLEMANAGEMENT_COLLECTION_ID = loadenv.rolemanagement_collection_id
PERMISSIONS_COLLECTION_ID = loadenv.permissions_collection_id

class ReactionRoles:
    def __init__(self, db_manager, server_id, message_id, role_id, emoji, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.message_id = message_id
        self.role_id = role_id
        self.emoji = emoji
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["message_id"],
            doc["role_id"],
            doc["emoji"],
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "message_id": self.message_id,
            "role_id": self.role_id,
            "emoji": self.emoji
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(REACTIONROLES_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(REACTIONROLES_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(REACTIONROLES_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(REACTIONROLES_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(REACTIONROLES_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]


class RoleManagement:
    def __init__(self, db_manager, server_id, role_id, user_id, assigned_at, expires_at=None, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.role_id = role_id
        self.user_id = user_id
        self.assigned_at = assigned_at
        self.expires_at = expires_at
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["role_id"],
            doc["user_id"],
            doc["assigned_at"],
            doc.get("expires_at"),
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "role_id": self.role_id,
            "user_id": self.user_id,
            "assigned_at": self.assigned_at,
            "expires_at": self.expires_at
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(ROLEMANAGEMENT_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(ROLEMANAGEMENT_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(ROLEMANAGEMENT_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(ROLEMANAGEMENT_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(ROLEMANAGEMENT_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]


class Permissions:
    def __init__(self, db_manager, server_id, role_id, permissions, user_id=None, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.role_id = role_id
        self.permissions = permissions
        self.user_id = user_id
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["role_id"],
            doc["permissions"],
            doc.get("user_id"),
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "role_id": self.role_id,
            "permissions": self.permissions,
            "user_id": self.user_id
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(PERMISSIONS_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(PERMISSIONS_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(PERMISSIONS_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(PERMISSIONS_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(PERMISSIONS_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]
