fn = raw_input('Which vocoder log would you like to analyze? : ')
if len(fn) == 0: fn = '53-58-amr-nb.txt'
try:
    fd = open(fn)
except:
    print "File doesn't exist"
    exit()

def list_dict_key_value(dict, total_width):
    for key, value in dict.items():
        print str(value).rjust(total_width) + '\r' + key

amr_rx_type = dict()
amr_wb_rx_type = dict()
codec_rate = dict()
codec_rate_wb = dict()
for line in fd:
    line = line.split()[:4]  # We only need list[0]~list[3]
    if '0x03' == line[1]:
        if '00' == line[3]:
            amr_rx_type['Speech Good'] = amr_rx_type.get('Speech Good', 0)+1
            if '00' == line[2]:
                codec_rate['4.75kbps'] = codec_rate.get('4.75kbps', 0)+1
            elif '01' == line[2]:
                codec_rate['5.15kbps'] = codec_rate.get('5.15kbps', 0)+1
            elif '02' == line[2]:
                codec_rate['5.9kbps'] = codec_rate.get('5.9kbps', 0)+1
            elif '03' == line[2]:
                codec_rate['6.7kbps'] = codec_rate.get('6.7kbps', 0)+1
            elif '04' == line[2]:
                codec_rate['7.4kbps'] = codec_rate.get('7.4kbps', 0)+1
            elif '05' == line[2]:
                codec_rate['7.95kbps'] = codec_rate.get('7.95kbps', 0)+1
            elif '06' == line[2]:
                codec_rate['10.2kbps'] = codec_rate.get('10.2kbps', 0)+1
            else:
                codec_rate['12.2kbps'] = codec_rate.get('12.2kbps', 0)+1        
        elif '01' == line[3]:
            amr_rx_type['Speech Degraded'] = amr_rx_type.get('Speech Degraded', 0)+1
        elif '02' == line[3]:
            amr_rx_type['Onset'] = amr_rx_type.get('Onset', 0)+1    
        elif '03' == line[3]:
            amr_rx_type['Speech Bad'] = amr_rx_type.get('Speech Bad', 0)+1    
        elif '04' == line[3]:
            amr_rx_type['SID First'] = amr_rx_type.get('SID First', 0)+1    
        elif '05' == line[3]:
            amr_rx_type['SID Update'] = amr_rx_type.get('SID Update', 0)+1    
        elif '06' == line[3]:
            amr_rx_type['SID Bad'] = amr_rx_type.get('SID Bad', 0)+1    
        else:
            amr_rx_type['No Data'] = amr_rx_type.get('No Data', 0)+1
    elif '0x0B' == line[1]:
        if '00' == line[3]:
            amr_wb_rx_type['Speech Good'] = amr_wb_rx_type.get('Speech Good', 0)+1
            if '02' == line[2]:
                codec_rate_wb['12.65kbps'] = codec_rate_wb.get('12.65kbps', 0)+1
            else:
                codec_rate_wb['Unknown'] = codec_rate_wb.get('Unknown', 0)+1
        elif '04' == line[3]:
            amr_wb_rx_type['SID First'] = amr_wb_rx_type.get('SID First', 0)+1
        elif '05' == line[3]:
            amr_wb_rx_type['SID Update'] = amr_wb_rx_type.get('SID Update', 0)+1    
        elif '07' == line[3]:
            amr_wb_rx_type['No Data'] = amr_wb_rx_type.get('No Data', 0)+1    
        else:
            amr_wb_rx_type['Unknown'] = amr_wb_rx_type.get('Unknown', 0)+1

if 0 != len(amr_rx_type):
    print "\n<AMR RX TYPE>"
    list_dict_key_value(amr_rx_type, 30)
    print "\n<Codec Types in Speech Good>"
    list_dict_key_value(codec_rate, 30)
if 0 != len(amr_wb_rx_type):    
    print "\n<AMR-WB RX TYPE>"
    list_dict_key_value(amr_wb_rx_type, 30)
    print "\n<Codec Types in Speech Good>"
    list_dict_key_value(codec_rate_wb, 30)