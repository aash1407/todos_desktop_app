FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as local_file:
        todos_local = local_file.readlines()
    return todos_local


def write_todos(local_todos, filepath=FILEPATH):
    """ writes to-do items to a text file."""
    with open(filepath, 'w') as local_file:
        local_file.writelines(local_todos)

