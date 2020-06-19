fibonacci_list = [1,2]
sum_of_even_terms = []
for i in range(2,1000000000):
    if fibonacci_list[i-2]+fibonacci_list[i-1] < 4000000:
        fibonacci_list.append(fibonacci_list[i-2]+fibonacci_list[i-1])
    else:
        break
    

print(fibonacci_list)
            
for i in fibonacci_list:
    if i % 2 == 0:
        sum_of_even_terms.append(i)

print(sum(sum_of_even_terms))