a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print("First four: ", a[:4])
print("Last four: ", a[-4:])
print("Middle two: ", a[3:-3])

print("\nFirst Twenty: ", a[:20])
print("Last Twenty: ", a[-20:])

b = a[4:]
print("\nBefore: ", b)
b[1] = 99
print("After: ", b)
print("No change: ", a)

print("\nBefore: ", a)
a[2:7] = [99, 22, 14]
print("After: ", a)

a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print("\nOdds: ", odds)
print("Evens: ", evens)

x = b'mongoose'
y = x[::-1]
print("\nY: ", y)

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("\n")
print(a[::2])
print(a[::-2])
print("\n")
print(a[2::2])
print(a[-2::-2])
print(a[-2:2:-2])
print(a[2:2:-2])