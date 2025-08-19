import subprocess

def get_wifi_profiles():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace")
    data = data.split('\n')
    return [i.split(':')[1][1:-1] for i in data if "All User Profile" in i]

def get_wifi_passwords(profiles):
    results = []
    for profile in profiles:
        try:
            output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="backslashreplace")
            password = [line.split(':')[1][1:-1] for line in output.split('\n') if "Key Content" in line]
            results.append((profile, password[0] if password else "Not Found"))
        except Exception as e:
            results.append((profile, f"Error: {str(e)}"))
    return results

def display_passwords(passwords):
    for profile, password in passwords:
        print(f'Profile Name: {profile}')
        print(f'Password: {password}\n')

def save_to_file(passwords, filename="wifi_passwords.txt"):
    with open(r"C:\Users\p1a2r\OneDrive\Desktop\Git Hub Projects" + filename, 'w') as f:
        for profile, password in passwords:
            f.write(f'Profile Name: {profile}\n')
            f.write(f'Password: {password}\n\n')
    print(f"Passwords have been saved to {filename}")

def main():
    print("WiFi Password")
    print("1. Display passwords on screen")
    print("2. Save passwords to a text file")
    print("3. Display and save passwords")
    
    while True:
        choice = input("\nEnter your choice (1-3): ")
        if choice in ['1', '2', '3']:
            break
        print("Invalid choice. Please enter 1, 2, or 3.")
    
    profiles = get_wifi_profiles()
    passwords = get_wifi_passwords(profiles)
    
    if choice == '1':
        display_passwords(passwords)
    elif choice == '2':
        save_to_file(passwords)
    else:  # choice == '3'
        display_passwords(passwords)
        save_to_file(passwords)

if __name__ == "__main__":
    main()