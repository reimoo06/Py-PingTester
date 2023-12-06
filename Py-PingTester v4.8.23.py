import os
import colorama
from colorama import Fore
from colorama import init
from colorama import Fore, Back, Style
init()
beforems = 0
sess = 0
totalping = 0
avgsus = 0
highestpingsus = 0
lowestpingsus = 100000000
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    red = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

input("reimoo06 -- Turn off all internet usage to get proper ping accuracy -- ENTER TO CONTINUE")
while True:
    try:
        ping = os.popen('ping www.google.com -n 1')
        sess += 1
        result = ping.readlines()
        msLine = result[-1].strip()
        rawms = msLine.split(' = ')[-1]
        donems = int(rawms.replace("ms",""))
        updownscl = beforems - donems
        upscl = 0
        downscl = 0
        totalping += donems
        avgsus = round(totalping/sess)
        

        if donems > highestpingsus:
            highestpingsus = donems
        if donems < lowestpingsus:
            lowestpingsus = donems
        
        if updownscl < 0:
            upscl = str(updownscl).replace("-","")
        if updownscl > 0:
            downscl = str(updownscl).replace("-","")

        #print(f'''Current: {donems}ms | {Fore.RED} ▲: {upscl} |  ▼: {downscl} | Session: {sess} | Avg: {avgsus} | Highest: {highestpingsus} | Lowest: {lowestpingsus}''')
        print("Current: ", donems,"ms | ", end='')
        print(Fore.RED + "▲:", upscl, end='')
        print(Fore.WHITE + " |",Fore.GREEN + "▼:", downscl, end='')
        print(Fore.WHITE + " |",Fore.WHITE + "Session: ", sess, end='')
        print(Fore.WHITE + " |",Fore.YELLOW+ "Avg:", avgsus, "ms",end='')
        print(Fore.WHITE + " |",Fore.RED+ "Highest:", highestpingsus, "ms",end='')
        print(Fore.WHITE + " |",Fore.GREEN + "Lowest:", lowestpingsus, "ms",end='')
        print(Fore.WHITE + " |",Fore.GREEN + "Status: OK", end='')
        print(Style.RESET_ALL)
        beforems=donems
    except:
        print("Current: ? | ", end='')
        print(Fore.RED + "▲: ?", end='')
        print(Fore.WHITE + " |",Fore.GREEN + "▼: ?", end='')
        print(Fore.WHITE + " |",Fore.WHITE + "Session: ?", end='')
        print(Fore.WHITE + " |",Fore.YELLOW+ "Avg: ?",end='')
        print(Fore.WHITE + " |",Fore.RED+ "Highest: ?",end='')
        print(Fore.WHITE + " |",Fore.GREEN + "Lowest: ? ",end='')
        print(Fore.WHITE + " |",Fore.RED + "Status: TIMEOUT", end='')
        print(Style.RESET_ALL)
    
    

