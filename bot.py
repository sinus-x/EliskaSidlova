import datetime
import json
import random
import traceback
import asyncio

import discord
from discord.ext import commands

from info import token
from female_names import names as female_names
from female_surnames import surnames as female_surnames
from male_names import names as male_names
from male_surnames import surnames as male_surnames

#

intents = discord.Intents.none()
intents.guilds = True
intents.members = True
intents.messages = True

bot = commands.Bot(
    command_prefix="$",
    help_command=None,
    allowed_mentions=discord.AllowedMentions(roles=False, everyone=False, users=False),
    intents=intents,
)


def log(message: str):
    now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    print(f"{now} | {message}")


@bot.event
async def on_ready():
    log("Ready")


@bot.event
async def on_error(event, *args, **kwargs):
    tb = traceback.format_exc()
    log(tb)


@commands.is_owner()
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Eliška Šídlová",
        description=(
            "The bot provides no feedback, "
            + "it is expected to be run directly from the command line."
        ),
    )
    embed.add_field(
        name="$ping",
        value="Display API latency",
        inline=False,
    )
    embed.add_field(
        name="$rename",
        value="Rename all guild members to random czech name.",
        inline=False,
    )
    embed.add_field(
        name="$restore",
        value="Rename members back to their original names/nicknames.",
        inline=False,
    )
    await ctx.send(embed=embed)


@commands.is_owner()
@bot.command()
async def ping(ctx):
    await ctx.send("pong: **{:.2f} s**".format(bot.latency))


@commands.is_owner()
@bot.command()
async def set_name(ctx, *, name: str):
    await bot.user.edit(username=name)
    log(f"Changed name to {name}.")


@commands.is_owner()
@bot.command()
async def set_avatar(ctx, *, filename: str):
    try:
        with open(filename, "rb") as image:
            await bot.user.edit(avatar=image.read())
            log("Avatar set.")
    except FileNotFoundError:
        log("Avatar file not found.")


@commands.is_owner()
@bot.command()
async def send(ctx, channel: discord.TextChannel, *, text: str):
    log(f"Sending message to #{channel.name}:" + "\n> " + text.replace("\n", "\n> "))
    message = await channel.send(text)
    embed = discord.Embed(
        title=f"Message in #{channel.name}",
        url=message.jump_url,
        description=text,
    )
    await ctx.send(embed=embed)


@commands.is_owner()
@commands.guild_only()
@bot.command()
async def rename(ctx):
    changed = dict()
    members = ctx.guild.members
    for i, member in enumerate(members, 1):
        if member.nick is not None:
            changed[str(member.id)] = member.nick
        if random.randint(0, 1) == 0:
            names = female_names
            surnames = female_surnames
        else:
            names = male_names
            surnames = male_surnames

        name = random.choice(names)
        surname = random.choice(surnames)
        surname = surname[0] + surname[1:].lower()
        log(f"Setting name of {member} to {name} {surname}.")

        try:
            await member.edit(nick=f"{name} {surname}")
        except discord.errors.Forbidden:
            log("> Forbidden, skipping.")

        if i % 20 == 0 and i > 0:
            log(f"> Sleeping five seconds to keep the API happy. {i}/{len(members)}.")
            await asyncio.sleep(5)

    log("Backing up nicknames...")
    with open(f"nickname-backup.{ctx.guild.id}.json", "w") as handle:
        json.dump(changed, handle)
    log("Done.")


@commands.is_owner()
@commands.guild_only()
@bot.command()
async def restore(ctx):
    with open(f"nickname-backup.{ctx.guild.id}.json", "r") as handle:
        changed = json.load(handle)

    members = ctx.guild.members
    for i, member in enumerate(members, 1):
        if str(member.id) in changed.keys():
            nickname = changed[str(member.id)]
            log(f"Resetting name of {member} to {nickname}.")
        else:
            nickname = None
            log(f"Resetting name of {member}.")

        try:
            await member.edit(nick=nickname)
        except discord.errors.Forbidden:
            log("> Forbidden, skipping.")

        if i % 20 == 0 and i > 0:
            log(f"> Sleeping five seconds to keep the API happy. {i}/{len(members)}.")
            await asyncio.sleep(5)
    log("Done.")


#

bot.run(token)
