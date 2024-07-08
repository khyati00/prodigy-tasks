import json

# Define a class for Contact
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number}, Email: {self.email}"

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    new_contact = Contact(name, phone_number, email)
    contacts[name] = new_contact
    print("Contact added successfully!")
    save_contacts_to_file(contacts)

# Function to view contact list
def view_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        for contact in contacts.values():
            print(contact)

# Function to edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        phone_number = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        contacts[name].phone_number = phone_number
        contacts[name].email = email
        print("Contact updated successfully!")
        save_contacts_to_file(contacts)
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
        save_contacts_to_file(contacts)
    else:
        print("Contact not found.")

# Function to load contacts from a file
def load_contacts_from_file():
    try:
        with open('contacts.json', 'r') as file:
            contacts_data = json.load(file)
            contacts = {contact['name']: Contact(**contact) for contact in contacts_data}
            return contacts
    except FileNotFoundError:
        return {}

# Function to save contacts to a file
def save_contacts_to_file(contacts):
    with open('contacts.json', 'w') as file:
        contacts_data = [contact.__dict__ for contact in contacts.values()]
        json.dump(contacts_data, file, indent=4)

# Main function to run the contact book program
def main():
    contacts = load_contacts_from_file()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add a new contact")
        print("2. View contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()