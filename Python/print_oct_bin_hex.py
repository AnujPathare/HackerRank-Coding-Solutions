def octal(n):

    if 1 <= n <= 7:
        return n

    quo = n//8
    result = 0
    lst = []

    while quo != 0:

        rem = n % 8
        quo = n // 8
        lst.append(rem)
        # print("quo",quo)

        # print("result",result)
        n = quo
        # print("n", n)

    octa = 0
    place = 1

    for i in lst:

        octa = (i*place) + octa
        place *= 10
    
    return octa

def hexadecimal(n):
    
    quo = n // 16
    rem = 0
    lst = []

    while quo != 0:
        
        rem = n % 16
        lst.append(rem)
        n = quo
        quo = n // 16

    lst.append(n)

    hexa = ""

    for i in range(-1, -len(lst) - 1, -1):
        temp = str(lst[i])

        hex_values = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}

        if temp in hex_values:
            hex_val = hex_values[temp]
            hexa += hex_val
        else:
            hexa += temp

    return hexa

def binary(n):

    quo = n // 2
    rem = 0
    lst = []
    while quo != 0:
        
        rem = n % 2
        lst.append(rem)
        n = quo
        quo = n // 2

    lst.append(1)

    bina = 0
    place = 1

    for i in lst:

        bina = (i*place) + bina
        place *= 10
   
    return bina

def print_formatted(number):
    # your code goes here
    width = len(str(binary(number)))

    for i in range(1, number+1):
        
        # octa = octal(i)
        # hexa = hexadecimal(i)
        # bina = binary(i)

        print(f"{i:>{width}} {octal(i):>{width}} {hexadecimal(i):>{width}} {binary(i):>{width}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# n = int(input("val: "))


# quo = n // 16
# rem = 0
# lst = []

# while quo != 0:
    
#     rem = n % 16
#     lst.append(rem)
#     n = quo
#     quo = n // 16

# lst.append(n)

# hexa = 0
# place = 1

# result = ""

# for i in range(-1, -len(lst) - 1, -1):
#     temp = str(lst[i])

#     hex_values = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}

#     if temp in hex_values:
#         hex_val = hex_values[temp]
#         result += hex_val
#     else:
#         result += temp

# print(result)


