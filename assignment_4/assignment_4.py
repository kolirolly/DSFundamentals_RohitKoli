def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Avoid empty lines
                date, calories = line.strip().split(',')
                data.append((date, float(calories)))
    return data

def date_to_tuple(date_str):
    day, month, year = map(int, date_str.split('/'))
    return (year, month, day)

def tuple_to_date(date_tuple):
    year, month, day = date_tuple
    return f"{day:02d}/{month:02d}/{year:04d}"

def is_within_range(date, from_date, to_date):
    return from_date <= date <= to_date

def calculate_statistics(data, from_date, to_date):
    filtered_data = [cal for date, cal in data if is_within_range(date_to_tuple(date), from_date, to_date)]

    if not filtered_data:
        return None, None, None, None

    num_days = len(filtered_data)
    total_calories = sum(filtered_data)
    average_per_day = total_calories / num_days

    highest_calories_day = max(filtered_data)
    highest_calories_meal = highest_calories_day

    mean = average_per_day
    variance = sum((x - mean) ** 2 for x in filtered_data) / num_days
    std_dev = (variance) ** 0.5

    return average_per_day, std_dev, highest_calories_day, highest_calories_meal

def main():
    file_path = "/content/drive/MyDrive/DS_foundation/assignment_4/calories_2.csv"
    data = read_csv(file_path)

    from_date_str = input("Enter the from date (DD/MM/YYYY): ")
    to_date_str = input("Enter the to date (DD/MM/YYYY): ")

    from_date = date_to_tuple(from_date_str)
    to_date = date_to_tuple(to_date_str)

    average_per_day, std_dev, highest_calories_day, highest_calories_meal = calculate_statistics(data, from_date, to_date)

    if average_per_day is None:
        print("No data available for the given date range.")
    else:
        print(f"From Date: {tuple_to_date(from_date)}")
        print(f"To Date: {tuple_to_date(to_date)}")
        print(f"Average Calories/Day: {average_per_day:.2f}")
        print(f"Standard Deviation: {std_dev:.2f}")
        print(f"Highest Calories/Day: {highest_calories_day:.2f}")
        print(f"Highest Calories/Meal: {highest_calories_meal:.2f}")

if __name__ == "__main__":
    main()
