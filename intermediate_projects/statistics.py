
from scipy import stats
import numpy as np
def intializer():
    print("***  Welcome to Corny  ***")

    list=[]
    while True:
        user_input=input("Enter your number or Q to quit: ")
        if user_input.upper() == "Q":
            break
        try :
            j=float(user_input)
            list.append(j)
        except:
            print("Invalid input. Enter a number: ")
            continue
    return list
        
def calculation(list):
    print("\033c")
    print(list)
    ar= np.array(list)
    count=0   

    try:
        count= len(list)
        print("Count:",count)
    except:
        print("Count: Error")

    try:
        m=max(list)
        print("Max:", m)
    except:
        print("Max: Error")

    try:
        mi=min(list)
        print("Min:", mi)
    except:
        print("Min: Error")

    try:
        total=np.sum(ar).round(2)
        print("Sum:", total)
    except:
        print("Sum: Error")
        
    try:
        mean= np.average(ar).round(2)
        print("Mean:",mean)
    except:
        print("Mean: Error")

    try:
        mode= max(set(list), key=list.count)
        print(f"Mode: {mode}")
    except:
        print("Mode: Error")   


    try:
        print("Range:",m-mi)
    except:
        print("Range: Error")   
        
    try:
        median= np.median(list)
        print(f"Median: {median}")
    except:
        print("Median: Error")   

    q1 = np.percentile(ar, 25).round(3)
    q3 = np.percentile(ar, 75).round(3)
    iqr= stats.iqr(ar).round(2)
    print(f"Q1: {q1}")    
    print(f"Q3: {q3}")
    print(f"IQR: {iqr}")

    try:
        pvariance= np.var(ar).round(2)
        print(f"Popu Variance: {pvariance}")
    except:
        print("Popu Variance: Error")  

    try:
        pstd= np.std(ar).round(2)
        print(f"Popu Std: {pstd}")
    except:
        print("Popu Std: Error")  
        
    try:
        svariance= np.var(list, ddof=1).round(2)
        print(f"Sample Variance:{svariance}")
    except:
        print("Sample Variance: Error") 

    try:
        sstd= np.std(ar, ddof=1).round(2)
        print(f"Sample Std: {sstd}")
    except:
        print("Sample Std: Error") 

def main():
    while True:
        numbers= intializer()
        calculation(numbers)
        check= input("Press Enter to continue or q to Quit: ")
        if check=="":
            continue
        elif check.upper()=="Q":
            break
        else:
            print("Invlaid input. Exiting the application")
            break

if __name__== "__main__":
     main()
