from instagram_private_api import Client,errors,ClientCompatPatch
from colorama import Fore
from time import sleep


def main():
    print("""{}--------------------------------------------------------
 @@@@@@  @@@@@@  @@@@@@@@@@  @@@@@@@@  @@@@@@  @@@      
!@@     @@!  @@@ @@! @@! @@! @@!      @@!  @@@ @@!      
 !@@!!  @!@!@!@! @!! !!@ @!@ @!!!:!   @!@  !@! @!!      
    !:! !!:  !!! !!:     !!: !!:      !!:  !!! !!:      
::.: :   :   : :  :      :    :        : :. :  : ::.: : 
{}--------------------------------------------------------
coder:SamirSalmanli
Github:SamirSalmanli
Instagram: @samirr_py
|---------------------|
|1)Proqramı başlat    |
|2)Exit               |
|---------------------| {}                                 
""".format(Fore.LIGHTBLUE_EX,Fore.RED,Fore.RESET))
    dax = int(input("Seçiminiz: "))
    if dax != 1 and dax != 2:
        print(f"{Fore.RED}Seçiminiz 1-2 arasında ola biler !")
        dax = int(input("Seçiminiz: "))

    if dax == 1:
        login()
    elif dax == 2:
        exit()


def login():
    print(Fore.YELLOW)
    username = input("Instagram nikinizi yazın :")
    password = input("Sifrenizi yazın :")
    print(Fore.RESET)

    if ( " " in username or username.strip() == ""):
        print(f"{Fore.RED}Instagram nikiniz bosluk ola bilmez yeniden cehd edin !")
        exit()
    if ( " " in password or password.strip() == ""):
        print(f"{Fore.RED}Instagram sifreniz bosluk ola bilmez yeniden cehd edin !")
        exit()

    try:
        api = Client(username,password)
    except errors.ClientLoginError:
        print(f"{Fore.RED}Instagram Nikiniz ve ya Sifreniz yanlisdi !")
        exit(0)
    except errors.ClientChallengeRequiredError:
        print(f"{Fore.RED}Doğrulama hetası VPN ile yoxlayın !")
        exit(0)
    except errors.ClientCheckpointRequiredError:
        print(f"{Fore.RED}Doğrulama hetası VPN ile yoxlayın !")
        exit(0)
    except errors.ClientSentryBlockError:
        print(f"{Fore.RED}Hesabiniz spam altinda oldugu ücün giriş olunmadı!")
        exit(0)
    except errors.ClientConnectionError:
        print(f"{Fore.RED}Internete bagli oldugunuzu yoxlayin !")
        exit(0)
    except errors.ClientError:
        print(f"{Fore.RED}Giriş olunmadı !")
        exit(0)
        print(Fore.RESET)

    print(f"{Fore.LIGHTBLUE_EX}Tebrikler giriş olundu !")

    users_id = [427553890, 173560420, 6860189, 25025320, 26669533, 232192182, 7719696, 12281817, 18428658,
                247944034, 6380930, 11830955, 460563723, 305701719, 451573056, 13460080, 325734299]

    while True:
        for user_id in users_id:
            api.friendships_create(user_id)
            print(f"{Fore.GREEN}Takip atıldı !:{user_id}")
            sleep(60)
        for user in users_id:
            api.friendships_destroy(user)
            print(f"{Fore.RED}Takipten atıldı :{user_id}")
            sleep(160)


main()