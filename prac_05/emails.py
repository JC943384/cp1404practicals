def main():
    user_data = {}
    while True:
        email = input("Please enter your email (enter a blank is exit): ").strip()
        if not email:
            break

        name = get_name(email)
        if name:
            name = name.replace(".", "  ")
            data_name = input(f"Is your name {name}? (Y/n)").strip().lower()

            if data_name in ["", "y"]:
                user_data[email] = name
            else:
                name = input("Please enter your correct name: ").strip()
                user_data[email] = name
        else:
            print("Invalid email format. Please enter a valid email.")
    print("\nUser Data")
    for email, name in user_data.items():
        print(f"{name} ({email})")


def get_name(email):
    parts = email.split('@')
    if len(parts) == 2:
        name_parts = parts[0].split('.')
        formatted_name = ' '.join(part.capitalize() for part in name_parts)
        return formatted_name
    return None


if __name__ == "__main__":
    main()
