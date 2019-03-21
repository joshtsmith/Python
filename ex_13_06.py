import urllib.request, urllib.parse, urllib.error
import json

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    #url = urllib.parse.urlencode({'address': address})
    print('Retrieving', address)
    uh = urllib.request.urlopen(address)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    info = json.loads(data)
    print('Count: ',len(info['comments']))
    sum = 0
    for item in info['comments']:
        num = int(item['count'])
        sum = sum + num
    print('Sum: ',sum)
