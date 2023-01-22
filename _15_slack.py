import requests
import json

slack_webhook_URL = 'https://hooks.slack.com/services/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'

def sendSlackWebhook(text):
    headers = {
        'content-type': 'application/json'
    }

    data = {'text': text}

    res = requests.post(slack_webhook_URL, headers = headers, data = json.dumps(data))

    if res.status_code == 200:
        output =  'OK'
    else:
        output = 'Error'


    return output


text = "TEST"

for i in range(10):
    sendSlackWebhook(text = f'{text} + {i}')
