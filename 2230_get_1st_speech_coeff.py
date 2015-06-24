fn = raw_input('Which speech coefficient would you like to extract? :')
if len(fn) == 0: fn = 'bplog_01_2015_0608_113311_2g3g_speech_coeff.txt'
try:
    fd = open(fn)
except:
    print "File doesn't exist"
    exit()
fd_out = open('extract.txt', 'w')

line_cursor = 1
codec_type_counts = dict()
amr_rx_type = dict()
for line in fd:
    if (line_cursor%4) == 1: # Record the frame number
        fd_out.write(line.split()[0])
    if (line_cursor%4) == 2: # Extract 2nd line of a frame
        fd_out.write(line)
        # create a dictionary to count codec type here
        if '3' == line[1]:
            codec_type_counts['AMR'] = codec_type_counts.get('AMR',0)+1
            if '0' == line[5]:
                amr_rx_type['RX_SPEECH_GOOD'] = amr_rx_type.get('RX_SPEECH_GOOD', 0)+1
            elif '1' == line[5]:
                amr_rx_type['RX_SPEECH_DEGRADED'] = amr_rx_type.get('RX_SPEECH_DEGRADED', 0)+1
            elif '2' == line[5]:
                amr_rx_type['RX_ONSET'] = amr_rx_type.get('RX_ONSET', 0)+1
            elif '3' == line[5]:
                amr_rx_type['RX_SPEECH_BAD'] = amr_rx_type.get('RX_SPEECH_BAD', 0)+1
            elif '4' == line[5]:
                amr_rx_type['RX_SID_FIRST'] = amr_rx_type.get('RX_SID_FIRST', 0)+1
            elif '5' == line[5]:
                amr_rx_type['RX_SID_UPDATE'] = amr_rx_type.get('RX_SID_UPDATE', 0)+1
            elif '6' == line[5]:
                amr_rx_type['RX_SID_BAD'] = amr_rx_type.get('RX_SID_BAD', 0)+1
            else:
                amr_rx_type['RX_NO_DATA'] = amr_rx_type.get('RX_NO_DATA', 0)+1                
        elif '0' == line[1]:
            codec_type_counts['FR'] = codec_type_counts.get('FR',0)+1
        elif '1' == line[1]:
            codec_type_counts['EFR'] = codec_type_counts.get('EFR',0)+1
        elif '2' == line[1]:
            codec_type_counts['HR'] = codec_type_counts.get('HR',0)+1
        else:
            codec_type_counts[line[1]] = codec_type_counts.get(line[1],0)+1
    line_cursor = line_cursor + 1
print "\n# of frames for every codec type: \n", codec_type_counts
print "\nAMR RX TYPE:"
for key, value in amr_rx_type.items():
    print key, value
fd_out.close()
print "Please checkout the extraction file, 'extract.txt'."