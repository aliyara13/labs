def calculate_running_average(numbers):
    running_sum = 0
    averages = []
    
    for i, num in enumerate(numbers, 1):
        running_sum += num
        averages.append(running_sum / i)
    
    return averages

numbers = [1, 2, 3, 4, 5]
running_averages = calculate_running_average(numbers)
print("Running averages as the series progresses:", running_averages)
