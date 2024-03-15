import os

import arc
import hikari
from dotenv import load_dotenv

# Welcome to arc!

# Useful links:
# - Documentation: https://arc.hypergonial.com
# - GitHub repository: https://github.com/hypergonial/hikari-arc
# - Discord server to get help: https://discord.gg/hikari

# Load token from '.env' file
load_dotenv()

# Add your bot token to the .env file!
bot = hikari.GatewayBot(os.environ["TOKEN"])

# Initialize arc with the bot:
client = arc.GatewayClient(bot)

# Load the extension from 'src/extensions/example.py'
client.load_extension("src.extensions.example")


@client.include  # Add command to client
@arc.slash_command("hi", "Say hi to someone!")  # Define command
async def hi_slash(
    # The context contains information about the command invocation
    ctx: arc.GatewayContext,
    # To add an option to a command, use the following syntax:
    user: arc.Option[hikari.User, arc.UserParams("The user to say hi to.")],
) -> None:
    await ctx.respond(f"Hey {user.mention}!")


# This must be on the last line, no code will run after this:
bot.run()
