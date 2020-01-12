import wget
import os
from fbchat import Client
from fbchat.models import *
from getpass import getpass

print("""
----------------------------------------------
FBCID (Facebook Conversation Image Downloader)
----------------------------------------------
""")

email = str(input('Enter email: '))
pswd = getpass('Enter password: ')

client = Client(email, pswd, max_tries=3)

thread_limit = 15

if client.isLoggedIn():
	threads = client.fetchThreadList(limit=thread_limit)

	for i in range(thread_limit):
		thread_info = client.fetchThreadInfo(threads[i].uid)[threads[i].uid]
		print('[{}] {}'.format(i, thread_info.name))
	
	selected_thread = int(input('Select thread: '))

	if not selected_thread > thread_limit-1:
		thread_uid = client.fetchThreadInfo(threads[selected_thread].uid)[threads[selected_thread].uid].uid
		print('Selected thread uid: {}'.format(thread_uid))

		if not os.path.isdir(thread_uid):
			os.mkdir(thread_uid)

		images = client.fetchThreadImages(thread_uid)
		
		image_count = 0
		for image in images:
			url = client.fetchImageUrl(image.uid)
			
			wget.download(url, thread_uid + '/' + image.uid + '.png')			
			image_count += 1

			if image_count > 1:
				print(' Downloaded {} images'.format(image_count))
			else:
				print(' Downloaded {} image'.format(image_count))

	else:
		print('Select thread from 0-{}!'.format(thread_limit-1))

client.logout()
