#Theory deleted for comfortable use#
import statistics



ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)

ages.sort()
print(ages)

print(f'Min num: {ages[0]}. Also the max num is: {ages[-1]}.')

min = ages[0]
max = ages[-1]
ages.insert(0, min)
ages.insert(-1, max)
print(ages)

#median
median = (len(ages) / 2) -1
print(f'Median of this list: {ages[int(median)]}')

#avg num
average = sum(ages) / len(ages)
print(f'Average is: {average}')

#range(max - min = x)
range_ages = max - min
print(f'Range of list is: {range_ages}')

#last
diff_min_avg = min - average
diff_max_avg = max - average
print(f'\nDiff of min and avg = {diff_min_avg}, of max and avg = {diff_max_avg}.\nP.S. without abs() method\n')

abs_diff_min_avg = abs(diff_min_avg)
abs_diff_max_avg = abs(diff_max_avg)
print(f'\nDiff of min and avg = {abs_diff_min_avg}, of max and avg = {abs_diff_max_avg}.\nP.S. with abs() method\n')

if abs_diff_max_avg > abs_diff_min_avg:
    print('Max num is farther from avg!')

if abs_diff_max_avg < abs_diff_min_avg:
    print('Min num is farther from avg!')

elif abs_diff_max_avg == abs_diff_min_avg:
    print('Min and max nums are equal far from avg number!')