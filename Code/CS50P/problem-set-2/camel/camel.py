camel_case_var = input("Enter a variable name in camel case: ")

snake_case_var = ''
for char in camel_case_var:
    if char.isupper():
        snake_case_var += '_' + char.lower()
    else:
        snake_case_var += char

snake_case_var = snake_case_var.lstrip('_')

print("Snake case variable name:", snake_case_var)
