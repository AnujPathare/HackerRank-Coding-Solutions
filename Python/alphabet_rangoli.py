import string


def print_rangoli(size):
    # your code goes here
    lower = list(string.ascii_lowercase[0:size][::-1])
    
   
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# import string
# def print_rangoli(n):
#     width = n * 4 - 3
#     re_alpha = list(string.ascii_lowercase[0:n][::-1])
    
#     for i in range(n):
#         row = re_alpha[:(i+1)] + re_alpha[:i][::-1]
#         print("-".join(row).center(width, "-"))


#     for i in range(n-1,0,-1):
#         row = re_alpha[:i] + re_alpha[:i-1][::-1]
#         print("-".join(row).center(width, "-"))


#     # for i in range(n-2, -1, -1):
#     #     row = re_alpha[:(i+1)] + re_alpha[:i][::-1]
#     #     print("-".join(row).center(width, "-"))

# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)

"""import string

lower = list(string.ascii_lowercase)  


def print_rangoli(size):
    # your code goes here

    if size == 1:
        print('a')
    
    else:
        n = size
        
        for x in range(n-1):
            
            
            for _ in range(2*n-2):
                print('-', end="")
            
            alpha = n
            for i in range(x+1):
                print(lower[x+alpha-1], end="")
                if i != x:
                    print('-', end="")
                alpha -= 1

            alpha = n-1
    
            if x != 0:
                for i in range(x):
                    print('-', end='')
                    print(lower[alpha+1], end='')
                    alpha += 1

            alpha = n
            for _ in range(2*n-2):
                print('-', end="")

            print("")
            n -= 1

        n = size
        alpha = n
        
        for i in range(2*n-1):
            if i < n:
                print(lower[alpha-1], end='')
                print('-', end='')
                alpha -= 1
            else:
                alpha += 1
                print(lower[alpha], end='')
                if i != (2*n-2):
                    print('-', end='')
                
        print("")
        n = size
        alpha = n

        for x in range(n-1):
            
            for _ in range((x+1)*2):
                print('-', end="")
                
            alpha = n + x
            for i in range(n-1):
                print(lower[alpha-1], end="")
                if i != n-2:
                    print('-', end='')
                alpha -= 1


            for i in range(n-2):
                alpha += 1
                print('-', end='')
                print(lower[alpha], end='')
                

            for _ in range((x+1)*2):
                print('-', end="")

            print("")
            n -= 1

        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
"""