# Main
if __name__ == "__main__":
    n = input("length of square: ")
    m = input("width of square: ")
    a = input("length of flagton: ")
    n = int(n)
    m = int(m)
    a = int(a)
    b = m%a
    m2= m+a-b
    c = n%a
    n2= n+a-c
    print(m2*n2/a**2)
    
