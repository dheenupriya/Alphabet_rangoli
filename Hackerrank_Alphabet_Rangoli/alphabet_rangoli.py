def print_rangoli(size):
    # your code goes here
    alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    s=[]
    for i in range(size):
        pattern = '-'.join(alp[i:size]) 
        s.append((pattern[::-1]+pattern[1:]).center(4*size-3,'-'))
    print('\n'.join(s[::-1]+s[1:]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)