import requests
from versi_requests import config_example

def getLastUpdates():
    req = requests.get(config_example.linkAPI + "getUpdates")
    apidata = req.json()
    datalength=len(apidata['result'])
    lastdatalist=datalength-1
    lastdata=apidata['result'][lastdatalist]
    return lastdata

def sendmessage(id, message):
    param={'chat_id':id, "text": message}
    link= config_example.linkAPI + 'sendMessage'
    resp=requests.post(link, data=param)
    return resp

update_id=""
botname=['teung', 'iteung']
while True:
    datalast=getLastUpdates()
    if update_id != datalast['update_id']:
        update_id=datalast['update_id']
        if datalast['message']['text'].lower() in botname:
            sendmessage(datalast['message']['chat']['id'], 'aya naon crot?')
    else:
        print('no new message!')