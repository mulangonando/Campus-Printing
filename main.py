# CampusPrint, stage 1: complete TODO 1 through TODO 8.
# Starter scaffold: menu repetition is supplied as an example of a while loop.
# You will write the field-validation loops and a for loop yourself.

BW_RATE = 10
COLOUR_RATE = 30
BINDING_RATE = 50
BULK_THRESHOLD = 100

completed_orders = 0
session_pages = 0
session_revenue = 0
running = True

print("Welcome to CampusPrint")
while running:
    print("\n1. New order\n2. Session summary\n0. Exit")
    choice = input("Choice: ").strip()

    if choice == "1":
        # TODO 1: Read pages and copies with int(input(...)).
        # Write a while loop for EACH field to retry until it is in range.
        # pages: 1..500; copies: 1..100. Do not count failed attempts.
        pass

        # TODO 2: Read mode (B/C) and binding (Y/N).
        # .strip().upper() is supplied vocabulary: it removes surrounding
        # whitespace and normalises letter case. Retry invalid choices.
        pass

        # TODO 3: Select rate with if/else and calculate printed_pages
        # and printing_subtotal. Use the named tariff constants above.
        pass

        # TODO 4: Select the bulk discount; calculate binding_charge
        # and total. Discount applies to printing only, never binding.
        pass

        # TODO 5: Display the five receipt lines in BUSINESS_RULES.md.
        # Example formatting: print("Printed pages:", printed_pages)
        pass

        # TODO 6: Use for ... in range(...) to print Copy 1 of n, etc.
        # range stop values are exclusive: check both 1 and 3 copies.
        pass

        # TODO 7: Update the THREE session accumulators exactly once,
        # after a valid order. Remove the temporary message below.
        print("New order is not implemented yet.")

    elif choice == "2":
        # TODO 8a: Display the three session summary lines.
        print("Summary is not implemented yet.")
    elif choice == "0":
        # TODO 8b: Display the same summary before terminating the loop.
        # Keep the line below; explain why the loop stops after it.
        running = False
    else:
        print("Invalid choice.")

print("Goodbye.")
