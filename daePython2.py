import json

FILENAME = 'holder.json'

def addPassword():
    print('Username:')
    username = input()
    print('Password')
    password = input()
    try:
        with open(FILENAME, 'r') as openfile:
            json_object = json.load(openfile)
    except:
        json_object = {}
    else:
        print('File Opened')
    finally:
        json_object.update({username: password})
        with open(FILENAME, "w") as outfile:
            json.dump(json_object, outfile)


def getPassword():
    with open(FILENAME, 'r') as openfile:
        json_object = json.load(openfile)
    print('Input username for the password you want to access')
    username = input()
    for x in json_object.keys():
        if x == username:
            return f'Username: {username}, Password: {json_object[username]}'
    return 'Username not foundcrF'
    

def main():
    empty_dict = {}
    
    while True:
        print('Input "create" to create a new password or "read" to recover an existing password. Input "end" to end')
        selection = input()
        if selection == 'create':
            addPassword()
        elif selection == 'read':
            print(getPassword())
        elif selection == 'end':
            break
        else:
            print('Misunderstood input')
main()