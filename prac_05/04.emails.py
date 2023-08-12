def get_name(email):
    parts = email.split('@')
    if len(parts) == 2:
        name = parts[0]
        return ' '.join(name.split('.')).title()
    return None


def main():
    user_date ={}
    while True:
        email = input("Please enter your email(enter a blank is exist):").strip()
        if not email:
            break

        name = get_name(email)
        if name:
           print(f"Get your name is:{name}")
           data_name = input("Is this name correct? [Y/n]").strip().lower()

           if data_name in ['', 'y']:
               user_date[email] = name
           else:
               name = input("Please enter your correct name:").strip()
               user_date[email] = name
        else:
             print("Invalid email format. Please enter a valid email.")
    print("\nUser Data:")
    for email, name in user_date.items():
        print(f"Email data: {email}, User name: {name}")
if __name__ =="__main__":
    main()



