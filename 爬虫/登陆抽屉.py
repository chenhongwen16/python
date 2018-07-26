import requests

response = requests.post(
    url='https://dig.chouti.com/login',
    data={
        'phone':'8613121758648',
        'password':'woshiniba',
        'oneMonth':'1'
    },
    headers = {
        'User-Agent':'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
    }
)

print(response.text)

# ret = requests.get(
#     url='https://dig.chouti.com/all/hot/recent/1',
#     headers = {
#         'User-Agent':'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
#     }
# )
# print(ret.text)
