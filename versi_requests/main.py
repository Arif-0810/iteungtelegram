import requests
from versi_requests import config


def getLastUpdates():
	req = requests.get(config.linkAPI + "getUpdates")
	apidata = req.json()
	datalength = len(apidata['result'])
	lastdatalist = datalength - 1
	lastdata = apidata['result'][lastdatalist]
	return lastdata


def sendmessage(id, message):
	param = {'chat_id': id, "text": message}
	link = config.linkAPI + 'sendMessage'
	resp = requests.post(link, data=param)
	return resp


update_id = ""
while True:
	print('on running')
	try:
		datalast = getLastUpdates()
		if update_id != datalast['update_id']:
			update_id = datalast['update_id']
			if datalast['message']['text'].lower() == 'wakudin':
				sendmessage(datalast['message']['chat']['id'], 'aya naon?')

			if datalast['message']['text'].lower() == 'love you':
				sendmessage(datalast['message']['chat']['id'], 'love you too')

			if datalast['message']['text'].lower() == 'halo':
				sendmessage(datalast['message']['chat']['id'], 'halo juga')
		else:
			print('no new message coming')
	except:
		print('skip data error')