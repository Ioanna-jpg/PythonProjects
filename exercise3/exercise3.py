import urllib.request
import json
from time import sleep
url = "https://api.opap.gr/draws/v3.0/1100/draw-date/2021-01-01/2021-01-13}"
r = urllib.request.urlopen(url)
html = r.read()
html = html.decode()
data= json.loads(html, strict=False)
for draw in data["content"]:
    print(draw["WinningNumbers"])["list"]
