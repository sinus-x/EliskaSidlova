# Eliška Šídlová

Velmi primitivní Discord bot, kterého jsme vyvinuli pro jednorázové přejmenování všech uživatelů na serveru.

**Jak to funguje?**

Soubory `{fe,}male_{sur,}names.py` obsahují seznamy českých jmen a příjmení. Pro každého uživatele se bot rozhodne, zda dostane mužské či ženské jméno a takové mu přiřadí.

**Jak to zprovoznit?**

Na [Discord Developers](https://discord.com/developers) vytvořte nového bota, pozvěte ho na svůj server a zkopírujte si token.

Zkopírujte repozitář:
```bash
git clone https://.git
```

Vytvořte soubor `info.py` a do něj token vložte ve formátu
```py
token = "my-secret.discord.token"
```

Spusťte ho
```bash
python bot.py
```

**Proč to jméno?**

Takové si bot vybral pro sebe při prvním spuštění.

**Zdroj dat**

Seznam jmen a příjmení pochází z webu Ministerstva vnitra České republiky. Kvůli nařízení GDPR o ochraně osobních údajů již data nejsou k dispozici, stále se k nim jde ale dostat přes WebArchive.

**Licence**

¯\\\_(ツ)\_/¯

Autorem fotografie/avataru je Christopher Campbell, viz [Unsplash](https://unsplash.com/photos/rDEOVtE7vOs).
