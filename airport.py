import subprocess
import re

airport_cmd  = "/System/Library/PrivateFrameworks/Apple80211.framework/"
airport_cmd += "Versions/Current/Resources/airport"

DEBUG=0

def wifi_scan():
    '''
    Uses the airport utility to perform a WiFi scan, parses the output and
    returns:
        Failure -> None
        Success -> List of dictionaries as returned by parse_stdout()
    '''
    if DEBUG==1: print("- Executing `airport -s`")
    stdout = execute_airport()
    if stdout != None:
        if DEBUG==1: print("- Parsing stdout")
        aps_list = parse_stdout(stdout)
        return aps_list
    else:
        if DEBUG==1: print("- [ERROR] Failed to execute airport. Please make "+
                     "sure you've got the right path: {0}".format(airport_cmd))
        return None

def execute_airport():
    '''
    Uses the airport utility to perform a WiFi scan. Returns:
        Failure -> None
        Success -> String containing stdout
    '''
    process = subprocess.Popen([airport_cmd, "-s"],    shell=False,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    retcode = process.returncode
    if retcode == 0:
        return out
    else:
        return None

def parse_stdout(string):
    '''
    Parses the stdout of the airport utility and returns a list of dicts:
    [
        { "bssid"   = "DE:AD:BE:EF:FE:ED",
          "ssid"    = "My SSID!",
          "rssi"    = -58,
          "channel" = 1,
          "ht"      = "Y",
          "cc"      = "DE",
          "security"= "WPA(PSK/AES,TKIP/TKIP) WPA2(PSK/AES,TKIP/TKIP)"
        },
        {...}
    ]
    '''
    aps_list = []
    idx = 0

    for line in string.split('\n'):
        p = re.compile(ur'(?:[0-9a-fA-F]:?){12}')
        #Find BSSID:
        bssid = re.findall(p, line)

        found_bssid = False
        #Split string to get SSID
        for match in re.finditer(p, line): #There will be just one
            bssid_start_idx = match.start()
            bssid_end_idx   = match.end()
            found_bssid = True
        if found_bssid == False: continue #It's the first line, with the name of each column.

        bssid = bssid[0]

        aps_list.append({})
        aps_list[idx]["bssid"] = bssid

        #Left side of BSSID
        ssid = line[:bssid_start_idx].lstrip().rstrip()
        aps_list[idx]["ssid"] = ssid

        #Right side of bssid. We chop the string to the first char after BSSID
        line = line[bssid_end_idx:].lstrip() #Chop line until idx[0] is on RSSI
        rssi = int(line[:line.find(' ')])    #rssi is between idx[0] and ' '
        aps_list[idx]["rssi"] = rssi

        line = line[line.find(' '):].lstrip() #Chop line until idx[0] is on Channel
        channel_str = line[:line.find(' ')]   #channel is between idx[0] and 
        channel = int(channel_str.split(',')[0])
        aps_list[idx]["channel"] = channel

        line = line[line.find(' '):].lstrip() #Chop line until idx[0] is on HT
        ht = line[0]                          #HT is 1 Character: idx[0]
        aps_list[idx]["ht"] = ht

        line = line[line.find(' '):].lstrip() #Chop line until idx[0] is on CC
        cc = line[:2]                         #CC is the 2 first chars of line
        aps_list[idx]["cc"] = cc

        line = line[line.find(' '):].lstrip() #Chop line until idx[0] is on Security
        security = line.rstrip()              #Security is the rest of the line
        aps_list[idx]["security"] = security

        idx += 1
    return aps_list

if __name__ == '__main__':
    DEBUG=1
    aps_list = wifi_scan()
    print aps_list
    for ap in aps_list:
        print "-----------------------------"
        print "ESSID:    {0}".format(ap["ssid"])
        print "BSSID:    {0}".format(ap["bssid"])
        print "RSSI:     {0}".format(ap["rssi"])
        print "Channel:  {0}".format(ap["channel"])
        print "HT:       {0}".format(ap["ht"])
        print "CC:       {0}".format(ap["cc"])
        print "Security: {0}".format(ap["security"])
