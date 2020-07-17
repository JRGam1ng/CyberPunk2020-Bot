import discord
import asyncio
import os
import random
import sqlite3
from discord.ext import commands
from discord.utils import get
import time

client = commands.Bot(command_prefix = '!')
#Database Connection
conn = sqlite3.connect('charinfo.db')
c = conn.cursor()


@client.command()
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f"I have left {channel}")
    else:
        await ctx.send("I'm not in a voice channel Choomba.")


#Start Bot
@client.event
async def on_ready():
    print('Bot is ready.')

#!clear command
@client.command(description="Deletes messages based on number you give it")
async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount)

@client.command(description="Loads extensions")
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Extension has been loaded.')

@client.command(description="Unloads extensions")
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Extension has been unloaded.')


@client.command()
async def roll(ctx, *args):
    try:
        totall = 0
        add = (len(args))
        droll = (args[0].partition("d"))
        amount = int(droll[0])
        sides = int(droll[2])
        rolls_list = []
        fumblecount = 0
        explode = False
        i = 0
        while i < amount:
            dtot = random.randint(1, sides)
            rolls_list.append(dtot)
            totall += dtot
            if dtot == 10 and sides == 10:
                amount += 1
                explode = True
            if dtot == 1 and amount <= 2:
                fumblecount += 1
            i += 1
        print(rolls_list)
        rolls_list.sort()
        if add == 2:
            total = int(totall) + int(args[1])
            await ctx.send(f'Your roll is {totall} + {args[1]} which = {total} {rolls_list}')
        if add != 2:
            await ctx.send("You Rolled a: "+str(totall) + str(rolls_list))
        if explode == True:
            vc = ctx.author.voice.channel
            if vc == None:
                await ctx.send('User is not in a voice channel.')
            if vc != None:
                channel = ctx.author.voice.channel
                await channel.connect()
                ctx.voice_client.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="Insert Sound Clip Here"))
                await ctx.send(f'DICE EXPLOSION!!!! {ctx.message.author}!')
                time.sleep(5)
                await ctx.voice_client.disconnect()
        elif fumblecount != 0:
            vc = ctx.author.voice.channel
            if vc == None:
                await ctx.send('User is not in a voice channel.')
            if vc != None:
                channel = ctx.author.voice.channel
                await channel.connect()
                ctx.voice_client.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="Insert Sound Clip Here"))
                await ctx.send(f'FUMBLE TABLE! FUMBLE TABLE! FUMBLE TABLE! FUMBLE TABLE! FUMBLE TABLE! FUMBLE TABLE! {ctx.message.author} roll a 1d10 to see how bad it is!')
                time.sleep(5)
                await ctx.voice_client.disconnect()
    finally:
        pass


