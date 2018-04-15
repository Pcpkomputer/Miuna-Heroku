import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse
import re
from re import *
import sys
import subprocess
import string
import os
from subprocess import Popen, PIPE, STDOUT
import glob, os

client = Bot(description="??????????????", command_prefix=".", pm_help = False)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	return await client.change_presence(game=discord.Game(name='Node.JS'))

@client.command()
async def aise(x, *z):
        if x=='baru':
                nama=re.compile(r"<h2 class=\"episodeye\">.*title=\"(.+)\">")
                tautan = 'https://aise.fansub.web.id'
                halaman = urlopen(tautan)
                ah=BeautifulSoup(halaman, 'html.parser')
                nama_01=nama.findall(str(ah))
                await client.say('```Rilisan terbaru : '+nama_01[0]+'```')
                await client.say("`Gunakan perintah: .aise getlink 0 untuk mengambil tautan`")

        if x=='list':
                nama=re.compile(r"<h2 class=\"episodeye\">.*title=\"(.+)\">")
                tautan = 'https://aise.fansub.web.id'
                halaman = urlopen(tautan)
                ah=BeautifulSoup(halaman, 'html.parser')
                nama_01=nama.findall(str(ah))
                tabel1=[]
                index=-1
                for x in nama_01:
                    index=index+1
                    tabel1.append("["+str(index)+"] "+x+"\n")
                luist="".join(tabel1)
                await client.say('```'+luist+'```')
                await client.say("`Gunakan perintah: .aise getlink [index] untuk mengambil tautan`")
        if x=='getlink':
                tautan = 'https://aise.fansub.web.id'
                halaman = urlopen(tautan)
                ah=BeautifulSoup(halaman, 'html.parser')
                link=re.compile(r"<h2 class=\"episodeye\">.*<a href=\"(.+)\" title")
                link_01=link.findall(str(ah))
                perpusindo=re.compile(r"(http:\/\/www.perpusindo.info\/.*)\">")
                mirrorcreator=re.compile(r'\"(https:\/\/www.mirrorcreator.com.*)\"\s*rel')
                tautanx = link_01[int(z[0])]
                halamanx = urlopen(tautanx)
                ahx=BeautifulSoup(halamanx, 'html.parser')
                #if mirrorcreator.match(str(ahx)):
                #        hmm1=mirrorcreator.findall(str(ahx))
                #        hasil=hmm1[0]
                #        await client.say(hasil)
                
                hmm=re.search(perpusindo,str(ahx))
                hasil=hmm.group(1)
                #boi="".join(hmm1)
                await client.say(hasil)
               
        
@client.command(pass_context=True)
async def an8(ctx, x, *z):
        try:
                if x=='baru':
                        regex = re.compile(r"<td>(\d)</td>\s*<.*>(.*)\s*</td>\s*<.*>(.*)</td>\s*</tr>\s*<!--Posting-->")
                        tautan = 'http://garismiring-an8.github.io/index.html'
                        halaman = urlopen(tautan)
                        ah=BeautifulSoup(halaman, 'html.parser')
                        tabel = re.search(regex,str(ah))
                        no = tabel.group(1)
                        rilisan = tabel.group(2)
                        ukuran = tabel.group(3)+'MB'
                        togel=int(no)
                        string='''```
Rilisan paling terbaru!
No :'''+no+'''
Berkas :'''+rilisan+'''
Ukuran :'''+ukuran+'''
```'''
                        await client.say(string)
                        await client.say("`Gunakan perintah: .an8 getlink "+str(togel)+" untuk mengambil tautan`")
                #else:
                        #await client.say("`Perintah tidak ditemukan!`")

                elif x=='list':
                        listregex = re.compile(r"<td class=\"name\">(.*)\s*</td>")
                        tautan = 'http://garismiring-an8.github.io/index.html'
                        halaman = urlopen(tautan)
                        ah=BeautifulSoup(halaman, 'html.parser')
                        xxx=listregex.findall(str(ah))
                        duar=0
                        hasil=[]
                        for x in xxx:
                            duar=duar+1
                            hasil.append('['+str(duar)+']'+x+'\n')
                        b=''.join(hasil)
                        await client.say("```"+b+"```")
                        await client.say("`Gunakan perintah: .an8 getlink [index] untuk mengambil tautan`")
                elif x=='getlink':
                        ##############
                        listregex = re.compile(r"<td class=\"name\">(.*)\s*</td>")
                        tautan = 'http://garismiring-an8.github.io/index.html'
                        halaman = urlopen(tautan)
                        ah=BeautifulSoup(halaman, 'html.parser')
                        boom=listregex.findall(str(ah))
                        a=0
                        for l in boom:
                            a+=1
                        #############
                        #if int(z[0])>a:
                        #    await client.say("`Index enggak nyampe sana GBLKKK!!!!!`")
                        regetlink=re.compile(r"<tr class=\"\" kode=\"..(.*)\">\s*<td>"+z[0]+"</td>")
                        tautan = 'http://garismiring-an8.github.io/index.html'
                        halaman = urlopen(tautan)
                        ah=BeautifulSoup(halaman, 'html.parser')
                        cari=re.search(regetlink,str(ah))
                        dude="https://drive.google.com/file/d/"+cari.group(1)
                        await client.say(dude)
                        
                else:
                        await client.say("`Perintah tidak ditemukan!`")
        except Exception as l:
                await client.say("`????????????????????????`")
                print(l)
                
                
        
client.run(process.env.BOT_TOKEN)

