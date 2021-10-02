
import pprint
 
def get_headers(text):
    texts = text.strip().split('\n')
    headers = {}
    for text in texts:
        each_line = text.partition(':')
        headers[each_line[0].strip()] = each_line[2].strip()
    return headers
 
if __name__ == '__main__':
 
    #将复制的头信息替换下面的字符串即可。
    headers = """
        Accept: */*
        Accept-Encoding: gzip, deflate, br
        Accept-Language: zh-CN,zh;q=0.9
        Connection: keep-alive
        Content-Length: 121
        Content-Type: application/x-www-form-urlencoded; charset=UTF-8
        Cookie: locale=zh; BAIDUID=58070134A8012CAF32BEF19F3275E41C:FG=1; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BIDUPSID=58070134A8012CAF32BEF19F3275E41C; PSTM=1554365396; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; H_PS_PSSID=1452_21094_28774_28723_28558_28585_28639_26350_28603_22158; PSINO=6; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1554271973,1554368793; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1554368793
        Host: fanyi.baidu.com
        Origin: https://fanyi.baidu.com
        Referer: https://fanyi.baidu.com/?aldtype=16047
        User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36
        X-Requested-With: XMLHttpRequest
    """
    headers = get_headers(headers)
    pprint.pprint (headers)
