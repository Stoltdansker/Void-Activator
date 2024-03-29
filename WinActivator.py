import os, time, fade, ctypes
from os import system
from pystyle import Colors

Home = "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"
Pro =  "W269N-WFGWX-YVC9B-4J6C9-T83GX"
Edu = "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2"
Ent = "NPPR9-FWDCX-D2C8J-H872K-2YT43"

logoc = f"""
                                                  ╦═╗┌─┐┌┬┐ ╔═╗┌┬┐┌─┐┬─┐
                                                  ╠╦╝├┤  ││ ╚═╗ │ ├─┤├┬┘
                                                  ╩╚═└─┘─┴┘ ╚═╝ ┴ ┴ ┴┴└─
                                                 ╔═════╦════════════════╗
                                                ╔╣ [1] ║     Win Home   ╠╗
                                                ║║ [2] ║     Win Pro    ║║
                                                ║║ [3] ║  Win Education ║║
                                                ║║ [4] ║ Win Enterprise ║║
                                                ║║ [5] ║     Discord    ║║
                                                ╚╣ [6] ║      Exit      ╠╝
                                                 ╚╦════╩═══════════════╦╝
                                                  ║ feds.lol/Spermklat ║
                                                  ╚╦══════════════════╦╝
                                                   ╚══════════════════╝"""
logocfade = fade.pinkred(logoc)
titletext = f"Windows Key Activator | Made by: SpermKlat"
ctypes.windll.kernel32.SetConsoleTitleW(titletext)
print(logocfade)
if not pyuac.isUserAdmin():
    pyuac.runAsAdmin()
    sys.exit()
else:
    pass
ch = int(input(f"{Colors.red}╔═[Root@Choose] \n╚══> {Colors.white}"))
if ch == 1:
    os.system(f"slmgr /ipk {Home}")
elif ch == 2:
    os.system(f"slmgr /ipk {Pro}")
elif ch == 3:
    os.system(f"slmgr /ipk {Edu}")
elif ch == 4:
    os.system(f"slmgr /ipk {Ent}")
elif ch == 5:
    os.system("start \"\" https://discord.gg/Cas8Fj3P8t")
elif ch == 6:
    SystemExit("Exitting...")

time.sleep(1)
os.system("slmgr /skms kms8.msguides.com")
time.sleep(1)
os.system("slmgr /ato")
time.sleep(1)
print("License has been applied.")
