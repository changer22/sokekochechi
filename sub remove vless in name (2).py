import requests
import urllib
import json
import re
import pickle
import base64
import string    
import random
def gen_rand(l=8):
    randomstr = ''.join(random.choices(string.ascii_uppercase + string.digits, k = l))
    return str(randomstr)
url_back = "/xui/inbound/list"
data_uni = {
    "Host": "159.69.189.163:1414",
    "Cookie": "session=MTY2OTg5MzQ4MXxEdi1CQkFFQ180SUFBUkFCRUFBQVpmLUNBQUVHYzNSeWFXNW5EQXdBQ2t4UFIwbE9YMVZUUlZJWWVDMTFhUzlrWVhSaFltRnpaUzl0YjJSbGJDNVZjMlZ5XzRNREFRRUVWWE5sY2dIX2hBQUJBd0VDU1dRQkJBQUJDRlZ6WlhKdVlXMWxBUXdBQVFoUVlYTnpkMjl5WkFFTUFBQUFHXy1FR0FFQ0FRVmhaRzFwYmdFTVQyMWxaMkZBTkRRNFFIWXlBQT09fGpJ8UYvdZesP7-jnw-Lnwd_ODKbDFRYbJlT3AVAPZhq"
}
pic_file=pickle.load(open("DONT_REMOVE_THIS","rb"))
proxy_port=pic_file["proxy-port"]
ips=[]
urls=[]
datas=[]
names=[]
def update_data():
    global pic_file
    global ips
    global names
    global urls
    global datas
    ips=[]
    urls=[]
    datas=[]
    names=[]
    for srv_data in pic_file["servers"]:
        names.append(srv_data["name"])
        ips.append(srv_data["ip"])
        urls.append("https://"+srv_data["ip"]+":"+srv_data["port"]+url_back)
        datas.append({
        "Host": srv_data["ip"]+":"+srv_data["port"],
        "Cookie": "session="+srv_data["co"]})
    return None
update_data()
proxy_addr='http://127.0.0.1:'+proxy_port
proxy={'http':proxy_addr}
action=0
while action != 4:
    print("script is running!\nselect the action:")
    print("1- vmees function")
    print("2- edit proxy port")
    print("3- server manager")
    print("4- EXIT")
    action=int(input("option number: "))
    if action == 1:
        for srv in range(0,len(names)):
            print (str(srv+1)+" - "+names[srv]+" ("+ips[srv]+")")
        p_number=int(input("choose a pannel to connect: "))-1
        if p_number<len(names):
            response = requests.post(urls[p_number], headers=datas[p_number],proxies=proxy)
            ans = json.dumps(response.text)
            ans=ans.replace("\\n","").replace("\\","").replace(" ","")
            ports=(re.findall("port.*?]",ans))
            acc = {}
            for port in ports:
                acc[re.findall('''port":([0-9]{1,5})''',port)[0]]=re.findall('''{"id":".{36}".*?}''',port)

            menue=[]
            for port in acc.keys():
                menue.append(str(port))
            for port in range(0,len(menue)):
                print(str(int(port)+1)+" : "+str(menue[port]))
            select_port=int(input("enter port number\n"))-1
            datass=(acc[menue[select_port]])
            print(str(len(datass))+" account's in this port.\nwhat do with them?\n1- generate vmess link\n2- create sub files")
            cr_op=int(input("enter option number:"))
            print("\n\n\n\n")
            if cr_op==1:
                lis=datass
                for i in lis:
                    t='''vless://mainuid@mci.hostgozarr.com:443?path=%2Fdownloader%2Fmainport&security=tls&encryption=none&host=mainhost&type=ws&sni=randomsrmainhost#mainname'''
                    st=t.replace("randomsr",gen_rand()).replace("mainname",urllib.parse.quote(str(json.loads(i)["email"].replace("vless","")+"mci"))).replace("mainuid",json.loads(i)["id"]).replace("mainport",str(menue[select_port])).replace("mainhost",ips[p_number])
                    print(json.loads(i)["email"]+"\n")
                    print("`"+st+"`\n\n\n")
                    t='''vless://mainuid@mtn.hostgozarr.com:443?path=%2Fdownloader%2Fmainport&security=tls&encryption=none&host=mainhost&type=ws&sni=randomsrmainhost#mainname'''
                    st=t.replace("randomsr",gen_rand()).replace("mainname",urllib.parse.quote(str(json.loads(i)["email"].replace("vless","")+"mtn"))).replace("mainuid",json.loads(i)["id"]).replace("mainport",str(menue[select_port])).replace("mainhost",ips[p_number])
                    print(json.loads(i)["email"]+"\n")
                    print("`"+st+"`\n\n\n")
            if cr_op==2:
                lis=datass
                for i in lis:
                    t='''vless://mainuid@mci.hostgozarr.com:443?path=%2Fdownloader%2Fmainport&security=tls&encryption=none&host=mainhost&type=ws&sni=randomsrmainhost#mainname'''
                    st=t.replace("randomsr",gen_rand()).replace("mainname",urllib.parse.quote(str(json.loads(i)["email"].replace("vless","")+"mci"))).replace("mainuid",json.loads(i)["id"]).replace("mainport",str(menue[select_port])).replace("mainhost",ips[p_number])
                    f=open(json.loads(i)["email"]+base64.b64encode(str(json.loads(i)["email"]).encode()).decode(),'w')
                    f.write(st)
                    f.write("\n")
                    t='''vless://mainuid@mtn.hostgozarr.com:443?path=%2Fdownloader%2Fmainport&security=tls&encryption=none&host=mainhost&type=ws&sni=randomsrmainhost#mainname'''
                    st=t.replace("randomsr",gen_rand()).replace("mainname",urllib.parse.quote(str(json.loads(i)["email"].replace("vless","")+"mtn"))).replace("mainuid",json.loads(i)["id"]).replace("mainport",str(menue[select_port])).replace("mainhost",ips[p_number])
                    f.write(st)
                    f.close()                
