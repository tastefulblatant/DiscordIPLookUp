import requests, discord, random, datetime
from discord.ext import commands

intents = discord.Intents.all()
intents.typing = True
intents.presences = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    await bot.tree.sync()
    await bot.change_presence(activity=discord.activity.Game(name="IpLookUp"),
                                status=discord.Status.idle)
    print(f"{bot.user.name} is ready!")

@bot.hybrid_command(name="ip")
async def ip(ctx, ip):
    try:
        url = f'http://ip-api.com/json/{ip}'
        response = requests.get(url)
        data = response.json()
        ip = data['query'] 
        city = data['city']
        region = data['region']
        region_name = data['regionName']
        countryname = data['country']
        countrycode = data['countryCode']
        zipcode = data['zip']
        lat = data['lat']
        lon = data['lon']
        cords = lat, lon
        time_zone = data['timezone']
        org = data['org']
        mbed = discord.Embed(
            title=f"IP Info: {ip}", description=f"```IP: {ip}\nCoordinates: {cords}\nCountry: {countryname}\nCity: {city}\nRegion: {region}\nRegion Name: {region_name}\nCountry Code: {countrycode}\nZip Code: {zipcode}\nORG: {org}\nTime Zone: {time_zone}\n```\n [Google Maps](https://www.google.com/maps/search/google+map+{data['lat']},{data['lon']})", color=25 + random.randrange(999999), timestamp=datetime.datetime.utcnow()
        )
        await ctx.send(embed=mbed)
    except Exception as e:
        await ctx.send("Error: " + str(e))

bot.run('YOUR TOKEN')
