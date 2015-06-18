fn = raw_input('Which speech coefficient would you like to extract? :')
# put default file name here
fd = open(fn)
fd_out = open('extract.txt', 'w')

num_of_line = 1
for line in fd:
    if (num_of_line%4) == 2:
        fd_out.write(line)
    num_of_line = num_of_line+1
# print num_of_line

#for i in range(num_of_line/4 +1):
# for i in range(5):
    # print i
    # fd_out.write('hello\n')
fd_out.close()