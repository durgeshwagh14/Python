def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone}\n")
    print(f"✅ Contact '{name}' saved.")

def view_contacts():
    print("\n📒 Contact List:")
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("📂 No contacts found.")
            else:
                for i, contact in enumerate(contacts, start=1):
                    name, phone = contact.strip().split(",")
                    print(f"{i}. {name} - {phone}")
    except FileNotFoundError:
        print("📂 No contacts file found.")

def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False
    try:
        with open("contacts.txt", "r") as file:
            for contact in file:
                name, phone = contact.strip().split(",")
                if search_name in name.lower():
                    print(f"🔍 Found: {name} - {phone}")
                    found = True
        if not found:
            print("❌ No matching contact found.")
    except FileNotFoundError:
        print("📂 No contacts file found.")

# Simple Menu
while True:
    print("\n📇 Contact Book Menu")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("👋 Exiting Contact Book.")
        break
    else:
        print("⚠️ Invalid choice. Please try again.")
