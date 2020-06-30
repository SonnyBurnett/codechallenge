# The sum of the squares of the first ten natural numbers is,

# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,

# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_sqr(n):
    answer=0
    for number in range(1,n+1):
        answer += number ** 2
    return answer

def sqr_sum(n):
    answer=0
    for number in range(1,n+1):
        answer += number
    return answer ** 2
   
if __name__ == "__main__":
    answer1 = sqr_sum(10) - sum_sqr(10)
    print(answer1)
    answer2 = sqr_sum(100) - sum_sqr(100)
    print(answer2)