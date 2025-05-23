# Write a function in which you have filesystem and you have to simplify the path.
# The function should take a string representing a file path and return the simplified version of that path.
def simplify_path(path):
    # Split the path by slashes
    parts = path.split('/')

    # Initialize a stack to keep track of the simplified path
    stack = []

    for part in parts:
        if part == '' or part == '.':
            continue  # Ignore empty parts and current directory
        elif part == '..':
            if stack:
                stack.pop()  # Go up one directory if possible
        else:
            stack.append(part)  # Add the valid part to the stack

    # Join the stack to form the simplified path
    simplified_path = '/' + '/'.join(stack)
    return simplified_path

c1=simplify_path("/home/")
print(c1)  # Output: "/home"
