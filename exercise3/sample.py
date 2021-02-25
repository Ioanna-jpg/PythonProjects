url='https://api.opap.gr/draws/v3.0/1100/draw-date/2020-01-01/2020-01-01/draw-id'
r= urllib.request.urlopen(url)
html= r.read()
html= html.decode()
data= json.loads(html)
fDrawId= data[0]
#gia ta statistika
url2= 'https://api.opap.gr/draws/v3.0/1100/%27+str(fDrawId)
r= urllib.request.urlopen(url2)
html= r.read()
html= html.decode()
data= json.loads(html)