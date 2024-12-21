import string
import getpass
from colorama import Fore, Style, init

# Initialize colorama for vibrant console output
init(autoreset=True)

def print_banner():
    print(f"""{Fore.GREEN}
██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░

░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
{Fore.YELLOW}🎉 Welcome to the Password Strength Checker 🎉
    """)

def check_pwd():
    password = getpass.getpass(f"{Fore.CYAN}Enter Password: {Style.RESET_ALL}")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1 
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = f"{Fore.RED}❌ The Password You Entered is Very BAD. Change ASAP ❌{Style.RESET_ALL}"
    elif strength == 2:
        remarks = f"{Fore.RED}❌ The Password You Entered is Very BAD. Change ASAP ❌{Style.RESET_ALL}"
    elif strength == 3:
        remarks = f"{Fore.YELLOW}⚠️ The Password You Entered is Very WEAK. Consider Changing it ⚠️{Style.RESET_ALL}"
    elif strength == 4:
        remarks = f"{Fore.BLUE}💪 The Complexity is Hard But You Can Make it MORE HARDER 💪{Style.RESET_ALL}"
    elif strength == 5:
        remarks = f"{Fore.GREEN}🔥 The Password You Entered is Very Very HARD and A Strong One 🔥{Style.RESET_ALL}"

    print(f'{Fore.MAGENTA}Your Password has:{Style.RESET_ALL}')
    print(f"{Fore.YELLOW}🔒 {lower_count} lowercase characters{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}🔒 {upper_count} uppercase characters{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}🔢 {num_count} numeric characters{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}❓ {wspace_count} whitespace characters{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}✨ {special_count} special characters{Style.RESET_ALL}")

    print(f"\n{Fore.CYAN}💼 Password Strength: {strength}{Style.RESET_ALL}")
    print(f"{remarks}")

def ask_pwd(another_pwd=False):
    valid = False
    if another_pwd:
        choice = input(f'{Fore.CYAN}🤔 Do You want to enter another password (y/n): {Style.RESET_ALL}')
    else:
        choice = input(f'{Fore.CYAN}💬 Do You Want to Check password strength (y/n): {Style.RESET_ALL}')  

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print(f'{Fore.RED}❗ Invalid input, Try Again ❗{Style.RESET_ALL}')

if __name__ == '__main__':
    print_banner()
    ask_pw = ask_pwd()
    while ask_pw:
        check_pwd()
        ask_pw = ask_pwd(True)
