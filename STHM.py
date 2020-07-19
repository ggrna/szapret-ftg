from telethon import events 
from .. import loader, utils 
import os 
import requests 
from PIL import Image,ImageFont,ImageDraw 
import re 
import io 
from textwrap import wrap 

def register(cb): 	
              cb(StathamMod()) 	 
class StathamMod(loader.Module):     	               
               ""Стэтхем""" 	
               strings = { 
                       'name': 'Стэтхем', 		
                       'usage': 'Напиши <code>.help Стэтхем</code> ', 	
                 } 	
               def __init__(self): 	
                   	self.name = self.strings['name'] 		
                       self._me = None 		  
                       self._ratelimit = [ ] 	
               async def client_ready(self, client, db): 		
                        self._db = db 	
                    	self._client = client 		
                        self.me = await client.get_me() 		 	    
               async def jcmd(self, message): 		
                        """.sth <реплай на сообщение/свой текст>\прикол он вообще работает ахаха"""
                     	ufr = requests.get("https://github.com/ggrna/szapret-ftg/raw/master/open-sans.ttf")
                 	f = ufr.content 

                     	reply = await message.get_reply_message() 		
                        args = utils.get_args_raw(message) 	
                      	if not args: 
                      		if not reply: 		
                         		await utils.answer(message, self.strings('usage', message))
                             	   	return
                                else: 	
		                    	txt = reply.raw_text 		                                                                                           			         			
                        else: 	
	                             	txt = utils.get_args_raw(message)
                                await message.edit("<b>Стэтхем говорит...</b>") 		     
                                pic = requests.get("https://www.meme-arsenal.com/memes/62e8c3029ab4aaa0db3ea9ae2c51c5b7.jpg") 		
                                pic.raw.decode_content = True
                            	img = Image.open(io.BytesIO(pic.content)).convert("RGB") 
	                        W, H = img.size 
                         	#txt = txt.replace("\n", "𓃐")
                         	text = "\n".join(wrap(txt, 19)) 
		                t = text + "\n" 		
                                #t = t.replace("𓃐","\n") 		     
                                draw = ImageDraw.Draw(img) 		          
                                font = ImageFont.truetype(io.BytesIO(f), 32, encoding='UTF-8') 	
                             	w, h = draw.multiline_textsize(t, font=font) 	
                             	imtext = Image.new("RGBA", (w+20, h+10), (0, 0,0,0)) 	
                             	draw = ImageDraw.Draw(imtext) 		                              
                                draw.multiline_text((10, 10),t,(225,225,225),font=font, align='center') 	
                             	imtext.thumbnail((W, H)) 		                              
                                 w, h = imtext.size	
                             	img.paste(imtext, (10,10), imtext) 	
                             	out = io.BytesIO() 		                              
                                out.name = "out.jpg" 		
                                img.save(out)
 	                           out.seek(0) 	
                             	await message.client.send_file(message.to_id, out, reply_to=reply) 
	                        await message.delete()