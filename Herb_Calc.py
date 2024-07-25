def main():
    total_price = 0
    total_ounces = 0
    herb_count = 0
    item = []

    while True:
        try:
            name = input("Enter the name of the item (or type 'done' to finish): ")
            if name.lower() == 'done':
                break
            price = float(input("Enter the price of the item: "))
            size = float(input("Enter the size of the item in ounces: "))
            total_price += price
            total_ounces += size
            herb_count += 1
            item.append((name, price, size))
        except ValueError:
            print("Invalid input. Please enter numeric values for price and size.")

    if herb_count > 0:
        average_price_per_ounce = total_price / total_ounces
        print("\nIndividual item entered:")
        for i, (name, price, size) in enumerate(item, 1):
            print(f"Herb {i}: Name = {name}, Price = ${price:.2f}, Size = {size:.2f} oz")
        print(f"\nTotal price of all items: ${total_price:.2f}")
        print(f"Average price per ounce: ${average_price_per_ounce:.2f}")
    else:
        print("No items were entered.")

if __name__ == "__main__":
    main()