# LMS Member Registration Module

members = []


def register_member(member_id, name, email, phone):
    if not member_id or not name or not email or not phone:
        return "Error: All fields are required."

    for member in members:
        if member["id"] == member_id:
            return "Error: Member ID already exists."

    if "@" not in email or "." not in email:
        return "Error: Invalid email address."

    members.append({
        "id": member_id,
        "name": name,
        "email": email,
        "phone": phone
    })

    return "Member registered successfully!"


def display_members():
    if not members:
        print("No members registered.")
        return

    for member in members:
        print(member)


def main():
    while True:
        print("\n1. Register Member")
        print("2. Display Members")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            member_id = input("Member ID: ").strip()
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            phone = input("Phone: ").strip()

            print(register_member(member_id, name, email, phone))

        elif choice == "2":
            display_members()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()