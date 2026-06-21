import discord

from redbot.core import commands, app_commands

class Status(commands.Cog):
    """A simple status cog"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def setstatus(self, interaction: discord.Interaction):
        await interaction.response.send_message("Status set!", ephemeral=True)

    @commands.command()
    async def pinging(self, ctx):
        """Funner ping command"""
        # Your code will go here
        await ctx.send("Ponging")
