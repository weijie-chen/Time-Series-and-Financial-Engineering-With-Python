
import os

def print_directory_tree(root_dir, prefix=''):
    """
    Prints the directory tree starting from the root directory.

    Args:
        root_dir (str): The root directory to start printing the tree from.
        prefix (str): The prefix for the current level (used for indentation).
    """
    # Get the list of files and directories in the current directory
    items = sorted(os.listdir(root_dir))

    # Iterate over the items
    for index, item in enumerate(items):
        # Create the full path
        item_path = os.path.join(root_dir, item)
        
        # Check if it's the last item in the current directory
        is_last = (index == len(items) - 1)

        # Determine the prefix for the current item
        current_prefix = '└── ' if is_last else '├── '

        # Print the current item with the appropriate prefix
        print(prefix + current_prefix + item)

        # If the current item is a directory, recursively print its contents
        if os.path.isdir(item_path):
            # Use a new prefix for the next level
            new_prefix = '    ' if is_last else '│   '
            print_directory_tree(item_path, prefix + new_prefix)

if __name__ == '__main__':
    print_directory_tree(root_dir='.', prefix='')