import random
import time
import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")


@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def ping(ctx):
    await ctx.send(f":ping_pong: Pong! {round(client.latency * 1000)} ms!")



@client.command()
async def cool(ctx):
    await ctx.send(":sunglasses: Cool!")

@client.command(aliases=["8ball"])
async def _8ball(ctx, * , question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]

    embed = discord.Embed(title="Question", description=f"{question}",color=0xB03BEF) 
    embed.add_field(name="Answer", value=f"{random.choice(responses)}")
    embed.set_footer(icon_url=ctx.author.avatar_url ,text= f"Requested by: {ctx.author.name}")
    await ctx.send(embed=embed)

@_8ball.error
async def _8ballerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":x: Please input all required parameters!")

@client.command()
async def amazing(ctx):
    embed = discord.Embed(title="Is this cool?", description=":sunglasses:",color=0xEF3B3B)
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@client.command()
async def whois(ctx, member : discord.Member):
    created_at = member.created_at.strftime("%b %d %y")
    embed = discord.Embed(title=f"{member.name}", description="Below is their userinfo!", inline=False,color=0xff1f1f)
    embed.add_field(name="ID", value=f"{member.id}")
    embed.add_field(name="Account creation date:", value= f"{created_at}")
    await ctx.send(embed=embed)

@whois.error
async def whois_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send(f":x: That is not a member of this server!")

f = open("nitrocodes.txt", "r")

@client.command()
async def nitrocodes(ctx):
    ncsending = True
    while ncsending:
        for code in f.readlines():
            await ctx.send(code)
            time.sleep(1)
            f.close()


client.run("NzcwMjcyODI0NDY4MDQ1ODY1.X5bKeA.LMfjjNVTpLJNqFIoZcasmChyJBo")
