# Name: Ajit kumar
# Roll Number: 
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
highest_temprature =temperatures[0]
lowest_tumprature  =temperatures[0]
for num in temperatures:
  if num>highest_temprature:
    highest_temprature=num
  if num<lowest_tumprature:
    lowest_tumprature=num
  print("highest temprature:",highest_temprature)
print("lowest temprature:",lowest_tumprature)


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
hot_count=0
for tem in temperatures:
  if tem <=30:
    continue
  hot_count +=1

print(f"hot day(>30):{hot_count}")


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
hot_count = 0
day = 1
for temp in temperatures:
    if temp >= 40:
        print(f"Alert! Extreme temperature {temp}°C detected on Day {day}")
        break
    if temp > 30:
        hot_count += 1
    day += 1
print(f"Hot Days before alert: {hot_count}")