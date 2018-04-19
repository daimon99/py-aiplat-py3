# -*- coding: UTF-8 -*-
import os
import json
import hashlib
from py_aiplat_py3 import apiutil

app_key = ''
app_id = ''

if __name__ == '__main__':
    seq = 0
    for_mat = 8
    rate = 16000
    bits = 16
    cont_res = 1
    once_size = 6400
    file_path = '../data/wxasrs.mp3'
    f = open(file_path, 'rb')
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    hash = md5obj.hexdigest()
    speech_id = str(hash).upper()
    f.close()
    f = open(file_path, 'rb')
    file_size = os.path.getsize(file_path)
    try:
        while True:
            chunk = f.read(once_size)
            if not chunk:
                break
            else:
                chunk_size = len(chunk)
                if (seq + chunk_size) == file_size:
                    end = 1
                else:
                    end = 0

            ai_obj = apiutil.AiPlat(app_id, app_key)

            print('----------------------SEND REQ----------------------')
            rsp = ai_obj.getAaiWxAsrs(chunk, speech_id, end, for_mat, rate, bits, seq, chunk_size, cont_res)
            seq += chunk_size
            if rsp['ret'] == 0:
                print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
                print('----------------------API SUCC----------------------')
            else:
                print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
                print('----------------------API FAIL----------------------')
    finally:
        f.close()
