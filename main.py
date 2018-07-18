from urllib2 import urlopen as qiubyzhukhi
import time
import os
import sys
import base64
#########################
# OPEN SOURCE TO RECODE #
#########################

class warna:
    """CLASS WARNA"""
    W  = '\033[0m'  # white (default)
    R  = '\033[31m' # red
    G  = '\033[1;32m' # green bold
    O  = '\033[33m' # orange
    B  = '\033[34m' # blue
    P  = '\033[35m' # purple
    C  = '\033[36m' # cyan
    GR = '\033[37m' # gray

cl = warna()
def menu():
    #Dictionary Data Url
    data = {1:["http://api.hackertarget.com/whois/?q=", "WHOIS"],
            2:["http://api.hackertarget.com/nmap/?q=","NMAP"],
            3:["http://api.hackertarget.com/geoip/?q=", "Find Anddress"],
            4:["http://api.hackertarget.com/zonetransfer/?q=","ZONE"],
            5:["http://api.hackertarget.com/reverseiplookup/?q=","REVERSE IP"],
            6:["http://api.hackertarget.com/dnslookup/?q=","DNS"],
            7:["http://api.hackertarget.com/subnetcalc/?q=","SUBNET MASK"],
            8:["http://api.hackertarget.com/httpheaders/?q=","CHECK HEADER"],
            9:["http://api.hackertarget.com/hostsearch/?q=","GRAB HOST"],
            }

    print cl.GR+"[ MENU ]"+cl.W
    #Memanggil Seluruh var data dengan Looping
    #Lalu menjadikannya Sebuah pilihan MENU
    for nomor, (url, judul) in data.items():
        print cl.O+"[%s] %s %s" % (str(nomor),judul, cl.W)

    #ASK MENU
    ask = int(raw_input(cl.P+"Number: "+cl.W))
    #memanggil spesifikasi dari var data/ memanggil isi dari dict dengan Angka"""
    return [data[ask][0]+ip, data[ask][1]]
#Anonymouse Function
a = lambda b: base64.b32decode(b)
def go(x):
    print "-------[CHECK]--------"
    print "> {}".format(x[1])
    #memanggil url dari data lalu requests
    req = qiubyzhukhi(x[0]).read()
    """Jika x[1] adalah GRAB HOST, GRAB HOST di perlakukan Khusus"""
    if x[1] == "GRAB HOST":
        print "Touch site untuk mengunjungi\n"
        #Mengawasi kesalahan list
        try:
            for i in req.split("\n"):
                i = i.split(",")
                format = "[+] HOST: {}http://{}\n{} ~IP: {}{}".format(cl.G, i[0],cl.B, i[1], cl.W)
                print format
        #Handle Seluruh kesalahan dari list
        except:
        #Nol Argumen, atau Tidak ada yang di eksekusi"""
            None
    #Jika Bukan GRAB HOST/ Bukan GRAB HOST/ Jika yang lain/ BUKAN"""
    else:
        """Print biasa"""
        print cl.P+req+cl.W
    print "-------[FINISH]-------"
#BANNER FUNCRION
def slowprint(s):
    os.system("clear")
    print cl.R+"TOOLS api.hackertarget.com "+cl.W
    print cl.G+"Host / Ip Checker"+cl.W
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(1./90)

if __name__ == "__main__":
#Text Welcome
    slowprint(a("KB4XI2DPNYQEG33EMVSDUIA=")+
    	cl.R+a("KFEVKQSZEA======")+
    		cl.W+a("LJEFKS2IJE======")+"\n"+
    			cl.O+a("FUWT2PJALMQFAQSNEBKEKQKNEBOSAPJ5FUWQ====")+"\n"+
    				cl.B+a("JZIECICUIVAU2===")+"\r\n"+cl.W)
    while True:
        ip = raw_input(cl.P+"Masukkan IP/Host: \n>"+cl.W)        
        go(menu())
        print "Press any Back to menu [E] for [E]xit"
        mmm = raw_input(cl.R+"options :\n>"+cl.W)
        if mmm != 'E':
            continue
        else:
            print "Exit"
            sys.exit()
            break