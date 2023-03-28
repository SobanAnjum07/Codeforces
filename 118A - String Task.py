if __name__ == '__main__':
    s = input()
    s = s.lower()
    
    resultant_str = ''
    
    for ele in s:
        
        if ele in ['a', 'e', 'i', 'o', 'y', 'u']:
            pass
        
        else:
            resultant_str += '.' + ele
            
    print(resultant_str)
    