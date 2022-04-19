import sublist3r, pyfiglet, os
from time import sleep
from random import choice
from colorama import Fore, init, Style
from multiprocessing.dummy import Pool as ThreadPool
from rich.console import Console

RedC = Fore.LIGHTRED_EX
CyanC = Fore.LIGHTCYAN_EX
WhiteC = Fore.WHITE

c = Console()

init(autoreset=True)

try:
    open("result_progress.txt", "a")
    open("result.txt", "a")
except:
    pass

def banner():
    os.system('cls|clear')
    my_banner = pyfiglet.figlet_format('Subdo-Enum', font='slant', justify='center')
    print(f'{RedC}{my_banner}')
    print(f'{CyanC}\t\t\t[ {WhiteC}Created By X-MrG3P5 {CyanC}]\n')

def SubdomainEnum(domain):
    try:
        with c.status("[green]Writing Subdomain", spinner=choice(["aesthetic","bouncingBall","bouncingBar","arc"])) as load:
            subdomains = sublist3r.main(domain, 100, 'result_progress.txt', ports= None, silent=False, verbose= False, enable_bruteforce= False, engines=None)
            sleep(0.01)
            load.update(f"[cyan]Writing [green]{domain} [white]Subdomain(s)")
            data_subdo = open("result_progress.txt", "r").read().replace("http://", "").replace("https://", "").splitlines()
            for x in data_subdo:
                open("result.txt", "a").write(x + "\n")
    except:
        pass


if __name__ =="__main__":
    banner()
    input_list = open(input(f"{CyanC}[ {WhiteC}? {CyanC}] {WhiteC}Domain List : "), "r").read().replace("http://", "").replace("https://", "").splitlines()
    Thread = input(f"{CyanC}[ {WhiteC}? {CyanC}] {WhiteC}Thread : ")
    pool = ThreadPool(int(Thread))
    pool.map(SubdomainEnum, input_list)
    pool.close()
    pool.join()
