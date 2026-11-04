def countdown(n):
    if n == 0:
        print("Launch!")
        return
    print(n)
    countdown(n - 1)

# Driver Code
n = int(input("Enter countdown number: "))
countdown(n)