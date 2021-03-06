import os
import time
from pyaria2 import Aria2RPC
 
def get_file_from_url(link, file_name):
    jsonrpc = Aria2RPC()
    set_dir = os.path.dirname(__file__)
    options = {"dir": set_dir, "out": file_name, }
    res = jsonrpc.addUri([link], options = options)
 
def get_file_from_cmd(link):
    exe_path = r'D:\aria2\aria2c.exe'
    order = exe_path + ' -s16 -x10 ' + link
    os.system(order)
 
if __name__ == '__main__':
    link = 'http://music.163.com/song/media/outer/url?id=400162138.mp3'
    filename = '海阔天空.mp3'
 
    start = time.time()
    get_file_from_cmd(link)
    end = time.time()
    print (f"耗时:{end-start:.2f}")
