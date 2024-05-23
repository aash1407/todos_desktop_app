import os
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items. If the file does not exist, create it.
    """
    # Create the file if it doesn't exist
    if not os.path.exists(filepath):
        with open(filepath, 'w') as local_file:
            open(filepath, 'w').close()

    with open(filepath, 'r') as local_file:
        todos_local = local_file.readlines()
    return todos_local


def write_todos(local_todos, filepath=FILEPATH):
    """ writes to-do items to a text file."""
    with open(filepath, 'w') as local_file:
        local_file.writelines(local_todos)

