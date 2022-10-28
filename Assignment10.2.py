# 10.2 Write a program to read through the mbox-short.txt and
# figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting
# the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file name: ")
fh = open(fname)

hours = dict()

for line in fh:
    if not line.startswith("From "): #or line.startswith("From:"):
        continue
    else:
        time = (line.split()[5])
        hour = (((time)[:2]))
        hours[hour] = hours.get(hour,0) + 1

temp = (sorted([(hour,rep) for hour,rep in hours.items()]))

for hour,rep in temp:
    print(hour,rep)