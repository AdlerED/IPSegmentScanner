# encoding: utf-8
import argparse
import commands
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ipaddress", help="Set IP and set the scan part as \'0\' (Like 192.0.1.1 will scan 192.[range].1.1)")
parser.add_argument("-r", "--range", help="Set IP scan part range like\'0-255\'")
parser.add_argument("-d", "--detial", help="Show the detials when scanning", action='store_true')
args = parser.parse_args()
ip = args.ipaddress
minRange = int(args.range.split("-")[0])
maxRange = int(args.range.split("-")[1])

list = []
direct = 3;
ipArray = ip.split(".")

for i in range(0,4):
	if ipArray[i] == '0':
		direct = int(i)

if direct == 0:
	print "Scanning " + args.range + '.' + str(ipArray[1]) + '.' + str(ipArray[2]) + '.' + str(ipArray[3])
	for i in range(minRange, maxRange+1):
		sql = 'fping -a -t 1 ' + str(i) + '.' + str(ipArray[1]) + '.' + str(ipArray[2]) + '.' + str(ipArray[3])
		(status, output) = commands.getstatusoutput(sql)
		if output.find('ICMP') == -1 and output != '':
			list.append(str(output))
			if args.detial:
				print("! " + str(i) + '.' + str(ipArray[1]) + '.' + str(ipArray[2]) + '.' + str(ipArray[3]))
		else:
			if args.detial:
				print(". " + str(i) + '.' + str(ipArray[1]) + '.' + str(ipArray[2]) + '.' + str(ipArray[3]))

elif direct == 1:
	print "Scanning " + str(ipArray[0]) + '.' + args.range + '.' + str(ipArray[2]) + '.' + str(ipArray[3])
	for i in range(minRange, maxRange+1):
		sql = 'fping -a -t 1 ' + str(ipArray[0]) + '.' + str(i) + '.' + str(ipArray[2]) + '.' + str(ipArray[3])
		(status, output) = commands.getstatusoutput(sql)
		if output.find('ICMP') == -1 and output != '':
			list.append(str(output))
			if args.detial:
				print("! " + str(ipArray[0]) + '.' + str(i) + '.' + str(ipArray[2]) + '.' + str(ipArray[3]))
		else:
			if args.detial:
				print(". " + str(ipArray[0]) + '.' + str(i) + '.' + str(ipArray[2]) + '.' + str(ipArray[3]))

elif direct == 2:
	print "Scanning " + str(ipArray[0]) + '.' + str(ipArray[1]) + '.' + args.range + '.' + str(ipArray[3])
	for i in range(minRange, maxRange+1):
		sql = 'fping -a -t 1 ' + str(ipArray[0]) + '.' + str(ipArray[1]) + '.' + str(i) + '.' + str(ipArray[3])
		(status, output) = commands.getstatusoutput(sql)
		if output.find('ICMP') == -1 and output != '':
			list.append(str(output))
			if args.detial:
				print("! " + str(ipArray[0]) + '.' + str(ipArray[1]) + '.' + str(i) + '.' + str(ipArray[3]))
		else:
			if args.detial:
				print(". " + str(ipArray[0]) + '.' + str(ipArray[1]) + '.' + str(i) + '.' + str(ipArray[3]))

elif direct == 3:
	print "Scanning " + str(ipArray[0]) + '.' + str(ipArray[1]) + '.' + str(ipArray[2]) + '.' + args.range
	for i in range(minRange, maxRange+1):
		sql = 'fping -a -t 1 ' + str(ipArray[0]) + '.' + str(ipArray[1]) + '.' + str(ipArray[2]) + '.' + str(i)
		(status, output) = commands.getstatusoutput(sql)
		if output.find('ICMP') == -1 and output != '':
			list.append(str(output))
			if args.detial:
				print("! " + str(ipArray[0]) + '.' + str(ipArray[1]) + '.' + str(ipArray[2]) + '.' + str(i))
		else:
			if args.detial:
				print(". " + str(ipArray[0]) + '.' + str(ipArray[1]) + '.' + str(ipArray[2]) + '.' + str(i))


print "\nALIVE HOSTS:"
if len(list) == 0:
	print "	No any alive host has been found!"
for i in range(0, len(list)):
	print "> " + list[i]
print str(len(list)) + " Online."
