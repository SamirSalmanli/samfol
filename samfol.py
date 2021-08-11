from instagram_private_api import Client,errors,ClientCompatPatch
from colorama import Fore,Style
from time import sleep


def main():
    print("""{}--------------------------------------------------------
 @@@@@@  @@@@@@  @@@@@@@@@@  @@@@@@@@  @@@@@@  @@@      
!@@     @@!  @@@ @@! @@! @@! @@!      @@!  @@@ @@!      
 !@@!!  @!@!@!@! @!! !!@ @!@ @!!!:!   @!@  !@! @!!      
    !:! !!:  !!! !!:     !!: !!:      !!:  !!! !!:      
::.: :   :   : :  :      :    :        : :. :  : ::.: : 
{}{}--------------------------------------------------------
coder:SamirSalmanli
Github:SamirSalmanli
Instagram: @samirr_py
|---------------------|
|1)Proqramı başlat    |
|2)Exit               |
|---------------------| {}                                 
""".format(Fore.LIGHTBLUE_EX,Style.BRIGHT,Fore.RED,Fore.RESET))
    dax = int(input(f"{Style.BRIGHT}[+]Seçiminiz[+]--> "))
    if dax != 1 and dax != 2:
        print(f"{Fore.RED}Seçiminiz 1-2 arasında ola biler !")
        dax = int(input("Seçiminiz: "))

    if dax == 1:
        login()
    elif dax == 2:
        exit()


def login():
    try:
        saniye = int(input(f"{Fore.BLUE}{Style.BRIGHT}[+]Takipler arasında neçe saniye gözlensin[+]-->"))
    except ValueError:
        print(f"{Fore.RED}[+]Saniye yerine herf yazıla bilmez[+]")
    username = input(f"{Fore.BLUE}{Style.BRIGHT}Instagram nikinizi yazın !-->")
    password = input(f"{Fore.MAGENTA}{Style.BRIGHT}Sifrenizi yazin-->")
    print(Fore.RESET)



    if ( " " in username or username.strip() == ""):
        print(f"{Fore.RED}[+]Instagram nikiniz bosluk ola bilmez yeniden cehd edin ![+]")
        exit()
    if ( " " in password or password.strip() == ""):
        print(f"{Fore.RED}[+]Instagram sifreniz bosluk ola bilmez yeniden cehd edin ![+]")
        exit()

    try:
        api = Client(username,password)
    except errors.ClientLoginError:
        print(f"{Fore.RED}[+]Instagram Nikiniz ve ya Sifreniz yanlisdi ![+]")
        exit(0)
    except errors.ClientChallengeRequiredError:
        print(f"{Fore.RED}[+]Doğrulama hetası VPN ile yoxlayın ![+]")
        exit(0)
    except errors.ClientCheckpointRequiredError:
        print(f"{Fore.RED}[+]Doğrulama hetası VPN ile yoxlayın ![+]")
        exit(0)
    except errors.ClientSentryBlockError:
        print(f"{Fore.RED}[+]Hesabiniz spam altinda oldugu ücün giriş olunmadı![+]")
        exit(0)
    except errors.ClientConnectionError:
        print(f"{Fore.RED}[+]Internete bagli oldugunuzu yoxlayin ![+]")
        exit(0)
    except errors.ClientError:
        print(f"{Fore.RED}[+]Giriş olunmadı ![+]")
        exit(0)
        print(Fore.RESET)

    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}[+]Tebrikler giriş olundu ![+]")

    users_id = [427553890, 173560420, 6860189, 25025320, 26669533, 232192182, 7719696, 12281817, 18428658,
                247944034, 6380930, 11830955, 460563723, 305701719, 451573056, 13460080, 325734299]
    data = api.username_info(username)
    data = api.user_followers(data["user"]["pk"], api.generate_uuid())
    tmp = data["users"]
    while True:
        for user in data["users"]:
            tmp = user["username"]
            for user_id in users_id:
                if (api.friendships_show(str(user_id))["following"] == True):
                    print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}[+]Onsuzda takip edilir[+]")
                    continue
                api.friendships_create(user_id)
                print(f"{Fore.GREEN}{Style.BRIGHT}[+]Takip atıldı !:{user_id}[+]")
                sleep(saniye)
            for usern in users_id:
                if (api.friendships_show(str(usern))["following"] == False):
                    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}[+]Onsuzda takip eilmir[+]")
                    continue
                api.friendships_destroy(usern)
                print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}[+]Takipten çıxarıldı : {usern}[+]")
                sleep(saniye)


main()
