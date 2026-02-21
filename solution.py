print("Laptop Service Center")

services = ["Repair", "Upgrade", "Cleaning"]
price = [1500, 3000, 800]

service = input("Enter service: ")
qty = int(input("Enter quantity: "))

index = services.index(service)
total = price[index] * qty

if total > 3000:
    discount = total * 0.1
else:
    discount = 0

print("Service:", service)
print("Total:", total)

for i in range(3):
    print("Booked")

print("End")