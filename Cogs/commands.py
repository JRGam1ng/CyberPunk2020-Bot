import sqlite3
from discord.ext import commands

@commands.command(description = "This is the add stat command, which should be formatted as !addstat (the stat) (Character Name) (Stat Number)")
async def add(ctx, *args):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    arguments = (len(args))
    command = command_lookup[args[0]]
    query = ("SELECT {} FROM character WHERE Character = '{}'".format(command, args[1]))
    cursor.execute(query)
    result = cursor.fetchone()
    if arguments == 3:
        if result[0] is None:
            sql = ("UPDATE character SET ('{}') = ? WHERE Character = '{}'".format(command, args[1]))
            val = (args[2],)
            print(sql)
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
            print('inserting...')
            await ctx.send(f'{args[1]}\'s {args[0]} stat has been set to {args[2]}')
        elif result is not None:
            print (result[0])
            print (args[2])
            add = int(str(result[0])) + int(args[2])
            sql = ("UPDATE character SET '{}' = ? WHERE Character = '{}'".format(command, args[1]))
            val = (add,)
            await ctx.send(f'{args[1]}\'s {args[0]} has been updated to {add}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
            print('inserted')
    if arguments <= 2:
        if result is None:
            sql = ("INSERT INTO character ('{}') VALUES(?)".format(command,))
            val = (args[1],)
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
            await ctx.send(f'{args[1]} has been created.')
        if result is not None:
            await ctx.send(f'{args[1]} already exists.')



command_lookup = {
"character":"character",
"int":"INT",
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
"awareness":"Awareness",
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
"streetdeal":"Streetdeal",
"wallet":"Eurobucks",
"savings":"Alleurobucks",
"ip":"ippoints"}

def setup(client):
   client.add_command(add)