import json
import pyttsx3

def cat(options):
    for key, value in options.items():
        print(f"{key} : {value}")
def asking(prompt):
    asked = input(prompt).lower()
    return asked
def get_data(demo):
    proceed = True
    while True:
        id_found = False
        id = asking("id: ")
        with open(demo, 'r') as file:
            content = json.load(file)
        for person in content:
            if person["id"] == id.strip():
                id_found = True
        if not id.replace(" ", "").isdigit():
            print('it should be a number')
        elif id_found:
            print('it should be a unique id number')
        else:
            while True:
                name = asking("name: ").lower()
                if name.replace(' ', '').replace('-', '').replace("'", '').isalpha():
                    while True:
                        age = asking("age: ")
                        if age == '':
                            proceed == False
                            return 'cancelled'
                        elif not age.replace(' ', '').isdigit():
                            print('enter a valid age pls')
                        else:
                            age = int(age)
                            if age >= 18 and age <= 100:

                                while True:
                                    number = asking('number: ')
                                    if number.replace(' ', '').isdigit() and len(number) == 3:
                                        data = {
                                            "id": id,
                                            "name": name,
                                            "age": age,
                                            "number": number
                                        }
                                        return data
                                    
                                    else:
                                        print('invalid')
                            else:
                                print('invalid')       
                else:
                    print('not alpha')
def add(demo):
    
    with open(demo, 'r') as file:
        content = file.read()
    if content == "":
        
        data = []
        with open(demo, 'w') as file:
            json.dump(data, file, indent=4)
        
        with open(demo, 'r') as file:
            output = json.load(file)
        info = get_data(demo)
        output.append(info)
        with open(demo, 'w') as file:
            json.dump(output, file, indent=4)
        return 'added successfully'
    else:
        with open(demo, 'r') as file:
            content2 = json.load(file)
        
        data = get_data(demo)
        content2.append(data)
        with open(demo, 'w') as file:
            json.dump(content2, file, indent=4)
        return 'added successfully'
        
def edit_data():
    proceed = False
    while True:
        name = asking("new name: ")
        if name.replace(' ', '').replace('-', '').replace("'", '').isalpha():
            while True:
                age = asking("new age: ")
                if age == '':
                    proceed == False
                    return 'cancelled'
                elif not age.replace(' ', '').isdigit():
                    print('enter a valid age pls')
                else:
                    age = int(age)
                    if age >= 18 and age <= 100:

                        while True:
                            number = asking('new number: ')
                            if number.replace(' ', '').isdigit() and len(number) == 3:
                                data = {
                                    "id": id,
                                    "name": name,
                                    "age": age,
                                    "number": number
                                }
                                return data
                            
                            else:
                                print('invalid')
                    else:
                        print('invalid')       
        else:
            print('not alpha')
   
def edit(demo):
    with open(demo, 'r') as file:
        content = json.load(file)
    id = asking('id: ')
    for value in content:
        if id == value["id"]:
            print('name:', value["name"])
            print('age:', value["age"])
            print('number:', value["number"])
    found = False
    for person in content:
        if id == person["id"]:
            edit = edit_data()
            person["name"] = edit["name"]
            person["age"] = edit["age"]
            person["number"] = edit["number"]
            found = True
    if found:
        with open(demo, 'w') as file:
            json.dump(content, file, indent=4)     
        return 'updated successfully'
    else:
        return 'editing failed'

