import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command('help')

TOKEN = "Bling was here."

@bot.command()
@commands.has_permissions(administrator=True)
async def unbanall(ctx):
    async for entry in ctx.guild.bans():
        userID = entry.user.id
        Userobject = await bot.fetch_user(userID)
        reason = entry.reason if entry.reason else "No reason provided"
        await ctx.guild.unban(Userobject)
        await ctx.send(f"**Unbanned:** {Userobject} **|** (ID: {userID}) **|** (Ban Reason: {reason})")
        print(f"Unbanned: {Userobject} (ID: {userID}) | Reason: {reason}")

bot.run(TOKEN)
