def copy_file(command: str) -> None:
    if command.startswith("cp"):
        split_command = command.split()
        if len(split_command) != 3:
            return
        _, source, dest = split_command
        if source == dest:
            return
        try:
            with open(source, "r") as file1, open(dest, "w") as file2:
                file2.write(file1.read())
        except FileNotFoundError:
            print("No file found")
