import requests;import pprint;import json

a = input("url:")
url = str(a)
res = requests.get(url)
print(res,type(res))
if '200' in str(res):
  a = res.text
  print(len(a+"文字"))
  print(a)
else:
  print("通信エラー")