def display(demo):

    with open(demo, 'r') as file:
        content = json.load(file)
    if not content:
        return 'no data to display'

    option = asking("press 1 to find a person | press 2 to display everything: ")
    count = 0
    if option == "2":
        with open(demo, 'r') as file:
            content = json.load(file)
        
        for person in content:
            print(f"id: {person["id"]}")
            print(f"name: {person["name"]}")
            print(f"age: {person["age"]}")
            print(f"number: {person["number"]}")
            print('--------------------')
            count += 1
        if count == 1:
            return f'{count} person found'
        else:
            return f'{count} people found'
    elif option == "1":
        found = False
        count = 0
        ask = asking("enter the name or id (press enter to cancel): ")
        with open(demo, 'r') as file:
            content = json.load(file)
        for data in content:
            if ask == data["id"] or ask == data["name"]:
                print(f"id: {data["id"]}")
                print(f"name: {data["name"]}")
                print(f"age: {data["age"]}")
                print(f"number: {data["number"]}")
                found = True
                count += 1
            
        if found and count == 1:
            return f'found {count} person'
        elif found and count >= 2:
            return f'found {count} people'
        else:
            return 'not found'
        
def remove(demo):
    with open(demo, 'r') as file:
        content = json.load(file)
    if not content:
        return 'no data to delete yet'
    while True:
        ask = asking("press 1 to delete a person | press 2 to delete everything: ")
        if ask == "1":
            with open(demo, 'r') as file:
                content = json.load(file)
            
            deleted = False
            new_list = []
            ask = asking('name: ')
            for person in content:
                if ask != person["name"]:
                    new_list.append(person)
                else:
                    deleted = True
                
            with open(demo, 'w') as file:
                json.dump(new_list, file, indent=4)

            if deleted:
                return 'deleted successfully'
            else:
                return 'name does not exist'

        elif ask == '2':
            with open(demo, 'r') as file:
                content = json.load(file)
            
            new = []

            with open(demo, 'w') as file:
                json.dump(new, file)
            return 'everything has been deleted'
                
def backup(demo, demo2, backup_file):
    
    cat(backup_file)
    ask2 = asking("press: ")
    if ask2 == '2':
        with open(demo, 'r') as file:
            content = json.load(file)
        if not content:
            return 'no data yet'
        else:
            ask = asking("do you want to save the content of file 1 to file 2?  y/n: ")
            if ask == 'y':
                with open(demo2, 'w') as file:
                    json.dump(content, file, indent=4)
                return "file 1 has been saved to file 2 "
            else:
                return "cancelled"
    elif ask2 == '1':
        with open(demo2, 'r') as file:
            content2 = file.read()
        if content2 == "":
            return 'no entries yet'
        else:
            count = 0
            with open(demo2, 'r') as file:
                content = json.load(file)
            for person in content:
                print(person)
                count += 1
            if count == 1:
                return f'{count} entry displayed'
            elif count >= 2:
                return f'{count} entries displayed'
            else:
                return 'no entries yet'            
    
    elif ask2 == '3':
        with open(demo2, 'r') as file:
            output = file.read()
        if output == "":
            return 'no data to remove'
        
        with open(demo2, 'r') as file:
            output2 = json.load(file)
        if not output2:
            return 'no data yet'
        ask3 = asking("press 1 to remove a person | press 2 to remove everything: ")
        if ask3 == '1':

            with open(demo2, 'r') as file:
                content = file.read()
            if content == "":
                return 'no data entries yet'
            else:
                with open(demo2, 'r') as file:
                    content = json.load(file)

                for i in content:
                    print(i)
                ask4 = asking("enter the id you would like to remove: ")
                new_list = []
                removed = False
                for person in content:
                    if ask4 != person["id"]:
                        new_list.append(person)
                        with open(demo2, 'w') as file:
                            json.dump(new_list, file, indent=4)
                    else:
                        removed = True
                if removed:
                    return 'removed successfully'
                else:
                    return 'id not matched'
        
        elif ask3 == '2':

            with open(demo2, 'r') as file:
                content = file.read()
            if content == "":
                return 'no data entries yet'
            else:
                while True:
                    ask5 = asking('are you sure? y/n:')
                    if ask5 == 'y':
                        with open(demo2, 'r') as file:
                            content = json.load(file)
                        empty = []
                        
                        with open(demo2, 'w') as file:
                            json.dump(empty, file, indent=4)
                            return 'removed everything successfully'
                    elif ask5 == 'n':
                        return 'cancelled'
                    else:
                        print('wrong key')
            
            
    elif ask2 == "":
        return 'cancelled'
    
