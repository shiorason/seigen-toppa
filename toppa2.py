import requests;import pprint;import json

a = input("url:"),b = input('cookie name:'),c = input('cookie value:')
k = "'"+b+"'"+":"+"'"+c+"'"
cookie = k
url = "https://"+str(a)
res = requests.get(url,cookies=cookie)
print(res,type(res))
if '200' in str(res):
  a = res.text
  print(len(a+"文字"))
  print(a)
else:
  print("通信エラー")
