#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, xmltodict, json, re
from requests.auth import HTTPDigestAuth

def main():
    # define your IP and credentials
    username = "fritz1234"
    password = "fox789"

    # what we want to access
    req_endpoint = '/igdupnp/control/WANIPConn1'
    service = 'urn:schemas-upnp-org:service:WANIPConnection:1'
    action = 'ForceTermination'

    # form-autofill for python users
    soapaction = service + '#' + action
    raw_envelope = re.sub(r"\s +", "",
        """<?xml version="1.0" encoding="utf-8"?><s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body><u:{action} xmlns:u="{service}"></u:{action}></s:Body></s:Envelope>""")

    # send the soap request
    auth = HTTPDigestAuth(username, password)
    device = "http://10.0.0.1:49000" + req_endpoint
    headers = {'soapaction': soapaction, 'content-type': 'text/xml','charset': 'utf-8'}
    envelope = raw_envelope.format(service=service, action=action)
    encoded = envelope.encode("utf-8")
    boxdata = requests.post(url=device, data=encoded, headers=headers, auth=auth).content.decode('utf-8')

    # XML to dict, remove outer nesting, pretty print JSON
    data_dict = xmltodict.parse(boxdata)
    response_tag = 'u:' + action + 'Response'
    data_dict = data_dict['s:Envelope']['s:Body'][response_tag]
    json_data = json.dumps(data_dict, indent=4)
    print(json_data)

main()
