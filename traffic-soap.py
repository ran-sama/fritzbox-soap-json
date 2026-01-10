#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as ET

url = "http://10.0.0.1:49000/igdupnp/control/WANCommonIFC1"
headers = {'soapaction': 'urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1#GetAddonInfos', 'content-type': 'text/xml','charset': 'utf-8'}

body = """<?xml version="1.0" encoding="utf-8"?><s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body><u:GetAddonInfos xmlns:u="urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1"></u:GetAddonInfos></s:Body></s:Envelope>"""

def getLoads():
    try:
        boxdata = requests.post(url,data=body,headers=headers).content.decode('utf-8')
        root = ET.fromstring(boxdata)
        raw_quota_DL = float(root.find(f".//NewX_AVM_DE_TotalBytesReceived64").text)
        raw_quota_UL = float(root.find(f".//NewX_AVM_DE_TotalBytesSent64").text)
        raw_rate_DL = float(root.find(f".//NewByteReceiveRate").text)
        raw_rate_UL = float(root.find(f".//NewByteSendRate").text)
        quota_DL = round(raw_quota_DL/1048576/1024, 3)#byte to MiB to GiB
        quota_UL = round(raw_quota_UL/1048576/1024, 3)#byte to MiB to GiB
        rate_DL = int(raw_rate_DL/125000)
        rate_UL = int(raw_rate_UL/125000)
        load_bytes = map(str, (quota_DL, quota_UL, rate_DL, rate_UL))
        return(load_bytes)
    except:
        return(map(str, (999, 999, 999, 999)))

print(list(getLoads()))
