Perform WiFi scans from python in OSX
=====================================

This module uses the airport utility to perform a wifi scan, parses stdout and
returns a list of dictionaries with all the info regarding each Access Point.

## Using the module

Using the module is as simple as this:

```
~/ $ git clone https://github.com/Palantir555/py-airport-scanner.git
Cloning into 'py-airport-scanner'...
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
Checking connectivity... done.
~/ $ cd py-airport-scanner/
~/py-airport-scanner/ [master] $ python
Python 2.7.9 (default, Jan  7 2015, 11:49:12)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.56)] on darwin
>>> import airport_scanner
>>> aps_list = airport_scanner.wifi_scan()
>>> print aps_list
[{'ssid': 'SKYDA378', 'bssid': '7c:4c:a5:fc:71:55', 'cc': 'DE', 'ht': 'Y', 'rssi': -70, 'security': 'WPA2(PSK/AES/AES)', 'channel': 13}, {'ssid': 'TALKTALK-255C94', 'bssid': '70:62:b8:25:5c:94', 'cc': 'GB', 'ht': 'Y', 'rssi': -79, 'security': 'WPA(PSK/TKIP,AES/TKIP) WPA2(PSK/TKIP,AES/TKIP)', 'channel': 11}, {'ssid': 'SKYEACF0', 'bssid': '7c:4c:a5:b3:39:7d', 'cc': 'DE', 'ht': 'Y', 'rssi': -84, 'security': 'WPA2(PSK/AES/AES)', 'channel': 11}, {'ssid': 'DIRECT-3r-BRAVIA', 'bssid': 'b2:10:41:c1:85:ac', 'cc': '--', 'ht': 'Y', 'rssi': -68, 'security': 'WPA2(PSK/AES/AES)', 'channel': 9}, {'ssid': 'TALKTALK-023BCD_EXT', 'bssid': '00:8e:f2:64:a1:8d', 'cc': '--', 'ht': 'Y', 'rssi': -64, 'security': 'WPA(PSK/AES,TKIP/TKIP) WPA2(PSK/AES,TKIP/TKIP)', 'channel': 9}, {'ssid': 'AFY', 'bssid': '10:a5:d0:6c:c2:f9', 'cc': '--', 'ht': 'Y', 'rssi': -79, 'security': 'WPA2(PSK/AES/AES)', 'channel': 6}, {'ssid': 'VhalarMorghulis', 'bssid': '00:1b:2f:f1:9b:2c', 'cc': '--', 'ht': 'N', 'rssi': -69, 'security': 'WPA(PSK/TKIP/TKIP)', 'channel': 6}, {'ssid': 'SKYD6F7B', 'bssid': '7c:4c:a5:28:34:81', 'cc': 'DE', 'ht': 'Y', 'rssi': -65, 'security': 'WPA2(PSK/AES/AES)', 'channel': 1}]
>>> print aps_list[0]
{'ssid': 'SKYDA378', 'bssid': '7c:4c:a5:fc:71:55', 'cc': 'DE', 'ht': 'Y', 'rssi': -70, 'security': 'WPA2(PSK/AES/AES)', 'channel': 13}
>>>
```

You can also see the module in action running `python airport\_scanner.py`. The
code inside `if __name__ == '__main__'` can be used as an example of how to use
the module.

## The airport utility

`airport\_scanner.py` assumes your airport utility is located in the default path:
`/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport`

If for any reason your airport utility is not there, update the
`airport\_scanner.airport\_cmd` variable to fit your system.


