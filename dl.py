# donwload the following files: "10.json","15.json","17.json","2.json","20.json","21.json","24.json","25.json","29.json","4.json","TOKENS.json" using eccadet.azurewebsites.net/ax/filename

import requests

files = ["10.json","15.json","17.json","2.json","20.json","21.json","24.json","25.json","29.json","4.json","TOKENS.json"]

for file in files:
    url = "http://eccadet.azurewebsites.net/ax/" + file
    r = requests.get(url, allow_redirects=True)
    open(file, 'wb').write(r.content)
    print("Downloaded " + file)