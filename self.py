# -*- coding: utf-8 -*-

# Lib edition 0.9.3/Tanysyz
import HelloWorld
from HelloWorld.lib.Gen.ttypes import *
from datetime import datetime
from Helper.main import qr
from time import sleep
from bs4 import BeautifulSoup
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz
import wikipedia, urllib
from gtts import gTTS
from googletrans import Translator

botStart = time.time() 

cl = HelloWorld.LINE()
cl.login(token=qr().get())
cl.loginResult()

#cl = HelloWorld.LINE()
#cl.login("EMAILMU","PASSWORD")
#cl.loginResult()

#cl = HelloWorld.LINE()
#cl.login(token="tokenmu")
#cl.loginResult()

print "[    Login Success    ]"
reload(sys)
sys.setdefaultencoding('utf-8')
mid = cl.getProfile().mid
key = ""

message = {
    "replyPesan1":"แทคทำไมคับ? มีไรทักส่วนตัวเลย..(-..-) เดะปั๊ดจับดูดปาก",
    "replyPesan2":"แทคอีกแระ? จิแทคเอาโล่รึไง..(-..-) เดะปั๊ดจับปี้ซะนี่",
}

settings = {
    "autoJoin":False,
    "autoAdd":False,
    "autoRead":False,
    "autoLeaveRoom":False,
    "checkContact":False,
    "checkPost":False,
    "responMention":True,
    "simiSimi":{},
	"userAgent": [
		"Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
		"Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
		"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
	],
}
    
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{}
}

mimic = {
    "copy":False,
    "status":False,
    "target":{}
    }
    
setTime = {}
setTime = read['readTime']

contact = cl.getProfile()
restoreprofile = cl.getProfile()
restoreprofile.displayName = contact.displayName
restoreprofile.statusMessage = contact.statusMessage                        
restoreprofile.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:   
        import urllib,request   
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                     
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)    
            time.sleep(0.1)   
            page = page[end_content:]
    return items

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    try:
        cl.sendMessage(msg)
    except Exception as error:
        print error
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)     

#==============================================================================#
#==============================================================================#
#==============================================================================#
def helpmessage():
    helpMessage ="""╔══════════════════ 
║  🌾RED BOT LINE THAILAND🌾
║    ─┅═✥👊ᵀᴴᴬᴵᴸᴬᴺᴰ👊✥═┅─
║       💀[RED SAMURI BOT]💀
╠══════════════════ 
║      ─┅═✥🌿คำสั่ง ทั่วไป🌿✥═┅─ 
╠══════════════════ 
╠❂➣ [Id]ไอดีเรา
╠❂➣ [Mid] เอาเอมไอดีเรา
╠❂➣ [Me] ส่งคทตัวเอง
╠❂➣ [TL 「Text」โพสบนทามไลน์
╠❂➣ [MyName]เปลี่ยนชื่อ
╠❂➣ [Gift] สงของขวัญ
╠❂➣ [Mid 「mid」
╠❂➣ [Group id]
╠❂➣ [Group cancel]
╠❂➣ [album 「id」]
╠❂➣ [Hapus album 「id」
╠❂➣ [เปิดคท] เปิด คท
╠❂➣ [ปิดคท] ปิด คท
╠❂➣ [เปิดเข้า] เปิดเข้าห้องอัตโมัติ
╠❂➣ [ปิดเข้า] ปิดเข้าห้องอัตโมัติ
╠❂➣ [Group cancel] ลบรัน
╠❂➣ [เปิดออก] เปิดไม่เข้าแชทรวม
╠❂➣ [ปิดออก] เข้าแชทรวม
╠❂➣ [เปิดแอด/ปิดแอด] เปิด/ปิดรับเพื่อน
╠❂➣ [Jam on]] เปิดชื่อนาฬิกา
╠❂➣ [Jam off] ปิดชื่อนาฬิกา
╠❂➣ [red say ] ส่งข้อความ
╠❂➣ [Up] อัพเดชชื่อ
╠❂➣ [Ban:on] เปิดสั่งแบน
╠❂➣ [Unban:on] เปิดแก้แบน
╠❂➣ [Banlist] เช็ครายชื่อโดนแบน
╠❂➣ [เปิดเม้น] เปิดคอมเม้น
╠❂➣ [ปิดเม้น] ปิดคอมเม้น
╠❂➣ [Com set:] ตั้งค่าคอมเม้น 
╠❂➣ [Mcheck] เช็คแบน
╠❂➣ [Conban,Contactban] ส่งคท คนโดนแบน
╠❂➣ [Cb]
╠❂➣ [Clear ban] ล้างแบน
╠❂➣ [พูด  ] สั่งเซลพูด
╠❂➣ [Message Confirmation] ยืนยันข้อความ
╠❂➣ [Mybio: 「Iตัส] เปลี่บนตัส
╠❂➣ [Key]
╠══════════════════ 
║•─✯͜͡ ✯RED★SAMURI★SELFBOT✯͜͡ ✯─•
╠══════════════════
╠http//:line.me/ti/p/~samuri5
╚══════════════════ """
    return helpMessage

