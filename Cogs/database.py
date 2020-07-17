import sqlite3
from discord.ext import commands

#Add Character
def add_user_to_db(args1):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("INSERT INTO character ('Character') VALUES (?)")
        cursor.execute(sql, (args1,))
        conn.commit()
    finally:
        pass

@commands.command(description="Adds your character to the database.")
async def addchar(ctx, args1):
    add_user_to_db(args1)
    await ctx.send(f'{args1} has been added to the database.')

#Add Intelligence
def add_int_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT int FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'INT' VALUES(?)")
            val = (args2,)
            print(f'{args1} INT has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET INT = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} INT has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's Intelligence stat to the database.")
async def addint(ctx, args1, args2):
    add_int_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Intelligence is now {args2}')

#Add Reflex
def add_ref_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT ref FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'REF' VALUES(?)")
            val = (args2,)
            print(f'{args1} REF has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET REF = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} REF has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's Reflex stat to the database.")
async def addref(ctx, args1, args2):
    add_ref_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Reflex is now {args2}')

#Add Luck
def add_luck_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT luck FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'luck' VALUES(?)")
            val = (args2,)
            print(f'{args1} Luck has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET Luck = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} Luck has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's Luck stat to the database.")
async def addluck(ctx, args1, args2):
    add_luck_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Luck is now {args2}')

#Add Movement Allowance
def add_ma_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT ma FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'ma' VALUES(?)")
            val = (args2,)
            print(f'{args1} Movement Allowance has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET ma = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} Movement Allowance has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's Movement Allowance stat to the database.")
async def addma(ctx, args1, args2):
    add_ma_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Movement Allowance is now {args2}')

#Add Run
def add_run_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT run FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'run' VALUES(?)")
            val = (args2,)
            print(f'{args1} Run has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET run = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} run has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's run stat to the database.")
async def addrun(ctx, args1, args2):
    add_run_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Run is now {args2}')

#Add Leap
def add_leap_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT leap FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'leap' VALUES(?)")
            val = (args2,)
            print(f'{args1} leap has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET leap = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} leap has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's leap stat to the database.")
async def addleap(ctx, args1, args2):
    add_leap_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Leap is now {args2}')

#Add Tech
def add_tech_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT tech FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'tech' VALUES(?)")
            val = (args2,)
            print(f'{args1} tech has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET tech = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} tech has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's tech stat to the database.")
async def addtech(ctx, args1, args2):
    add_tech_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Tech is now {args2}')

#Add Cool
def add_cool_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT cool FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'cool' VALUES(?)")
            val = (args2,)
            print(f'{args1} cool has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET cool = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} cool has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's cool stat to the database.")
async def addcool(ctx, args1, args2):
    add_cool_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Cool is now {args2}')

#Add Attractiveness
def add_attr_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT attr FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'attr' VALUES(?)")
            val = (args2,)
            print(f'{args1} attractiveness has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET attr = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} attractiveness has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's attractiveness stat to the database.")
async def addattr(ctx, args1, args2):
    add_attr_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Attractiveness is now {args2}')

#Add Empathy
def add_emp_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT emp FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'emp' VALUES(?)")
            val = (args2,)
            print(f'{args1} empathy has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET emp = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} empathy has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's empathy stat to the database.")
async def addemp(ctx, args1, args2):
    add_emp_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Empathy is now {args2}')

#Add Humanity
def add_human_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT humanity FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'humanity' VALUES(?)")
            val = (args2,)
            print(f'{args1} humanity has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET humanity = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} humanity has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's humanity stat to the database.")
async def addhuman(ctx, args1, args2):
    add_human_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Humanity is now {args2}')

#Add CyberCost
def add_cybcst_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT cybercost FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'cybercost' VALUES(?)")
            val = (args2,)
            print(f'{args1} cyber cost has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET cybercost = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} cyber cost has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's cybercost stat to the database.")
async def addcybcst(ctx, args1, args2):
    add_cybcst_to_db(args1, args2)
    await ctx.send(f'{args1}\'s CyberCost is now {args2}')

#Add Body
def add_body_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT body FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'body' VALUES(?)")
            val = (args2,)
            print(f'{args1} body has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET body = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} body has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's body stat to the database.")
async def addbody(ctx, args1, args2):
    add_body_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Body is now {args2}')

#Add Interface
def add_inter_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT interface FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'interface' VALUES(?)")
            val = (args2,)
            print(f'{args1} interface has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET interface = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} interface has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's interface stat to the database.")
async def addinter(ctx, args1, args2):
    add_inter_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Interface is now {args2}')

#Add Accounting
def add_acc_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT accounting FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'accounting' VALUES(?)")
            val = (args2,)
            print(f'{args1} accounting has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET accounting = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} accounting has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's accounting stat to the database.")
async def addacc(ctx, args1, args2):
    add_acc_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Accounting is now {args2}')

#Add Anthropology
def add_anthr_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT anthropology FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'anthropology' VALUES(?)")
            val = (args2,)
            print(f'{args1} anthropology has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET anthropology = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} anthropology has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's anthropology stat to the database.")
async def addanthr(ctx, args1, args2):
    add_anthr_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Anthropology is now {args2}')

#Add Awarness
def add_awar_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT awarness FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'awarness' VALUES(?)")
            val = (args2,)
            print(f'{args1} awarness has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET awarness = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} awarness has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's awarness stat to the database.")
async def addawar(ctx, args1, args2):
    add_awar_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Awarness is now {args2}')

#Add Biology
def add_bio_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT biology FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'biology' VALUES(?)")
            val = (args2,)
            print(f'{args1} biology has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET biology = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} biology has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's biology stat to the database.")
async def addbio(ctx, args1, args2):
    add_bio_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Biology is now {args2}')

#Add Botany
def add_botn_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT botany FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'botany' VALUES(?)")
            val = (args2,)
            print(f'{args1} botany has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET botany = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} botany has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's botany stat to the database.")
async def addbot(ctx, args1, args2):
    add_botn_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Botany is now {args2}')

#Add Chemistry
def add_chem_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT chemistry FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'chemistry' VALUES(?)")
            val = (args2,)
            print(f'{args1} chemistry has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET chemistry = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} chemistry has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's chemistry stat to the database.")
async def addchem(ctx, args1, args2):
    add_chem_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Chemistry is now {args2}')

#Add Composition
def add_comp_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT composition FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'composition' VALUES(?)")
            val = (args2,)
            print(f'{args1} composition has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET composition = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} composition has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's composition stat to the database.")
async def addcomp(ctx, args1, args2):
    add_comp_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Composition is now {args2}')

#Add Diagnose_Illness
def add_diag_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT Diagnose_Illness FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'Diagnose_Illness' VALUES(?)")
            val = (args2,)
            print(f'{args1} diagnose illness has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET Diagnose_Illness = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} diagnose illness has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's diagnose illness stat to the database.")
async def adddiag(ctx, args1, args2):
    add_diag_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Diagnose Illness is now {args2}')

#Add Education
def add_ed_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT education FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'education' VALUES(?)")
            val = (args2,)
            print(f'{args1} education has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET education = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} education has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's education stat to the database.")
async def added(ctx, args1, args2):
    add_ed_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Education is now {args2}')

#Add Expert
def add_exp_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT expert FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'expert' VALUES(?)")
            val = (args2,)
            print(f'{args1} expert has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET expert = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} expert has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's expert stat to the database.")
async def addexp(ctx, args1, args2):
    add_exp_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Expert is now {args2}')

#Add Gamble
def add_gamb_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT gamble FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'gamble' VALUES(?)")
            val = (args2,)
            print(f'{args1} gamble has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET gamble = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} gamble has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's gamble stat to the database.")
async def addgamb(ctx, args1, args2):
    add_gamb_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Gamble is now {args2}')

#Add Geology
def add_geo_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT geology FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'geology' VALUES(?)")
            val = (args2,)
            print(f'{args1} geology has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET geology = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} geology has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's geology stat to the database.")
async def addgeo(ctx, args1, args2):
    add_geo_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Geology is now {args2}')

#Add Hide
def add_hide_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT hide FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'hide' VALUES(?)")
            val = (args2,)
            print(f'{args1} hide has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET hide = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} hide has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's hide stat to the database.")
async def addhide(ctx, args1, args2):
    add_hide_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Hide is now {args2}')

#Add History
def add_hist_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT history FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'history' VALUES(?)")
            val = (args2,)
            print(f'{args1} history has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET history = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} history has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's history stat to the database.")
async def addhist(ctx, args1, args2):
    add_hist_to_db(args1, args2)
    await ctx.send(f'{args1}\'s History is now {args2}')

#Add Language1
def add_lang1_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT language1 FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'language1' VALUES(?)")
            val = (args2,)
            print(f'{args1} language1 has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET language1 = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} language1 has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's Language 1 stat to the database.")
async def addlang1(ctx, args1, args2):
    add_lang1_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Language 1 is now {args2}')

#Add Language2
def add_lang2_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT language2 FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'language2' VALUES(?)")
            val = (args2,)
            print(f'{args1} language2 has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET language2 = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} language2 has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's Language 2 stat to the database.")
async def addlang2(ctx, args1, args2):
    add_lang2_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Language 2 is now {args2}')

#Add Language3
def add_lang3_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT language3 FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'language3' VALUES(?)")
            val = (args2,)
            print(f'{args1} language3 has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET language3 = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} language3 has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's Language 3 stat to the database.")
async def addlang3(ctx, args1, args2):
    add_lang3_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Language 3 is now {args2}')

#Add Library Search
def add_libsrch_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT library_search FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'library_search' VALUES(?)")
            val = (args2,)
            print(f'{args1} library search has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET library_search = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} library search has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's Library Search stat to the database.")
async def addlibsrch(ctx, args1, args2):
    add_libsrch_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Library Search is now {args2}')

#Add Mathematics
def add_math_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT mathematics FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'mathematics' VALUES(?)")
            val = (args2,)
            print(f'{args1} mathematics has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET mathematics = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} mathematics has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's mathematics stat to the database.")
async def addmath(ctx, args1, args2):
    add_math_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Mathematics is now {args2}')

#Add Physics
def add_phy_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT physics FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'physics' VALUES(?)")
            val = (args2,)
            print(f'{args1} physics has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET physics = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} physics has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's physics stat to the database.")
async def addphy(ctx, args1, args2):
    add_phy_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Physics is now {args2}')

#Add Programming
def add_prog_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT programming FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'programming' VALUES(?)")
            val = (args2,)
            print(f'{args1} programming has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET programming = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} programming has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's programming stat to the database.")
async def addprog(ctx, args1, args2):
    add_prog_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Programming is now {args2}')

#Add Shadow
def add_shad_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT shadow FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'shadow' VALUES(?)")
            val = (args2,)
            print(f'{args1} shadow has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET shadow = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} shadow has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's shadow stat to the database.")
async def addshadow(ctx, args1, args2):
    add_shad_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Shadow is now {args2}')

#Add Stock Market
def add_stk_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT stock_market FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'stock_market' VALUES(?)")
            val = (args2,)
            print(f'{args1} stock market has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET stock_market = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} stock market has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's stock market stat to the database.")
async def addstk(ctx, args1, args2):
    add_stk_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Stock Market is now {args2}')

#Add System Knowledge
def add_sys_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT system_knowledge FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'system_knowledge' VALUES(?)")
            val = (args2,)
            print(f'{args1} system knowledge has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET system_knowledge = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} system knowledge has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's system knowledge stat to the database.")
async def addsys(ctx, args1, args2):
    add_sys_to_db(args1, args2)
    await ctx.send(f'{args1}\'s System Knowledge is now {args2}')

#Add Teaching
def add_teach_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT teaching FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'teaching' VALUES(?)")
            val = (args2,)
            print(f'{args1} teaching has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET teaching = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} teaching has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's teaching stat to the database.")
async def addteach(ctx, args1, args2):
    add_teach_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Teaching is now {args2}')

#Add Wilderness Survival
def add_wild_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT wilderness_survival FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'wilderness_survival' VALUES(?)")
            val = (args2,)
            print(f'{args1} wilderness survival has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET wilderness_survival = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} wilderness survival has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's wilderness survival stat to the database.")
async def addwild(ctx, args1, args2):
    add_wild_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Wilderness Survival is now {args2}')

#Add Zoology
def add_zoo_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT zoology FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'zoology' VALUES(?)")
            val = (args2,)
            print(f'{args1} zoology has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET zoology = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} zoology has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's zoology stat to the database.")
async def addzoo(ctx, args1, args2):
    add_zoo_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Zoology is now {args2}')

#Add Personal Grooming
def add_pgroom_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT personal_grooming FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'personal_grooming' VALUES(?)")
            val = (args2,)
            print(f'{args1} personal grooming has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET personal_grooming = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} personal grooming has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's personal grooming stat to the database.")
async def addpgroom(ctx, args1, args2):
    add_pgroom_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Personal Grooming is now {args2}')

#Add Wardrobe
def add_ward_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT wardrobe FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'wardrobe' VALUES(?)")
            val = (args2,)
            print(f'{args1} wardrobe has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET wardrobe = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} wardrobe has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's wardrobe stat to the database.")
async def addward(ctx, args1, args2):
    add_ward_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Wardrobe is now {args2}')

#Add Endurance
def add_end_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT endurance FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'endurance' VALUES(?)")
            val = (args2,)
            print(f'{args1} endurance has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET endurance = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} endurance has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's endurance stat to the database.")
async def addend(ctx, args1, args2):
    add_end_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Endurance is now {args2}')

#Add Strength
def add_stren_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT strength FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'strength' VALUES(?)")
            val = (args2,)
            print(f'{args1} strength has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET strength = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} strength has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's strength stat to the database.")
async def addstren(ctx, args1, args2):
    add_stren_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Strength is now {args2}')

#Add Swimming
def add_swim_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT swimming FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'swimming' VALUES(?)")
            val = (args2,)
            print(f'{args1} swimming has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET swimming = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} swimming has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's swimming stat to the database.")
async def addswim(ctx, args1, args2):
    add_swim_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Swimming is now {args2}')

#Add Interrogation
def add_interro_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT interrogation FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'interrogation' VALUES(?)")
            val = (args2,)
            print(f'{args1} interrogation has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET interrogation = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} interrogation has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's interrogation stat to the database.")
async def addinterro(ctx, args1, args2):
    add_interro_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Interrogation is now {args2}')

#Add Intimidate
def add_intim_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT intimidate FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'intimidate' VALUES(?)")
            val = (args2,)
            print(f'{args1} intimidate has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET intimidate = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} intimidate has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's intimidate stat to the database.")
async def addintim(ctx, args1, args2):
    add_intim_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Intimidate is now {args2}')

#Add Oratory
def add_orat_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT oratory FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'oratory' VALUES(?)")
            val = (args2,)
            print(f'{args1} oratory has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET oratory = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} oratory has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's oratory stat to the database.")
async def addorat(ctx, args1, args2):
    add_orat_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Oratory is now {args2}')

#Add Resist Torture
def add_resist_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT resist_torture FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'resist_torture' VALUES(?)")
            val = (args2,)
            print(f'{args1} resist torture has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET resist_torture = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} resist torture has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's resist torture stat to the database.")
async def addresist(ctx, args1, args2):
    add_resist_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Resist Torture is now {args2}')

#Add Streetwise
def add_street_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT streetwise FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'streetwise' VALUES(?)")
            val = (args2,)
            print(f'{args1} streetwise has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET streetwise = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} streetwise has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's streetwise stat to the database.")
async def addstreet(ctx, args1, args2):
    add_street_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Streetwise is now {args2}')

#Add Human Perception
def add_humanp_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT human_perception FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'human_perception' VALUES(?)")
            val = (args2,)
            print(f'{args1} human perception has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET human_perception = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} human perception has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's human perception stat to the database.")
async def addhumanp(ctx, args1, args2):
    add_humanp_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Human Perception is now {args2}')

#Add Interview
def add_interview_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT interview FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'interview' VALUES(?)")
            val = (args2,)
            print(f'{args1} interview has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET interview = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} interview has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's interview stat to the database.")
async def addinterv(ctx, args1, args2):
    add_interview_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Interview is now {args2}')

#Add Leadership
def add_leadership_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT leadership FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'leadership' VALUES(?)")
            val = (args2,)
            print(f'{args1} leadership has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET leadership = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} leadership has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's leadership stat to the database.")
async def addleader(ctx, args1, args2):
    add_leadership_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Leadership is now {args2}')

#Add Seduction
def add_seduction_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT seduction FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'seduction' VALUES(?)")
            val = (args2,)
            print(f'{args1} seduction has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET seduction = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} seduction has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's seduction stat to the database.")
async def addsedu(ctx, args1, args2):
    add_seduction_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Seduction is now {args2}')

#Add Social
def add_social_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT social FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'social' VALUES(?)")
            val = (args2,)
            print(f'{args1} social has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET social = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} social has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's social stat to the database.")
async def addsocial(ctx, args1, args2):
    add_social_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Social is now {args2}')

#Add Persuasion
def add_persuasion_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT persuasion FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'persuasion' VALUES(?)")
            val = (args2,)
            print(f'{args1} persuasion has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET persuasion = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} persuasion has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's persuasion stat to the database.")
async def addpers(ctx, args1, args2):
    add_persuasion_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Persuasion is now {args2}')

#Add Perform
def add_perform_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT perform FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'perform' VALUES(?)")
            val = (args2,)
            print(f'{args1} perform has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET perform = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} perform has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's perform stat to the database.")
async def addperf(ctx, args1, args2):
    add_perform_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Perform is now {args2}')

#Add Archery
def add_archery_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT archery FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'archery' VALUES(?)")
            val = (args2,)
            print(f'{args1} archery has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET archery = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} archery has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's archery stat to the database.")
async def addarch(ctx, args1, args2):
    add_archery_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Archery is now {args2}')

#Add Athletics
def add_athletics_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT athletics FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'athletics' VALUES(?)")
            val = (args2,)
            print(f'{args1} athletics has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET athletics = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} athletics has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's athletics stat to the database.")
async def addath(ctx, args1, args2):
    add_athletics_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Athletics is now {args2}')

#Add Brawling
def add_brawling_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT brawling FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'brawling' VALUES(?)")
            val = (args2,)
            print(f'{args1} brawling has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET brawling = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} brawling has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's brawling stat to the database.")
async def addbrawl(ctx, args1, args2):
    add_brawling_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Brawling is now {args2}')

#Add Dance
def add_dance_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT dance FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'dance' VALUES(?)")
            val = (args2,)
            print(f'{args1} dance has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET dance = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} dance has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's dance stat to the database.")
async def adddance(ctx, args1, args2):
    add_dance_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Dance is now {args2}')

#Add Dodge
def add_dodge_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT dodge FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'dodge' VALUES(?)")
            val = (args2,)
            print(f'{args1} dodge has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET dodge = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} dodge has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's dodge stat to the database.")
async def adddodge(ctx, args1, args2):
    add_dodge_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Dodge is now {args2}')

#Add Driving
def add_driving_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT driving FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'driving' VALUES(?)")
            val = (args2,)
            print(f'{args1} driving has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET driving = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} driving has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's driving stat to the database.")
async def adddrive(ctx, args1, args2):
    add_driving_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Driving is now {args2}')

#Add Fencing
def add_fencing_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT fencing FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'fencing' VALUES(?)")
            val = (args2,)
            print(f'{args1} fencing has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET fencing = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} fencing has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's fencing stat to the database.")
async def addfence(ctx, args1, args2):
    add_fencing_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Fencing is now {args2}')

#Add Handgun
def add_handgun_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT handgun FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'handgun' VALUES(?)")
            val = (args2,)
            print(f'{args1} handgun has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET handgun = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} handgun has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's handgun stat to the database.")
async def addhand(ctx, args1, args2):
    add_handgun_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Handgun is now {args2}')

#Add Heavy Weapons
def add_hvywep_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT heavy_weapons FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'heavy_weapons' VALUES(?)")
            val = (args2,)
            print(f'{args1} heavy weapons has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET heavy_weapons = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} heavy weapons has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's heavy weapons stat to the database.")
async def addhvywp(ctx, args1, args2):
    add_hvywep_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Heavy Weapons is now {args2}')

#Add Martial1
def add_martial1_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT martial1 FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'martial1' VALUES(?)")
            val = (args2,)
            print(f'{args1} martial 1 has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET martial1 = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} martial 1 has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's martial 1 stat to the database.")
async def addmart1(ctx, args1, args2):
    add_martial1_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Martial 1 is now {args2}')

#Add Martial2
def add_martial2_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT martial2 FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'martial2' VALUES(?)")
            val = (args2,)
            print(f'{args1} martial 2 has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET martial2 = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} martial 2 has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's martial 2 stat to the database.")
async def addmart2(ctx, args1, args2):
    add_martial2_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Martial 2 is now {args2}')

#Add Martial3
def add_martial3_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT martial3 FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'martial3' VALUES(?)")
            val = (args2,)
            print(f'{args1} martial 3 has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET martial3 = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} martial 3 has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's martial 3 stat to the database.")
async def addmart3(ctx, args1, args2):
    add_martial3_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Martial 3 is now {args2}')

#Add Melee
def add_melee_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT melee FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'melee' VALUES(?)")
            val = (args2,)
            print(f'{args1} melee has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET melee = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} melee has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's melee stat to the database.")
async def addmelee(ctx, args1, args2):
    add_melee_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Melee is now {args2}')

#Add Motorcycle
def add_motorcycle_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT motorcycle FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'motorcycle' VALUES(?)")
            val = (args2,)
            print(f'{args1} motorcycle has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET motorcycle = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} motorcycle has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's motorcycle stat to the database.")
async def addmotor(ctx, args1, args2):
    add_motorcycle_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Motorcycle is now {args2}')

#Add Operate Hvy Machinery
def add_ophvymach_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT operate_hvy_machinery FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'operate_hvy_machinery' VALUES(?)")
            val = (args2,)
            print(f'{args1} operate hvy machinery has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET operate_hvy_machinery = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} operate hvy machinery has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's operate hvy machinery stat to the database.")
async def addophvy(ctx, args1, args2):
    add_ophvymach_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Operate Hvy Machinery is now {args2}')

#Add Pilot G
def add_pilotg_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT pilot_g FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'pilot_g' VALUES(?)")
            val = (args2,)
            print(f'{args1} pilot g has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET pilot_g = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} pilot g has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's pilot g stat to the database.")
async def addpilotg(ctx, args1, args2):
    add_pilotg_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Pilot G is now {args2}')

#Add Pilot FW
def add_pilotfw_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT pilot_fw FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'pilot_fw' VALUES(?)")
            val = (args2,)
            print(f'{args1} pilot fw has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET pilot_fw = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} pilot fw has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's pilot fw stat to the database.")
async def addpilotfw(ctx, args1, args2):
    add_pilotfw_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Pilot FW is now {args2}')

#Add Pilot Dir
def add_pilotdir_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT pilot_dir FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'pilot_dir' VALUES(?)")
            val = (args2,)
            print(f'{args1} pilot dir has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET pilot_dir = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} pilot dir has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's pilot dir stat to the database.")
async def addpilotdir(ctx, args1, args2):
    add_pilotdir_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Pilot Dir is now {args2}')

#Add Pilot Thrust
def add_pilotthrust_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT pilot_thrust FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'pilot_thrust' VALUES(?)")
            val = (args2,)
            print(f'{args1} pilot thrust has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET pilot_thrust = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} pilot thrust has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's pilot thrust stat to the database.")
async def addpilotthr(ctx, args1, args2):
    add_pilotthrust_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Pilot Thrust is now {args2}')

#Add Rifle
def add_rifle_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT rifle FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'rifle' VALUES(?)")
            val = (args2,)
            print(f'{args1} rifle has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET rifle = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} rifle has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's rifle stat to the database.")
async def addrifle(ctx, args1, args2):
    add_rifle_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Rifle is now {args2}')

#Add Stealth
def add_stealth_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT stealth FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'stealth' VALUES(?)")
            val = (args2,)
            print(f'{args1} stealth has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET stealth = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} stealth has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's stealth stat to the database.")
async def addstealth(ctx, args1, args2):
    add_stealth_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Stealth is now {args2}')

#Add Submachinegun
def add_subm_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT submachinegun FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'submachinegun' VALUES(?)")
            val = (args2,)
            print(f'{args1} submachinegun has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET submachinegun = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} submachinegun has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's submachinegun stat to the database.")
async def addsubm(ctx, args1, args2):
    add_subm_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Submachinegun is now {args2}')

#Add MedTech
def add_medtech_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT medtech FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'medtech' VALUES(?)")
            val = (args2,)
            print(f'{args1} medtech has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET medtech = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} medtech has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's medtech stat to the database.")
async def addmedtech(ctx, args1, args2):
    add_medtech_to_db(args1, args2)
    await ctx.send(f'{args1}\'s MedTech is now {args2}')

#Add Aero Tech
def add_aerotech_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT aero_tech FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'aero_tech' VALUES(?)")
            val = (args2,)
            print(f'{args1} aero tech has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET aero_tech = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} aero tech has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's aero tech stat to the database.")
async def addaero(ctx, args1, args2):
    add_aerotech_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Aero Tech is now {args2}')

#Add AV Tech
def add_avtech_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT av_tech FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'av_tech' VALUES(?)")
            val = (args2,)
            print(f'{args1} av tech has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET av_tech = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} av tech has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's av tech stat to the database.")
async def addavtech(ctx, args1, args2):
    add_avtech_to_db(args1, args2)
    await ctx.send(f'{args1}\'s AV Tech is now {args2}')

#Add Basic Tech
def add_basictech_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT basic_tech FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'basic_tech' VALUES(?)")
            val = (args2,)
            print(f'{args1} basic tech has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET basic_tech = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} basic tech has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's basic tech stat to the database.")
async def addbasic(ctx, args1, args2):
    add_basictech_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Basic Tech is now {args2}')

#Add Cryotank Operation
def add_cryotankop_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT cryotank_operation FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'cryotank_operation' VALUES(?)")
            val = (args2,)
            print(f'{args1} cryotank operation has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET cryotank_operation = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} cryotank operation has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's cryotank operation stat to the database.")
async def addcryoop(ctx, args1, args2):
    add_cryotankop_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Cryotank Operation is now {args2}')

#Add Cyberdeck Design
def add_cyberdes_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT cyberdeck_design FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'cyberdeck_design' VALUES(?)")
            val = (args2,)
            print(f'{args1} cyberdeck design has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET cyberdeck_design = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} cyberdeck design has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's cyberdeck design stat to the database.")
async def addcyberdes(ctx, args1, args2):
    add_cyberdes_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Cyberdeck Design is now {args2}')

#Add Cybertech
def add_cybertech_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT cybertech FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'cybertech' VALUES(?)")
            val = (args2,)
            print(f'{args1} cybertech has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET cybertech = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} cybertech has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's cybertech stat to the database.")
async def addcyber(ctx, args1, args2):
    add_cybertech_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Cybertech is now {args2}')

#Add Demolitions
def add_demolitions_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT demolitions FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'demolitions' VALUES(?)")
            val = (args2,)
            print(f'{args1} demolitions has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET demolitions = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} demolitions has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's demolitions stat to the database.")
async def adddemo(ctx, args1, args2):
    add_demolitions_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Demolitions is now {args2}')

#Add Disguise
def add_disguise_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT disguise FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'disguise' VALUES(?)")
            val = (args2,)
            print(f'{args1} disguise has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET disguise = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} disguise has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's disguise stat to the database.")
async def adddis(ctx, args1, args2):
    add_disguise_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Disguise is now {args2}')

#Add Electronics
def add_electronics_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT electronics FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'electronics' VALUES(?)")
            val = (args2,)
            print(f'{args1} electronics has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET electronics = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} electronics has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's electronics stat to the database.")
async def addelec(ctx, args1, args2):
    add_electronics_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Electronics is now {args2}')

#Add Electronic Security
def add_elecsec_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT electronic_security FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'electronic_security' VALUES(?)")
            val = (args2,)
            print(f'{args1} electronic security has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET electronic_security = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} electronic security has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's electronic security stat to the database.")
async def addelecsec(ctx, args1, args2):
    add_elecsec_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Electronic Security is now {args2}')

#Add First Aid
def add_firstaid_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT first_aid FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'first_aid' VALUES(?)")
            val = (args2,)
            print(f'{args1} first aid has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET first_aid = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} first aid has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's first aid stat to the database.")
async def addfirst(ctx, args1, args2):
    add_firstaid_to_db(args1, args2)
    await ctx.send(f'{args1}\'s First Aid is now {args2}')

#Add Forgery
def add_forgery_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT forgery FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'forgery' VALUES(?)")
            val = (args2,)
            print(f'{args1} forgery has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET forgery = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} forgery has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's forgery stat to the database.")
async def addforg(ctx, args1, args2):
    add_forgery_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Forgery is now {args2}')

#Add Gyro Tech
def add_gyro_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT gyro_tech FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'gyro_tech' VALUES(?)")
            val = (args2,)
            print(f'{args1} gyro tech has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET gyro_tech = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} gyro tech has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's gyro tech stat to the database.")
async def addgyro(ctx, args1, args2):
    add_gyro_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Gyro Tech is now {args2}')

#Add Paint
def add_paint_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT paint FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'paint' VALUES(?)")
            val = (args2,)
            print(f'{args1} paint has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET paint = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} paint has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's paint stat to the database.")
async def addpaint(ctx, args1, args2):
    add_paint_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Paint is now {args2}')

#Add Photo
def add_photo_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT photo FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'photo' VALUES(?)")
            val = (args2,)
            print(f'{args1} photo has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET photo = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} photo has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's photo stat to the database.")
async def addphoto(ctx, args1, args2):
    add_photo_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Photo is now {args2}')

#Add Pharmacuticals
def add_pharma_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT pharmacuticals FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'pharmacuticals' VALUES(?)")
            val = (args2,)
            print(f'{args1} pharmacuticals has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET pharmacuticals = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} pharmacuticals has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's pharmacuticals stat to the database.")
async def addpharma(ctx, args1, args2):
    add_pharma_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Pharmacuticals is now {args2}')

#Add Pick Lock
def add_pickl_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT pick_lock FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'pick_lock' VALUES(?)")
            val = (args2,)
            print(f'{args1} pick lock has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET pick_lock = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} pick lock has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's pick lock stat to the database.")
async def addpickl(ctx, args1, args2):
    add_pickl_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Pick Lock is now {args2}')

#Add Pick Pocket
def add_pickp_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT pick_pocket FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'pick_pocket' VALUES(?)")
            val = (args2,)
            print(f'{args1} pick pocket has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET pick_pocket = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} pick pocket has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's pick pocket stat to the database.")
async def addpickp(ctx, args1, args2):
    add_pickp_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Pick Pocket is now {args2}')

#Add Play Instrument
def add_play_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT play_instrument FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'play_instrument' VALUES(?)")
            val = (args2,)
            print(f'{args1} play instrument has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET play_instrument = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} play instrument has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's play instrument stat to the database.")
async def addplay(ctx, args1, args2):
    add_play_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Play Instrument is now {args2}')

#Add Weaponsmith
def add_wpsmth_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT weaponsmith FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'weaponsmith' VALUES(?)")
            val = (args2,)
            print(f'{args1} weaponsmith has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET weaponsmith = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} weaponsmith has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's weaponsmith stat to the database.")
async def addwpsmth(ctx, args1, args2):
    add_wpsmth_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Weaponsmith is now {args2}')

#Add Charismatic Leadership
def add_charldr_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT charismatic_leadership FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'charismatic_leadership' VALUES(?)")
            val = (args2,)
            print(f'{args1} charismatic leadership has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET charismatic_leadership = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} charismatic leadership has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's charismatic leadership stat to the database.")
async def addcharldr(ctx, args1, args2):
    add_charldr_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Charismatic Leadership is now {args2}')

#Add Combat Sense
def add_comsns_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT combat_sense FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'combat_sense' VALUES(?)")
            val = (args2,)
            print(f'{args1} combat sense has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET combat_sense = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} combat sense has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's combat sense stat to the database.")
async def addcomsns(ctx, args1, args2):
    add_comsns_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Combat Sense is now {args2}')

#Add Credibility
def add_cred_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT credibility FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'credibility' VALUES(?)")
            val = (args2,)
            print(f'{args1} credibility has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET credibility = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} credibility has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's credibility stat to the database.")
async def addcred(ctx, args1, args2):
    add_cred_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Credibility is now {args2}')

#Add Family
def add_family_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT family FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'family' VALUES(?)")
            val = (args2,)
            print(f'{args1} family has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET family = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} family has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's family stat to the database.")
async def addfamily(ctx, args1, args2):
    add_family_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Family is now {args2}')

#Add Authority
def add_auth_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT authority FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'authority' VALUES(?)")
            val = (args2,)
            print(f'{args1} authority has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET authority = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} authority has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's authority stat to the database.")
async def addauth(ctx, args1, args2):
    add_auth_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Authority is now {args2}')

#Add Jury Rig
def add_jury_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT jury_rig FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'jury_rig' VALUES(?)")
            val = (args2,)
            print(f'{args1} jury rig has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET jury_rig = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} jury rig has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's jury rig stat to the database.")
async def addjury(ctx, args1, args2):
    add_jury_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Jury Rig is now {args2}')

#Add Resources
def add_resc_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT resources FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'resources' VALUES(?)")
            val = (args2,)
            print(f'{args1} resources has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET resources = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} resources has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's resources stat to the database.")
async def addresc(ctx, args1, args2):
    add_resc_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Resources is now {args2}')

#Add Streetdeal
def add_streetdeal_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT streetdeal FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'streetdeal' VALUES(?)")
            val = (args2,)
            print(f'{args1} streetdeal has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET streetdeal = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'{args1} streetdeal has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's streetdeal stat to the database.")
async def addstrtdeal(ctx, args1, args2):
    add_streetdeal_to_db(args1, args2)
    await ctx.send(f'{args1}\'s Streetdeal is now {args2}')

#Add Character Sheet
def add_cs_to_db(args1, args2):
    try:
        conn = sqlite3.connect('charinfo.db')
        cursor = conn.cursor()
        sql = ("SELECT cs FROM character WHERE 'Character'=?")
        val = (args1,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result is None:
            sql = ("INSERT INTO character 'cs' VALUES(?)")
            val = (args2,)
            print(f'The link to {args1}\'s character sheet has been set to {args2}')
        elif result is not None:
            sql = ("UPDATE character SET cs = ? WHERE Character = ?")
            val = (args2, args1)
            print(f'The link to {args1}\'s character sheet has been updated to {args2}')
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
    finally:
        pass

@commands.command(description="Adds/Updates your character's IP Points to the database.")
async def addcs(ctx, args1, args2):
    add_cs_to_db(args1, args2)
    await ctx.send(f'{args1}\'s character sheet is now {args2}')


def setup(client):
   client.add_command(addchar)
   client.add_command(addint)
   client.add_command(addref)
   client.add_command(addluck)
   client.add_command(addma)
   client.add_command(addrun)
   client.add_command(addleap)
   client.add_command(addtech)
   client.add_command(addcool)
   client.add_command(addattr)
   client.add_command(addemp)
   client.add_command(addhuman)
   client.add_command(addcybcst)
   client.add_command(addbody)
   client.add_command(addinter)
   client.add_command(addacc)
   client.add_command(addanthr)
   client.add_command(addawar)
   client.add_command(addbio)
   client.add_command(addbot)
   client.add_command(addchem)
   client.add_command(addcomp)
   client.add_command(adddiag)
   client.add_command(added)
   client.add_command(addexp)
   client.add_command(addgamb)
   client.add_command(addgeo)
   client.add_command(addhide)
   client.add_command(addhist)
   client.add_command(addlang1)
   client.add_command(addlang2)
   client.add_command(addlang3)
   client.add_command(addlibsrch)
   client.add_command(addmath)
   client.add_command(addphy)
   client.add_command(addprog)
   client.add_command(addshadow)
   client.add_command(addstk)
   client.add_command(addsys)
   client.add_command(addteach)
   client.add_command(addwild)
   client.add_command(addzoo)
   client.add_command(addpgroom)
   client.add_command(addward)
   client.add_command(addend)
   client.add_command(addstren)
   client.add_command(addswim)
   client.add_command(addinterro)
   client.add_command(addintim)
   client.add_command(addorat)
   client.add_command(addresist)
   client.add_command(addstreet)
   client.add_command(addhumanp)
   client.add_command(addinterv)
   client.add_command(addleader)
   client.add_command(addsedu)
   client.add_command(addsocial)
   client.add_command(addpers)
   client.add_command(addperf)
   client.add_command(addarch)
   client.add_command(addath)
   client.add_command(addbrawl)
   client.add_command(adddance)
   client.add_command(adddodge)
   client.add_command(adddrive)
   client.add_command(addfence)
   client.add_command(addhand)
   client.add_command(addhvywp)
   client.add_command(addmart1)
   client.add_command(addmart2)
   client.add_command(addmart3)
   client.add_command(addmelee)
   client.add_command(addmotor)
   client.add_command(addophvy)
   client.add_command(addpilotg)
   client.add_command(addpilotfw)
   client.add_command(addpilotdir)
   client.add_command(addpilotthr)
   client.add_command(addrifle)
   client.add_command(addstealth)
   client.add_command(addsubm)
   client.add_command(addmedtech)
   client.add_command(addaero)
   client.add_command(addavtech)
   client.add_command(addbasic)
   client.add_command(addcryoop)
   client.add_command(addcyberdes)
   client.add_command(addcyber)
   client.add_command(adddemo)
   client.add_command(adddis)
   client.add_command(addelec)
   client.add_command(addelecsec)
   client.add_command(addfirst)
   client.add_command(addforg)
   client.add_command(addgyro)
   client.add_command(addpaint)
   client.add_command(addphoto)
   client.add_command(addpharma)
   client.add_command(addpickl)
   client.add_command(addpickp)
   client.add_command(addplay)
   client.add_command(addwpsmth)
   client.add_command(addcharldr)
   client.add_command(addcomsns)
   client.add_command(addcred)
   client.add_command(addfamily)
   client.add_command(addauth)
   client.add_command(addjury)
   client.add_command(addresc)
   client.add_command(addstrtdeal)
   client.add_command(addcs)