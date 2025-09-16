# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]

def total_sales_by_product(data, product_key):
    """Calculates the total sales of a specific product in 30 days."""
    total = 0
    for day_data in data:
        total += day_data.get(product_key, 0)
    return total


def average_daily_sales(data, product_key):
    """Calculates the average daily sales of a specific product."""
    total = total_sales_by_product(data, product_key)
    if len(data) == 0:
        return 0
    return total / len(data)


def best_selling_day(data):
    """Finds the day with the highest total sales."""
    max_sales = -1
    best_day = None
    for day_data in data:
        daily_total = day_data.get("product_a", 0) + day_data.get("product_b", 0) + day_data.get("product_c", 0)
        if daily_total > max_sales:
            max_sales = daily_total
            best_day = day_data.get("day")
    return best_day


def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""
    count = 0
    for day_data in data:
        if day_data.get(product_key, 0) > threshold:
            count += 1
    return count


def top_product(data):
    """Determines which product had the highest total sales in 30 days."""
    products = ["product_a", "product_b", "product_c"]
    product_totals = {p: total_sales_by_product(data, p) for p in products}
    
    best_product = None
    max_total = -1
    
    for product, total in product_totals.items():
        if total > max_total:
            max_total = total
            best_product = product
            
    return best_product

def worst_selling_day(data):
    """Encuentra el día con las peores ventas totales."""

    min_sales = float('inf')
    worst_day = None

    for day_data in data:
        daily_total = day_data.get("product_a", 0) + day_data.get("product_b", 0) + day_data.get("product_c", 0)
        if daily_total < min_sales:
            min_sales = daily_total
            worst_day = day_data.get("day")
    return worst_day


def top_three_days(data):
    """Ordena los días por ventas totales y muestra los 3 mejores."""

    days_with_totals = []

    for day_data in data:
        daily_total = day_data.get("product_a", 0) + day_data.get("product_b", 0) + day_data.get("product_c", 0)
        days_with_totals.append({"day": day_data.get("day"), "total_sales": daily_total})
    
    sorted_days = sorted(days_with_totals, key=lambda x: x["total_sales"], reverse=True)
    
    return sorted_days[:3]

def product_sales_range(data, product_key):
    """Calcula el rango (máximo - mínimo) de las ventas de un producto."""

    sales = [day_data.get(product_key, 0) for day_data in data]

    if not sales:
        return 0
    return max(sales) - min(sales)

# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))

print("Day with the worst sales:", worst_selling_day(sales_data))
print("Top 3 days by total sales:", top_three_days(sales_data))
print("Sales range for product_c:", product_sales_range(sales_data, "product_c"))