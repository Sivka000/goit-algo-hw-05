def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#Декодер для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please provide the correct number of arguments."
    return inner

#Додавання контакту в словник
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

#Видалення контакту з словника та попередження про видалення
@input_error
def delete_contact(args, contacts):
    name = args[0]
    if name in contacts:
        confirmation = input(f"Are you sure you want to delete a contact '{name}'? (y/n): ").strip().lower()
        if confirmation in ("y", "yes"):
            del contacts[name]
            return f"Contact '{name}' deleted."
        else:
            return "Deletion is canceled."
    else:
        raise KeyError

#Оновлення номеру
@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

#Пошук номеру через ім'я
@input_error
def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}."
    else:
        raise KeyError

#Список всіх контактів
@input_error
def list_contacts(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts available."

#Список команд для допомоги користувачу
command_list = (
    "Command list:\n"
    "Add (username) (phone) - adds a contact;\n"
    "Delete, del (username) - delete a contact;\n"
    "Phone (username) - searches for a phone number by username;\n"
    "Change (username) (phone) - stores the new phone number for username in memory;\n"
    "All, list - shows all contacts;\n"
    "Close, exit - finishes the work;"
    )
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input: #Обробка помилки при пустому вводі
            print("Error!\nPlease enter a command.")
            continue

        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command in ["delete", "del"]:
            print(delete_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command in ["all", "list"]:
            print(list_contacts(contacts))
        elif command in ["help", "command"]:
            print(command_list)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()