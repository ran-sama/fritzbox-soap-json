# fritzbox-soap-json
Using Python 3 to send SOAP requests and get JSON formatted replies.
```
sudo apt install python3-xmltodict
```
Technically this is all vanilla python, but for the sake of nice JSON output I used xmltodict, which is part of the Debian packages and also pip on any distro.

## Examples

```
ran@raspberrypi:~ $ ./soap-dsl1.py
{
    "@xmlns:u": "urn:schemas-upnp-org:service:WANIPConnection:1",
    "NewConnectionStatus": "Connected",
    "NewLastConnectionError": "ERROR_NONE",
    "NewUptime": "14517"
}
```
```
ran@raspberrypi:~ $ ./soap-dsl2.py
{
    "@xmlns:u": "urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1",
    "NewByteSendRate": "10867",
    "NewByteReceiveRate": "292355",
    "NewPacketSendRate": "0",
    "NewPacketReceiveRate": "0",
    "NewTotalBytesSent": "214248160",
    "NewTotalBytesReceived": "3792338136",
    "NewAutoDisconnectTime": "0",
    "NewIdleDisconnectTime": "2",
    "NewDNSServer1": "82.xxx.xxx.xxx",
    "NewDNSServer2": "82.xxx.xxx.xxx",
    "NewVoipDNSServer1": "82.xxx.xxx.xxx",
    "NewVoipDNSServer2": "82.xxx.xxx.xxx",
    "NewUpnpControlEnabled": "1",
    "NewRoutedBridgedModeBoth": "1",
    "NewX_AVM_DE_TotalBytesSent64": "214248160",
    "NewX_AVM_DE_TotalBytesReceived64": "3792338136",
    "NewX_AVM_DE_WANAccessType": "DSL"
}
```
```
ran@raspberrypi:~ $ ./soap-dsl3.py
{
    "@xmlns:u": "urn:dslforum-org:service:WANDSLInterfaceConfig:1",
    "NewEnable": "1",
    "NewStatus": "Up",
    "NewDataPath": "Fast",
    "NewUpstreamCurrRate": "46719",
    "NewDownstreamCurrRate": "292023",
    "NewUpstreamMaxRate": "50556",
    "NewDownstreamMaxRate": "309182",
    "NewUpstreamNoiseMargin": "100",
    "NewDownstreamNoiseMargin": "80",
    "NewUpstreamAttenuation": "70",
    "NewDownstreamAttenuation": "110",
    "NewATURVendor": "aabb0011",
    "NewATURCountry": "0X00",
    "NewUpstreamPower": "498",
    "NewDownstreamPower": "514"
}
```
```
ran@raspberrypi:~ $ ./soap-dsl4.py
{
    "@xmlns:u": "urn:dslforum-org:service:WANDSLInterfaceConfig:1",
    "NewReceiveBlocks": "101792299",
    "NewTransmitBlocks": "72894892",
    "NewCellDelin": "0",
    "NewLinkRetrain": "2",
    "NewInitErrors": "0",
    "NewInitTimeouts": "0",
    "NewLossOfFraming": "0",
    "NewErroredSecs": "0",
    "NewSeverelyErroredSecs": "0",
    "NewFECErrors": "0",
    "NewATUCFECErrors": "0",
    "NewHECErrors": "0",
    "NewATUCHECErrors": "0",
    "NewCRCErrors": "0",
    "NewATUCCRCErrors": "0"
}
```
```
ran@raspberrypi:~ $ ./soap-dsl6.py
{
    "@xmlns:u": "urn:dslforum-org:service:WANDSLLinkConfig:1",
    "NewATMTransmittedBlocks": "2479240354",
    "NewATMReceivedBlocks": "397225172",
    "NewAAL5CRCErrors": "0",
    "NewATMCRCErrors": "0"
}
```
```
ran@raspberrypi:~ $ ./soap-dsl7.py
{
    "@xmlns:u": "urn:dslforum-org:service:WANPPPConnection:1",
    "NewEnable": "1",
    "NewConnectionStatus": "Connected",
    "NewPossibleConnectionTypes": "IP_Routed, IP_Bridged",
    "NewConnectionType": "IP_Routed",
    "NewName": "internet",
    "NewUptime": "14537",
    "NewUpstreamMaxBitRate": "45786566",
    "NewDownstreamMaxBitRate": "36902530",
    "NewLastConnectionError": "ERROR_NONE",
    "NewIdleDisconnectTime": "0",
    "NewRSIPAvailable": "0",
    "NewUserName": "redacted",
    "NewNATEnabled": "1",
    "NewExternalIPAddress": "89.xxx.xxx.xxx",
    "NewDNSServers": "82.xxx.xxx.xxx, 82.xxx.xxx.xxx",
    "NewMACAddress": "AA:BB:CC:DD:EE:FF",
    "NewConnectionTrigger": "AlwaysOn",
    "NewLastAuthErrorInfo": null,
    "NewMaxCharsUsername": "128",
    "NewMinCharsUsername": "3",
    "NewAllowedCharsUsername": "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-._@()#/%[]{}*+\u00a7$&=?!:;,",
    "NewMaxCharsPassword": "64",
    "NewMinCharsPassword": "3",
    "NewAllowedCharsPassword": "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-._@()#/%[]{}*+\u00a7$&=?!:;,",
    "NewTransportType": "PPPoE",
    "NewRouteProtocolRx": "Off",
    "NewPPPoEServiceName": null,
    "NewRemoteIPAddress": null,
    "NewPPPoEACName": "redacted",
    "NewDNSEnabled": "1",
    "NewDNSOverrideAllowed": "1"
}
```
```
ran@raspberrypi:~ $ ./soap-dsl8.py
{
    "@xmlns:u": "urn:dslforum-org:service:DeviceInfo:1",
    "NewManufacturerName": "AVM",
    "NewManufacturerOUI": "000XXX",
    "NewModelName": "FRITZ!Box 7590 (UI)",
    "NewDescription": "FRITZ!Box 7590 (UI) Release 154.07.57",
    "NewProductClass": "FRITZ!Box",
    "NewSerialNumber": "redacted",
    "NewSoftwareVersion": "154.07.57",
    "NewHardwareVersion": "FRITZ!Box 7590 (UI)",
    "NewSpecVersion": "1.0",
    "NewProvisioningCode": "0XX.000.000.000",
    "NewUpTime": "455673",
    "NewDeviceLog": null
}
```
```
ran@raspberrypi:~ $ ./soap-dsl9.py
{
    "@xmlns:u": "urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1",
    "NewWANAccessType": "DSL",
    "NewLayer1UpstreamMaxBitRate": "45644000",
    "NewLayer1DownstreamMaxBitRate": "280064000",
    "NewPhysicalLinkStatus": "Up"
}
```
```
ran@raspberrypi:~ $ ./soap-ip.py
{
    "@xmlns:u": "urn:schemas-upnp-org:service:WANIPConnection:1",
    "NewExternalIPAddress": "89.xxx.xxx.xxx"
}
```
```
ran@raspberrypi:~ $ ./soap-get-sid.py
{
    "@xmlns:u": "urn:dslforum-org:service:DeviceConfig:1",
    "NewX_AVM-DE_UrlSID": "sid=aabbccddeeff0011"
}
```

```
ran@odroidxu4:~$ chmod +x traffic-soap.py
ran@odroidxu4:~$ ./traffic-soap.py
['442.044', '58.469', '8', '0']
```
Values for total download, upload in GiB and current download and upload in Mbit/s. To be used with wireless displays or rrdtool scripts as in my other projects.

## Traffic monitor RRDtool example
```
rrdtool create traffic.rrd --step 60 DS:download:GAUGE:600:U:U DS:upload:GAUGE:600:U:U RRA:MAX:0.5:1:1080
```
![alt text](https://raw.githubusercontent.com/ran-sama/fritzbox-soapless-soap-requests/master/images/dl_example.png
)
![alt text](https://raw.githubusercontent.com/ran-sama/fritzbox-soapless-soap-requests/master/images/ul_example.png
)

## Docs  
https://avm.de/service/schnittstellen/  
https://avm.de/fileadmin/user_upload/Global/Service/Schnittstellen/IGD2.pdf  
https://avm.de/fileadmin/user_upload/Global/Service/Schnittstellen/AVM_TR-064_first_steps.pdf  

## License
Licensed under the WTFPL license.
