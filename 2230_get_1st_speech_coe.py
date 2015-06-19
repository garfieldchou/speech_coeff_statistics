fn = raw_input('Which speech coefficient would you like to extract? :')
if len(fn) == 0: fn = '2g_speech_coeff.txt'
try:
    fd = open(fn)
except:
    print "File doesn't exist"
    exit()
fd_out = open('extract.txt', 'w')

num_of_line = 1
for line in fd:
    if (num_of_line%4) == 2: # Extract 2nd line of a frame
        fd_out.write(line)
    num_of_line = num_of_line+1
# print num_of_line

#for i in range(num_of_line/4 +1):
# for i in range(5):
    # print i
    # fd_out.write('hello\n')
fd_out.close()