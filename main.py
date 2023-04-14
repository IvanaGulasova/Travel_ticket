greet = "VITEJTE U NASI APLIKACE DESTINATIO!"
cities = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
domains = ("gmail.com", "seznam.cz", "email.cz")
discount = ("Olomouc", "Svitavy", "Ostrava")
prices = (150, 200, 120, 120, 180, 100)
double_line = "=" * 35
line = "-" * 35
table = """-----------------------------------
   NUM. |   LOCATION  |   PRICES(Kc)
-----------------------------------
   1    |   Praha     |     150
   2    |   Vieden    |     200
   3    |   Olomouc   |     120
   4    |   Svitavy   |     120
   5    |   Zlin      |     180
   6    |   Ostrava   |     100
"""

def main():
    print(f"\n{greet}\n{table}{line}")
    location = locat()
    location_name = locat_name(cities, location)
    ticket_price = prices[int(location) - 1]
    print(line)

    while True:
        f_name = input("First name: ")
        l_name = input("Last name: ")
        if f_name.isalpha() and len(f_name) >= 3 and l_name.isalpha() and len(l_name) >= 3:
            break
        else:
            print(f"Incorrect inputs for first name or\nlast name, please try again.")
            print(line)

    print(f"{double_line}\nCustomer: {f_name} {l_name}\n{double_line}")

    mail = e_mail()
    end = conclusion(f_name, location_name, ticket_price, mail)



def locat():
    while True:
        try:
            location = int(input("Select a location number (1-6): "))
            if location >= 1 and location < 7:
                break
            else:
                print(f"The entered number does not exist,\n- enter number 1-6.\n{line}")
        except ValueError:
            print(f"Incorrect input - enter number 1-6\n{line}")
    return  location

def locat_name(cities, location):
    location_name = cities[int(location) - 1]
    if location_name in discount:
        discounted_ticket = prices[int(location) - 1] * 0.75
        print(f"Travel ticket to: {location_name}.")
        print(f"-25 % on the ticket price!\nPrice: {discounted_ticket} Kc.")
    else:
        ticket_price = prices[int(location) - 1]
        print(f"Travel ticket to: {location_name}.\nPrice: {ticket_price} Kc.")
    return location_name

def e_mail():
    while True:
        mail = input("E-mail: ")
        end = mail.split("@")[1]
        if "@" in mail and end in domains:
            print("Verified email address.")
            print(line)
            break
        else:
            print("Incorrectly entered e-mail address.")
            print(line)
    return mail

def conclusion(f_name, location_name, ticket_price, mail):
    print(f"{f_name}, thank you for the order.")
    print(f"Travel ticket to: {location_name}")
    print(f"Price: {ticket_price} Kc")
    print(f"Travel document will be sent to your\nemail: {mail}\n{line}")

main()