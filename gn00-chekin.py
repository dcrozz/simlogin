#created by ukeyim 2015 Fri 10 Jul
#This python script is used to auto checkin to the gn00.com
#crontab will be added soon

import requests

s = requests.Session()
loginurl = 'http://www.gn00.com/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=LK7x4&inajax=1'
post = {
   'username':''
   'password':''}
s.post(loginurl,data=post)
checkin = 'http://www.gn00.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1'
mood = {
'fastreply':'0',
'formhash':'e4007e7e',
'qdmode':'3',
'qdxq':'kx',
'todaysay':''
}
headers = {
'Host': 'www.gn00.com',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Referer': 'http://www.gn00.com/plugin.php?id=dsu_paulsign:sign',
'Cookie': '0ncN_2132_saltkey=uCA0I2L1; 0ncN_2132_lastvisit=1435848409; pgv_pvi=236723464; Hm_lvt_8392588571de614afd983a8226d83e07=1435880818,1436408695,1436477347; 0ncN_2132_ulastactivity=1436461399%7C0; 0ncN_2132_lastcheckfeed=237096%7C1436448549; 0ncN_2132_connect_is_bind=1; 0ncN_2132_nofavfid=1; 0ncN_2132_reminder=237096D1D1_1_1; 0ncN_2132_lastact=1436461638%09plugin.php%09; 0ncN_2132_myrepeat_rr=R0; 0ncN_2132_connect_last_report_time=2015-07-10; pgv_info=ssi=s1274525000; Hm_lpvt_8392588571de614afd983a8226d83e07=1436490343; 0ncN_2132_lastsubset=2; 0ncN_2132_auth=37a0%2Fo2k8tKn7ahjLwroXEUqUEH6UvHurqFdaSOR6UCm28p7AuPgAPkXsuJUPGA7YhhnfW%2BhdXKjuhxVRtmDYtJKoHM; 0ncN_2132_lip=101.228.212.38%2C1436448549; 0ncN_2132_security_cookiereport=80e5iNabBDCHArgvKv9kuC5aMjzunQ0y4RiOER4F1hSdFxJ2Y%2BR6; 0ncN_2132_sendmail=1',
'Connection': 'keep-alive'
}
r = s.post(checkin,data = mood,headers = headers)
print r.url
