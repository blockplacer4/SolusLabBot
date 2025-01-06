import ezcord
from appwrite.client import Client
from appwrite.services.databases import Databases

class DatabaseManager:
    def __init__(self, endpoint, project_id, api_key, database_id):
        self.client = Client().set_endpoint(endpoint).set_project(project_id).set_key(api_key)
        self.database_id = database_id
        self.databases = Databases(self.client)

    def create_document(self, collection_id, data, document_id=None):
        return self.databases.create_document(
            database_id=self.database_id,
            collection_id=collection_id,
            document_id=document_id or "unique()",
            data=data
        )

    def get_document(self, collection_id, document_id):
        return self.databases.get_document(
            database_id=self.database_id,
            collection_id=collection_id,
            document_id=document_id
        )

    def update_document(self, collection_id, document_id, data):
        return self.databases.update_document(
            database_id=self.database_id,
            collection_id=collection_id,
            document_id=document_id,
            data=data
        )

    def delete_document(self, collection_id, document_id):
        return self.databases.delete_document(
            database_id=self.database_id,
            collection_id=collection_id,
            document_id=document_id
        )

    def list_documents(self, collection_id, queries=None):
        return self.databases.list_documents(
            database_id=self.database_id,
            collection_id=collection_id,
            queries=queries or []
        )

    def delete_ghost_users(self, user_collection_id, server_collection_id):
        users = self.list_documents(user_collection_id)["documents"]
        servers = self.list_documents(server_collection_id)["documents"]
        for user in users:
            if not any(server["$id"] in user["servers"] for server in servers):
                self.delete_document(user_collection_id, user["$id"])
        new_users = self.list_documents(user_collection_id)["documents"]
        ezcord.log.info(f"Deleted {len(users) - len(new_users)} ghost users")
        return len(new_users)
