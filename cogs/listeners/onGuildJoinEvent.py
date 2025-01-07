import discord
import ezcord
import utils
from discord.ext import commands
from models.core import Server, User
from services.loaddatabase import getdatabase

class OnGuildJoinEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_manager = None

    @commands.Cog.listener()
    async def on_ready(self):
        self.db_manager = await getdatabase()
        ezcord.log.info("Cog - onGuildJoinEvent - Database loaded")


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        server = Server(
            db_manager=self.db_manager,
            server_id=str(guild.id),
            name=guild.name,
            owner_id=str(guild.owner_id),
            created_at=guild.created_at.isoformat(),
            settings=[]
        )
        server.save()
        for member in guild.members:
            if member.bot:
                continue
            user = User(
                db_manager=self.db_manager,
                servers=[server.doc_id],
                user_id=str(member.id),
                username=member.name,
                created_at=member.created_at.isoformat(),
                profile=[]
            )
            user.save()

        self.db_manager.delete_ghost_users(utils.loadenv.user_collection_id, utils.loadenv.server_collection_id)

def setup(bot):
    bot.add_cog(OnGuildJoinEvent(bot))