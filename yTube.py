# yTube - download videos from youtube
#
# By: yHaper/Marcio
# yTube
# Version: 1.0
#
#
##################

from pytube import YouTube
from pytube.cli import on_progress
import os
import time
os.system("clear")

print ("\033[1;31mＹＴ  Ｄｏｗｎｌｏａｄ\033[m\n\033[0;31m   ᵇʸ ʸᴴᵃᵖᵉʳ\n\033[m")
name = input("\033[1;31mType your name: \033[m")
os.system("clear")

var = 0
while var <1:
	print ("\033[1;31mＹＴ  Ｄｏｗｎｌｏａｄ\033[m MP4\n\033[0;31m   ᵇʸ ʸᴴᵃᵖᵉʳ\n\033[m")
	print ("\033[0;31mWhat do you want, {} ?\033[m" .format(name))
	print ("\033[31m[1] \033[mDownload MP4\n\033[0;31m[2] \033[mDownload MP3\n\033[0;31m[3]\033[m Go out")
	py = input("\n\033[0;31m~ \033[m")
	
	
	if py == '2':
		os.system("clear")
		
		print ("\033[1;31mＹＴ  Ｄｏｗｎｌｏａｄ\033[m MP3\n\033[0;31m   ᵇʸ ʸᴴᵃᵖᵉʳ\n\033[m")
		
		link = input("\033[1;31mLink of the audio you want to download: \033[m")
		
		yt = YouTube(link, on_progress_callback = on_progress)
		
		os.system("clear")
		print ("\033[0;32mDownloading... /\033[m")
		print ("Titulo = ", yt.title)
		time.sleep(0.3)
		os.system("clear")
		
		print ("\033[0;32mDownloading... -\033[m")
		print ("Titulo = ", yt.title)
		time.sleep(0.3)
		os.system("clear")
		
		print ("\033[0;32mDownloading... \  \033[m")
		print("Titulo = ", yt.title)
		time.sleep(0.3)
		os.system("clear")
		
		ys = yt.streams.get_audio_only()
		
		out_file = ys.download()
		base, ext = os.path.splitext(out_file)
		new_file = base + '.mp3'
		os.rename(out_file, new_file)
		
		
		os.system("clear")
		print ("\033[1;32mDone!\033[m")
		break
		
	if py == '1':
		os.system("clear")
		
		print ("\033[1;31mＹＴ  Ｄｏｗｎｌｏａｄ\033[m MP4\n\033[0;31m   ᵇʸ ʸᴴᵃᵖᵉʳ\n\033[m")
		
		link = input("\033[1;31mLink of the video you want to download: \033[m")
		
		yt = YouTube(link, on_progress_callback = on_progress)
		
		os.system("clear")
		print ("\033[0;32mDownloading... /\033[m")
		print ("Titulo = ", yt.title)
		time.sleep(0.3)
		os.system("clear")
		
		print ("\033[0;32mDownloading... -\033[m")
		print ("Titulo = ", yt.title)
		time.sleep(0.3)
		os.system("clear")
		
		print ("\033[0;32mDownloading... \  \033[m")
		print("Titulo = ", yt.title)
		time.sleep(0.3)
		os.system("clear")
		
		ys = yt.streams.get_highest_resolution()
		
		ys.download()
		
		os.system("clear")
		print("\033[1;32mDone!\033[m")
		break
	
	if py == '3':
		os.system("clear")
		print ("\033[0;31mGoodbye!\033[m")
		break
		
	else:
		os.system("clear")
