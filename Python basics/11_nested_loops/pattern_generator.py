print("======PATTERN GENERATOR======")
print("1. Right Triangle")
print("2. Inverted Triangle")
print("3. Square")
print("4. Rectangle")
print("5. Number Triangle")
print("6. Left Triangle")
choice = int(input("Enter a pattern: "))

if choice == 1:
    size = int(input("Enter the size of the pattern: "))
    for i in range(1, size+1):
        for j in range(1, i+1):
            print("*", end = "")
        print()
elif choice == 2:
    size = int(input("Enter the size of the pattern: "))
    for i in range(size):
        for j in range(size-i):
            print("*", end = "")
        print()
elif choice == 3:
    size = int(input("Enter the size of the pattern: "))
    for i in range(1, size+1):
        for j in range(1, size+1):
            print("*", end ="")
        print()
elif choice == 4:
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    for i in range(rows):
        for j in range(cols):
            print("*", end = "")
        print()
elif choice == 5:
    size = int(input("Enter the size of the pattern: "))
    for i in range(1, size+1):
        for j in range(1, i+1):
            print(j, end = "")
        print()
elif choice == 6:
    size = int(input("Enter the size of the pattern: "))
    for i in range(size):
        for j in range(size-i-1):
            print(" ", end ="")
        for j in range(i+1):
            print("*", end = "")
        print()
else:
    print("Invalid choice")