@client.command()
async def skillroll(ctx, *args):
    command = skill_list[args[0]]
    stat = skill_lookup[args[0]]
    try:
        totall = 0
        add = (len(args))
        amount = 1
        sides = 10
        rolls_list = []
        fumblecount = 0
        explode = False
        i = 0
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        query = ("SELECT {} FROM character WHERE Character = '{}'".format(command,args[1]))
        cursor.execute(query)
        result = cursor.fetchone()
        query2 = ("SELECT {} FROM character WHERE Character = '{}'".format(stat,args[1]))
        cursor.execute(query2)
        result2 = cursor.fetchone()
        if result[0] == None:
            res2 = int(str(result2[0]))
            amount = 2
            i = 0
            dtot = random.randint(1, sides)
            rolls_list.append(dtot)
            totall += dtot
            if dtot == 1 and amount <= 3:
                    fumblecount += 1
            dtot = random.randint(1, sides)
            rolls_list.append(dtot)
            totall += dtot
            rolls_list.sort()
            if rolls_list[0] == 1:
                    await ctx.send(f'FUMBLE TABLE.... Please dont be dead, please dont be dead, please do-')
                    fumblecount += 1
            while rolls_list[0] == 10:
                dtot = random.randint(1, sides)
                rolls_list.append(dtot)
                totall += dtot
                amount += 1
                explode = True
                rolls_list.sort()
            totall += res2
            if add == 3:
                total = int(rolls_list[0]) + int(args[2]) + res2
                await ctx.send(f'Your roll is [{rolls_list[0]}] + {args[2]} + {res2} which = {total} :game_die: {rolls_list}')
            if add != 3:
                if len(rolls_list) > 2:
                    total2 = int(totall) - int(res2)
                    await ctx.send("You rolled a " + str(total2) + " + " + str(res2) + " which = " + str(totall) + ":game_die: " + " " + str(rolls_list))
                else:
                    total1 = int(rolls_list[0]) + int(res2)
                    await ctx.send("You Rolled a: ["+ str(rolls_list[0]) + "] + " + str(res2) + " which = " + str(total1) + ":game_die: " + " " + str(rolls_list))
            if explode == True:
                vc = ctx.author.voice.channel
                if vc == None:
                    await ctx.send('User is not in a voice channel.')
                if vc != None:
                    channel = ctx.author.voice.channel
                    await channel.connect()
                    ctx.voice_client.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="Insert Sound Clip Here"))
                    await ctx.send(f'DICE EXPLOSION!!!! {ctx.message.author}!')
                    time.sleep(5)
                    await ctx.voice_client.disconnect()
            if fumblecount != 0:
                print(fumblecount)
                vc = ctx.author.voice.channel
                if vc == None:
                    await ctx.send('User is not in a voice channel.')
                if vc != None:
                    channel = ctx.author.voice.channel
                    await channel.connect()
                    ctx.voice_client.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="Insert Sound Clip Here"))
                    time.sleep(5)
                    await ctx.voice_client.disconnect()
        if result[0] != None:
            i = 0
            res2 = int(str(result2[0]))
            res = int(str(result[0]))
            while i < amount:
                dtot = random.randint(1, sides)
                rolls_list.append(dtot)
                totall += dtot
                if dtot == 10 and sides == 10:
                    amount += 1
                    explode = True
                if dtot == 1 and amount <= 3:
                    fumblecount += 1
                i += 1
            rolls_list.sort()
            if rolls_list[0] == 1:
                await ctx.send(f'FUMBLE TABLE.... Please dont be dead, please dont be dead, please do-')
                fumblecount += 1   
            totall += res
            totall += res2
            if add == 3:
                total = int(totall) + int(args[2])
                await ctx.send(f'Your roll is {rolls_list[0]} + {args[2]} + {res} + {res2} which = {total} :game_die: {rolls_list}')
            if add != 3:
                await ctx.send(f"You rolled a: {rolls_list} + {res} + {res2} = {totall}")
            if explode == True:
                vc = ctx.author.voice.channel
                if vc == None:
                    await ctx.send('User is not in a voice channel.')
                if vc != None:
                    channel = ctx.author.voice.channel
                    await channel.connect()
                    ctx.voice_client.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="Insert Sound Clip Here"))
                    await ctx.send(f'DICE EXPLOSION!!!! {ctx.message.author}!')
                    time.sleep(5)
                    await ctx.voice_client.disconnect()
            if fumblecount != 0:
                vc = ctx.author.voice.channel
                if vc == None:
                    await ctx.send('User is not in a voice channel.')
                if vc != None:
                    channel = ctx.author.voice.channel
                    await channel.connect()
                    ctx.voice_client.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="Insert Sound Clip Here"))
                    time.sleep(5)
                    await ctx.voice_client.disconnect()
    finally:
        pass


