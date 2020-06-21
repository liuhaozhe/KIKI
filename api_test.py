#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import ssl, time, hashlib, string
from urllib import request, parse, error;
from urllib.parse import quote


def sort(rubbish):
    api_url = 'https://cspe.api.storeapi.net/api/71/181';
    appid = '2481';
    secret = '132af0367602a281170987cf620e78bc';
    data = {
        'appid': '1',
        'format': 'json',
        'rbh_name': rubbish,
        'time': '1545829466',
    };
    data['appid'] = appid;
    data['time'] = round(time.time());
    keysArr = list(data.keys())
    keysArr.sort()
    md5String = '';
    params = []
    for key in keysArr:
        if data[key]:
            val = str(data[key])
            md5String += key + val
            params.append(key + "=" + val)
    md5String += secret;
    m = hashlib.md5()
    b = md5String.encode(encoding='utf-8')
    m.update(b)
    sign = m.hexdigest()
    params.append('sign=' + sign)
    params = '&'.join(tuple(params));
    ssl._create_default_https_context = ssl._create_unverified_context
    url = api_url + '?' + params;
    url = quote(url, safe=string.printable)
    req = request.Request(url)
    opener = request.build_opener()
    r = opener.open(fullurl=req)
    doc = r.read();
    #print(eval(doc.decode('utf-8')))
    if ((eval(doc.decode('utf-8'))['codeid']) == 10000):
        if ((eval(doc.decode('utf-8'))['retdata']['rbh_isbig']) == '大件垃圾'):
            print(eval(doc.decode('utf-8'))['retdata']['rbh_abstract'])
        else:
            print(eval(doc.decode('utf-8'))['retdata']['rbh_type_name'])
            print(eval(doc.decode('utf-8'))['retdata']['rbh_abstract']+eval(doc.decode('utf-8'))['retdata']['rbh_content'])
            print(eval(doc.decode('utf-8'))['retdata']['rbh_type_name'] + "包括：" + eval(doc.decode('utf-8'))['retdata'][
                'rbh_example'])
    elif ((eval(doc.decode('utf-8'))['codeid']) == 30012):
        print("暂时无法查询到该垃圾的分类结果，有待我们完善")
    else:
        print("出现错误，请联系管理员")


sort('橘子皮')
