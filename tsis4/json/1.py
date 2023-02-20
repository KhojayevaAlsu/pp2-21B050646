import json

jsondata = open("sample-data.json").read()

json_object = json.loads(jsondata)
print(
    "=======================================================================================" "\n"
    "DN                                                 Description           Speed    MTU" "\n" 
    "-------------------------------------------------- --------------------  ------  ------")
imdata = json_object["imdata"]
for i in imdata:
        DN = i["l1PhysIf"]["attributes"]["dn"]
        description = i["l1PhysIf"]["attributes"]["descr"]
        speed = i["l1PhysIf"]["attributes"]["speed"]
        MTU = i["l1PhysIf"]["attributes"]["mtu"]
        # print fields formatted in columns
        print("{0:50} {1:20} {2:7} {3:6}".format(DN,description,speed,MTU))