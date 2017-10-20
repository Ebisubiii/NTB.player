# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(token='Els8nCB8fneMKHZr37F6.p3q4xhPrOgDXJ/23Wu9xrG.zHqgQdiw6glWERSv25iy90I4drqerU3KBSUecBDy+Hg=')
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token='El4946s5oo3Hce0WjzP6.qXTD/U9pV2sS6GXV7uaSrG.yvl+h+2CiX+1Cm4dtufFZnBALTX8eTeoBVi3k/afVF8=')
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token='Eljmig046zEl0z8ETWr3.FKHj4TZ0cE0D3s1XT7FM8W.BhiUBaa3eCs/6uSA8Ox3BDsVTFFvx/84KIBxuHf1VK0=')
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token='ElH6GKgjTyITKLJlNiLb.Z0/HuJAY8hX+9Mwq7qR2wW.OHJHR46NWeadbBBgybFzFO1RF+iXCN6uTUxrlcV2HaM=')
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token='ElcRugGtdyHpERXt7Jga.o4lvSE9UgAT11oz0Npme6G.gMvWkzoth4E6YbeqeBYX0THcnSKDsN6MM5eJRJff7h4=')
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token='ElIiPv4jOy2wmlSTxv45.ovqlCVGWM9wqwxQ69uoTbq.OI/VskSEAkdCH1KVVk7GrItxSNBVNRBXhT41jxXoRQQ=')
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token='Elus5ATjLuoRwmnP9Yi9.rhpvHK0M0H7vNqQlQaB+Mq.tM5sHK2UaM9pWooMDACB25GSpt0l/WYFBWk/+TCCQRU=')
ki6.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""» мүsтнιc bot command «

👉 PUBLIC COMMAND

[Bot?]     Cek Akun Bot
[Jam update] Update Jam
[Id Group] Cek Id Group
[Ginfo]    Group Info
[Mid all]   Cek All mid Bot
[BOT 1/2/3/4] Cek Mid Bot
[Respon]   Cek Respon Bot
[Speedbot] Cek Kecepatan Bot
[Up]       Fungsi Spam Chat
[Banlist]  Cek List Akun Banned
[Gn namagroup] Ganti Nama Group
[Cancel] Cancel User Masuk Group
[Tag All]      Mention Semua User
[Set View] Cek Privasi Group
[Ourl]  Membuka Url Group
[Curl] Menutup Url Group

􀔃􀅕👉PRIVATE COMMAND

[SetGroup] Menggatur Privasi Grup
[Banned @] Bann Target
[Unban @]  Unbann Target
[Kill @] Kick Target Ban
[Nk @]   Kick Target User
[All join] Invite Semua Bot
[_namabot join] Invite Bot
[Bye _namabot]  Leave Bot
SSH by мүsтнιc line.me/ti/p/~mysthic21
"""

Setgroup =""" MODE PROTECT GROUP

