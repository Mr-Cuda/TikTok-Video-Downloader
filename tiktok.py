class color:
   DARKCYAN = '\033[36m'
    
import requests
import tikvid
import colorama

video = input('URL: ')
id = tikvid.parseLink(video)

output = tikvid.downloadLink(id)
v_content = requests.get(output)

with open('TikVideo.mp4', 'wb') as f:
	f.write(v_content.content)
  
print(f' ')
print(color.DARKCYAN + f'Video downloaded!')
print(f' ')
