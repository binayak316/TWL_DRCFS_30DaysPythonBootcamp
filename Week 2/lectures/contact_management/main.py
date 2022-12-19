from typing import Any

FILE_PATH = 'Week 2/lectures/contact_management/contact.txt'

def add_contact(name: str, email: str, phone: int) -> bool:
    with open(FILE_PATH,'a') as file:
        file.write(','.join((name,email,str(phone))))
        file.write('\n')
        return 1 #1 is for true and 0 is false bool gareko
    return 0

def find_contact(username: str) -> list:
    with open(FILE_PATH,'r') as file: #with is context manager with le error aa vane direct close gardinxa euta error handling ko way ho internally garxa jun kam chai
        contents = file.read()
        contents = [i.split(',') for i in contents.split('\n')][:-1]
        # print(contents)
        res =[]
        for name,email,phone in contents:
            if name.lower() == username.lower():
                res.append((name,email,phone))
        return res

def update_contact(old_details: tuple, new_details: tuple):
    '''
    This functions updates the given contact:
    Args:
        old_details: tuple containing name, email, phone of the existing data
        new_details: tuple containing name, email, phone of the new data that should replace the existing data
    Returns:
        do anything you want but make it functional.
    '''

    print(new_details)
    print(old_details)
  
    lines = open(FILE_PATH,'r').readlines()
    for i, line in enumerate(lines):
        print(old_details[0][0], line.split(',')[0])
        # print(line)
        if str(old_details[0][0]).lower().strip() == line.split(',')[0].lower().strip():
            lines.remove(line)
            lines.append(f"{new_details[0][0]}, {new_details[0][1]}, {new_details[0][2]}")
    
    with open(FILE_PATH, 'w') as file:
        file.writelines(lines)
    
    # steps to follow:
    # 1. open file
    # 2. Search contact like we did in find contact
    # 3. change the particular lines of the file 
    # the following code might be of reference for you
    ####################################################
    # find line_num before hand.
    # lines = open(file_name, 'r').readlines()
    # lines[line_num] = text #yo line ma exact line thapauna paryo jasle tyo line change garna milos
    # out = open(file_name, 'w')
    # out.writelines(lines)
    # out.close()
    ###########################################################
    # 4. Remove the pass keyword once done

    # pass

def delete_contact(name: str):
    # same as update contact but instead of editing the list in the particular index you just delete the given index.
    print(name)
    lines = open(FILE_PATH,'r').readlines()
    for i, line in enumerate(lines):
        print(line)
        

    # pass

def import_contacts(filename) -> bool:
    try:
        # we are reading the file provided by user
        file = open(filename,'r').readlines()
        with open(FILE_PATH,'a') as contacts:
            for items in file:
                contact_details = items.split(',')
                # TODO: ADD VALIDATION
                contacts.write(','.join(contact_details))
            contacts.write('\n')
            return 1 #python ma 1 vannu nai true ho bool ma 
            
    except Exception as e:
        print('CANNOT OPEN GIVEN FILE')
        return 0

def print_all():
    print('PRINTING ALL CONTACTS')
    try:
        contacts = open(FILE_PATH,'r').readlines()
        for i, contact in enumerate(contacts):
            contact = contact.split(',')
            print(f'Contact No. {i}')
            print(f'Name: {contact[0]}')
            print(f'Email: {contact[1]}')
            print(f'Phone: {contact[2]} \n')
    except Exception as e:
        print('No Contacts found.. INVALID FILE PATH. Please change the Relative path of the file in code to run it in windows properly')

def check_int_type(inp: Any) -> int:
    '''
    Helper function:
    Converts the given input to integer if possible if, else returns exception.
    Parameter: inp -> input
    Returns inp as int or exception
    '''

    try:
        inp = int(inp) #input lai int ma convert garera inp ma pass gareko ani return tehi input
        return inp
    except Exception as exception:
        print('\n'+'#'*100)
        print('Conversion Error. The following exception was thrown: ' + str(exception))
        print("Invalid option, please only enter integers and kindly omit other details. Restarting the program....")
        print('#'*100+'\n')
        return 0 #0 means false return false 

def main():
    '''
    This function is executed when the file is run.
    '''
    print('#'*60)
    print('Welcome to My Contact Management System')
    print('#'*60)

    while True:
        print('*'*80)
        print('Please choose one of the following options!')
        print('*'*100)

        print('''Option 1. Add a Contact \t Option 2. Search for a contact by name\t Option 3 Update a contact
        \nOption 4. Delete a Contact \t Option 5. Import contacts from a file\t option 6. Print all contacts 
        \nOption 7. Exit the program
        ''')
        print('-'*100)
        task  = input("Enter Your Choice here: ")
        task  = check_int_type(task)

        if task == 0:
            pass
        elif task == 1:
            name = input('Enter Contact Name: ')
            email = input('Enter Contact Email: ')
            phone = input('Enter Contact Phone Number (Do not enter 0): ')
            phone = check_int_type(phone) #this line checks or validates input to the int field

            if phone and len(str(phone)) == 10:
                res = add_contact(name, email, phone)
                print('-'*100)
                print("Addition success" if res else "Addition failed")
                print('-'*100)

            else:
                print('Please enter a valid phone number with 10 digits and omit country codes')\

        elif task == 2:
            name = input("Enter Name to Search: ")
            contacts = find_contact(name)
            print(contacts)
            if len(contacts):
                print('#'*100)
                print('The following contacts were found in the contacts book with the provided name')
                print('#'*100)
                for i, contact in enumerate(contacts):
                    print(f'Contact No. {i}')
                    print(f'Name: {contact[0]}')
                    print(f'Email: {contact[1]}')
                    print(f'Phone: {contact[2]} \n')

            else:
                print('#'*60)
                print("NO CONTACTS FOUND")
                print('#'*60)

        elif task == 3:
            # complete this as homework
            
            search = input("Enter your name to update: ")
            old_details = find_contact(search)
            print(old_details)
            new_name = input(f"Enter new username for {search} : ")
            new_email = input(f"Enter new email for {search} : ")
            new_phone = input(f"Enter new phone for {search} : ")
            new_details = [(new_name, new_email, new_phone)]

            update_contact(old_details, new_details)
           
            
            # passssss
        elif task == 4:
            # complete his as homework
            search = input("Enter your name to delete: ")
            name = find_contact(search)
            print(name)
            delete_contact(name)
           
            # pass
        elif task == 5:
            file_path = input("Enter File Path Here (Hint: paste precontact.txt file path): ")
            if import_contacts(file_path):
                print('CONTACTS IMPORTED SUCCESSFULLY')
            else:
                print("RESTARTING THE PROGRAM")
                print('*SAD*'*10)
        elif task == 6:
            print_all()
        elif task == 7:
            print('Thanks for using my contact management system. I hope you liked it...')
            break
        else:
            print("Please enter a valid number between 0 and 6")
        
if __name__ == '__main__':
    main()