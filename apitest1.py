import requests


# r =requests.get('https://nephele.qtestnet.com')
# print(r.status_code)
# print()
# print(r.headers)
# print()
# print(r.headers['Content-Type'])
api_endpoint="https://nouveau.qtestnet.com/oauth/token"
#Authorization: Basic bm91dmVhdTo="
# r.headers['Authorization'] = "Basic bm91dmVhdTo="
data={'grant_type':"password",
      'username':"auppuluri@nouveau-labs.com",
      'password':"password123"}
#data=r.json()
#print("data:%d \n" %(data))
r = requests.post(url = api_endpoint,data=data, headers={"Authorization" : "Basic bm91dmVhdTo="})
past_url=r.text
print("the past_url is:%s"%past_url)
