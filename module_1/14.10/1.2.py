while True:
    time = int(input("time from 24:00 in seconds: "))
    choice = input("Choice sec/min/hr: ")
    total_seconds = 86400
    left = total_seconds - time
    if choice == "sec":
        print(f"{left}")
    elif choice == "min":
        print(f"{left / 60}")
    elif choice == "hr":
        print(f"{left / 3600}")
    else:
        print("інкорект")