def myself():
    Myself ="""
╠══════════════════ 
║─┅═✥🌿คำสั่งสายขาว🌿✥═┅─  
╠══════════════════ 
╠❂➣ [Copy @] ก๊อปโปรไฟล์
╠❂➣ [Kembali] กลับคืนร่าง
╠❂➣ [ส่องรูป @] ดูรูปปนะจำตัว
╠❂➣ [ส่องปก @] ดูรูปปก
╠❂➣ [จับ] ต้้งค่าคนอ่าน
╠❂➣ [อ่าน] ดูคนอ่าน
╠❂➣ [เปิดอ่าน] เปิดการอ่าน
╠❂➣ [ปิดอ่าน] ปิดการอ่าน
╠❂➣ [อ่าน] ดูคนอ่าน
╠❂➣ [ใครแทค] แทกชื่อสมาชิก
╠❂➣ [Sider on/off][จับคนอ่านแบบเรียงตัว]
╠❂➣ [ยกเลิกเชิญ] ลบค้างเชิญ 
╠❂➣ [Gbroadcast] ประกาศกลุ่ม
╠❂➣ [Cbroadcast] ประกาศแชท
╠❂➣ [siri (ใส่ข้อความ)]
╠❂➣ [siri: (ใส่ข้อความ)]
╠══════════════════ 
║•─✯͜͡ ✯RED★SAMURI★SELFBOT✯͜͡ ✯─•
╠══════════════════
╠http//:line.me/ti/p/~samuri5
╚══════════════════ """
    return Myself

def helpgroup():
    helpGroup ="""
╠══════════════════ 
╠❂➣ [Url][ขอลื้งกลุ่ม]
╠❂➣ [Cancel][ยกค้างเชิญ]
╠❂➣ [Gcreator][ผู้สร้างกลุ่ม]
╠❂➣ [Gname:][เปลี่ยนชื่อกลุ่ม]
╠❂➣ [Infogrup][ดูข้อมูลกลุ่ม]
╠❂➣ [Gruplist][ดูรูปกลุ่ม]
╠❂➣ [ออก:][+จำนวนกลุ่มที่จะปฏิเสธ]
╠❂➣ [ออก:off][ปิดปฏิเสธการเชิญเข้ากลุ่ม]
╠❂➣ [playstore (text)][เซิร์ในเพลสโต]
╠❂➣ [Profileig (username)]
╠❂➣ [wikipedia (text)][เซิร์ทในเว็บ]
╠❂➣ [idline (text)][เชิร์ทไอดีไลน์]
╠❂➣ [ytsearch  (text)][เซิรทในยูทูป]
╠❂➣ [Time][ดูเวลา]
╠❂➣ [lirik (text)]
╠══════════════════ 
║•─✯͜͡ ✯RED★SAMURI★SELFBOT✯͜͡ ✯─•
╠══════════════════
╠http//:line.me/ti/p/~samuri5
╚══════════════════"""
    return helpGroup

