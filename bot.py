import discord
import random
import sqlite3
from discord.ext import commands
client = commands.Bot(command_prefix = '!')
#Database Connection
conn = sqlite3.connect('charinfo.db')

c = conn.cursor()

#Start Bot
@client.event
async def on_ready():
    print('Bot is ready.')
#!clear command
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.group(invoke_without_command=True)
async def addchar(self, ctx):
    await ctx.send('Character Creation Commands: \nwelcome channel <#channel>\nwelcome text <message>')
    
@addchar.command(name='int')
async def _INT(self, ctx, args1, args2):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT int FROM character WHERE 'character name' = {args1}")
    result = cursor.fetchone()
    if result is None:
        sql = ("INSERT INTO character ('Character Name', 'INT') VALUES (?, ?)")
        val = (args1, args2)
        print(f'Character INT has been set to {args2}')
    elif result is not None:
        sql = ("UPDATE character SET int = ? WHERE 'Character Name' = ?")
        val = (args2, args1)
        print(f'Character INT has been updated to {args2}')
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    conn.close()

#def add_user_to_db(args1, args2#):
#    try:
#        conn = sqlite3.connect('charinfo.db#')
#        cursor = conn.cursor()
#        sql = ("INSERT INTO character ('Character Name', 'INT') VALUES (?, ?)")
#        cursor.execute(sql,(args1, args2))
#        conn.commit()
#    finally:
#        pass

#@client.command()
#async def addchar(ctx, args1, args2):
#    add_user_to_db(args1, args2)
#    print("Your character's INT has been added to the database.")

client.run('Njc2NTc3ODA3NzQ0MTA2NTQz.XkMtFw.TcEJhHSI9wwDHegvMyXl1c91h9c')