[Protect QR -- Qr on / off]
[Mid Via Contact -- Contact On / Off]
[Reject Invite -- Guest On / Off]
SSH by ғrαɴѕ line.me/ti/p/~Fransgans
"""

KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = ki2.getProfile().mid
Cmid = ki3.getProfile().mid
Dmid = ki4.getProfile().mid
Emid = ki5.getProfile().mid
Fmid = ki6.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,","]
admin=["ua6cc2bfe8e9808aabff052aaeb98d5cd"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"OPEN
Penyewaan Bot Protect

Harga Bisa Chat Ya :)
By мүsтнιc line.me/ti/p/~mysthic21",
    "lang":"JP",.
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"мүsтнιc ᴘʀᴏᴛᴇᴄᴛ ",
    "cName2":"мүsтнιc ᴘʀᴏᴛᴇᴄᴛ ",
    "cName3":"мүsтнιc ᴘʀᴏᴛᴇᴄᴛ ",
    "cName4":"мүsтнιc ᴘʀᴏᴛᴇᴄᴛ ",
    "cName5":"мүsтнιc ᴘʀᴏᴛᴇᴄᴛ ",
    "cName6":"мүsтнιc ᴘʀᴏᴛᴇᴄᴛ ",
    "cName7":"мүsтнιc ᴘʀᴏᴛᴇᴄᴛ ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":True,
    "ProtectQR":True,
    "Protectguest":True,
    "Protectcancel":True,
    "protectionOn":True,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
    
setTime = {}
setTime = wait2['setTime']

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = cl.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += "\n・" + Name
                    wait2['ROM'][op.param1][op.param2] = "・" + Name
            else:
                pass
    except:
        pass
        
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        
        #------Open QR Kick start------#
        if op.type == 11:
           if wait["ProtectQR"] == True:
               if op.param2 not in Bots:
                 if op.param2 not in admin:           
                   G = cl.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   ki.kickoutFromGroup(op.param1,[op.param2])
                   cl.updateGroup(G)
        #------Open QR Kick finish-----#
        
        #------Invite User Kick start------#
        if op.type == 13:
           if wait["Protectguest"] == True:
               if op.param2 not in Bots:
               	 if op.param2 not in admin:
                  random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick Finish------#
        
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                
                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        
                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        
                if op.param3 in Fmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace(" ",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list) 
        
        if op.type == 19:
           if op.param2 not in Bots:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              
        if op.type == 19:
           if op.param3 in admin:
              cl.kickoutFromGroup(op.param1,[op.param2])
              cl.inviteIntoGroup(op.param1,admin)
           else:
               pass
          
        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki2.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = ki2.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki3.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki3.updateGroup(X)
                    Ti = ki3.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki2.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki2.updateGroup(G)
                    Ticket = ki2.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki4.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki4.updateGroup(X)
                    Ti = ki4.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki3.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki3.updateGroup(G)
                    Ticket = ki3.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki5.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki5.updateGroup(X)
                    Ti = ki5.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki4.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki4.updateGroup(G)
                    Ticket = ki4.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki6.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki6.updateGroup(X)
                    Ti = ki6.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki5.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki5.updateGroup(G)
                    Ticket = ki5.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                    	cl.kickoutFromGroup(op.param1,[op.param2])
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki6.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki6.updateGroup(G)
                    Ticket = ki6.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
      
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace(" ",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
                            
           #------Cancel User Kick start------#
        if op.type == 32:
            if op.param2 not in Bots:
              if op.param2 not in admin:	
               cl.kickoutFromGroup(op.param1,[op.param2])
           #-----Cancel User Kick Finish------#
           
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")
        
               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        ki2.sendText(msg.to,"deleted")
                        ki3.sendText(msg.to,"deleted")
                        ki4.sendText(msg.to,"deleted")
                        ki5.sendText(msg.to,"deleted")
                        ki6.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        ki2.sendText(msg.to,"It is not in the black list")
                        ki3.sendText(msg.to,"It is not in the black list")
                        ki4.sendText(msg.to,"It is not in the black list")
                        ki5.sendText(msg.to,"It is not in the black list")
                        ki6.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        ki2.sendText(msg.to,"already")
                        ki3.sendText(msg.to,"already")
                        ki4.sendText(msg.to,"already")
                        ki5.sendText(msg.to,"already")
                        ki6.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        ki2.sendText(msg.to,"aded")
                        ki3.sendText(msg.to,"aded")
                        ki4.sendText(msg.to,"aded")
                        ki5.sendText(msg.to,"aded")
                        ki6.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        ki2.sendText(msg.to,"deleted")
                        ki3.sendText(msg.to,"deleted")
                        ki4.sendText(msg.to,"deleted")
                        ki5.sendText(msg.to,"deleted")
                        ki6.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        ki2.sendText(msg.to,"It is not in the black list")
                        ki3.sendText(msg.to,"It is not in the black list")
                        ki4.sendText(msg.to,"It is not in the black list")
                        ki5.sendText(msg.to,"It is not in the black list")
                        ki6.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
            	if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,helpMessage)
                    else:
                        cl.sendText(msg.to,helpt)
            elif msg.text in ["SetGroup","Set"]:
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,Setgroup)
                    else:
                        cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bot1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Bot1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bot2 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Bot2 gn ","")
                    ki2.updateGroup(X)
                else:
                    ki2.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bot3 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Bot3 gn ","")
                    ki3.updateGroup(X)
                else:
                    ki3.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
            	if msg.from_ in admin:
                    midd = msg.text.replace("Kick ","")
                    cl.kickoutFromGroup(msg.to,[midd])
            elif "Bot1 kick " in msg.text:
            	if msg.from_ in admin:
                    midd = msg.text.replace("Bot1 kick ","")
                    ki.kickoutFromGroup(msg.to,[midd])
            elif "Bot2 kick " in msg.text:
                midd = msg.text.replace("Bot2 kick ","")
                ki2.kickoutFromGroup(msg.to,[midd])
            elif "Bot3 kick " in msg.text:
                midd = msg.text.replace("Bot3 kick ","")
                ki3.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
            	if msg.from_ in admin:
                    midd = msg.text.replace("Invite ","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
            elif "Bot1 " in msg.text:
                midd = msg.text.replace("Bot1 invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Bot2 invite " in msg.text:
                midd = msg.text.replace("Bot2 invite ","")
                ki2.findAndAddContactsByMid(midd)
                ki2.inviteIntoGroup(msg.to,[midd])
            elif "Bot3 invite " in msg.text:
                midd = msg.text.replace("Bot3 invite ","")
                ki3.findAndAddContactsByMid(midd)
                ki3.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
            	if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    cl.sendMessage(msg)
            elif msg.text in ["Ki2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif msg.text in ["Ki3"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                ki2.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
            	if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '5'}
                    msg.text = None
                    cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Bot1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Bot2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                ki2.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Bot3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        if X.invitee is not None:
                            gInviMids = [contact.mid for contact in X.invitee]
                            cl.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"No one is inviting")
                            else:
                                cl.sendText(msg.to,"Sorry, nobody absent")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Can not be used outside the group")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv cancel","Bot cancel"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        G = ki3.getGroup(msg.to)
                        if G.invitee is not None:
                            gInviMids = [contact.mid for contact in G.invitee]
                            ki3.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                ki3.sendText(msg.to,"No one is inviting")
                            else:
                                ki3.sendText(msg.to,"Sorry, nobody absent")
                    else:
                        if wait["lang"] == "JP":
                            ki3.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Link on"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Done")
                        else:
                            cl.sendText(msg.to,"already open")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Can not be used outside the group")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot1 ourl","Bot1 link on"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Done ")
                        else:
                            ki.sendText(msg.to,"already open")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Can not be used outside the group")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot2 ourl","Bot2 link on"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = ki2.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki2.sendText(msg.to,"Done ")
                        else:
                            ki2.sendText(msg.to,"already open")
                    else:
                        if wait["lang"] == "JP":
                            ki2.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki2.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot3 ourl","Bot3 link on"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = ki3.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki3.sendText(msg.to,"Done ")
                        else:
                            ki3.sendText(msg.to,"already open")
                    else:
                        if wait["lang"] == "JP":
                            ki3.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki3.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Done")
                        else:
                            cl.sendText(msg.to,"already close")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Can not be used outside the group")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot1 curl","Bot1 link off"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = ki.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Done ")
                        else:
                            ki.sendText(msg.to,"already close")
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot2 curl","Bot2 link off"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = ki2.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki2.sendText(msg.to,"Done ")
                        else:
                            ki2.sendText(msg.to,"already close")
                    else:
                        if wait["lang"] == "JP":
                            ki2.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki2.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot3 curl","Bot3 link off"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = ki3.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki3.sendText(msg.to,"Done ")
                        else:
                            ki3.sendText(msg.to,"already close")
                    else:
                        if wait["lang"] == "JP":
                            ki3.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki3.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		replace=msg.text.lower().replace("jointicket ")
		if replace == "on":
			wait["atjointicket"]=True
		elif replace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            invitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Bmid)
                ki2.sendText(msg.to,Bmid)
                ki3.sendText(msg.to,Cmid)
                ki4.sendText(msg.to,Dmid)
                ki5.sendText(msg.to,Emid)
                ki6.sendText(msg.to,Fmid)
            elif "Mid" == msg.text:
                ki.sendText(msg.to,mid)
            elif "Bot1 mid" == msg.text:
                ki.sendText(msg.to,Amid)
            elif "Bot2 mid" == msg.text:
                ki2.sendText(msg.to,Bmid)
            elif "Bot3 mid" == msg.text:
                ki3.sendText(msg.to,Cmid)
            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Galon"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot1 rename "]:
                string = msg.text.replace("Bot1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot2 rename "]:
                string = msg.text.replace("Bot2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki2.getProfile()
                    profile_B.displayName = string
                    ki2.updateProfile(profile_B)
                    ki2.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Protect On","guest on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Protect Aktif")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Protect Aktif")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect Off","guest off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Protect Mati")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Protect Mati")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr protect on","Qr on"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Nyala")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Nyala")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr protect off","Qr off"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protecct QR Mati")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Mati")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
            	if msg.from_ in admin:
                    if wait["contact"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["contact"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
            	if msg.from_ in admin:
                    if wait["contact"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done ")
                    else:
                        wait["contact"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
            	if msg.from_ in admin:
                    if wait["autoJoin"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoJoin"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
            	if msg.from_ in admin:
                    if wait["autoJoin"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoJoin"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
            	if msg.from_ in admin:
                    try:
                        strnum = msg.text.replace("Gcancel:","")
                        if strnum == "off":
                            wait["autoCancel"]["on"] = False
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                            else:
                                cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                        else:
                            num =  int(strnum)
                            wait["autoCancel"]["on"] = True
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                            else:
                                cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                    except:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Value is wrong")
                        else:
                            cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
            	if msg.from_ in admin:
                    if wait["leaveRoom"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["leaveRoom"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
            	if msg.from_ in admin:
                    if wait["leaveRoom"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["leaveRoom"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
            	if msg.from_ in admin:
                    if wait["timeline"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["timeline"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
            	if msg.from_ in admin:
                    if wait["timeline"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["timeline"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
                            
            elif msg.text in ["GL"]:
                cl.updateGroups()
                arg = msg.split(' ')
                if sender.id in myfriend:
                    if arg[1] == 'group':
                        listG = []
                        gr = client.groups
                        for x in range(len(gr)):
                            listG.append(gr[x].name)
                            pass
                        listG.sort();
                        jo = '\n[*] '.join(str(l) for l in listG)
                    cl.sendText("[%s]\n %s" % (receiver.name, jo))
                else: 
                    cl.sendText("Mau lompat eaa")
                
            elif msg.text in ["Set View"]:
                md = ""
                if wait["Protectcancel"] == True: md+=" Protect Cancel : on\n"
                else: md+=" Protect Cancel : off\n"
                if wait["ProtectQR"] == True: md+=" Protect Qr      : on\n"
                else: md+=" Protect Qr   : off\n"
                if wait["Protectguest"] == True: md+=" Block Invite : on\n"
                else: md+=" Block Invite : off\n"
                if wait["contact"] == True: md+=" Contact    : on\n"
                else: md+=" Contact    : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave    : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share   : on\n"
                else:md+=" Share   : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                cl.sendText(msg.to,md)
                
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeâ†’" in msg.text:
                gid = msg.text.replace("album removeâ†’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
            	if msg.from_ in admin:
                    if wait["autoAdd"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoAdd"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
            	if msg.from_ in admin:
                    if wait["autoAdd"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoAdd"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
            	if msg.from_ in admin:
                    wait["message"] = msg.text.replace("Message change: ","")
                    cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
            	if msg.from_ in admin:
                    wait["message"] = msg.text.replace("Message add: ","")
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"message changed")
                    else:
                        cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
            	if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                    else:
                        cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
            	if msg.from_ in admin:
                    c = msg.text.replace("Comment:","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"message changed")
                    else:
                        wait["comment"] = c
                        cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
            	if msg.from_ in admin:
                    c = msg.text.replace("Add comment:","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"String that can not be changed")
                    else:
                        wait["comment"] = c
                        cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
            	if msg.from_ in admin:
                    if wait["commentOn"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"already on")
                    else:
                        wait["commentOn"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment off","Comment:off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
            	if msg.from_ in admin:
                    if wait["commentOn"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"already off")
                    else:
                        wait["commentOn"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
            	if msg.from_ in admin:
                    cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["url"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        x = cl.getGroup(msg.to)
                        if x.preventJoinByTicket == True:
                            x.preventJoinByTicket = False
                            cl.updateGroup(x)
                        gurl = cl.reissueGroupTicket(msg.to)
                        cl.sendText(msg.to,"line://ti/g/" + gurl)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Can't be used outside the group")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot2 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki2.updateGroup(x)
                    gurl = ki2.reissueGroupTicket(msg.to)
                    ki2.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot3 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki3.updateGroup(x)
                    gurl = ki3.reissueGroupTicket(msg.to)
                    ki3.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
            	if msg.from_ in admin:
                    if wait["jam"] == True:
                        cl.sendText(msg.to,"Jam menyala")
                    else:
                        wait["jam"] = True
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"(%H:%M)")
                        profile = cl.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
            	if msg.from_ in admin:
                    if wait["jam"] == False:
                        cl.sendText(msg.to,"Jam off")
                    else:
                        wait["jam"] = False
                        cl.sendText(msg.to,"Jam mati")
            elif msg.text in ["Jam update"]:
            	if msg.from_ in admin:
                    n = msg.text.replace("Jam update","")
                    if len(n.decode("utf-8")) > 13:
                        cl.sendText(msg.to,"changed")
                    else:
                        wait["cName"] = n
                        cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
            	if msg.from_ in admin:
                    if wait["Jam"] == True:
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"(%H:%M)")
                        profile = cl.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Clock Updated")
                    else:
                        cl.sendText(msg.to,"Aktifkan jamnya")
                       
            elif msg.text == "Set":
                    cl.sendText(msg.to, "Check sider")
                    ki.sendText(msg.to, "Check sider")
                    ki2.sendText(msg.to, "Check sider")
                    ki3.sendText(msg.to, "Check sider")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Check":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "T E R C Y D U K⏬%s\n\n⏬Yang Ngeliat doang⏬\n%sGa jelas lu liat apaan\nWaktu dan tanggal pembaca:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-----------------------------------------------
			
#------------------------------------------------

            elif msg.text in ["Sayang"]:
            	    if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif msg.text in ["1 join"]:
              if msg.from_ in admin:
                  X = ki.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  ki.updateGroup(X)
                  invsend = 0
                  Ti = ki.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["2 join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
            
            elif msg.text in ["3 join"]:
              if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByYicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki2.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["4 join"]:
              if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByYicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki3.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
           #Fungsi Tag all ----+++++++++#
                  
            elif msg.text in ["Summon, Tag all"]:
                group = cl.getGroup(msg.to)
                jw = [contact.mid for contact in group.members]
                cb = ""
	        cb2 = ""
                strt = int(0)
                akh = int(0)
                for rs in jw:
                    xname = cl.getContact(rs).displayName
                    xlen = int(len('x')+1)
                    akh = akh + xlen
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(rs)+"},"""
                    strt = strt + int(len('x')+3)
		    akh = akh + 2
		    cb2 += "@x \n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print error
                    
             #Finish----------+++++++++++++#

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Bot3 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Bye"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                    try:
                         ki.leaveGroup(msg.to)
                         ki2.leaveGroup(msg.to)
                         ki3.leaveGroup(msg.to)
                         ki4.leaveGroup(msg.to)
                         ki5.leaveGroup(msg.to)
                         ki6.leaveGroup(msg.to)
                    except:
                         pass
            elif msg.text in ["Bye 1"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.eaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye 2"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.laveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bot1 @bye"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            ki.leaveGroup(msg.to)
                        except:
                            pass
            elif msg.text in ["Bot2 @bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bot3 @bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ratakan" in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Ratakan","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("all","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = kk.getGroup(msg.to)
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                              targets.append(g.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:                           	
                            	if not target in Bots:
                            	  	if not target in admin:
		                                try:
		                                    klist=[cl,ki,kk,kc,]
		                                    kicker=random.choice(klist)
		                                    kicker.kickoutFromGroup(msg.to,[target])
		                                    print (msg.to,[g.mid])
		                                except:
		                                    ki.sendText(msg.to,"Sukses Bosqu")
		                                    kk.sendText(msg.to,"masih mauko sundala")
            elif msg.text in ["Kill"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        group = ki.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ki3.sendText(msg.to,"hahahahaha")
                            ki4.sendText(msg.to,"masih mauko")
                            ki5.sendText(msg.to,"sundala nu")
                            ki6.sendText(msg.to,"kodong di kick")
                            return
                        for jj in matched_list:
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5,ki6]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass
            elif "Ratakan" in msg.text:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        print "ok"
                        _name = msg.text.replace("Ratakan","")
                        gs = ki.getGroup(msg.to)
                        gs = ki2.getGroup(msg.to)
                        gs = ki3.getGroup(msg.to)
                        ki.sendText(msg.to,"Siap")
                        ki2.sendText(msg.to,"Bersedia")
                        ki3.sendText(msg.to,"Ratakan :v")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                            ki2.sendText(msg.to,"Not found.")
                            ki3.sendText(msg.to,"Not found.")
                        else:
                            for target in targets: 
                            	if not target in Bots:
                            	  	if not target in admin:
	                                    try:
	                                        klist=[ki,ki2,ki3,cl]
	                                        kicker=random.choice(klist)
	                                        kicker.kickoutFromGroup(msg.to,[target])
	                                        print (msg.to,[g.mid])
	                                    except:
	                                        ki.sendText(msg.to,"Rata Anjing")
	                                        ki2.sendText(msg.to,"hahahahaha")
	                                        ki3.sendText(msg.to,"Suck My Dick Sundala")
            elif "Nk " in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Nk ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                           targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 klist=[cl,ki,ki2,ki3,ki4,ki5,ki6]
                                 kicker=random.choice(klist)
                                 kicker.kickoutFromGroup(msg.to,[target])
                                 print (msg.to,[g.mid])
                             except:
                                 ki2.sendText(msg.to,"Succes ")
                                 ki3.sendText(msg.to,"Fuck You")
            elif "Bl @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Bl @","")
                    _kicktarget = _name.rstrip(' ')
                    gs = ki2.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _kicktarget == g.displayName:
                            targets.append(g.mid)
                            if targets == []:
                                cl.sendText(msg.to,"Not found")
                            else:
                                for target in targets:
                                    try:
                                        wait["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        ki.sendText(msg.to,"Succes")
                                    except:
                                        cl.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        print "[Banned]ok"
                        _name = msg.text.replace("Banned @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found ")
                        else:
                            for target in targets:
                            	if not target in Bots:
                            	  	if not target in admin:
		                                try:
		                                    wait["blacklist"][target] = True
		                                    f=codecs.open('st2__b.json','w','utf-8')
		                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
		                                    cl.sendText(msg.to,"Succes ")
		                                except:
		                                    cl.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        print "[Unban]ok"
                        _name = msg.text.replace("Unban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found ")
                        else:
                            for target in targets:
                            	if not target in Bots:
                            	  	if not target in admin:
		                                try:
		                                    del wait["blacklist"][target]
		                                    f=codecs.open('st2__b.json','w','utf-8')
		                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
		                                    cl.sendText(msg.to,"Succes ")
		                                except:
		                                	cl.sendText(msg.to,"Succes ")

#-----------------------------------------------
            elif msg.text in ["Test"]:
            	ki.sendText(msg.to,"Ok  􀨁􀄻double thumbs up􏿿")
                ki2.sendText(msg.to,"Ok  􀨁􀄻double thumbs up􏿿")
                ki3.sendText(msg.to,"Ok  􀨁􀄻double thumbs up􏿿")
                ki4.sendText(msg.to,"Ok  􀨁􀄻double thumbs up􏿿")
                ki5.sendText(msg.to,"Ok  􀨁􀄻double thumbs up􏿿")
                ki6.sendText(msg.to,"Ok  􀨁􀄻double thumbs up􏿿")
#-----------------------------------------------
            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
#-----------------------------------------------

            elif msg.text in ["say hi"]:
                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                ki2.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                ki3.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                ki4.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                ki5.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                ki6.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------

            elif msg.text in ["say hinata pekok"]:
                ki2.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                ki3.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                ki4.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["hai","hi","halo",]:
                ki2.sendText(msg.to,"Hai juga 􀜁􀅔Har Har􏿿")
                ki3.sendText(msg.to,"Halo")
                ki4.sendText(msg.to,"kikuk 􀜁􀅔Har Har􏿿")
            elif msg.text in ["say bobo ah","Bobo dulu ah"]:
                ki2.sendText(msg.to,"Have a nice dream  Har Har􏿿")
                ki3.sendText(msg.to,"Have a nice dream  Har Har􏿿")
                ki4.sendText(msg.to,"Have a nice dream  􀜁􀅔Har Har􏿿")
            elif msg.text in ["say chomel pekok"]:
                ki2.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                ki3.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                ki4.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Selamat datang !!")
                ki2.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki2.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ki3.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ki4.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------
            elif msg.text in ["Respon","respon"]:
            	ki.sendText(msg.to,"Ready")
                ki2.sendText(msg.to,"Ready")
                ki3.sendText(msg.to,"Ready")
                ki4.sendText(msg.to,"Ready")
                ki5.sendText(msg.to,"Ready")
                ki6.sendText(msg.to,"Ready")
#-----------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
            	if msg.from_ in admin:
                    start = time.time()
                    cl.sendText(msg.to, "Progress...")
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki3.sendText(msg.to, "%sseconds" % (elapsed_time))
                    #ki4.sendText(msg.to, "%sseconds" % (elapsed_time))
                    #ki5.sendText(msg.to, "%sseconds" % (elapsed_time))
                    #ki6.sendText(msg.to, "%sseconds" % (elapsed_time))

#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
            	if msg.from_ in admin:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unbanned"]:
            	if msg.from_ in admin:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"send contact")
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban","Bunuh"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        ki.sendText(msg.to,"There was no blacklist user")
                        ki2.sendText(msg.to,"There was no blacklist user")
                        ki3.sendText(msg.to,"There was no blacklist user")
                        ki4.sendText(msg.to,"There was no blacklist user")
                        ki5.sendText(msg.to,"There was no blacklist user")
                        ki6.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        ki2.kickoutFromGroup(msg.to,[jj])
                        ki3.kickoutFromGroup(msg.to,[jj])
                        ki4.kickoutFromGroup(msg.to,[jj])
                        ki5.kickoutFromGroup(msg.to,[jj])
                        ki6.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist")
                    ki.sendText(msg.to,"emang")
                    ki2.sendText(msg.to,"pantas")
                    ki3.sendText(msg.to,"tuk")
                    ki4.sendText(msg.to,"di")
                    ki5.sendText(msg.to,"usir")
                    ki6.sendText(msg.to,"hahaha")
            elif msg.text in ["Clear"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(msg.to,[_mid])
                        cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random:" in msg.text:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        strnum = msg.text.replace("random:","")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                        try:
                            num = int(strnum)
                            group = cl.getGroup(msg.to)
                            for var in range(0,num):
                                name = "".join([random.choice(source_str) for x in xrange(10)])
                                time.sleep(0.01)
                                group.name = name
                                cl.updateGroup(group)
                        except:
                            cl.sendText(msg.to,"Error")
            elif "albumâ†’" in msg.text:
                try:
                    albumtags = msg.text.replace("albumâ†’","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = ki2.getProfile()
                profile3.displayName = wait["cName3"]
                ki2.updateProfile(profile3)

                profile3 = ki3.getProfile()
                profile3.displayName = wait["cName3"]
                ki3.updateProfile(profile3)

                profile3 = ki4.getProfile()
                profile3.displayName = wait["cName3"]
                ki4.updateProfile(profile3)

                profile3 = ki5.getProfile()
                profile3.displayName = wait["cName3"]
                ki5.updateProfile(profile3)
                
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile4 = ki6.getProfile()
                profile4.displayName = wait["cName4"] + nowT
                ki6.updateProfile(profile4)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
     for zx in range(0,50):
        hasil = cl.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == True:
          try:    
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by : Reina\n\nhttp://line.me/ti/p/~muhmursalind")
            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by : Reina\n\nhttp://line.me/ti/p/~muhmursalind")
            ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by : Reina\n\nhttp://line.me/ti/p/~muhmursalind")
            ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by : Reina\n\nhttp://line.me/ti/p/~muhmursalind")
            ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by : Reina\n\nhttp://line.me/ti/p/~muhmursalind")
            ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by : Reina\n\nhttp://line.me/ti/p/~muhmursalind")
            ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by : Reina\n\nhttp://line.me/ti/p/~muhmursalind")
            print "Like"
          except:
            pass
        else:
            print "Already Liked"
     time.sleep(600)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