def helpsettings():
    helpSettings ="""
╠══════════════════ 
╠❂➣ [เช็ค1][]
╠❂➣ [เช็ค2][]
╠❂➣ [เปิดแชร์/ปิดแชร์][]
╠❂➣ [เปิดเม้น/ปิดเม้น][]
╠❂➣ [เปิดคท/ปิดคท][]
╠❂➣ [เปิดเข้า/ปิดเข้า][]
╠❂➣ [เปิดออก/ปิดออก][]
╠❂➣ [เปิดแอด/ปิดแอด][]
╠❂➣ [เปิดไลค์/ปิดไลค์][]
╠❂➣ [like friend][]
╠❂➣ [respon on/off][]
╠❂➣ [read on/off][]
╠❂➣ [simisimi on/off][]
╠❂➣ [Kicktag on/off][]
╠❂➣ 
╠══════════════════ 
║•─✯͜͡ ✯RED★SAMURI★SELFBOT✯͜͡ ✯─•
╠══════════════════
╠http//:line.me/ti/p/~samuri5
╚══════════════════"""
    return helpSettings

def helpmedia():
    helpMedia ="""╠══════════════════ 
╠❂➣ [Kalender][thex]
╠❂➣ [CheckDate][thex]
╠❂➣ [YoutubeSearch][thex]
╠❂➣ [ImageSearch][thex
╠❂➣ [Music (text)][เซิรทในยูทูป]]
╠❂➣ [ProfileIg][thex]
╠❂➣ [playstore (text)][เซิร์ในเพลสโต]
╠❂➣ [Profileig (username)]
╠❂➣ [wikipedia (text)][เซิร์ทในเว็บ]
╠❂➣ [idline (text)][เชิร์ทไอดีไลน์]  
╠❂➣ [Time][ดูเวลา]
╠❂➣ [lirik (text)]
╠══════════════════ 
║•─✯͜͡ ✯RED★SAMURI★SELFBOT✯͜͡ ✯─•
╠══════════════════
╠http//:line.me/ti/p/~samuri5
╚══════════════════"""
    return helpMedia
    
def helptexttospeech():
    helpTextToSpeech ="""╔══════════════════
║       🎀✨คำสั่งใช้ลบรัน✨🎀
╠══════════════════
║✰ลบรัน      ➠เซลบอทลบรัน
║✰ลบแชท        ➠เซลบอทลบแชต
╠══════════════════
║       ✦เปิด/ปิดข้อความต้อนรับ✦
╠══════════════════
║✰ Thx1 on ➠เปิดข้อความต้อนรับ
║✰ Thx1 off ➠ปิดข้อความต้อนรับ
║✰ Thx2 on ➠เปิดข้อความออกกลุ่ม
║✰ Thx2 off ➠เปิดข้อความออกกลุ่ม
║✰ Thx3 on ➠เปิดข้อความคนลบ
║✰ Thx3 off ➠เปิดข้อความคนลบ
║✰ M on ➠เปิดเเจ้งเตือนตนเอง
║✰ M off ➠ปิดเเจ้งเตือนตนเอง
║✰ Tag on ➠เปิดกล่าวถึงเเท็ค
║✰ Tag off ➠ปิดกล่าวถึงเเท็ค
║✰ Kicktag on ➠เปิดเตะคนเเท็ค
║✰ Kicktag off ➠ปิดเตะคนเเท็ค
╠══════════════════
║         ⌚โหมดตั้งค่าข้อความ⌚
╠══════════════════
║✰ Thx1˓: ➠ไส่ข้อความต้อนรับ
║✰ Thx2˓: ➠ไส่ข้อความออกจากกลุ่ม
║✰ Thx3˓: ➠ไส่ข้อความเมื่อมีคนลบ
╠══════════════════
║✰ Thx1 ➠เช็คข้อความต้อนรับ
║✰ Thx2 ➠เช็คข้อความคนออก
║✰ Thx3 ➠เช็คข้อความคนลบ
╠═════════════════
║            ─┅═✥ᵀᴴᴬᴵᴸᴬᴺᴰ✥═┅─
║ •─✯͜͡ ✯RED★SAMURI★SELFBOT✯͜͡ ✯─•
╠══════════════════"""
    return helpTextToSpeech
    
    