#--------------------------------------------------------------------------
    if action==2:
        print("edit proxy port")
        print("current port is: "+str(proxy_port))
        new_port=input("enter new port number to change.just press enter to no change.\nnew port : ")
        if new_port!='':
            pic_file["proxy-port"]=new_port
            proxy_port=new_port
            pickle.dump(pic_file,open("DONT_REMOVE_THIS","wb"))
            proxy_addr='http://127.0.0.1:'+proxy_port
            proxy={'http':proxy_addr}
            
    if action==3:
        print("panel manager\n\n\n")
        print("you have "+str(len(names))+" panels:\n")
        for srv in range(0,len(names)):
            print (names[srv]+" ("+ips[srv]+")")
        print("\n\n\n1- add a new panel")
        print("2- edit a panel")
        srv_mng=(input("3- delete a panel\nenter the actin: "))
        if srv_mng == "1":
            add_name=input("name for panel: ")
            add_ip=input("ip of panel: ")
            add_port=str(input("port of x-ui panel: "))
            add_co=input("enter the cookie from browser: ")
            if add_co != '' and add_port != '' and add_ip != '' and add_name != '':
                pic_file["servers"].append({'name': add_name, 'ip': add_ip, 'port': add_port, 'co':add_co})
                pickle.dump(pic_file, open("DONT_REMOVE_THIS", "wb"))
                pic_file = pickle.load(open("DONT_REMOVE_THIS", "rb"))
                update_data()
        if srv_mng == "2":
            for srv in range(0, len(names)):
                print(str(srv + 1) + " - " + names[srv] + " (" + ips[srv] + ")")
            ed_serv = int(input("choose a pannel to edit: ")) - 1
            ed_name=input("current name is "+names[ed_serv]+" \n send new name or just press enter to not change: ")
            ed_ip = input("current ip is " + ips[ed_serv] + " \n send new ip or just press enter to not change: ")
            ed_port = input("current port is " + pic_file["servers"][ed_serv]["port"] + " \n send new port or just press enter to not change: ")
            ed_co = input("current cookie is " + pic_file["servers"][ed_serv]["co"] + " \n send new cookie or just press enter to not change: ")
            if ed_name != '' or ed_port != '' or ed_ip != '' or ed_co != '':
                if ed_name != '':
                    pic_file["servers"][ed_serv]["name"]=ed_name
                if ed_ip != '':
                    pic_file["servers"][ed_serv]["ip"] = ed_ip
                if ed_port !='':
                    pic_file["servers"][ed_serv]["port"] = ed_port
                if ed_co != '':
                    pic_file["servers"][ed_serv]["co"] = ed_co
                pickle.dump(pic_file, open("DONT_REMOVE_THIS", "wb"))
                pic_file = pickle.load(open("DONT_REMOVE_THIS", "rb"))
                update_data()
        if srv_mng == "3":
            for srv in range(0, len(names)):
                print(str(srv + 1) + " - " + names[srv] + " (" + ips[srv] + ")")
            del_serv = int(input("choose a pannel to edit: ")) - 1
            pic_file["servers"].pop(del_serv)
            pickle.dump(pic_file, open("DONT_REMOVE_THIS", "wb"))
            pic_file = pickle.load(open("DONT_REMOVE_THIS", "rb"))
            update_data()
        if srv_mng == '':
            print("Exit!")
