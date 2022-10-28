#9.4 Write a program to read through the mbox-short.
# txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those
# lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail
# address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the
# dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file name: ")
fh = open(fname)
emails = dict()

for line in fh:
    if not line.startswith("From "): #or line.startswith("From:"): this part should be "not line..." too
        continue
    else:
        email = (line.split())[1]
        emails[email] = emails.get(email,0) + 1

sent = None
count = 0

for email,times in emails.items():

    if times > count:
        sent = email
        count = times

print(sent,count)