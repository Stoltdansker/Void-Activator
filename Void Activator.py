import time, os, fade, requests, ctypes, os, shutil, ctypes, pyuac
from pystyle import Colors

ct = ctypes.windll.kernel32.SetConsoleTitleW

def clear():
    if os.name == 'posix': # Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt': # Windows
        os.system('cls')
    else:
        print("Unsupported operating system")
        raise SystemExit
    
def pause(text: str = None):
    if text: print(text)
    if os.name == 'posix': # Unix/Linux/MacOS
        os.system('read -n 1 -s -r -p ""')
    elif os.name == 'nt': # Windows
        os.system('pause >nul')
    else:
        print("Unsupported operating system")
        raise SystemExit

logo = f"""
                                                       , - ~ ~ ~ - ,
                                                   , '               ' ,
                                                 ,                       ,
                                                ,      █ █ █▀█ █ █▀▄      ,
                                               ,       ▀▄▀ █▄█ █ █▄▀       ,
                                               ,                           ,
                                               ,                           ,
                                                ,                         ,
                                                 ,                       ,
                                                   ,                  , '
                                                     ' - , _ _ _ ,  '"""
logoc = f"""
                                                       , - ~ ~ ~ - ,
                                                   , '               ' ,
                                                 ,                       ,
                                                ,      █ █ █▀█ █ █▀▄      ,
                                               ,       ▀▄▀ █▄█ █ █▄▀       ,
                                               ,                           ,
                                               ,                           ,
                                                ,                         ,
                                                 ,                       ,
                                                   ,                  , '
                                                     ' - , _ _ _ ,  '
                                                 ╔═════╦════════════════╗
                                                ╔╣ [1] ║  Winrar  Key   ╠╗
                                                ╚╣ [2] ║  Windows Key   ╠╝
                                                 ╚╦════╩═══════════════╦╝
                                                  ║ feds.lol/Spermklat ║
                                                  ╚╦══════════════════╦╝
                                                   ╚══════════════════╝"""
logoc1 = f"""
                                                       , - ~ ~ ~ - ,
                                                   , '               ' ,
                                                 ,                       ,
                                                ,      █ █ █▀█ █ █▀▄      ,
                                               ,       ▀▄▀ █▄█ █ █▄▀       ,
                                               ,                           ,
                                               ,                           ,
                                                ,                         ,
                                                 ,                       ,
                                                   ,                  , '
                                                     ' - , _ _ _ ,  '
                                                 ╔═════╦════════════════╗
                                                ╔╣ [1] ║     Win Home   ╠╗
                                                ║║ [2] ║     Win Pro    ║║
                                                ║║ [3] ║  Win Education ║║
                                                ╚╣ [4] ║ Win Enterprise ╠╝
                                                 ╚╦════╩═══════════════╦╝
                                                  ║ feds.lol/Spermklat ║
                                                  ╚╦══════════════════╦╝
                                                   ╚══════════════════╝"""
wrarac = f"""{Colors.red}
                                                ╔═════════════════════════╗
                                                ║ Winrar is now activated ║
                                                ╠═════════════════════════╣
                                                ╚╗   feds.lol/Spermklat  ╔╝
                                                 ╚═══════════════════════╝{Colors.white}"""
winac = f"""{Colors.red}
                                               ╔══════════════════════════╗
                                               ║ Windows is now activated ║
                                               ╠══════════════════════════╣
                                               ╚╗   feds.lol/Spermklat   ╔╝
                                                ╚════════════════════════╝{Colors.white}"""

logocc = fade.pinkred(logoc)
logocc1 = fade.pinkred(logoc1)
logofade = fade.pinkred(logo)


URL = "https://cdn.discordapp.com/attachments/1223039062529802271/1223039078585467070/rarreg.key?ex=661866e7&is=6605f1e7&hm=d8af5f7be8ea37ce6ae98f5ff06cc18a8224c82c160fd7135359112ca2dcc88a&"

source = "rarreg.key"
destination = "C:/Program Files/WinRAR"


Home = "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"
Pro =  "W269N-WFGWX-YVC9B-4J6C9-T83GX"
Edu = "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2"
Ent = "NPPR9-FWDCX-D2C8J-H872K-2YT43"

while True:
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:
        pass
    ct("Void Activator | Made by: Void")
    os.system("start \"\" https://discord.gg/Cas8Fj3P8t")
    clear()
    print(logocc)
    choice = input(f'{Colors.red}╔═[Void@Choice] \n╚══> {Colors.white}')
    if choice == '1':
        response = requests.get(URL)
        open("rarreg.key", "wb").write(response.content) 
        time.sleep(2)

        if os.path.isfile('C:/Program Files/WinRAR/rarreg.key'):
            os.remove('C:/Program Files/WinRAR/rarreg.key')
            time.sleep(1)
            shutil.move(source, destination)
            clear()
            print(logofade)
            print(wrarac)
            time.sleep(2)
        else:
            time.sleep(1)
            shutil.move(source, destination)
            clear()
            print(logofade)
            print(wrarac)
            time.sleep(2)
        break
    elif choice == '2':
            clear()
            print(logocc1)
            ch = int(input(f"{Colors.red}╔═[Void@Choose] \n╚══> {Colors.white}"))
            if ch == 1:
                os.system(f"slmgr /ipk {Home}")
            elif ch == 2:
                os.system(f"slmgr /ipk {Pro}")
            elif ch == 3:
                os.system(f"slmgr /ipk {Edu}")
            elif ch == 4:
                os.system(f"slmgr /ipk {Ent}")
            time.sleep(1)
            os.system("slmgr /skms kms8.msguides.com")
            time.sleep(1)
            os.system("slmgr /ato")
            time.sleep(1)
            print(logofade)
            print(winac)
            time.sleep(2)
            break