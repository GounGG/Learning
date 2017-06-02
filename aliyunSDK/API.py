# coding: utf-8


import sys
import urllib
import time
import json
import base64
import hmac
import uuid
from hashlib import sha1
import requests



access_key_id = 'LTAICYnd0O6o6Aey'
access_key_secret = 'weZ9tapicoQTbWJUliuzXJcG8p3lJj'
server_address = 'https://ecs.aliyuncs.com'
#定义参数
user_params = {
        'action':'DescribeDisks',
        'RegionId':'cn-hangzhou',
        'PageNumber':'1',
        'ZoneId':'cn-hangzhou-b',
        'PageSize': '100'
        }

#短信服务需要在云通信中开通使用
#user_params = {'Action': 'SingleSendSms', 'ParamString': '', 'RecNum': '17091951200','SignName': '','TemplateCode': 'xx' }

def percent_encode(encodeStr):
    encodeStr = str(encodeStr)
    res = urllib.quote(encodeStr.decode('utf8').encode('utf8'), '')
    res = res.replace('+', '%20')
    res = res.replace('*', '%2A')
    res = res.replace('%7E', '~')
    return res

def compute_signature(parameters, access_key_secret):
    sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])
    canonicalizedQueryString = ''
    for (k,v) in sortedParameters:
        canonicalizedQueryString += '&' + percent_encode(k) + '=' + percent_encode(v)
    stringToSign = 'GET&%2F&' +  percent_encode(canonicalizedQueryString[1:])
    h = hmac.new(access_key_secret + "&", stringToSign, sha1)
    signature = base64.encodestring(h.digest()).strip()
    return signature

def compose_url(user_params):
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time()))
    parameters = { \
            'Format'        : 'JSON', \
            'version'       : '2014-05-26', \
            'AccessKeyId'   : access_key_id, \
            'SignatureVersion'  : '1.0', \
            'SignatureMethod'   : 'HMAC-SHA1', \
            'SignatureNonce'    : str(uuid.uuid1()), \
            'RegionId': 'cn-hangzhou',
            'Timestamp'     : timestamp\
    }
    for key in user_params.keys():
        parameters[key] = user_params[key]
    signature = compute_signature(parameters, access_key_secret)
    parameters['Signature'] = signature
    url = urllib.urlencode(parameters)
    return url

def make_request(user_params, quiet=False):
    url = compose_url(user_params)
    r = requests.get(url = server_address, params = url)
    try:
        obj = json.loads(r.text)
        if quiet:
           return obj
    except ValueError, e:
        raise SystemExit(e)
    #return json.dumps(obj)
    json.dump(obj, sys.stdout, sort_keys=True, indent=2)
    sys.stdout.write('\n')

make_request(user_params)
