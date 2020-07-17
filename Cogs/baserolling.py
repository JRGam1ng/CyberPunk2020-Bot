import sqlite3
import random
import math
from discord.ext import commands
from discord.utils import get

@commands.command()
async def rolls(ctx, *args):
    command = cmd_list[args[0]]
    try:
        totall = 0
        add = (len(args))
        droll = (args[2].partition("d"))
        amount = int(droll[0])
        sides = int(droll[2])
        rolls_list = []
        fumblecount = 0
        explode = False
        i = 0
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        query = ("SELECT {} FROM character WHERE Character = '{}'".format(command,args[1]))
        cursor.execute(query)
        result = cursor.fetchone()
        if result[0] == 0 or result[0] == None:
            amount = 2
            i = 0
            dtot = random.randint(1, sides)
            rolls_list.append(dtot)
            totall += dtot
            dtot = random.randint(1, sides)
            rolls_list.append(dtot)
            totall += dtot
            rolls_list.sort()
            if rolls_list[0] == 1:
                    await ctx.send(f'FUMBLE TABLE.... Please dont be dead, please dont be dead, please do-')
            while rolls_list[0] == 10:
                dtot = random.randint(1, sides)
                rolls_list.append(dtot)
                totall += dtot
                amount += 1
                explode = True
                rolls_list.sort()
            if add == 4:
                total = int(rolls_list[0]) + int(args[3])
                await ctx.send(f'Your roll is {rolls_list[0]} + {args[3]} which = {total} {rolls_list}')
            if add != 4:
                if len(rolls_list) > 2:
                    await ctx.send("You Rolled a: "+ str(totall) + " " + str(rolls_list))
                else:
                    await ctx.send("You Rolled a: "+ str(rolls_list[0]) + " " + str(rolls_list))
            if explode == True:
                await ctx.send(f'Dice Explosion! Take all of the numbers!')
        if result[0] != None:
            i = 0
            res = int(str(result[0]))
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
            rolls_list.sort()
            totall += res
            if add == 4:
                total = int(totall) + int(args[3])
                await ctx.send(f'Your roll is {totall} + {args[3]} which = {total} {rolls_list}')
            if add != 4:
                await ctx.send(f"You rolled a: {rolls_list} + {res} = {totall}")
            if explode == True:
                await ctx.send(f'Dice Explosion! Take all of the numbers!')
            if fumblecount != 0:
                await ctx.send(f'FUMBLE TABLE.... Please dont be dead, please dont be dead, please do-')
    finally:
        pass

cmd_list = {"int":"int",
"ref":"REF",
"luck":"LUCK",
"ma":"MA",
"run":"Run",
"leap":"Leap",
"tech":"TECH",
"cool":"COOL",
"attr":"ATTR",
"emp":"EMP",
"human":"Humanity",
"cybcst":"CyberCost",
"body":"BODY",
"inter":"Interface",
"acc":"Accounting",
"anthr":"Anthropology",
"awar":"Awarness",
"bio":"Biology",
"bot":"Botany",
"chem":"Chemistry",
"comp":"Composition",
"diag":"Diagnose_Illness",
"ed":"Education",
"exp":"Expert",
"gamb":"Gamble",
"geo":"Geology",
"hide":"Hide",
"hist":"History",
"lang1":"Language1",
"lang2":"Language2",
"lang3":"Language3",
"libsrch":"Library_Search",
"math":"Mathematics",
"phy":"Physics",
"prog":"Programming",
"shadow":"Shadow",
"stk":"Stock_Market",
"sys":"System_Knowledge",
"teach":"Teaching",
"wild":"Wilderness_Survival",
"zoo":"Zoology",
"pgroom":"Personal_Grooming",
"ward":"Wardrobe",
"end":"Endurance",
"stren":"Strength",
"swim":"Swimming",
"interro":"Interrogation",
"intim":"Intimidate",
"orat":"Oratory",
"resist":"Resist_Torture",
"street":"Streetwise",
"humanp":"Human_Perception",
"interv":"Interview",
"leader":"Leadership",
"sedu":"Seduction",
"social":"Social",
"pers":"Persuasion",
"perf":"Perform",
"arch":"Archery",
"ath":"Athletics",
"brawl":"Brawling",
"dance":"Dance",
"dodge":"Dodge",
"drive":"Driving",
"fence":"Fencing",
"hand":"Handgun",
"hvywp":"Heavy_Weapons",
"mart1":"Martial1",
"mart2":"Martial2",
"mart3":"Martial3",
"melee":"Melee",
"motor":"Motorcycle",
"ophvy":"Operate_Hvy_Machinery",
"pilotg":"Pilot_G",
"pilotfw":"Pilot_FW",
"pilotdir":"Pilot_Dir",
"pilotthr":"Pilot_Thrust",
"rifle":"Rifle",
"stealth":"Stealth",
"subm":"Submachinegun",
"medtech":"MedTech",
"aero":"Aero_Tech",
"avtech":"AV_Tech",
"basic":"Basic_Tech",
"cryoop":"Cryotank_Operation",
"cyberdes":"Cyberdeck_Design",
"cyber":"Cybertech",
"demo":"Demolitions",
"dis":"Disguise",
"elec":"Electronics",
"elecsec":"Electronic_Security",
"first":"First_Aid",
"forg":"Forgery",
"gyro":"Gyro_Tech",
"paint":"Paint",
"photo":"Photo",
"pharma":"Pharmacuticals",
"pickl":"Pick_Lock",
"pickp":"Pick_Pocket",
"play":"Play_Instrument",
"wpsmth":"Weaponsmith",
"charldr":"Charismatic_Leadership",
"comsns":"Combat_Sense",
"cred":"Credibility",
"family":"Family",
"auth":"Authority",
"jury":"Jury_Rig",
"resc":"Resources",
"strtdeal":"Streetdeal"}

def setup(client):
    client.add_command(rolls)