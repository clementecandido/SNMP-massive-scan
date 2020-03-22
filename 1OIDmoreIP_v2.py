import os

lineList = [line.rstrip('\n') for line in open("IP list.txt")]

print(lineList)
oid = input('Inserisci OID (es. .1.3.6.1.2.1.1.3.0): ')


for x in lineList:
  print(x)

  os.system("snmpget -v 2c -c public %s %s" % (x, oid))

#  os.system("snmpget -v 2c -c public 192.168.231.253 .1.3.6.1.2.1.1.3.0")