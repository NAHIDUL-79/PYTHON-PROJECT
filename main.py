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
comm ='''\033[0;31m
LOGIN ERROR ....
'''
while True:
    clear_screen()
    print(BANNER)
    print('[1] DEMO FILE')
    print('[2] CLONE FILE')
    CHOICE = input('\033[1;34mENTER YOUR CHOICE : ')
    if CHOICE =='1':
        os.system('python demo.py')
    elif CHOICE=='2':
        os.system('python clone.py')
    else:
        for i in range(10,0,-1):
            sleep(0.5)
            clear_screen()
            print(BANNER)
            print(comm)
            print(f'TRY AFTER {i} SECOND')
            sleep(0.5)
# developed by NAHID-VIRUS 4.4
