from utils import loadenv

FAQSYSTEM_COLLECTION_ID = loadenv.faqsystem_collection_id
KNOWLEDGEBASE_COLLECTION_ID = loadenv.knowledgebase_collection_id
MULTILANGUAGE_COLLECTION_ID = loadenv.multilanguage_collection_id
SCHEDULEDEVENTS_COLLECTION_ID = loadenv.scheduledevents_collection_id

class FAQSystem:
    def __init__(self, db_manager, server_id, question, answer, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.question = question
        self.answer = answer
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["question"],
            doc["answer"],
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "question": self.question,
            "answer": self.answer
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(FAQSYSTEM_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(FAQSYSTEM_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(FAQSYSTEM_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(FAQSYSTEM_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(FAQSYSTEM_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]


class KnowledgeBase:
    def __init__(self, db_manager, server_id, title, content, links, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.title = title
        self.content = content
        self.links = links
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["title"],
            doc["content"],
            doc["links"],
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "title": self.title,
            "content": self.content,
            "links": self.links
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(KNOWLEDGEBASE_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(KNOWLEDGEBASE_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(KNOWLEDGEBASE_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(KNOWLEDGEBASE_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(KNOWLEDGEBASE_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]


class MultiLanguage:
    def __init__(self, db_manager, server_id, language, translations, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.language = language
        self.translations = translations
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["language"],
            doc["translations"],
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "language": self.language,
            "translations": self.translations
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(MULTILANGUAGE_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(MULTILANGUAGE_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(MULTILANGUAGE_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(MULTILANGUAGE_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(MULTILANGUAGE_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]


class ScheduledEvents:
    def __init__(self, db_manager, server_id, event_name, event_description, event_time, channel_id, doc_id=None):
        self.db_manager = db_manager
        self.server_id = server_id
        self.event_name = event_name
        self.event_description = event_description
        self.event_time = event_time
        self.channel_id = channel_id
        self.doc_id = doc_id

    @classmethod
    def from_document(cls, db_manager, doc):
        return cls(
            db_manager,
            doc["server_id"],
            doc["event_name"],
            doc["event_description"],
            doc["event_time"],
            doc["channel_id"],
            doc["$id"]
        )

    def to_document(self):
        return {
            "server_id": self.server_id,
            "event_name": self.event_name,
            "event_description": self.event_description,
            "event_time": self.event_time,
            "channel_id": self.channel_id
        }

    def save(self):
        data = self.to_document()
        if self.doc_id:
            updated_doc = self.db_manager.update_document(SCHEDULEDEVENTS_COLLECTION_ID, self.doc_id, data)
            return self.from_document(self.db_manager, updated_doc)
        else:
            created_doc = self.db_manager.create_document(SCHEDULEDEVENTS_COLLECTION_ID, data)
            return self.from_document(self.db_manager, created_doc)

    def delete(self):
        if self.doc_id:
            return self.db_manager.delete_document(SCHEDULEDEVENTS_COLLECTION_ID, self.doc_id)

    @classmethod
    def get_by_id(cls, db_manager, doc_id):
        doc = db_manager.get_document(SCHEDULEDEVENTS_COLLECTION_ID, doc_id)
        return cls.from_document(db_manager, doc)

    @classmethod
    def list_all(cls, db_manager, queries=None):
        doc_list = db_manager.list_documents(SCHEDULEDEVENTS_COLLECTION_ID, queries)
        return [cls.from_document(db_manager, d) for d in doc_list["documents"]]
