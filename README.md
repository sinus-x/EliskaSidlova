<img title="Eliška Šídlová" alt="Eliška Šídlová" src="avatar.jpg" width="200px" height="200px" style="display:inline-block;border-radius:100%;float:right;margin:0 0 1em 1em;" />

# Eliška Šídlová

Very primitive Discord bot, which was developed over one evening for one-time rename of all users on our server.

[Dostupné česky](README.cs.md)

**How does it work?**

Files `{fe,}male_{sur,}names.py` contain lists of czech names and surnames. For every user, the bot desides wheter it will assign a male or female name and then picks one.

**How to make it work?**

Create new bot on [Discord Developers](https://discord.com/developers), copy its token and ivite it on your server.

Copy this repository:
```bash
git clone git@github.com:sinus-x/EliskaSidlova.git
cd EliskaSidlova
```

Create file `info.py` and insert neccesary information:
```py
token = "my-secret.discord.token"
```

Run the bot with
```bash
python bot.py
```

**Why the name?**

The bot picked it itself when it was run for the first time.

**Data source**

The lists come from Czech republic's Home Office website. Because of the GDPR regulation the data is not available anymore, but the old, 2006 version can be retrieved via the Web Archive.

**License**

[MIT](LICENSE).

Author of the photo/avatar is Christopher Campbell, see the [Unsplash post](https://unsplash.com/photos/rDEOVtE7vOs).
