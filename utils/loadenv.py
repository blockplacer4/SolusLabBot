from dotenv import load_dotenv
import os

load_dotenv()

# Tokens and IDs from .env file
discord_bot_token = os.getenv("DISCORD_BOT_TOKEN")

appwrite_api_token = os.getenv("APPWRITE_API_TOKEN")
appwrite_project_id = os.getenv("APPWRITE_PROJECT_ID")
appwrite_database_id = os.getenv("APPWRITE_DATABASE_ID")

# Collection IDs from .env file
server_collection_id = os.getenv("SERVERS_COLLECTION_ID")
moderation_collection_id = os.getenv("MODERATION_COLLECTION_ID")
logging_collection_id = os.getenv("LOGGING_COLLECTION_ID")
levelsystem_collection_id = os.getenv("LEVELSYSTEM_COLLECTION_ID")
reactionroles_collection_id = os.getenv("REACTIONROLES_COLLECTION_ID")
autowelcome_collection_id = os.getenv("AUTOWELCOME_COLLECTION_ID")
reminders_collection_id = os.getenv("REMINDERS_COLLECTION_ID")
autoresponses_collection_id = os.getenv("AUTORESPONSES_COLLECTION_ID")
minigames_collection_id = os.getenv("MINIGAMES_COLLECTION_ID")
memegenerator_collection_id = os.getenv("MEMEGENERATOR_COLLECTION_ID")
soundboard_collection_id = os.getenv("SOUNDBOARD_COLLECTION_ID")
customcommands_collection_id = os.getenv("CUSTOMCOMMANDS_COLLECTION_ID")
polls_collection_id = os.getenv("POLLS_COLLECTION_ID")
rolemanagement_collection_id = os.getenv("ROLEMANAGEMENT_COLLECTION_ID")
faqsystem_collection_id = os.getenv("FAQSYSTEM_COLLECTION_ID")
studyrooms_collection_id = os.getenv("STUDYROOMS_COLLECTION_ID")
knowledgebase_collection_id = os.getenv("KNOWLEDGEBASE_COLLECTION_ID")
scheduledevents_collection_id = os.getenv("SCHEDULEDEVENTS_COLLECTION_ID")
multilanguage_collection_id = os.getenv("MULTILANGUAGE_COLLECTION_ID")
permissions_collection_id = os.getenv("PERMISSIONS_COLLECTION_ID")
user_collection_id = os.getenv("USERS_COLLECTION_ID")
