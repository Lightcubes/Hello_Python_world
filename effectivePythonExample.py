import struct

def main():
    numbers = [8, 3, 2, 4, 1, 5, 7, 6, 0, 13, 11]
    group = {1, 3, 5, 7, 9}
    sortPriority(numbers, group)
    print(numbers)
'''
    for i in range (127, 255):
        print(i, ">>>", chr(i), '\n')
'''



def sortPriority(numbers, group):
    def helper(x):
        if x in group:
            print(0, x)
            return(0, x)
        else:
            print(1, x)
            return(1, x)
    print(numbers.sort(key = helper))


if __name__ == "__main__":
    main()
    data = struct.pack('>i4shf', 2, 'spam', 3, 1.234)
    print(data)