def signup(demo3):
    first_signed = False
    with open(demo3, 'r') as file:
        content = file.read()
    if content == "":
        data = []
        with open(demo3, 'w') as file:
            json.dump(data, file, indent=4)
            first_signed = True
    with open(demo3, 'r') as file:
        content2 = json.load(file)
    while True:
        speech("enter a username!")
        username = input('username: ')
        if username.replace(' ', '').isalpha() and len(username) > 3:
            while True:
                speech('enter a password')
                password = input('password: ')
                if password.replace(' ', '').isdigit() and len(password) > 3:
                    signing = {
                        "username": username,
                        "password": password
                    }
                    content2.append(signing)
                    with open(demo3, 'w') as file:
                        json.dump(content2, file, indent=4)

                    if first_signed:
                        speech('congratulations, your account was the first account has been created')
                        return 'congratulations! first account has been created'
                    else:
                        speech('great!, new account has been made')
                        return 'new account has been created'
                    
                else:
                    print('invalid')
                    speech('it should be a digit, and atleast greater than 3 digits')
        
        else:
            print('invalid')
            speech('it should be an alphabet, and atleast greater than 3 words')


    

def signin(demo3):
    with open(demo3, 'r') as file:
        content2 = file.read()
    if content2 == "":
        return False
    with open(demo3, 'r') as file:
        content = json.load(file)
    speech("enter your username")
    username = input('username: ')
    speech('enter your password')
    password = input('password: ')
    for person in content:
        if person["username"] == username and person["password"] == password:
            speech('easy peasy!!!')
            return True


def speech(prompt):
    jarvis = pyttsx3.init()
    jarvis.setProperty('rate', 170)
    jarvis.say(prompt)
    jarvis.runAndWait()


def main():
    demo = "database/json-handling.json"
    demo2 = "database/json-handling2.json"
    demo3 = "database/json-handling3.json"

    backup_file = {
        "1": "display content",
        "2": "save content to file2",
        "3": "remove content"
    }

    options = {
        "a": "add",
        "d": "display",
        "r": "remove",
        "e": "edit",
        "b": "backup",
        "x": "exit"

    }
    
    auth = {
        "1": "sign up",
        "2": "sign in",
        "3": "exit",
    }
    print('AI is talking....')
    speech("hello, i am friday, and this is authentication, press 1, to sign up, press 2, to sign in, and press 3, to exit")
    print('test 1')

    print('hello world 1')

    print("this is the final output")

    print("requesting pull request")

    print("requesting second pull request")

    print(1000 - 1000)


    
    while True:
        print("-----------authentication-----------")
        cat(auth)
        ask2 = asking('choose an option: ')
        if ask2 == '1':
            print("sign up page")
            print(signup(demo3))
        elif ask2 == '2':
            print("sign in page")
            account = signin(demo3)
            if account:
                speech('credentials accepted successfully, welcome to contact information, choose an option below, thanks')
                while True:
                    print('-----------contact info-----------')
                    cat(options)
                    ask = asking('enter option: ')
                    if ask == 'a':
                        speech('add person entry')
                        print(add(demo))
                    elif ask == 'd':
                        speech('display person entry')
                        print(display(demo))
                    elif ask == 'r':
                        speech('remove person entry')
                        print(remove(demo))
                    elif ask == 'e':
                        speech('add person entry')
                        print(edit(demo))
                    elif ask == 'b':
                        speech('backup person entry')
                        print(backup(demo, demo2, backup_file)) 
                    elif ask == 'x':
                        print("exit")
                        return False
            elif account == False:
                print('no user account in the database yet')
            else:
                print('invalid credentials')
                speech("invalid credentials, please try again!")
        elif ask2 == '3':
            print('exit')
            speech('exit')
            return False
        else:
            speech('wrong key') 
    
main()

    


