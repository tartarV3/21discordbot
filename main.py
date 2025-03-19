import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

lobby = []
games = {}
players = ["player 1", "player 2", "bot"]
n = 0
turn = 0
mode = 1

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def join(ctx):
    global lobby
    if ctx.author not in lobby:
        lobby.append(ctx.author)
        await ctx.send(f"{ctx.author.name} has joined the lobby!")

@bot.command()
async def start_game(ctx):
    global lobby, games
    if len(lobby) >= 2:
        players = lobby[:2]
        lobby = lobby[2:]
        game = Game(players)
        games[game.id] = game
        await game.start(ctx)
    else:
        await ctx.send("Not enough players in the lobby!")

@bot.command()
async def play(ctx, number: int):
    global games
    game = games.get(ctx.channel.id)
    if game:
        await game.play(ctx, number)
    else:
        await ctx.send("No game in progress!")

class Game:
    def __init__(self, players):
        self.players = players
        self.id = players[0].id 
        self.n = 0
        self.turn = 0

    async def start(self, ctx):
        await ctx.send("Loading BionicEngine Assets...")
        await ctx.send("Game started!")

    async def play(self, ctx, number):
        pass

bot.run('YOUR_TOKEN_HERE')
