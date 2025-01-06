from appwrite.client import Client
from appwrite.services.databases import Databases

import utils.loadenv

# Execute this just one time to get the collection IDs, YOU UNDERSTAND LUKAS? JUST ONE TIME!

def export_collections_as_env(endpoint, project_id, api_key, database_id):
    client = Client()
    client.set_endpoint(endpoint)
    client.set_project(project_id)
    client.set_key(api_key)

    db = Databases(client)

    collections = db.list_collections(database_id=database_id)

    env_lines = []
    for collection in collections["collections"]:
        name = collection["name"]
        coll_id = collection["$id"]
        env_key = name.upper().replace(" ", "_") + "_COLLECTION_ID"
        env_line = f"{env_key}={coll_id}"
        env_lines.append(env_line)

    return "\n".join(env_lines)


if __name__ == "__main__":
    APPWRITE_ENDPOINT = "https://cloud.appwrite.io/v1"
    APPWRITE_PROJECT_ID = utils.loadenv.appwrite_project_id
    APPWRITE_API_KEY = utils.loadenv.appwrite_api_token
    APPWRITE_DATABASE_ID = utils.loadenv.appwrite_database_id

    result = export_collections_as_env(
        endpoint=APPWRITE_ENDPOINT,
        project_id=APPWRITE_PROJECT_ID,
        api_key=APPWRITE_API_KEY,
        database_id=APPWRITE_DATABASE_ID
    )
    with open('../.env', 'a') as file:
        file.write("\n")
        file.write("# All the collection IDs\n")
        file.write("\n")
        file.write(result)
