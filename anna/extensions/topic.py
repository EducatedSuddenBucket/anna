import random
from nextcord.ext import commands
from extensions.topics_list import topics


class Topic(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def topic(self, ctx: commands.Context):
        """Sends a random topic from the predefined list."""
        random_topic = random.choice(topics)
        await ctx.send(random_topic)


def setup(bot: commands.Bot):
    bot.add_cog(Topic(bot))
