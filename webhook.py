try:
    import time,sys,os
    import requests
    import colorama
    from colorama import Fore, init
except (ModuleNotFoundError):
    os.system('pip install requests colorama')
    os.system('pip install time')
    os.system('pip install os')
    os.system('pip install sys')

def webhook():
  choice = int(input('')) 
  if choice not in [1, 2]:
    print(f'---\n{Fore.MAGENTA}Webhook{Fore.RESET} -> {Fore.RED}Error{Fore.RESET} : Invalid Choice')
    time.sleep(1)

  if choice == 1:
    print(f"---\n{Fore.MAGENTA}Webhook URL{Fore.RESET}")
    webhook = str(input(" > "))
    print(f"{Fore.MAGENTA}Message{Fore.RESET}")
    message = str(input(" > "))
    while True:
      try:
        _data = requests.post(webhook, json={'content': message}, headers={'Content-Type': 'application/json'})
        if _data.status_code < 400:
            print('Sent {message} to > {webhook}')
      except:
          print(f"{Fore.MAGENTA}Invalid Response From The API{Fore.RESET}")
          print(f"{Fore.RED}Resetting The Program{Fore.RESET}")
          exit()
  if choice == 2:
    print(f"---\n{Fore.MAGENTA}Webhook URL{Fore.RESET}")
    webhook = str(input(" > "))
    requests.delete(webhook.rstrip())

def starter():
  print(f'{Fore.MAGENTA}Discord Webhook Tool seth#0008\n{Fore.RESET}\nChoices:\n1. Spam Webhook\n2. Delete Webhook')
  print(f'\n{Fore.MAGENTA}Choice ->: {Fore.RESET}', end='')
  webhook()

starter()
