import urllib.request
import random
import re
import time
import requests
import socket
import urllib.error
timeout =5
sleep_download_time =3
file_path="domain.txt"
print("please input the url that you want to get:")
main_url= input()
jubing=open("domain.txt")
url=[]
domain=[]
for i in range(0,200):
    second_url = jubing.readline()
    second_url=second_url.strip('\n')
    url.append(str("http://")+str(second_url)+str(".")+str(main_url)+str("/"))
for i in range(len(url)):
    try:
        s_url=str(url[i])
        s=requests.session()
        # time.sleep(sleep_download_time)
        html=s.head(s_url)
        if "200" in str(html.status_code):
             print("domain:"+s_url)
             domain.append(s_url)
        elif "302" in str(html.status_code):
            print("domain:" + s_url+"---302")
        elif "404" in str(html.status_code):
            print("domain:"+s_url+"---404")
        else:
            pass

    except UnicodeDecodeError as e:
        print('---UnicodeDecodeerror url',s_url)
    except urllib.error.URLError as e:
        print('---urllib.error.URLError:',s_url)
    except socket.timeout as e:
        print('---socket.timeout:',s_url)
    except socket.gaierror as e:
        print('socket.gaierror:',s_url)
    except requests.exceptions.ConnectionError as e:
        print('---requests.exceptions.ConnectionError:',s_url)
print(domain)





