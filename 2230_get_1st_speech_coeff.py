fn = raw_input('Which speech coefficient would you like to extract? :')
if len(fn) == 0: fn = 'simplified_2g_speech_coeff.txt'
try:
    fd = open(fn)
except:
    print "File doesn't exist"
    exit()
fd_out = open('extract.txt', 'w')

num_of_line = 1
codec_type_counts = dict()
for line in fd:
    if (num_of_line%4) == 2: # Extract 2nd line of a frame
        fd_out.write(line)
        # create a dictionary to count codec type here
        if '3' == line[1]:
            codec_type_counts['AMR'] = codec_type_counts.get('AMR',0)+1
        elif '0' == line[1]:
            codec_type_counts['FR'] = codec_type_counts.get('FR',0)+1
        elif '1' == line[1]:
            codec_type_counts['EFR'] = codec_type_counts.get('EFR',0)+1
        elif '2' == line[1]:
            codec_type_counts['HR'] = codec_type_counts.get('HR',0)+1
        else:
            codec_type_counts[line[1]] = codec_type_counts.get(line[1],0)+1
        # print codec_type_counts
    num_of_line = num_of_line+1
# print num_of_line
print codec_type_counts
#for i in range(num_of_line/4 +1):
# for i in range(5):
    # print i
    # fd_out.write('hello\n')
fd_out.close()
print "Please checkout the extraction file, 'extract.txt'."