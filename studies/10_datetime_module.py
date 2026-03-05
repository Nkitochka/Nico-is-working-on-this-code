import datetime
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute

print(f'Day: {day}, month: {month}, year: {year}, hour: {hour}, minute: {minute}.')

time_now = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_now)

next_year = datetime(year = 2027, month = 1, day = 1)
diff_time = next_year - now
print(f'Till New Year: {diff_time}')