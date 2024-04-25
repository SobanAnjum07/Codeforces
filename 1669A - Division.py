# For Division 1: 1900≤rating
# For Division 2: 1600≤rating≤1899
# For Division 3: 1400≤rating≤1599
# For Division 4: rating≤1399

def sol(n):
    
    if n <= 1399:
        return "Division 4"
    elif 1400 <= n <= 1599:
        return "Division 3"
    elif 1600 <= n <= 1899:
        return "Division 2"
    else:
        return "Division 1"

if __name__ == "__main__":
    
    for _ in range(int(input())):
        
        n = int(input())
        print(sol(n))