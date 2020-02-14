import sqlite3
from discord.ext import commands


def add_user_to_db(args1):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("INSERT INTO character ('Character Name') VALUES (?)")
        cursor.execute(sql, (args1,))
        conn.commit()
    finally:
        pass

@commands.command()
async def addchar(ctx, args1):
    add_user_to_db(args1)
    await ctx.send("Your character has been added to the database.")


def add_int_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT int FROM character WHERE 'Character Name'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO character ('INT') WHERE EXISTS(SELECT ? FROM character WHERE int = ?")
            val = (args2, args1)
            print(f'{args1} INT has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET int = ? WHERE 'Character Name' = ? ")
            val = (args2, args1)
            print(f'{args1} INT has been updated to {args2}')
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()
    finally:
        pass

@commands.command()
async def addint(ctx, args1, args2):
    add_int_to_db(args1, args2)




def setup(client):
   client.add_command(addchar)
   client.add_command(addint)