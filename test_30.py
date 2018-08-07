import requests

headers={
    'Cookie': 'tgw_l7_route=860ecf76daf7b83f5a2f2dc22dccf049; _xsrf=L7BZUMTsEkUW4KAuHqL1c1ddSLZopgf8; _zap=8569433b-b34f-42be-8a8e-07ee04db88ae; d_c0="AFBnm1TaBA6PTnd9zyR_y1oopGWCQs3zKFM=|1533623838"; capsion_ticket="2|1:0|10:1533623882|14:capsion_ticket|44:NDE0ZGIyOTg2NTlkNGJhZjgwYTk0ZTA3MmEwMGU5ZjM=|de5c993e99493fee2f8706b8a04b5dd5e4055d0d4e81df24cc077920b9fe777e"; z_c0="2|1:0|10:1533623921|4:z_c0|92:Mi4xaUhXeEF3QUFBQUFBVUdlYlZOb0VEaVlBQUFCZ0FsVk5jWXhXWEFCMm9VazVuTmhsNUhob09tSHZoV2xOd3BkZW9B|1e137f0e9556702a6d328f4a4d3d5c87c31b081ff92d79319106959ae6c0ce8d"; unlock_ticket="AIAAzed12QomAAAAYAJVTXlFaVv0g_BrY324QUDTBmIlrGgBKwOtGw=="; q_c1=cd75934616f841829e147eb995077e58|1533623921000|1533623921000',
    'Host': 'www.zhihu.com',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
}

r=requests.get('https://www.zhihu.com',headers=headers)
print(r.text)
