from colorama import init
from colorama import Fore, Back, Style
init()
print(Back.BLACK)
print(Fore.CYAN)
print("Script by Zevi/Скрипт сделан Zevi")
print('▄▀▄ █▄░▄█ ▀ █▄░█ ▄▀▄ █░░░█ ▄▀▄ █░░ █░░ ▄▀▀ █▀▄ ▄▀▄ █▄░▄█')
print("█▀█ █░█░█ █ █░▀█ █░█ █░█░█ █▀█ █░▄ █░▄ ░▀▄ █░█ █▀█ █░█░█")
print("▀░▀ ▀░░░▀ ▀ ▀░░▀ ░▀░ ░▀░▀░ ▀░▀ ▀▀▀ ▀▀▀ ▀▀░ █▀░ ▀░▀ ▀░░░▀")
import amino
#инпут почты и пароля чтобы бот зашел в аккаунт
email=input("Email/Почта:")
password=input("Password/Пароль:")
comid=input('Type community id/Введите id сообщества:')
client = amino.Client()
client.login(email=email, password=password)
sub_client = amino.SubClient(comId=comid,profile=client.profile)
print('\nLogged in/Бот зашел!')
userlink=input("Type user link/Введите ссылку на пользователя: ")
user=client.get_from_code(userlink)
userId=user.objectId
comId=user.path[1:user.path.index('/')]
subclient=amino.SubClient(comId=comid ,profile=client.profile)
comment=input("Message/Сообщение:")
while True:
	try:
		sub_client.comment(message=comment,userId=userId)
	except:
		pass