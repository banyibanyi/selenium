import requests

r = requests.get('https://github.com/timeline.json')
print('get demo response is \n' ,r.text)

r = requests.post("http://httpbin.org/post")
print('post demo response is \n' ,r.text)

''''r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")'''
