# executes the program
def main() -> None:
    try:
        with open("src/secret_data.txt", "r") as file:
            print("Login mit Daten:\n")
            while True:
                ch = file.read(1)
                if not ch:
                    break
                print(ch, end="")
    except ValueError:
        print("Die Datei konnte nicht geöffnet werden.")
        return 1
    return 0

main()