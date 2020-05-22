# bilibli is still using avid to get likes

import requests
import vid_generator

Stat_Url = "https://api.bilibili.com/x/web-interface/archive/stat?aid="

# need login cookie
headers = {
    "bfe_id": "fdfaf33a01b88dd4692ca80f00c2de7f",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

if __name__ == '__main__':
    vid_generator.generate_avid()
    avid_list = vid_generator.avid_list
    for avid in avid_list:
        resp = requests.get(Stat_Url + str(avid), headers=headers)
        print(resp)
