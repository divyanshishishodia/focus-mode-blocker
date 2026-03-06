hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

websites = [
    "www.instagram.com",
    "instagram.com",
    "www.youtube.com",
    "youtube.com"
]

print("Focus Mode 🚀")
print("1. Start Blocking")
print("2. Stop Blocking")

choice = input("Enter choice: ")

if choice == "1":
    with open(hosts_path, "r+") as file:
        content = file.read()

        for site in websites:
            if site not in content:
                file.write(redirect + " " + site + "\n")

    print("Websites blocked!")

elif choice == "2":
    with open(hosts_path, "r+") as file:
        content = file.readlines()
        file.seek(0)

        for line in content:
            if not any(site in line for site in websites):
                file.write(line)

        file.truncate()

    print("Websites unblocked!")
