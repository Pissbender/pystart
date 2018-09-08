from urllib.parse import parse_qs

my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
print(repr(my_values))

print("Red: ", my_values.get("red"))  # Returns ['5']
print("Green: ", my_values.get("green"))  # Returns ['']
print("Opacity: ", my_values.get("opacity"))  # Returns None

# Do the job, hard to read
red = int(my_values.get("red", [''])[0] or 0)  # Returns 5 as int
green = int(my_values.get("green", [''])[0] or 0)  # Returns 0 as int
opacity = int(my_values.get("opacity", [''])[0] or 0)  # Returns 0 as int

print('Red: %r' % red)
print('Green: %r' % green)
print('Opacity: %r' % opacity)

# Better method
red = my_values.get("red")
red = int(red[0]) if red[0] else 0

print('Red: %r' % red)


# With helper method
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if (found[0]):
        found = int(found[0])
    else:
        found = default
    return found


green = get_first_int(my_values, 'green')
print('Green: %r' % green)
