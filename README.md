Perform WiFi scans from python in OSX
=====================================

This module uses the airport utility to perform a wifi scan, parses stdout and
returns a list of dictionaries with all the info regarding each Access Point.

## Testing the script:

Using the module from the interpreter is as simple as this:

```
$ git clone https://github.com/Palantir555/airport_scanner_py.git
[...]
$ python
Python 2.7.9 (default, Jan  7 2015, 11:49:12)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.56)] on darwin
>>> import airport_scanner_py.airport as airport
>>> airport.wifi_scan()
[{'ssid': 'SKYDA378', 'bssid': '7c:4c:a5:fc:71:55', 'cc': 'DE', 'ht': 'Y', 'rssi': -67, 'security': 'WPA2(PSK/AES/AES)', 'channel': 13}, {'ssid': 'TALKTALK-023BCD', 'bssid': '6c:19:8f:02:3b:cd', 'cc': 'GB', 'ht': 'Y', 'rssi': -71, 'security': 'WPA(PSK/TKIP,AES/TKIP) WPA2(PSK/TKIP,AES/TKIP)', 'channel': 9}, {'ssid': 'TALKTALK-023BCD_EXT', 'bssid': '00:8e:f2:64:a1:8d', 'cc': '--', 'ht': 'Y', 'rssi': -64, 'security': 'WPA(PSK/AES,TKIP/TKIP) WPA2(PSK/AES,TKIP/TKIP)', 'channel': 9}, {'ssid': 'TALKTALKFFBFCA', 'bssid': '60:e7:01:ff:bf:d0', 'cc': '--', 'ht': 'Y', 'rssi': -67, 'security': 'WPA(PSK/AES,TKIP/TKIP) WPA2(PSK/AES,TKIP/TKIP)', 'channel': 3}, {'ssid': 'SKYD6F7B', 'bssid': '7c:4c:a5:28:34:81', 'cc': 'DE', 'ht': 'Y', 'rssi': -64, 'security': 'WPA2(PSK/AES/AES)', 'channel': 1}]
>>>
```

## Importing the module from your script

First of all you need to clone this repo into the folder where your script is.
Then you can simply:

```
import airport_scanner_py.airport as airport
networks_list = airport.wifi_scan()
for ap in networks_list:
    print "-----------------------------"
    print "ESSID:    {0}".format(ap["ssid"])
    print "BSSID:    {0}".format(ap["bssid"])
    print "RSSI:     {0}".format(ap["rssi"])
    print "Channel:  {0}".format(ap["channel"])
    print "HT:       {0}".format(ap["ht"])
    print "CC:       {0}".format(ap["cc"])
    print "Security: {0}".format(ap["security"])
```

## The airport utility

`airport_scanner.py` assumes your airport utility is located in the default path:
`/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport`

If for any reason your airport utility is not there, update the
`airport.airport_cmd` variable to fit your system.
