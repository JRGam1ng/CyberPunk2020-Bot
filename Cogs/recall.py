import sqlite3
from discord.ext import commands

#Recall Commands

@commands.command(name = "int", description = "Returns given characters' intelligence stat. Netrunners and Coroporates require the highest out of all classes, but intelligence is important for any character.")
async def _int(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT int FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s intelligence stat is {result[0]}. To change the value of this stat, please use command !addint.")

@commands.command(description = "Returns given characters' reflex stat. Reflex is highly important for any character you expect to see a lot of combat.")
async def ref(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT ref FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s reflex stat is {result[0]}. To change the value of this stat, please use command !addref.")

@commands.command(description = "Returns given characters' luck stat. Luck is just what it sounds like. You can add it to rolls and the stat refills each in game session.")
async def luck(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT luck FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s luck stat is {result[0]}. To change the value of this stat, please use command !addluck.")

@commands.command(description = "Returns given characters' movement allowance stat. This determines how fast your character can move.")
async def ma(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT ma FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s movement allowance stat is {result[0]}. To change the value of this stat, please use command !addma.")

@commands.command(description = "Returns given characters' run stat. Run is your ma times 3.")
async def run(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT run FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s run stat is {result[0]}. To change the value of this stat, please use command !addrun.")

@commands.command(description = "Returns given characters' leap stat. Leap is your run divided by 4.")
async def leap(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT leap FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s leap stat is {result[0]}. To change the value of this stat, please use command !addleap.")

@commands.command(description = "Returns given characters' tech stat. Tech is important to all charachers, but especially techies of any kind.")
async def tech(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT tech FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s tech stat is {result[0]}. To change the value of this stat, please use command !addtech.")


@commands.command(description = "Returns given characters' cool stat. This is how well the character holds up under pressure. Solos and Nomads should excell here.")
async def cool(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT cool FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s cool stat is {result[0]}. To change the value of this stat, please use command !addcool.")
    
@commands.command(description = "Returns given characters' attractiveness stat. In Cyberpunk, looks matter. Medias and Rockerboys feel this more than others.")
async def attr(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT attr FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s attractiveness stat is {result[0]}. To change the value of this stat, please use command !addattr.")

@commands.command(description = "Returns given characters' empathy stat. Empathy is a measure of how well you relate to others. An empathy of 2 is practically cold and unpleasent. An empathy of 1 is violent and sociopathic. An empathy of 0 or less is full cyberpsychosis and no longer playable.")
async def emp(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT emp FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s empathy stat is {result[0]}. To change the value of this stat, please use command !addemp.")

@commands.command(description = "Returns given characters' humanity stat. Humanity is found by taking your emp times 10. For every 10 points of humanity lost, you lose a point of empathy.")
async def humanity(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT humanity FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s humanity stat is {result[0]}. To change the value of this stat, please use command !addhuman.")

@commands.command(description = "Returns given characters' CyberCost.")
async def cybercost(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT cybercost FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s CyberCost is {result[0]}. To change the value of this stat, please use command !addcybcst.")
    
@commands.command(description = "Returns given characters' body stat. A body size of 5-7 is considered average.")
async def body(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT body FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s body stat is {result[0]}. To change the value of this stat, please use command !addbody.")

@commands.command(description = "Returns given characters' interface skill.")
async def interface(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT interface FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s interface skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !addinter.")

@commands.command(description = "Returns given characters' accounting skill.")
async def accounting(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT accounting FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s accounting skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !addacc.")

@commands.command(description = "Returns given characters' anthropology skill.")
async def anthropology(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT anthropology FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s anthropology skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !addanthr.")

@commands.command(description = "Returns given characters' awarness skill.")
async def awarness(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT awarness FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s awarness skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !addawar.")

@commands.command(description = "Returns given characters' biology skill.")
async def biology(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT biology FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s biology skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !addbio.")

@commands.command(description = "Returns given characters' botany skill.")
async def botany(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT botany FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s botany skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !addbot.")

@commands.command(description = "Returns given characters' chemistry skill.")
async def chemistry(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT chemistry FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s chemistry skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !addchem.")

@commands.command(description = "Returns given characters' composition skill.")
async def composition(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT composition FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s composition skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !addcomp.")

@commands.command(description = "Returns given characters' diagnose illness skill.")
async def diagnose(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT diagnose_illness FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s diagnose illness skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !adddiag.")

@commands.command(description = "Returns given characters' education skill.")
async def education(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT education FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s education skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !added.")

@commands.command(description = "Returns given characters' expert skill.")
async def expert(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT expert FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s expert skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !addexp.")

@commands.command(description = "Returns given characters' gamble skill.")
async def gamble(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT gamble FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s gamble skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !addgamb.")

@commands.command(description = "Returns given characters' geology skill.")
async def geology(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT geology FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s geology skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !addgeo.")


@commands.command(description = "Returns given characters' hide skill.")
async def hide(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT hide FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s hide skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !addhide.")

@commands.command(description = "Returns given characters' history skill.")
async def history(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT history FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s history skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !addhist.")

@commands.command(description = "Returns given characters' language1 skill.")
async def language1(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT language1 FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s language1 skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !addlang1.")

@commands.command(description = "Returns given characters' language2 skill.")
async def language2(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT language2 FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s language2 skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !addlang2.")

@commands.command(description = "Returns given characters' language3 skill.")
async def language3(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT language3 FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s language3 skill is {result[0]}. This skill is based on the intelligence stat. To change the value of this skill, please use command !addlang3.")

@commands.command(description = "Returns given characters' library search skill.")
async def libsrch(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT library_search FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s library search skill is {result[0]}. This skill is based on the intelligence stat. To change this skills value, please use command !addlibsrch.")

@commands.command(description = "Returns given characters' mathematics search skill.")
async def math(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT mathematics FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s mathematics skill is {result[0]}. This skill is based on the intelligence stat. To change this skills value, please use command !addmath.")

@commands.command(description = "Returns given characters' physics search skill.")
async def physics(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT physics FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s physics skill is {result[0]}. This skill is based on the intelligence stat. To change this skills value, please use command !addphy.")

@commands.command(description = "Returns given characters' programming skill.")
async def programming(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT programming FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s programming skill is {result[0]}. This skill is based on the intelligence stat. To change this skills value, please use command !addprog.")

@commands.command(description = "Returns given characters' shadow skill.")
async def shadow(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT shadow FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s shadow skill is {result[0]}. This skill is based on the intelligence stat. To change this skills value, please use command !addshadow.")

@commands.command(description = "Returns given characters' stock market skill.")
async def market(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT stock_market FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s stock market skill is {result[0]}. This skill is based on the intelligence stat. To change this skills value, please use command !addshadow.")

@commands.command(description = "Returns given characters' system knowledge skill.")
async def sysknw(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT system_knowledge FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s system knowledge skill is {result[0]}. This skill is based on the intelligence stat. To change this skills value, please use command !addshadow.")

@commands.command(description = "Returns given characters' teaching skill.")
async def teaching(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT teaching FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s teaching skill is {result[0]}. This skill is based on the intelligence stat. To change this skills value, please use command !addteach.")

@commands.command(description = "Returns given characters' wilderness survival skill.")
async def wildsurv(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT wilderness_survival FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s wilderness survival skill is {result[0]}. This skill is based on the intelligence stat. To change this skills value, please use command !addwild.")

@commands.command(description = "Returns given characters' zoology skill.")
async def zoology(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT zoology FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s zoology skill is {result[0]}. This skill is based on the intelligence stat. To change this skills value, please use command !addzoo.")

@commands.command(description = "Returns given characters' personal grooming skill.")
async def pgroom(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT personal_grooming FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s personal grooming skill is {result[0]}. This skill is based on the attractiveness stat. To change this skills value, please use command !addpgroom.")

@commands.command(description = "Returns given characters' wardrobe skill.")
async def wardrobe(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT wardrobe FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s wardrobe skill is {result[0]}. This skill is based on the attractiveness stat. To change this skills value, please use command !addward.")

@commands.command(description = "Returns given characters' endurance skill.")
async def endurance(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT endurance FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s endurance skill is {result[0]}. This skill is based on the body type stat. To change this skills value, please use command !addend.")

@commands.command(description = "Returns given characters' strength skill.")
async def strength(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT strength FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s strength skill is {result[0]}. This skill is based on the body type stat. To change this skills value, please use command !addstren.")

@commands.command(description = "Returns given characters' swimming skill.")
async def swimming(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT swimming FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s swimming skill is {result[0]}. This skill is based on the body type stat. To change this skills value, please use command !addswim.")

@commands.command(description = "Returns given characters' interrogation skill.")
async def interrogation(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT interrogation FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s interrogation skill is {result[0]}. This skill is based on the cool/willpower stat. To change this skills value, please use command !addinterro.")

@commands.command(description = "Returns given characters' intimidate skill.")
async def intimidate(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT intimidate FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s intimidate skill is {result[0]}. This skill is based on the cool/willpower stat. To change this skills value, please use command !addintim.")

@commands.command(description = "Returns given characters' oratory skill.")
async def oratory(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT oratory FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s oratory skill is {result[0]}. This skill is based on the cool/willpower stat. To change this skills value, please use command !addorat.")

@commands.command(description = "Returns given characters' resist torture skill.")
async def resist(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT resist_torture FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s resist torture skill is {result[0]}. This skill is based on the cool/willpower stat. To change this skills value, please use command !addresist.")

@commands.command(description = "Returns given characters' streetwise skill.")
async def streetwise(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT streetwise FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s streetwise skill is {result[0]}. This skill is based on the cool/willpower stat. To change this skills value, please use command !addstreet.")

@commands.command(description = "Returns given characters' human perception skill.")
async def humanp(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT human_perception FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s human perception skill is {result[0]}. This skill is based on the empathy stat. To change this skills value, please use command !addhumanp.")

@commands.command(description = "Returns given characters' interview skill.")
async def interview(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT interview FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s interview skill is {result[0]}. This skill is based on the empathy stat. To change this skills value, please use command !addinterv.")

@commands.command(description = "Returns given characters' leadership skill.")
async def leadership(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT leadership FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s leadership skill is {result[0]}. This skill is based on the empathy stat. To change this skills value, please use command !addleader.")

@commands.command(description = "Returns given characters' seduction skill.")
async def seduction(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT seduction FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s seduction skill is {result[0]}. This skill is based on the empathy stat. To change this skills value, please use command !addsedu.")

@commands.command(description = "Returns given characters' social skill.")
async def social(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT social FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s social skill is {result[0]}. This skill is based on the empathy stat. To change this skills value, please use command !addsocial.")

@commands.command(description = "Returns given characters' persuasion skill.")
async def persuasion(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT persuasion FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s persuasion skill is {result[0]}. This skill is based on the empathy stat. To change this skills value, please use command !addpers.")

@commands.command(description = "Returns given characters' perform skill.")
async def perform(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT perform FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s perform skill is {result[0]}. This skill is based on the empathy stat. To change this skills value, please use command !addperf.")

@commands.command(description = "Returns given characters' archery skill.")
async def archery(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT archery FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s archery skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addarch.")

@commands.command(description = "Returns given characters' athletics skill.")
async def athletics(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT athletics FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s athletics skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addath.")

@commands.command(description = "Returns given characters' brawling skill.")
async def brawling(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT brawling FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s brawling skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addbrawl.")

@commands.command(description = "Returns given characters' dance skill.")
async def dance(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT dance FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s dance skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !adddance.")

@commands.command(description = "Returns given characters' dodge skill.")
async def dodge(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT dodge FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s dodge skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !adddodge.")

@commands.command(description = "Returns given characters' driving skill.")
async def driving(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT driving FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s driving skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !adddrive.")

@commands.command(description = "Returns given characters' fencing skill.")
async def fencing(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT fencing FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s fencing skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addfence.")

@commands.command(description = "Returns given characters' handgun skill.")
async def handgun(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT handgun FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s handgun skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addhand.")

@commands.command(description = "Returns given characters' heavy weapons skill.")
async def hvywep(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT heavy weapons FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s heavy weapons skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addhvywp.")

@commands.command(description = "Returns given characters' martial1 skill.")
async def martial1(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT martial1 FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s martial1 skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addmart1.")

@commands.command(description = "Returns given characters' martial2 skill.")
async def martial2(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT martial2 FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s martial2 skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addmart2.")

@commands.command(description = "Returns given characters' martial3 skill.")
async def martial3(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT martial3 FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s martial3 skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addmart3.")

@commands.command(description = "Returns given characters' melee skill.")
async def melee(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT melee FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s melee skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addmelee.")

@commands.command(description = "Returns given characters' motorcycle skill.")
async def motorcycle(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT motorcycle FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s motorcycle skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addmotor.")

@commands.command(description = "Returns given characters' operate heavy machinery skill.")
async def ophvy(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT operate_hvy_machinery FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s operate heavy machinery skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addophvy.")

@commands.command(description = "Returns given characters' pilot g skill.")
async def pilotg(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT pilot_g FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s pilot g skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addpilotg.")

@commands.command(description = "Returns given characters' pilot fw skill.")
async def pilotfw(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT pilot_fw FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s pilot fw skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addpilotfw.")

@commands.command(description = "Returns given characters' pilot dir skill.")
async def pilotdir(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT pilot_dir FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s pilot dir skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addpilotdir.")

@commands.command(description = "Returns given characters' pilot thrust skill.")
async def pilotthrust(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT pilot_thrust FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s pilot thrust skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addpilotthr.")

@commands.command(description = "Returns given characters' rifle skill.")
async def rifle(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT rifle FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s rifle skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addrifle.")

@commands.command(description = "Returns given characters' stealth skill.")
async def stealth(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT stealth FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s stealth skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addstealth.")

@commands.command(description = "Returns given characters' submachinegun skill.")
async def submachine(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT submachinegun FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s submachinegun skill is {result[0]}. This skill is based on the reflex stat. To change this skills value, please use command !addsubm.")

@commands.command(description = "Returns given characters' medtech skill.  MedTech's main skill is Tech.")
async def medtech(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT medtech FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s medtech skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addmedtech.")

@commands.command(description = "Returns given characters' aero tech skill.")
async def aerotech(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT aero_tech FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s aero tech skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addaero.")

@commands.command(description = "Returns given characters' av tech skill.")
async def avtech(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT av_tech FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s av tech skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addavtech.")

@commands.command(description = "Returns given characters' basic tech skill.")
async def basictech(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT basic_tech FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s basic tech skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addbasic.")

@commands.command(description = "Returns given characters' cryotank operation skill.")
async def cryoop(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT cryotank_operation FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s cryotank operation skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addcryoop.")

@commands.command(description = "Returns given characters' cyberdeck design skill.")
async def cyberdes(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT cyberdeck_design FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s cyberdeck design skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addcyberdes.")

@commands.command(description = "Returns given characters' cybertech skill.")
async def cybertech(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT cybertech FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s cybertech skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addcyber.")

@commands.command(description = "Returns given characters' demolitions skill.")
async def demo(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT demolitions FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s demolitions skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !adddemo.")

@commands.command(description = "Returns given characters' disguise skill.")
async def disguise(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT disguise FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s disguise skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !adddis.")

@commands.command(description = "Returns given characters' electronics skill.")
async def electronics(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT electronics FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s electronics skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addelec.")

@commands.command(description = "Returns given characters' electronic security skill.")
async def elecsec(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT electronic_security FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s electronic security skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addelecsec.")

@commands.command(description = "Returns given characters' first aid skill.")
async def firstaid(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT first_aid FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s first aid skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addfirst.")

@commands.command(description = "Returns given characters' forgery skill.")
async def forgery(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT forgery FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s forgery skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addforg.")

@commands.command(description = "Returns given characters' gyro tech skill.")
async def gyrotech(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT gyro_tech FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s gyro tech skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addgyro.")

@commands.command(description = "Returns given characters' paint skill.")
async def paint(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT paint FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s paint skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addpaint.")

@commands.command(description = "Returns given characters' photo skill.")
async def photo(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT photo FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s photo skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addphoto.")

@commands.command(description = "Returns given characters' pharmacuticals skill.")
async def pharma(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT pharmacuticals FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s pharmacuticals skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addpharma.")

@commands.command(description = "Returns given characters' pick lock skill.")
async def picklock(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT pick_lock FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s pick lock skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addpickl.")

@commands.command(description = "Returns given characters' pick pocket skill.")
async def pickpocket(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT pick_pocket FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s pick pocket skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addpickp.")

@commands.command(description = "Returns given characters' play instrument skill.")
async def playinstru(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT play_instrument FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s play instrument skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addplay.")

@commands.command(description = "Returns given characters' weaponsmith skill.")
async def weaponsmith(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT weaponsmith FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s weaponsmith skill is {result[0]}. This skill is based on the tech stat. To change this skills value, please use command !addwpsmth.")

@commands.command(description = "Returns given characters' charismatic leadership skill.")
async def charldr(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT charismatic_leadership FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s charismatic leadership skill is {result[0]}. Charismatic leadership is added to your cool stat. To change this skills value, please use command !addcharldr.")

@commands.command(description = "Returns given characters' combat sense skill.")
async def combatsense(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT combat_sense FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s combat sense skill is {result[0]}. This skill gives a bonus to awarness skill and initiative equal to this skill value. To change this skills value, please use command !addcomsns.")

@commands.command(description = "Returns given characters' credibility skill.")
async def credibility(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT credibility FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s credibility skill is {result[0]}. Credibility is applied to your int stat. To change this skills value, please use command !addcred.")

@commands.command(description = "Returns given characters' family skill.")
async def family(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT family FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s family skill is {result[0]}. To change this skills value, please use command !addfamily.")

@commands.command(description = "Returns given characters' authority skill.")
async def authority(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT authority FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s authority skill is {result[0]}. Authority is applied to your cool stat. To change this skills value, please use command !addauth.")

@commands.command(description = "Returns given characters' jury rig skill.")
async def juryrig(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT jury_rig FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s jury rig skill is {result[0]}. To change this skills value, please use command !addjury.")

@commands.command(description = "Returns given characters' resources skill.")
async def resources(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT resources FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s resources skill is {result[0]}. Resource is applied to your intelligence stat. To change this skills value, please use command !addresc.")

@commands.command(description = "Returns given characters' streetdeal skill.")
async def streetdeal(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT streetdeal FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s streetdeal skill is {result[0]}. Streetdeal is applied to your cool stat. To change this skills value, please use command !addstrtdeal.")

@commands.command(description = "Returns given characters' eurobuck amount that is currently on them.")
async def eb(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT eurobucks FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1} has {result[0]} Eurobucks on them currently. Eurobucks are the in-game currency. To change this skills value, please use command !addeb.")

@commands.command(description = "Returns given characters' eurobuck amount in total.")
async def savedeb(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT alleurobucks FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1} has {result[0]} Eurobucks stored. Eurobucks are the in-game currency. To change this skills value, please use command !addalleb.")

@commands.command(description = "Returns given characters' IP point amount.")
async def ip(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT ippoints FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1} has {result[0]} IP points. Every 10 IP points will equal one usuable skill point to apply to any skill you wish (except other classes specific skills). To change this skills value, please use command !addip.")

@commands.command(description = "Returns given characters' character sheet.")
async def cs(ctx, args1):
    conn = sqlite3.connect('charinfo.db')
    cursor = conn.cursor()
    query = "SELECT cs FROM character WHERE Character=?"
    val = (args1,)
    cursor.execute(query, val)
    result = cursor.fetchone()
    await ctx.send(f"{args1}\'s character sheet is {result}. To change your character sheet, please use command !addcs.")

def setup(client):
    client.add_command(_int)
    client.add_command(ref)
    client.add_command(luck)
    client.add_command(ma)
    client.add_command(run)
    client.add_command(leap)
    client.add_command(tech)
    client.add_command(cool)
    client.add_command(attr)
    client.add_command(emp)
    client.add_command(humanity)
    client.add_command(cybercost)
    client.add_command(body)
    client.add_command(interface)
    client.add_command(accounting)
    client.add_command(anthropology)
    client.add_command(awarness)
    client.add_command(biology)
    client.add_command(botany)
    client.add_command(chemistry)
    client.add_command(composition)
    client.add_command(diagnose)
    client.add_command(education)
    client.add_command(expert)
    client.add_command(gamble)
    client.add_command(geology)
    client.add_command(hide)
    client.add_command(history)
    client.add_command(language1)
    client.add_command(language2)
    client.add_command(language3)
    client.add_command(libsrch)
    client.add_command(math)
    client.add_command(physics)
    client.add_command(programming)
    client.add_command(shadow)
    client.add_command(market)
    client.add_command(sysknw)
    client.add_command(teaching)
    client.add_command(wildsurv)
    client.add_command(zoology)
    client.add_command(pgroom)
    client.add_command(wardrobe)
    client.add_command(endurance)
    client.add_command(strength)
    client.add_command(swimming)
    client.add_command(interrogation)
    client.add_command(intimidate)
    client.add_command(oratory)
    client.add_command(resist)
    client.add_command(streetwise)
    client.add_command(humanp)
    client.add_command(interview)
    client.add_command(leadership)
    client.add_command(seduction)
    client.add_command(social)
    client.add_command(persuasion)
    client.add_command(perform)
    client.add_command(archery)
    client.add_command(athletics)
    client.add_command(brawling)
    client.add_command(dance)
    client.add_command(dodge)
    client.add_command(driving)
    client.add_command(fencing)
    client.add_command(handgun)
    client.add_command(hvywep)
    client.add_command(martial1)
    client.add_command(martial2)
    client.add_command(martial3)
    client.add_command(melee)
    client.add_command(motorcycle)
    client.add_command(ophvy)
    client.add_command(pilotg)
    client.add_command(pilotfw)
    client.add_command(pilotdir)
    client.add_command(pilotthrust)
    client.add_command(rifle)
    client.add_command(stealth)
    client.add_command(submachine)
    client.add_command(medtech)
    client.add_command(aerotech)
    client.add_command(avtech)
    client.add_command(basictech)
    client.add_command(cryoop)
    client.add_command(cyberdes)
    client.add_command(cybertech)
    client.add_command(demo)
    client.add_command(disguise)
    client.add_command(electronics)
    client.add_command(elecsec)
    client.add_command(firstaid)
    client.add_command(forgery)
    client.add_command(gyrotech)
    client.add_command(paint)
    client.add_command(photo)
    client.add_command(pharma)
    client.add_command(picklock)
    client.add_command(pickpocket)
    client.add_command(playinstru)
    client.add_command(weaponsmith)
    client.add_command(charldr)
    client.add_command(combatsense)
    client.add_command(credibility)
    client.add_command(family)
    client.add_command(authority)
    client.add_command(juryrig)
    client.add_command(resources)
    client.add_command(streetdeal)
    client.add_command(eb)
    client.add_command(savedeb)
    client.add_command(ip)
    client.add_command(cs)