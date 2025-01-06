from utils.db_manager import DatabaseManager
from utils import loadenv

async def getdatabase():
    return DatabaseManager(
        endpoint="https://cloud.appwrite.io/v1",
        project_id=loadenv.appwrite_project_id,
        api_key=loadenv.appwrite_api_token,
        database_id=loadenv.appwrite_database_id
    )