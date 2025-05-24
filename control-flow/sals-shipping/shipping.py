from decimal import Decimal, ROUND_HALF_UP

def calculate_shipping_cost(weight, rate, flat_charge=Decimal("0.00")):
  return (rate * weight + flat_charge).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

try:
    weight = Decimal(input("Enter shipping weight: "))
    if weight <= 0:
        raise ValueError("Please enter a positive weight.")
except (InvalidOperation, ValueError) as e:
    print("There was an error:", e)
    exit()

# Ground Shipping
ground_shipping_flat = Decimal("20.00")
if weight <= 2:
    ground_shipping_rate = Decimal("1.50")
elif weight <= 6:
    ground_shipping_rate = Decimal("3.00")
elif weight <= 10:
    ground_shipping_rate = Decimal("4.00")
else:
    ground_shipping_rate = Decimal("4.75")
ground_shipping_cost = calculate_shipping_cost(weight, ground_shipping_rate, ground_shipping_flat)

# Premium Ground Shipping
premium_ground_shipping_cost = Decimal("125.00")

# Drone Shipping
if weight <= 2:
    drone_shipping_rate = Decimal("4.50")
elif weight <= 6:
    drone_shipping_rate = Decimal("9.00")
elif weight <= 10:
    drone_shipping_rate = Decimal("12.00")
else:
    drone_shipping_rate = Decimal("14.25")
drone_shipping_cost = calculate_shipping_cost(weight, drone_shipping_rate)

# Calculate cheapest option
if ground_shipping_cost < premium_ground_shipping_cost and ground_shipping_cost < drone_shipping_cost:
    print(f"Cheapest shipping: Ground Shipping for ${ground_shipping_cost:.2f}")
elif premium_ground_shipping_cost < ground_shipping_cost and premium_ground_shipping_cost < drone_shipping_cost:
    print(f"Cheapest shipping: Premium Ground Shipping for ${premium_ground_shipping_cost:.2f}")
else:
  print(f"Cheapest shipping: drone Shipping for ${drone_shipping_cost:.2f}")