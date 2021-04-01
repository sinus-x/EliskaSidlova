<img title="Eliška Šídlová" alt="Eliška Šídlová" src="avatar.jpg" width="200px" height="200px" style="display:inline-block;border-radius:100%;float:right;margin:0 0 1em 1em;" />

# Eliška Šídlová

Velmi primitivní Discord bot, kterého jsme vyvinuli pro jednorázové přejmenování všech uživatelů na serveru.

[Read in English](README.md)

**Jak to funguje?**

Soubory `{fe,}male_{sur,}names.py` obsahují seznamy českých jmen a příjmení. Pro každého uživatele se bot rozhodne, zda dostane mužské či ženské jméno a jedno mu přiřadí.

**Jak to zprovoznit?**

Na [Discord Developers](https://discord.com/developers) vytvořte nového bota, zkopírujte jeho token a pozvěte ho na svůj server. *Roli přesuňte zcela nahoru, bez toho nebude mít oprávnění a nikdo přejmenován nebude.*

```bash
# naklonování repozitáře
git clone git@github.com:sinus-x/EliskaSidlova.git
cd EliskaSidlova
# vytvoření venv prostředí; volitelné, ale doporučené
python3 -m venv .venv
source .venv/bin/activate
# nainstalování potřebných balíčků
python3 -m pip install -r requirements.txt
```

Vytvořte soubor `info.py` a do něj token vložte ve formátu
```py
token = "my.secret.discord.token"
```

Bota spusťte pomocí
```bash
python bot.py
```

**Příkazy**

| příkaz   | popis                              |
|----------|------------------------------------|
| $help    | zobrazení nápovědy                 |
| $ping    | zobrazení API latence              |
| $send #channel {text} | poslání textu do zadaného kanálu |
| $rename  | změna přezdívek všech uživatelů    |
| $restore | vrácení jmen a přezdívek uživatelů |

Změna jmen nějakou dobu trvá, naše rychlost byla zhruba 56 uživatelů za minutu.

**Proč to jméno?**

Takové si bot vybral pro sebe při prvním spuštění.

**Zdroj dat**

Seznam jmen a příjmení pochází z webu Ministerstva vnitra České republiky. Kvůli nařízení GDPR o ochraně osobních údajů již data nejsou k dispozici, stále se k nim jde ale dostat přes Web Archive.

**Licence**

[MIT](LICENSE).

Autorem fotografie/avataru je Christopher Campbell, viz [příspěvěk na Unsplash](https://unsplash.com/photos/rDEOVtE7vOs).
