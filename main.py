import os
from twitchio.ext import commands

# set up the bot
bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"j20pHey am here to help now!")#am here to help now!


@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    await bot.handle_commands(ctx)

    # await ctx.channel.send(ctx.content)

    if 'hello' in ctx.content.lower():
        await ctx.channel.send(f"Welcome in  @{ctx.author.name}!")

    if 'j20pGG' in ctx.content.lower():
        await ctx.channel.send('j20pGG')

@bot.event
async def event_message(message):

 @bot.event
 async def event_message(message):
     try:
         name = message.tags["display-name"]
         print(name,message.content)
     except TypeError:
         print(message.author,message.content)
     await bot.handle_commands(message)

#async def event_error(self, error, data=None):
    #pass

#async def event_command_error(self, ctx, exc):
    #pass

###########################################

async def event_join(self, user):
    print(f"{user.name} joined.")

async def event_raw_pubsub(self, data):
    print(data)
    await self.channel.send(f"Thanks for subscribing <3 <3 <3!")

@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')

@bot.command(name='archer')
async def test(ctx):
    await ctx.send('Preferred Specialization for Archer is Pinning!')

@bot.command(name='flagbearer')
async def test(ctx):
    await ctx.send('Preferred Specialization for Flag Bearer is Threatening!')

@bot.command(name='rouge')
async def test(ctx):
    await ctx.send('Preferred Specialization for Rouge is Swiftfoot!')

@bot.command(name='tank')
async def test(ctx):
    await ctx.send('Preferred Specialization for Tank is Heavy!')

@bot.command(name='warrior')
async def test(ctx):
    await ctx.send('Preferred Specialization for Warrior is Vengeful!')

@bot.command(name='barb')
async def test(ctx):
    await ctx.send('Specialization for Barbarian is Wild!')

@bot.command(name='bomber')
async def test(ctx):
    await ctx.send('Preferred Specialization for Bomber is Farsight!')

@bot.command(name='buster')
async def test(ctx):
    await ctx.send('Preferred Specialization for Buster is Volatile!')

@bot.command(name='healer')
async def test(ctx):
    await ctx.send('Preferred Specialization for Healer is Invigorating!')

@bot.command(name='paladin')
async def test(ctx):
    await ctx.send('Preferred Specialization for Paladin is Heavy!')

@bot.command(name='berserker')
async def test(ctx):
    await ctx.send('Preferred Specialization for Berserker is Rampaging!')

@bot.command(name='cent')
async def test(ctx):
    await ctx.send('Preferred Specialization for Centurion is Heavy!')

@bot.command(name='FR')
async def test(ctx):
    await ctx.send('Preferred Specialization for Flying Rouge is Focused!')

@bot.command(name='monk')
async def test(ctx):
    await ctx.send('Preferred Specialization for Monk is Martyr!')

@bot.command(name='musk')
async def test(ctx):
    await ctx.send('Preferred Specialization for Musketeer is Sniping!')

@bot.command(name='ron9')
async def test(ctx):
    await ctx.send('watch ur cornhole  @ronmiser11')

@bot.command(name='mgun')
async def test(ctx):
    await ctx.send('Watch out, Anjjo got a massive massage gun!')

@bot.command(name='Anjjo')
async def test(ctx):
    await ctx.send('Anjjo is super big!')

@bot.command(name='anjjo')
async def test(ctx):
    await ctx.send('Anjjo is super big!')

if __name__ == "__main__":
    bot.run()

