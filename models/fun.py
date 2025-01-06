from utils import loadenv

MINIGAMES_COLLECTION_ID = loadenv.minigames_collection_id
MEMEGENERATOR_COLLECTION_ID = loadenv.memegenerator_collection_id
POLLS_COLLECTION_ID = loadenv.polls_collection_id

class MiniGames:
    def __init__(self, db_manager, server_id, game_type, participants, game_state, started_at, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.game_type = game_type
        self.participants = participants
        self.game_state = game_state
        self.started_at = started_at
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["game_type"],
            doc["participants"],
            doc["game_state"],
            doc["started_at"],
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "game_type": self.game_type,
            "participants": self.participants,
            "game_state": self.game_state,
            "started_at": self.started_at
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(MINIGAMES_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(MINIGAMES_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(MINIGAMES_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(MINIGAMES_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(MINIGAMES_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]


class MemeGenerator:
    def __init__(self, db_manager, server_id, template_id, template_url, default_text, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.template_id = template_id
        self.template_url = template_url
        self.default_text = default_text
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["template_id"],
            doc["template_url"],
            doc["default_text"],
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "template_id": self.template_id,
            "template_url": self.template_url,
            "default_text": self.default_text
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(MEMEGENERATOR_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(MEMEGENERATOR_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(MEMEGENERATOR_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(MEMEGENERATOR_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(MEMEGENERATOR_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]


class Polls:
    def __init__(self, db_manager, server_id, question, options, votes, created_at, expires_at, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.question = question
        self.options = options
        self.votes = votes
        self.created_at = created_at
        self.expires_at = expires_at
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["question"],
            doc["options"],
            doc["votes"],
            doc["created_at"],
            doc["expires_at"],
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "question": self.question,
            "options": self.options,
            "votes": self.votes,
            "created_at": self.created_at,
            "expires_at": self.expires_at
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(POLLS_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(POLLS_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(POLLS_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(POLLS_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(POLLS_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]
