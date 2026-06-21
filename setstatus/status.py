import discord

from redbot.core import commands, app_commands

class Status(commands.Cog):
    """A simple status cog"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    @app_commands.describe(status="The text to set the custom status to")
    async def setstatus(self, interaction: discord.Interaction, status: str):
        """Set a custom status for the bot"""
        await interaction.response.send_message(f"Status set to: {status}", ephemeral=True)

    @commands.command()
    async def pinging(self, ctx):
        """Funner ping command"""
        # Your code will go here
        await ctx.send("Ponging")
