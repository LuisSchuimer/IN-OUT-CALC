import os
import calculator

#Clear Command
def clear():
    os.system("cls")





calc = calculator.calculator()
while True:
    clear()
    print("IN-OUT CALC")
    print("Predictions------")
    for i in calc.predictions:
        time, often, value = i.split(";")
        print(f"In {often}{time}: {value}€")
    print("----------------"
          "\n")
    print("Balances--------")
    for i in calc.balances:
        name, value = i.split(";")
        print(f"{name}: {value}€")
    print(f"""
----------
Balances: {calc.balance_value}€
----------
""")
    print(f"Income---------")
    for i in calc.incomes:
        name, value, often = i.split(";")
        print(f"{name}: {value}€ ({often})")
    print(f"""
----------
Income per Day: {round(calc.income_d, 2)}€
Income per Week: {round(calc.income_w, 2)}€
Income per Month: {round(calc.income_m, 2)}€
Income per Year: {round(calc.income_y, 2)}€
""")
    print("Expenditures----------")
    for i in calc.expenditures:
        name, value, often = i.split(";")
        print(f"{name}: {value}€ ({often})")
    print(f"""
----------
Expenditures per Day: {round(calc.expenditure_d, 2)}€
Expenditures per Week: {round(calc.expenditure_w, 2)}€
Expenditures per Month: {round(calc.expenditure_m, 2)}€
Expenditures per Year: {round(calc.expenditure_y, 2)}€

After Expenditures----------
Income per Day: {round(calc.income_d - calc.expenditure_d, 2)}€
Income per Week: {round(calc.income_w - calc.expenditure_w, 2)}€
Income per Month: {round(calc.income_m - calc.expenditure_m, 2)}€
Income per Year: {round(calc.income_y - calc.expenditure_y, 2)}€

Balance + Income - Expenditures--------
Balance after one Day: {round(calc.balance_value + calc.income_d - calc.expenditure_d, 2)}€
Balance after one Week: {round(calc.balance_value + calc.income_w - calc.expenditure_w, 2)}€
Balance after one Month: {round(calc.balance_value + calc.income_m - calc.expenditure_m, 2)}€
Balance after one Year: {round(calc.balance_value + calc.income_y - calc.expenditure_y, 2)}€

Savings Goals----------""")
    if not len(calc.savings_goals) == 0:
        if not calc.income_m - calc.expenditure_m == 0:
                for i in calc.savings_goals:
                    name, value = i.split(";")
                    print(f"{name}: {value}€ ({round(int(value)/(calc.income_m - calc.expenditure_m), 2)} Months until reached)")
        else:
            for i in calc.savings_goals:
                name, value = i.split(";")
                print(f"{name}: {value}€ ( ∞ Months until reached)")


    print(f"""
---------
Savings Goals: {round(calc.savings_goal_value, 2)}€
-----------
1. Add Income
2. Add Expenditure
3. Add Savings Goal
4. Add Balance
5. Time Machine
6. Edit
7. Delete
8. Make Report
""")
    action = input("]")

    #Actions
    if action == "1":
        clear()
        print("Add Income")
        print("Title of Income")
        title = input("]")
        print("Value")
        value = int(input("]"))
        print("""
1. Every Day
2. Every Week
3. Every Month
4. Every Year
        """)
        action_o = input("]")
        if action_o == "1":
            often =  "d"
        elif action_o == "2":
            often = "w"
        elif action_o == "3":
            often = "m"
        elif action_o == "4":
            often =  "y"
        calc.add_income(value, title, often)


    if action == "2":
        clear()
        print("Add Expenditure")
        print("Title of Expenditure")
        title = input("]")
        print("Value")
        value = int(input("]"))
        print("""
1. Every Day
2. Every Week
3. Every Month
4. Every Year
                """)
        action_o = input("]")
        if action_o == "1":
            often = "d"
        elif action_o == "2":
            often = "w"
        elif action_o == "3":
            often = "m"
        elif action_o == "4":
            often = "y"
        calc.add_expenditures(value, title, often)

    if action == "3":
        clear()
        print("Add Savings Goal")
        print("Title of Savings Goal")
        title = input("]")
        print("Value")
        value = int(input("]"))
        calc.add_savings_goal(value, title)

    if action == "4":
        clear()
        print("Add Balance")
        print("Title of Balance")
        title = input("]")
        print("Value")
        value = int(input("]"))
        calc.add_balance(value, title)

    if action == "5":
        clear()
        print("Time Machine")
        print("Time Format")
        print("""
1. Day
2. Week
3. Month
4. Year
                        """)
        action_o = input("]")
        if action_o == "1":
            often = "d"
        elif action_o == "2":
            often = "w"
        elif action_o == "3":
            often = "m"
        elif action_o == "4":
            often = "y"
        print(f"How many {often} do you want to fast forward")
        time = input(f"In {often}] ")
        calc.predict_balance(often, time)

    if action == "6":
        clear()
        found = False
        found_name = ""
        get = ""
        selected_par_list = ""
        selected_par = ""
        while found == False:
            count_b = 0
            last_b = ""
            count_i = 0
            last_i = ""
            count_e = 0
            last_e = ""
            count_sg = 0
            last_sg = ""
            if get == "":
                clear()
                print("Edit Parameters")
                print("Balances-----------")
                for i in calc.balances:
                    name, value = i.split(";")
                    print(f"{name}: {value}€ (B)")
                print("Incomes------------")
                for i in calc.incomes:
                    name, value, often = i.split(";")
                    print(f"{name}: {value} ({often}) (I)")
                print("Expenditures-------")
                for i in calc.expenditures:
                    name, value, often = i.split(";")
                    print(f"{name}: {value} ({often}) (E)")
                print("Savings Goals-------")
                for i in calc.savings_goals:
                    name, value = i.split(";")
                    print(f"{name}: {value} (SG)")
            else:
                clear()
                print("Edit Parameters")
                print("Balances-----------")
                count_b = 0
                last_b = ""
                for i in calc.balances:
                    name, value = i.split(";")
                    if get in name:
                        count_b += 1
                        last_b = name
                        print(f"{name}: {value}€ (B)")
                print("Incomes------------")
                count_i = 0
                last_i = ""
                for i in calc.incomes:
                    name, value, often = i.split(";")
                    if get in name:
                        count_i += 1
                        last_i = name
                        print(f"{name}: {value} ({often}) (I)")
                print("Expenditures-------")
                count_e = 0
                last_e = ""
                for i in calc.expenditures:
                    name, value, often = i.split(";")
                    if get in name:
                        count_e += 1
                        last_e = name
                        print(f"{name}: {value} ({often}) (E)")
                print("Savings Goals-------")
                count_sg = 0
                last_sg = ""
                for i in calc.savings_goals:
                    name, value = i.split(";")
                    if get in name:
                        count_sg += 1
                        last_sg = name
                        print(f"{name}: {value} (SG)")

            action = ""
            selected_par = ""
            selected_par_list = ""

            if count_b == 1:
                print(f"Do you want to select '{last_b}'?")
                action = input("3 for y or enter for no]")
                if action == "3":
                    selected_par = last_b
                    selected_par_list = "b"
                    found = True
            elif count_i == 1:
                print(f"Do you want to select '{last_i}'?")
                action = input("3 for y or enter for no]")
                if action == "3":
                    selected_par = last_i
                    selected_par_list = "i"
                    found = True
            elif count_e == 1:
                print(f"Do you want to select '{last_e}'?")
                action = input("3 for y or enter for no]")
                if action == "3":
                    selected_par = last_e
                    selected_par_list = "e"
                    found = True
            elif count_sg == 1:
                print(f"Do you want to select '{last_sg}'?")
                action = input("3 for y or enter for no]")
                if action == "3":
                    selected_par = last_sg
                    selected_par_list = "sg"
                    found = True


            if action == "":
                get = input("Enter name or keyword or press enter to see the entire list]")

        clear()
        if selected_par_list == "b":
            name_sel = ""
            value_sel = ""
            for i in calc.balances:
                name, value = i.split(";")
                if name == selected_par:
                    name_sel = name
                    value_sel = value
                    break
            print(f"Change the 'Title' of '{selected_par}' (prev. '{name_sel}')")
            new_name = input("Press Enter to skip] ")
            print(f"Change the 'Value' of '{selected_par}' (prev. '{value_sel}')")
            new_value = input("Press Enter to skip] ")
            if new_value == "":
                new_value = value_sel
            if new_name == "":
                new_name = name_sel

            new_data = f"{new_name};{new_value}"
            calc.change_balance(new_data, name_sel, value_sel)

        if selected_par_list == "i":
            name_sel = ""
            value_sel = ""
            often_sel = ""
            for i in calc.incomes:
                name, value, often = i.split(";")
                if name == selected_par:
                    name_sel = name
                    value_sel = value
                    often_sel = often
                    break
            print(f"Change the 'Title' of '{selected_par}' (prev. '{name_sel}')")
            new_name = input("Press Enter to skip] ")
            print(f"Change the 'Value' of '{selected_par}' (prev. '{value_sel}')")
            new_value = input("Press Enter to skip] ")
            print(f"Change the 'Often' of '{selected_par}' (prev. '{often_sel}')")
            print("""
1. Every Day
2. Every Week
3. Every Month
4. Every Year
                            """)
            action_o = input("Press Enter to skip] ")
            new_often = ""
            if action_o == "1":
                new_often = "d"
            elif action_o == "2":
                new_often = "w"
            elif action_o == "3":
                new_often = "m"
            elif action_o == "4":
                new_often = "y"

            if new_value == "":
                new_value = value_sel
            if new_name == "":
                new_name = name_sel
            if new_often == "":
                new_often = often_sel

            new_data = f"{new_name};{new_value};{new_often}"
            calc.change_income(new_data, name_sel, value_sel, often_sel)

        if selected_par_list == "e":
            name_sel = ""
            value_sel = ""
            often_sel = ""
            for i in calc.expenditures:
                name, value, often = i.split(";")
                if name == selected_par:
                    name_sel = name
                    value_sel = value
                    often_sel = often
                    break
            print(f"Change the 'Title' of '{selected_par}' (prev. '{name_sel}')")
            new_name = input("Press Enter to skip] ")
            print(f"Change the 'Value' of '{selected_par}' (prev. '{value_sel}')")
            new_value = input("Press Enter to skip] ")
            print(f"Change the 'Often' of '{selected_par}' (prev. '{often_sel}')")
            print("""
1. Every Day
2. Every Week
3. Every Month
4. Every Year
                                        """)
            action_o = input("Press Enter to skip] ")
            new_often = ""
            if action_o == "1":
                new_often = "d"
            elif action_o == "2":
                new_often = "w"
            elif action_o == "3":
                new_often = "m"
            elif action_o == "4":
                new_often = "y"

            if new_value == "":
                new_value = value_sel
            if new_name == "":
                new_name = name_sel
            if new_often == "":
                new_often = often_sel

            new_data = f"{new_name};{new_value};{new_often}"
            calc.change_expenditures(new_data, name_sel, value_sel, often_sel)

        if selected_par_list == "sg":
            name_sel = ""
            value_sel = ""
            for i in calc.savings_goals:
                name, value = i.split(";")
                if name == selected_par:
                    name_sel = name
                    value_sel = value
                    break
            print(f"Change the 'Title' of '{selected_par}' (prev. '{name_sel}')")
            new_name = input("Press Enter to skip] ")
            print(f"Change the 'Value' of '{selected_par}' (prev. '{value_sel}')")
            new_value = input("Press Enter to skip] ")
            if new_value == "":
                new_value = value_sel
            if new_name == "":
                new_name = name_sel

            new_data = f"{new_name};{new_value}"
            calc.change_savings_goals(new_data, name_sel, value_sel)

    if action == "7":
        clear()
        found = False
        found_name = ""
        get = ""
        selected_par_list = ""
        selected_par = ""
        while found == False:
            count_b = 0
            last_b = ""
            count_i = 0
            last_i = ""
            count_e = 0
            last_e = ""
            count_sg = 0
            last_sg = ""
            if get == "":
                clear()
                print("Delete Parameters")
                print("Balances-----------")
                for i in calc.balances:
                    name, value = i.split(";")
                    print(f"{name}: {value}€ (B)")
                print("Incomes------------")
                for i in calc.incomes:
                    name, value, often = i.split(";")
                    print(f"{name}: {value} ({often}) (I)")
                print("Expenditures-------")
                for i in calc.expenditures:
                    name, value, often = i.split(";")
                    print(f"{name}: {value} ({often}) (E)")
                print("Savings Goals-------")
                for i in calc.savings_goals:
                    name, value = i.split(";")
                    print(f"{name}: {value} (SG)")
            else:
                clear()
                print("Delete Parameters")
                print("Balances-----------")
                count_b = 0
                last_b = ""
                for i in calc.balances:
                    name, value = i.split(";")
                    if get in name:
                        count_b += 1
                        last_b = name
                        print(f"{name}: {value}€ (B)")
                print("Incomes------------")
                count_i = 0
                last_i = ""
                for i in calc.incomes:
                    name, value, often = i.split(";")
                    if get in name:
                        count_i += 1
                        last_i = name
                        print(f"{name}: {value} ({often}) (I)")
                print("Expenditures-------")
                count_e = 0
                last_e = ""
                for i in calc.expenditures:
                    name, value, often = i.split(";")
                    if get in name:
                        count_e += 1
                        last_e = name
                        print(f"{name}: {value} ({often}) (E)")
                print("Savings Goals-------")
                count_sg = 0
                last_sg = ""
                for i in calc.savings_goals:
                    name, value = i.split(";")
                    if get in name:
                        count_sg += 1
                        last_sg = name
                        print(f"{name}: {value} (SG)")

            action = ""
            selected_par = ""
            selected_par_list = ""

            if count_b == 1:
                print(f"Do you want to select '{last_b}'?")
                action = input("3 for y or enter for no]")
                if action == "3":
                    selected_par = last_b
                    selected_par_list = "b"
                    found = True
            elif count_i == 1:
                print(f"Do you want to select '{last_i}'?")
                action = input("3 for y or enter for no]")
                if action == "3":
                    selected_par = last_i
                    selected_par_list = "i"
                    found = True
            elif count_e == 1:
                print(f"Do you want to select '{last_e}'?")
                action = input("3 for y or enter for no]")
                if action == "3":
                    selected_par = last_e
                    selected_par_list = "e"
                    found = True
            elif count_sg == 1:
                print(f"Do you want to select '{last_sg}'?")
                action = input("3 for y or enter for no]")
                if action == "3":
                    selected_par = last_sg
                    selected_par_list = "sg"
                    found = True

            if action == "":
                get = input("Enter name or keyword or press enter to see the entire list]")

        clear()
        if selected_par_list == "b":
            name_sel = ""
            value_sel = ""
            for i in calc.balances:
                name, value = i.split(";")
                if name == selected_par:
                    name_sel = name
                    value_sel = value
                    break

            calc.delete_balance(name_sel, value_sel)

        if selected_par_list == "i":
            name_sel = ""
            value_sel = ""
            often_sel = ""
            for i in calc.incomes:
                name, value, often = i.split(";")
                if name == selected_par:
                    name_sel = name
                    value_sel = value
                    often_sel = often
                    break

            calc.delete_income(name_sel, value_sel, often_sel)

        if selected_par_list == "e":
            name_sel = ""
            value_sel = ""
            often_sel = ""
            for i in calc.expenditures:
                name, value, often = i.split(";")
                if name == selected_par:
                    name_sel = name
                    value_sel = value
                    often_sel = often
                    break
            calc.delete_expenditures(name_sel, value_sel, often_sel)

        if selected_par_list == "sg":
            name_sel = ""
            value_sel = ""
            for i in calc.savings_goals:
                name, value = i.split(";")
                if name == selected_par:
                    name_sel = name
                    value_sel = value
                    break

            calc.delete_savings_goal(name_sel, value_sel)














