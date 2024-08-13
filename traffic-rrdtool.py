#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, rrdtool, pytz, requests
from datetime import datetime
import xml.etree.ElementTree as ET

url = "http://10.0.0.1:49000/igdupnp/control/WANCommonIFC1"
headers = {'soapaction': 'urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1#GetAddonInfos', 'content-type': 'text/xml','charset': 'utf-8'}

body = """<?xml version="1.0" encoding="utf-8"?><s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body><u:GetAddonInfos xmlns:u="urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1"></u:GetAddonInfos></s:Body></s:Envelope>"""

def getLoads():
    global quota_DL
    global quota_UL
    try:
        boxdata = requests.post(url,data=body,headers=headers).content.decode('utf-8')
        root = ET.fromstring(boxdata)
        raw_quota_DL = root.find(f".//NewX_AVM_DE_TotalBytesReceived64").text
        raw_quota_UL = root.find(f".//NewX_AVM_DE_TotalBytesSent64").text
        quota_DL = int(raw_quota_DL) / 1048576 / 1024#byte to MiB to GiB
        quota_UL = int(raw_quota_UL) / 1048576 / 1024#byte to MiB to GiB
    except:
        pass

def fbTrafficDL():
    ret = rrdtool.graph("/media/purple/plotted/traffic1.png",
                  '--color', 'CANVAS#000000',
                  '--color', 'FONT#07FFFE',
                  '--color', 'BACK#000000',
                  '--color', 'MGRID#0066FF',
                  '--alt-autoscale',
                  '--units-exponent', '0',
                  '--left-axis-format', '%4.1lf',
                  '--right-axis', '1:0',
                  '--right-axis-format', '%4.1lf',
                  '--imgformat', 'PNG',
                  '--width', '790',
                  '--height', '300',
                  '--start', "-64800",
                  '--end', "now",
                  '--vertical-label', 'GiB',
                  '--title', 'fritzbox_traffic_dl',
                  'DEF:download=/media/purple/traffic.rrd:download:MAX',
                  'AREA:download#00bf00:download %s' % str(round(quota_DL, 1)) + " GiB",
                  'COMMENT:%s' % iso_stamp)

def fbTrafficUL():
    ret = rrdtool.graph("/media/purple/plotted/traffic2.png",
                  '--color', 'CANVAS#000000',
                  '--color', 'FONT#07FFFE',
                  '--color', 'BACK#000000',
                  '--color', 'MGRID#0066FF',
                  '--alt-autoscale',
                  '--units-exponent', '0',
                  '--left-axis-format', '%4.1lf',
                  '--right-axis', '1:0',
                  '--right-axis-format', '%4.1lf',
                  '--imgformat', 'PNG',
                  '--width', '790',
                  '--height', '300',
                  '--start', "-64800",
                  '--end', "now",
                  '--vertical-label', 'GiB',
                  '--title', 'fritzbox_traffic_ul',
                  'DEF:upload=/media/purple/traffic.rrd:upload:MAX',
                  'AREA:upload#bf0000:upload %s' % str(round(quota_UL, 1)) + " GiB",
                  'COMMENT:%s' % iso_stamp)

def main():
    global iso_stamp
    try:
        while True:
            getLoads()
            ret = rrdtool.update('/media/purple/traffic.rrd','N:' + str(quota_DL) + ':' + str(quota_UL))
            iso_stamp = datetime.now(pytz.timezone("Europe/Berlin")).replace(microsecond=0).isoformat().replace(":", "\:")
            fbTrafficDL()
            fbTrafficUL()
            time.sleep(60)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
