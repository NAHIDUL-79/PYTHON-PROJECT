# <!--
# #----------------------------------------------INFO-----------------------------------------------------#
# #ADMIN       : MD.NAHIDUL ISLAM
# #TEAM NAME   : TEAM JACKFRUIT
# #MY FACEBOOK : I HATE FACEBOOK . FUCK YOU.
# #MY YOU TUBE : https://www.youtube.com/channel/UCRzCWOq05e-ew9XVGMNrrug
# #MY TIC TOC  : I AM NOT A FALTU PERSON
# HELLO MY CHILD THIS IS MY TOOL IF YOU THINK YOU CAN STILL MY CODE.REMAMBER THIS >(I AM YOUR DAD)
# #----------------------------------------------EXIT-----------------------------------------------------#
# -->
import webbrowser
banner='''
\033[0;32m
.----------------.  .----------------.  .---------------. 
| .--------------. || .--------------. || .------------. |
| |     _____    | || |   ______     | || |    _____   | |
| |    |_   _|   | || |  |_   __ \   | || |   |_   _|  | |
| |      | |     | || |    | |__) |  | || |     | |    | |
| |   _  | |     | || |    |  ___/   | || |     | |    | |
| |  | |_' |     | || |   _| |_      | || |    _| |_   | |
| |  `.___.'     | || |  |_____|     | || |   |_____|  | |
| '--------------' || '--------------' || '------------' |
 '----------------'  '----------------'  '--------------'      Verson 2.2
\033[0;34m
'''
STUDENT=['ABDULLAH','MAHIBUL','PARTHO','JUBAER','AKASH','CHAYON','ABUJAR','SALMAN','ABIR','NAFISA','RABBY','KHOKON','SOWROV','ARAFAT','SAGOR','RAYHAN','ABIR','LIMON','ASIF','SHUVRO','SABBAB','ANIK','RABEYA','MEHADI','TAMIM','SHAKIL','SHAFIQUL','ROTHEN','ZAYED','RIYED','NAHID','ASHIF','MUSTAKIN','AFRIDI','SAZID','FAYSAL','FAHIM','JEHAD','URFE','SIMI','MAHIA','RANI','RUMPA','ADRITA','HANA','ROHAN']
for i in range(1,6):
    print(banner)
    name1 =input("ENTER YOUR NAME :")
    name =name1.upper()
    if name in STUDENT:
        print(f"\033[0;32m YES {name} IS A STUDENT OF JASHORE POLYTECHNIC INSTITUTE !")
    else:
        print(f"\033[0;31m NO {name} IS NOT A STUDENT OF THIS COLLAGE")
    if name =="NAHID":
        admin= input("\033[1m ENTER YOUR PASSWORD  TO ACCESS ADMIN PANNEL :")
        if admin =="119887":
            print("NAHID INFO")
            webbrowser.open_new("https://sites.google.com/view/team-jackfruit/home")
        else:
            print("\t\t\tLOGIN FAILED")
print("Cradit Limit Is Over.")
site =input("Earn cradit to press 1 and enter :")
if site =="1":
    webbrowser.open_new("https://sites.google.com/view/nahidul407/home")
print("LOVE YOU JAN . ONK VALO BASE AJ O TOKA . JAIDIN TAKA HOBA TOR SAMNA DIYA TAKA URAITA URAITA JABO.")
