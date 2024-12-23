def sol(exam):
    
    sorted_exam = sorted(exam, key=lambda x: (x[0], x[1]))
    
    best = -1
    
    for i in range(len(sorted_exam)):
        if best <= sorted_exam[i][1]:
            best = sorted_exam[i][1]
        else:
            best = sorted_exam[i][0]
    return best
            

if __name__ == "__main__":
    exam = []
    for i in range(int(input())):
        
        a = tuple(map(int, input().split()))
        
        exam.append(a)
    
    print(sol(exam))