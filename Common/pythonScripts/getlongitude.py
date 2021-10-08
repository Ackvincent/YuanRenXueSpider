url = "https://apis.map.qq.com/ws/place/v1/suggestion/"
headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Referer": "https://lbs.qq.com/tool/getpoint/getpoint.html"
}
param = {
    "keyword":"双井地铁站",
    "region": "",
    "key":"K76BZ-W3O2Q-RFL5S-GXOPR-3ARIT-6KFE5",
    "output":"jsonp",
    "callback":"jQuery191023148659560008777_1554977748452",
    "_":"1554977748452"
}
response = requests.get(url,params=param,headers=headers)
print(response.text)


# | 参数名称 | 是否必须 | 参数类型 | 说明                                      |
# | -------- | -------- | -------- | ----------------------------------------- |
# | keyword  | 是       | String   | 位置                                      |
# | region   | 否       | String   | 城市                                      |
# | key      | 是       | String   | 默认  K76BZ-W3O2Q-RFL5S-GXOPR-3ARIT-6KFE5 |
# | output   | 是       | String   | 默认 jsonp                                |
# | callback | 是       | String   | jQuery191023148659560008777_13位的时间戳  |
# | _        | 是       | imestamp | 13位的时间戳                              |
