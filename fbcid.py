import wget
import sys
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

try:
	print('Logging in...')
	client = Client(email, pswd, logging_level=50)
except FBchatUserError as e:
	print(e)
	sys.exit();

thread_limit = 15

if client is not None and client.isLoggedIn():
	print('Logged in as ' + email)
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

		attachments = client.fetchThreadImages(thread_uid)
		
		files_count = 0
		for attachment in attachments:
			url = client.fetchImageUrl(attachment.uid)
			
			if type(attachment) == ImageAttachment:
				wget.download(url, thread_uid + '/' + attachment.uid + '.png')
			elif type(attachment) == VideoAttachment:
				wget.download(url, thread_uid + '/' + attachment.uid + '.mp4')
			
			files_count += 1

			print(' Downloaded {} {}'.format(files_count, ['file', 'files'][files_count > 1]))

	else:
		print('Select thread from 0-{}!'.format(thread_limit-1))

client.logout()
