def display_menu():  
    print()
    print('Contact Book Menu:')
    print('1. Add Contact')
    print('2. View Contact')
    print('3. Edit Contact')
    print('4. Delete Contact')
    print('5. List All Contacts')
    print('6. Exit')

def add_contact(contact_book):
    print()
    name = input('name: ')
    if name in contact_book:
        print('Contact already exists!')
    else:
        contact_book[name] = {
            "phone" : input('phone: '), 
            "email": input('email: '), 
            'address': input('address: ')
            }
        print('Contact added successfully!')
def view_contact(contact_book):
    print()
    name = input('name: ')
    if name in contact_book:
        contact = contact_book[name]
        print('Name:', name)
        print('Phone:', contact["phone"])
        print('Email:', contact["email"])
        print('Address:', contact["address"])
    else: 
        print('Contact not found!')
def edit_contact(contact_book):
    print()
    name = input('name: ')
    if name in contact_book:
        contact_book[name]['phone'] = input('phone: ')
        contact_book[name]['email'] = input('email: ')
        contact_book[name]['address'] = input('address: ')
        print('Contact updated successfully!')
    else:
        print('Contact not found!')
def delete_contact(contact_book):
    print()
    name = input('name: ')
    if name in contact_book:
        del contact_book[name]
        print('Contact deleted successfully!')
    else:
        print('Contact not found!')
def list_all_contacts(contact_book):
    print()
    if len(contact_book) == 0:
        print('No contacts available.')
    else:
        for name, info in contact_book.items():
            print('Name:', name)
            print("Phone:", info['phone'])
            print("Email:", info['email'])
            print("Address:", info['address'])
            print()
contact_book = {}

while True:
    display_menu()
    action = input('Enter your choice: ')
    if action == "1":
        add_contact(contact_book)
    elif action == '2':
        view_contact(contact_book)
    elif action == '3':
        edit_contact(contact_book)
    elif action == '4':
        delete_contact(contact_book)
    elif action == '5':
        list_all_contacts(contact_book)
    else:
        break