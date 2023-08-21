def main():
    f = int(input("Enter Fuel (1 for Petrol / 2 for Diesel):\n"))
    pol = input("Litre or Price (l / p):\n")
    
    if f == 1:
        if pol == 'p':
            pet = int(input("How much rupees Petrol you want:\n"))
            p = pet * 0.0095
            print(f"\n{p} liter petrol you got\nThank You Visit Again :)")
        else:
            pet = int(input("How much Liter Petrol you want:\n"))
            p = pet * 106.2
            print(f"\n{p} You want to pay\nThank You Visit Again :)")
    else:
        if pol == 'p':
            die = int(input("How much rupees Diesel you want:\n"))
            d = die * 0.0107
            print(f"\n{d} liter Diesel you got\nThank You Visit Again :)")
        else:
            die = int(input("How much Liter Diesel you want:\n"))
            d = die * 93.1
            print(f"\n{d} You want to pay\nThank You Visit Again :)")

if __name__ == "__main__":
    main()
