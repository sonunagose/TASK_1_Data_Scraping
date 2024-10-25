import requests

durl ='https://httpbin.org/patch'

dheader ={
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'user-name' : "['arc', 'vigo']"
}

dResp = requests.patch(url = durl, headers = dheader)

jResp = dResp.json()

print('dResp.content ', jResp['headers'])