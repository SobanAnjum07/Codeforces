
def sol():
    
    a =  int(input())
    b =  int(input())
    c =  int(input())
    
    
    
    # writing all the combination and thus the problem will be solved in constant time
    
    first = a + b + c
    second = a + b * c
    third = a * (b + c)
    fourth = a * b * c
    fifth = (a + b) * c
    
    return (max(first, second, third, fourth, fifth))

if __name__ == '__main__':
    print(sol())
    
