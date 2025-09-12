# euler projects: problem 2
# answer is: 4613732
numbers = [1,2]
def fibonacci(end):
    for i in range(end):
        numbers.append(numbers[-1]+numbers[-2])
        if numbers[-1] >= end:
            numbers.pop()
            break
fibonacci(4_000_000)
evensum = 0
for pointer in numbers:
    if pointer % 2 == 0:
        evensum = evensum + pointer
        print(evensum)
print (evensum)