#Add current EB count
@client.command(description="Adds/updates your characters' current EuroBuck amount to the database.")
async def addeb(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        query = ("SELECT eurobucks FROM character WHERE Character = '{}'".format(args1))
        # val = (args1,)
        cursor.execute(query)
        result = cursor.fetchone()
        print (f'{result}')
        if result is None or result == 0:
            sql = ("INSERT INTO character 'eurobucks' VALUES(?)")
            val = (args2,)
            print(f'{args1} EuroBucks has been set to {args2}')
        if result is not None:
            sql = ("UPDATE character SET eurobucks = ? WHERE Character = ?")
            add = int(args2) + int(result[0])
            val = (add, args1)
            print(f'{args1} EuroBucks has been updated to {add}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
            print('done')
    finally:
        pass


skill_list = {"int":"INT",
"ref":"REF",
"luck":"LUCK",
"ma":"MA",
"run":"Run",
"leap":"Leap",
"tech":"TECH",
"cool":"COOL",
"attr":"ATTR",
"emp":"EMP",
"humanity":"Humanity",
"cybercost":"CyberCost",
"body":"BODY",
"interface":"Interface",
"accounting":"Accounting",
"anthropology":"Anthropology",
"awareness":"Awarness",
"biology":"Biology",
"botany":"Botany",
"chemistry":"Chemistry",
"composition":"Composition",
"diagnose":"Diagnose_Illness",
"education":"Education",
"expert":"Expert",
"gamble":"Gamble",
"geology":"Geology",
"hide":"Hide",
"history":"History",
"language1":"Language1",
"language2":"Language2",
"language3":"Language3",
"library":"Library_Search",
"math":"Mathematics",
"physics":"Physics",
"programming":"Programming",
"shadow":"Shadow",
"market":"Stock_Market",
"systems":"System_Knowledge",
"teaching":"Teaching",
"survival":"Wilderness_Survival",
"zoology":"Zoology",
"grooming":"Personal_Grooming",
"wardrobe":"Wardrobe",
"endurance":"Endurance",
"strength":"Strength",
"swimming":"Swimming",
"interrogation":"Interrogation",
"intimidate":"Intimidate",
"oratory":"Oratory",
"resist":"Resist_Torture",
"streetwise":"Streetwise",
"perception":"Human_Perception",
"interview":"Interview",
"leadership":"Leadership",
"seduction":"Seduction",
"social":"Social",
"persuasion":"Persuasion",
"perform":"Perform",
"archery":"Archery",
"athletics":"Athletics",
"brawling":"Brawling",
"dance":"Dance",
"dodge":"Dodge",
"driving":"Driving",
"fencing":"Fencing",
"handgun":"Handgun",
"heavy":"Heavy_Weapons",
"martial1":"Martial1",
"martial2":"Martial2",
"martial3":"Martial3",
"melee":"Melee",
"motorcycle":"Motorcycle",
"machinery":"Operate_Hvy_Machinery",
"pilotg":"Pilot_G",
"pilotfw":"Pilot_FW",
"pilotdir":"Pilot_Dir",
"pilotthrust":"Pilot_Thrust",
"rifle":"Rifle",
"stealth":"Stealth",
"smg":"Submachinegun",
"medtech":"MedTech",
"aerotech":"Aero_Tech",
"avtech":"AV_Tech",
"basictech":"Basic_Tech",
"cryotank":"Cryotank_Operation",
"cyberdeck":"Cyberdeck_Design",
"cybertech":"Cybertech",
"demolitions":"Demolitions",
"disguise":"Disguise",
"electronics":"Electronics",
"security":"Electronic_Security",
"firstaid":"First_Aid",
"forgery":"Forgery",
"gyrotech":"Gyro_Tech",
"paint":"Paint",
"photo":"Photo",
"pharmacy":"Pharmacuticals",
"picklock":"Pick_Lock",
"pickpocket":"Pick_Pocket",
"instrument":"Play_Instrument",
"weaponsmith":"Weaponsmith",
"charismatic":"Charismatic_Leadership",
"combatsense":"Combat_Sense",
"credibility":"Credibility",
"family":"Family",
"authority":"Authority",
"juryrig":"Jury_Rig",
"resources":"Resources",
"streetdeal":"Streetdeal"}


skill_lookup = {
"interface":"int",
"accounting":"int",
"anthropology":"int",
"awareness":"int",
"biology":"int",
"botany":"int",
"chemistry":"int",
"composition":"int",
"diagnose":"int",
"education":"int",
"expert":"int",
"gamble":"int",
"geology":"int",
"hide":"int",
"history":"int",
"language1":"int",
"language2":"int",
"language3":"int",
"library":"int",
"math":"int",
"physics":"int",
"programming":"int",
"shadow":"int",
"market":"int",
"systems":"int",
"teaching":"int",
"survival":"int",
"zoology":"int",
"grooming":"attr",
"wardrobe":"attr",
"endurance":"body",
"strength":"body",
"swimming":"body",
"interrogation":"cool",
"intimidate":"cool",
"oratory":"cool",
"resist":"cool",
"streetwise":"cool",
"perception":"emp",
"interview":"emp",
"leadership":"emp",
"seduction":"emp",
"social":"emp",
"persuasion":"emp",
"perform":"emp",
"archery":"ref",
"athletics":"ref",
"brawling":"ref",
"dance":"ref",
"dodge":"ref",
"driving":"ref",
"fencing":"ref",
"handgun":"ref",
"heavy":"ref",
"martial1":"ref",
"martial2":"ref",
"martial3":"ref",
"melee":"ref",
"motorcycle":"ref",
"machinery":"ref",
"pilotg":"ref",
"pilotfw":"ref",
"pilotdir":"ref",
"pilotthrust":"ref",
"rifle":"ref",
"stealth":"ref",
"smg":"ref",
"medtech":"tech",
"aerotech":"tech",
"avtech":"tech",
"basictech":"tech",
"cryotank":"tech",
"cyberdeck":"tech",
"cybertech":"tech",
"demolitions":"tech",
"disguise":"tech",
"electronics":"tech",
"security":"tech",
"firstaid":"tech",
"forgery":"tech",
"gyrotech":"tech",
"paint":"tech",
"photo":"tech",
"pharmacy":"tech",
"picklock":"tech",
"pickpocket":"tech",
"instrument":"tech",
"weaponsmith":"tech",
"charismatic":"cool",
"credibility":"int",
"family":"int",
"authority":"cool",
"resources":"int",
"streetdeal":"cool",
}



extensions = ['cogs.recall', 'cogs.baserolling', 'cogs.commands']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)
client.run('Insert Token Here')