def helptranslate():
    helpTranslate ="""
╠══════════════════ 
╠❂➣ [Id @en]
╠❂➣ [En @id]
╠❂➣ [Id @jp]
╠❂➣ [Jp @id]
╠❂➣ [Id @th]
╠❂➣ [Th @id]
╠❂➣ [Id @ar]
╠❂➣ [Ar @id]
╠❂➣ [Id @ko]
╠❂➣ [Ko @id]
╠❂➣ [Say-id]
╠❂➣ [Say-en]
╠❂➣ [Say-jp]
╠❂➣ [พูด ][ข้อความ]
╠══════════════════ 
║•─✯͜͡ ✯RED★SAMURI★SELFBOT✯͜͡ ✯─•
╠══════════════════
╠http//:line.me/ti/p/~samuri5
╚══════════════════"""
    return helpTranslate
#==============================================================================#
#==============================================================================#
#==============================================================================#
def bot(op):
    try:
        if op.type == 0:
            return
#==============================================================================#
#==============================================================================#
#==============================================================================# 
        if op.type == 5:
            if settings["autoAdd"] == True: 
                cl.findAndAddContactsByMid(op.param1)
                xname = cl.getContact(op.param1).displayName
                cl.sendText(op.param1, "Halo " + xname + " ,terimakasih telah menambahkan saya sebagai teman :3")
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
        if op.type == 22:
            if settings["autoLeaveRoom"] == True:
                cl.sendText(op.param1, "Goblok ngapain invite gw")
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if settings["autoLeaveRoom"] == True:
                cl.sendText(op.param1, "Goblok ngapain invite gw")
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if settings["checkContact"] == True:
                    try:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        cover = cl.channel.getCover(msg.contentMetadata["mid"]) 
                        path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        try:
                            cl.sendImageWithURL(msg.to, str(path))
                        except:
                            pass
                        ret_ = "╔══[ Details Contact ]"
                        ret_ += "\n╠ Nama : {}".format(str(contact.displayName))
                        ret_ += "\n╠ MID : {}".format(str(msg.contentMetadata["mid"]))
                        ret_ += "\n╠ Bio : {}".format(str(contact.statusMessage))
                        ret_ += "\n╠ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        ret_ += "\n╠ Gambar Cover : {}".format(str(cover))
                        ret_ += "\n╚══[ Finish ]"
                        cl.sendText(msg.to, str(ret_))
                    except:
                        cl.sendText(msg.to, "Kontak tidak valid")
            if msg.contentType == 16:
                if wait["checkPost"] == True:
                    msg.contentType = 0
                    msg.text = "URL : \n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            if 'MENTION' in msg.contentMetadata.keys()!=None:
                 if settings["responMention"] == True:
                    names = re.findall(r'@(\w+)',msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in mid:
                            xname = cl.getContact(msg.from_).displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            balas = "@" + xname + " " + str(message["replyPesan1"]),"@" + xname + " " + str(message["replyPesan2"])
                            msg.text = balas
                            msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(msg.from_)+'}]}','EMTVER':'4'}
                            cl.sendMessage(msg)
            if settings["autoRead"] == True:
                cl.sendChatChecked(to, msg_id)
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, data['result']['response'].encode('utf-8'))
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)
#==============================================================================#
#==============================================================================#
#==============================================================================#
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                return            
            if msg.contentType == 16:
                if wait["checkPost"] == True:
                    msg.contentType = 0
                    msg.text = "URL : \n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
#==============================================================================#
#==============================================================================#
#==============================================================================#
            if msg.contentType == 0:
                if msg.text == None:
                    return

              

#==============================================================================#
#==============================================================================#
#==============================================================================#
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
#                            Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "ฮั่นแน่ " + "☞ " + Name + " ☜" + "\nรู้นะว่าอ่านอยู่. . .\nออกมาคุยเดี๋ยวนี้ (-__-)   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                        cl.sendText(op.param1, "ฮั่นแน่ " + "☞ " + Name + " ☜" + "\nนี่ก็อีกคน. . .อ่านอย่างเดียวเลย\nไม่ออกมาคุยล่ะ (-__-)   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                    cl.sendText(op.param1, "ฮั่นแน่ " + "☞ " + Name + " ☜" + "\nแอบกันจังเลยนะ???\nคิดว่าเป็นนินจารึไง...??😆😆   ")
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
           
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                        json.dump(read, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            
        if op.type == 59:
            print op
            
    except Exception as error:
        print error

while True:
	bot(cl.Poll.stream(500000))
