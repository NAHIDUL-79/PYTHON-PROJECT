# import section Start
import os 
from time import sleep
# import section end
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
BANNER='''\033[1;32m
$$\   $$\  $$$$$$\  $$\   $$\ $$$$$$\ $$$$$$$\         $$\    $$\ $$$$$$\ $$$$$$$\  $$\   $$\  $$$$$$\  
$$$\  $$ |$$  __$$\ $$ |  $$ |\_$$  _|$$  __$$\        $$ |   $$ |\_$$  _|$$  __$$\ $$ |  $$ |$$  __$$\ 
$$$$\ $$ |$$ /  $$ |$$ |  $$ |  $$ |  $$ |  $$ |       $$ |   $$ |  $$ |  $$ |  $$ |$$ |  $$ |$$ /  \__|
$$ $$\$$ |$$$$$$$$ |$$$$$$$$ |  $$ |  $$ |  $$ |$$$$$$  $$\  $$  |  $$ |  $$$$$$$  |$$ |  $$ |\$$$$$$\  
$$ \$$$$ |$$  __$$ |$$  __$$ |  $$ |  $$ |  $$ |\______|\$$\$$  /   $$ |  $$  __$$< $$ |  $$ | \____$$\ 
$$ |\$$$ |$$ |  $$ |$$ |  $$ |  $$ |  $$ |  $$ |         \$$$  /    $$ |  $$ |  $$ |$$ |  $$ |$$\   $$ |
$$ | \$$ |$$ |  $$ |$$ |  $$ |$$$$$$\ $$$$$$$  |          \$  /   $$$$$$\ $$ |  $$ |\$$$$$$  |\$$$$$$  |
\__|  \__|\__|  \__|\__|  \__|\______|\_______/            \_/    \______|\__|  \__| \______/  \______/   Verson-4.4
'''
command_list='''
[1] JPI INFO CST STUDENT 
[2] AUTO SMS COMMAND
'''
comm ='''\033[0;31m
LOGIN ERROR ....
'''
while True:
    clear_screen()
    print(BANNER)
    print(command_list)
    CHOICE = input('\033[1;34mENTER YOUR CHOICE : ')
    if CHOICE =='1':
        os.system('python JPI.py')
    elif CHOICE=='2':
        os.system('python auto-sms.py')
    else:
        for i in range(10,0,-1):
            sleep(0.5)
            clear_screen()
            print(BANNER)
            print(comm)
            print(f'TRY AFTER {i} SECOND')
            sleep(0.5)
# developed by NAHID-VIRUS 4.4
