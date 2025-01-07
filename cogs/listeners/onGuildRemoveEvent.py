import discord
import ezcord
from appwrite.query import Query

import utils.loadenv
from appwrite.id import ID
from discord.ext import commands
from models.core import Server, User
from services.loaddatabase import getdatabase

class OnGuildRemoveEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_manager = None

    @commands.Cog.listener()
    async def on_ready(self):
        self.db_manager = await getdatabase()
        ezcord.log.info("Cog - onGuildRemoveEvent - Database loaded")


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        ezcord.log.info(f"Removing server {guild.id} from database")
        query = Query.equal("server_id", str(guild.id))
        server = Server.from_document(self.db_manager, self.db_manager.list_documents(utils.loadenv.server_collection_id, [query])["documents"][0])
        server.delete()

        # einfach useless, passiert sowieso xd
        # members = self.db_manager.list_documents(utils.loadenv.user_collection_id, Query.contains("servers", server.doc_id))["documents"]
        # ezcord.log.info(f"Removing server {server['name']} from {len(members)} members")
        # for member in members:
        #     member["servers"].remove(server[server.doc_id])
        #     self.db_manager.update_document(utils.loadenv.user_collection_id, member.doc_id, member)

        self.db_manager.delete_ghost_users(utils.loadenv.user_collection_id, utils.loadenv.server_collection_id)


def setup(bot):
    bot.add_cog(OnGuildRemoveEvent(bot))