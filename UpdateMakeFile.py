import re
import os


def main():
    with open('Makefile', 'r') as file:
        data = file.readlines()

    # Regex to find "SRC =" can between the SRC and the = can by any number of spaces or tabs
    regex = "^SRC\s*="
    serverRegex = "^SERVER\s*="
    clientRegex = "^CLIENT\s*="

    files = []
    server = []
    client = []

    if os.path.exists("src"):
        for file in os.listdir("src/common"):
            files.append("src/common/" + file)
        for file in os.listdir("src/server"):
            server.append("src/server/" + file)
        for file in os.listdir("src/client"):
            client.append("src/client/" + file)

    # For each line in the file
    for i in range(len(data)):
        # If the line matches the regex
        if re.search(regex, data[i]):
            data[i] = data[i].split("=")[0] + "=".rstrip() + " " + " ".join(files) + "\n"
            continue
        if re.search(serverRegex, data[i]):
            data[i] = data[i].split("=")[0] + "=".rstrip() + " " + " ".join(server) + "\n"
            continue
        if re.search(clientRegex, data[i]):
            data[i] = data[i].split("=")[0] + "=".rstrip() + " " + " ".join(client) + "\n"
            continue

    with open('Makefile', 'w') as file:
        file.writelines(data)


if __name__ == "__main__":
    main()
