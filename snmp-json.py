from pysnmp.hlapi import *
import json

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('public', mpmodel=0),
           UdpTransportTarget('https://www.bbc.com/news'),
           ContextData(),
           ObjectType(ObjectIdentity('1.3.6.1.4.1.2021.4.6.0')),
           ObjectType(ObjectIdentity('1.3.6.1.4.1.2021.4.11.0')))
    )

if (errorIndication):
    print(errorIndication)

elif(errorStatus):
    print('%s at %s' % (errorStatus.prettyPrint()),
                        errorIndex and varBinds[int(errorIndex)-1][0] or '?')

else:
    for varBind in varBinds:
        d = ('='.join([x.prettyPrint() for x in varBind]))

json_file ={'Manar':[{'ram' : d }]}
with open('Manar.json', 'w') as f:
    json.dump(json_file, f)


    
           
