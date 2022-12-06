#!/usr/bin/python

time = raw_input().strip()
h, m, s = time[:-2].split(':')
o = time[-2:-1]

if o == 'P':
    if int(h) == 12:
        print("{}:{}:{}".format(h, m, s))
    else:
        print("{}:{}:{}".format(int(h)+12, m, s))
else:
    if int(h) == 12:
        print("{}:{}:{}".format("0"+str(int(h)-12), m, s))
    else:
        print("{}:{}:{}".format(h, m, s))

