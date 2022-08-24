import json 
data = '''{
    "name" : "Ossama",
    "phone" : {"type" : "intl", "number" : "+971 50 244 5467"},
    "email" : {"hide" : "No" }

    }'''

info = json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])

input = '''[
 { "id" : "001", "x" : "5", "name" : "Ossama"} ,
 { "id" : "009","x" : "10","name" : "Omar" }
 ]'''

info = json.loads(input) 
print ('User count:', len(info)) 
for item in info:
    print('\nName', item['name'])
    print('Id', item['id'])
    print('Attribute', item['X'])

    
