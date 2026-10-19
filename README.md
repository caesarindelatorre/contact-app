### Python Contact Book Application

A lightweight, command-line interface (CLI) Contact Book application built using Python. This application allows users to manage their personal contacts by storing names, phone numbers, email addresses, and physical addresses dynamically in memory. 

### Features

* **Add Contact**: Save a new contact with unique names, phone numbers, emails, and addresses. Prevents duplicate entries.
* **View Contact**: Look up a specific contact by name to see all their details.
* **Edit Contact**: Update the phone, email, or address of an existing contact.
* **Delete Contact**: Remove a contact completely from the contact book.
* **List All Contacts**: Display a complete list of all saved contacts in a clean format.

### How to Run

1. Make sure you have Python installed on your system.
2. Clone this repository or download the source code file.
3. Open your terminal or command prompt and navigate to the project directory.
4. Run the application using the following command:

python contact_book.py 

### Code Overview

The project is structured entirely in Python using core functional programming concepts: 

* **Dictionaries**: Utilizes a nested dictionary structure (contact_book) for efficient O(1) time complexity lookups, updates, and deletions.
* **Control Flow**: Implements a continuous while loop interface paired with conditional logic to handle user menu choices seamlessly.