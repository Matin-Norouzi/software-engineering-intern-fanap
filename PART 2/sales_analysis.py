FILE_NAME = 'sales.csv'

# Step 1: Create the CSV file manually using open and write

with open(FILE_NAME, 'w') as file:
    # Write the header
    file.write("date,amount,product\n")
    # Write sample data rows
    file.write("2025-01-01,10000,Keyboard\n")
    file.write("2025-01-01,15000,Mouse\n")
    file.write("2025-01-02,20000,Monitor\n")
    file.write("2025-01-03,5000,USB Cable\n")
    file.write("2025-01-03,35000,Laptop\n")
    file.write("2025-01-04,10000,Mouse Pad\n")
    file.write("2025-01-05,25000,Headphones\n")
    file.write("2025-01-06,18000,Webcam\n")
    file.write("2025-01-06,8000,Speaker\n")
    file.write("2025-01-07,4000,Adapter\n")

print(f"{FILE_NAME} created.")

# Step 2: Read and analyze the file
def analyze_sales():
    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()
    total = 0
    count = 0
    daily_totals = {}

    for i in range(1, len(lines)):  # Skip header
        parts = lines[i].strip().split(',')
        date = parts[0]
        amount = int(parts[1])
        total += amount
        count += 1
        if date in daily_totals:
            daily_totals[date] += amount
        else:
            daily_totals[date] = amount

    average = total / count
    max_day = ""
    max_amount = 0

    for day in daily_totals:
        if daily_totals[day] > max_amount:
            max_amount = daily_totals[day]
            max_day = day

    print("\nSales Summary:")
    print("Total Sales:", total)
    print("Average Sale Amount:", round(average, 2))
    print("Highest Sales in One Day:", max_amount, "on", max_day)




analyze_sales()