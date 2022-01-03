'''You are given an integer N

. Your task is to print an alphabet rangoli of size N
'''

def rangoli():
    import string
    alpha = string.ascii_lowercase
    n= int(input("ENter the size :"))
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))

    print('\n'.join(L[:0:-1] + L))



rangoli()
