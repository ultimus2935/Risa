import discord
from discord.ext import commands

class CogTemplate(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    # Example of a command that is called by the user, in this case the command in discord would be 
    @commands.command()
    async def command(self, ctx, parameter):
        pass # Replace this line with your code
        
    # Example of a command that is run everytimes a certain event occurs, in this case the command will run when a message is sent by anyone
    @commands.Cog.listener()
    async def on_message(self, message):
        pass # Replace with line your code