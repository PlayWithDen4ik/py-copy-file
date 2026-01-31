def copy_file(command: str) -> None:
    if not command:
        return
    split_command = command.split()
    if len(split_command) != 3:
        return
    cmd, source, dest = split_command
    if cmd != "cp":
        return
    if source == dest:
        return
    try:
        with open(source, "r") as file1, open(dest, "w") as file2:
            file2.write(file1.read())
    except FileNotFoundError:
        return
