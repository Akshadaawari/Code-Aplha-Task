lim = int (input("Enter the limit for fibonacci seq:"))
def generate_fibonacci(lim):
    fibonacci_seq = [0,1]
    while fibonacci_seq[-1]+fibonacci_seq[-2] <= lim:
        new_fibonacci = fibonacci_seq[-1]+fibonacci_seq[-2]
        fibonacci_seq.append(new_fibonacci)
    return fibonacci_seq
#lim = int (input("Enter the limit for fibonacci seq:"))
fibonacci_num = generate_fibonacci(lim)
print("fibonacci seq up to ",lim, ":",fibonacci_num)
#Explanation:firstly

