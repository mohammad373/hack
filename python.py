# hack
from colorama import Fore
import time
print(Fore.RED + "Hello . I`m Bot Welcome Back ;)\n")
time.sleep(1)
print(Fore.RED+"[1]"+Fore.GREEN+"Cloud Flare ;)")
print(Fore.RED+"[2]"+Fore.GREEN+"Scan Web Site 2 ;)")
m1 = int(input(Fore.YELLOW+"\nEnter You Number 1 / 2  ==>  "))



if m1 == 1:

    import sys
    import socket
    import time
    from colorama import Fore
    def __name__():
        print(Fore.RED+"Hello . I`m Bot \nCan I Help You?\n")
        site = input(Fore.YELLOW+"Enter Your Address WebSite ==>  ")
        if site == "":
            try:
                print("You Are 5 Sec Go To The Mano ;)")
                time.sleep(5)
                sys.exit()
            except:
                pass
        my_list = ["www" , "cpanel"]
        for item in my_list:
            hosts = str(item) + "." + str(site)
            bypass = socket.gethostbyname(str(hosts))
            print(Fore.YELLOW+"your ip ==> "+Fore.RED + str(bypass) + Fore.YELLOW +" | " + Fore.RED +str(hosts))
    __name__()


# ___________________________________________________________________

if m1 == 2:

    import sys
    import requests
    import time

    def __start__():
        try:
            print("Hello . Welome Back ;) \n")
            time.sleep(2)
            web = input("Enter Your Address WebSite ==> ")
            if web == "":
                try:
                    print("You Are 5 Sec Go To The Mano ;)")
                    time.sleep(5)
                    sys.exit()
                except:
                    pass
            req = requests.get("https://api.hackertarget.com/dnslookup/?q" , site).text
            print(req)
        except:
            try:
                print("You Are 5 Sec Go To The Mano ;)")
                time.sleep(5)
                sys.exit()
            except:
                pass
    __start__()
if m1 >=3 :
    print(Fore.RED +"[!]"+Fore.GREEN+"This In Not Found ;)")
