class calculator:
    def __init__(self):
        self.n_value = 0
        self.incomes = []
        self.income_p = 0
        self.income_d = 0
        self.income_w = 0
        self.income_m = 0
        self.income_y = 0
        self.expenditure_p = 0
        self.expenditure_d = 0
        self.expenditure_w = 0
        self.expenditure_m = 0
        self.expenditure_y = 0
        self.balance_p = 0
        self.balance_d = 0
        self.balance_w = 0
        self.balance_m = 0
        self.balance_y = 0
        self.balance_value = 0
        self.balances = []
        self.expenditures = []
        self.predictions = []
        self.savings_goals = []
        self.savings_goal_value = 0

    def add_balance(self, value, title):
        self.balances.append(f"{title};{value}")
        self.balance_value += value
        calculator.refresh_predicts(self)

    def change_balance(self, new_data, name_o, value_o):
        count = 0
        for i in self.balances:
            name, value = i.split(";")
            if name == name_o:
                if value == value_o:
                    del self.balances[count]
                    self.balances.append(new_data)
            count += 1
        calculator.refresh_balance(self)

    def refresh_balance(self):
        self.balance_value = 0
        for i in self.balances:
            name, value = i.split(";")
            self.balance_value += int(value)

    def delete_balance(self, name_o, value_o):
        count = 0
        for i in self.balances:
            name, value = i.split(";")
            if name == name_o:
                if value == value_o:
                    del self.balances[count]
            count += 1
        calculator.refresh_balance(self)



    def predict_balance(self, time, often):
        if time == "d":
            self.prediction = round(((self.balance_value + self.income_d) - self.expenditure_d) * int(often), 2)
        elif time == "w":
            self.prediction = round(((self.balance_value + self.income_w) - self.expenditure_w) * int(often), 2)
        elif time == "m":
            self.prediction = round(((self.balance_value + self.income_m) - self.expenditure_m) * int(often), 2)
        elif time == "y":
            self.prediction = round(((self.balance_value + self.income_y) - self.expenditure_y) * int(often), 2)

        self.predictions.append(f"{time};{often};{self.prediction}")
        return self.prediction

    def refresh_predicts(self):
        print(self.predictions)
        new_predictions = []
        for i in self.predictions:
            time, often, prediction = i.split(";")
            if time == "d":
                self.prediction = round(((self.balance_value + self.income_d) - self.expenditure_d) * int(often), 2)
            elif time == "w":
                self.prediction = round(((self.balance_value + self.income_w) - self.expenditure_w) * int(often), 2)
            elif time == "m":
                self.prediction = round(((self.balance_value + self.income_m) - self.expenditure_m) * int(often), 2)
            elif time == "y":
                self.prediction = round(((self.balance_value + self.income_y) - self.expenditure_y) * int(often), 2)

            new_predictions.append(f"{time};{often};{self.prediction}")

        self.predictions.clear()
        for i in new_predictions:
            time, often, prediction = i.split(";")
            self.predictions.append(f"{time};{often};{prediction}")



        print(self.predictions)

    def add_income(self, value, title, often):
        self.incomes.append(f"{title};{value};{often}")
        if often == "w":
            self.n_value = value/7
        elif often == "d":
            self.n_value = value
        elif often == "m":
            self.n_value = value/30
        elif often == "y":
            self.n_value = value/360

        self.income_d += self.n_value
        self.income_p = self.n_value * 7
        self.income_w += self.income_p
        self.income_p = self.n_value * 30
        self.income_m += self.income_p
        self.income_p = self.n_value * 360
        self.income_y += self.income_p
        calculator.refresh_predicts(self)

    def change_income(self, new_data, name_o, value_o, often_o):
        count = 0
        for i in self.incomes:
            name, value, often = i.split(";")
            if name == name_o:
                if value == value_o:
                    if often == often_o:
                        del self.incomes[count]
                        self.incomes.append(new_data)
            count += 1
        calculator.refresh_income(self)

    def delete_income(self, name_o, value_o, often_o):
        count = 0
        for i in self.incomes:
            name, value, often = i.split(";")
            if name == name_o:
                if value == value_o:
                    if often == often_o:
                        del self.incomes[count]
            count += 1
        calculator.refresh_income(self)

    def refresh_income(self):
        self.income_p = 0
        self.income_d = 0
        self.income_w = 0
        self.income_m = 0
        self.income_y = 0
        for i in self.incomes:
            name, value, often = i.split(";")
            if often == "w":
                self.n_value = int(value)/7
            elif often == "d":
                self.n_value = int(value)
            elif often == "m":
                self.n_value = int(value)/30
            elif often == "y":
                self.n_value = int(value)/360

            self.income_d += self.n_value
            self.income_p = self.n_value * 7
            self.income_w += self.income_p
            self.income_p = self.n_value * 30
            self.income_m += self.income_p
            self.income_p = self.n_value * 360
            self.income_y += self.income_p
        calculator.refresh_predicts(self)

    def add_expenditures(self, value, title, often):
        self.expenditures.append(f"{title};{value};{often}")
        if often == "w":
            self.n_value = value/7
        elif often == "m":
            self.n_value = value/30
        elif often == "d":
            self.n_value = value
        elif often == "y":
            self.n_value = value/360

        self.expenditure_d += self.n_value
        self.expenditure_p = self.n_value * 7
        self.expenditure_w += self.expenditure_p
        self.expenditure_p = self.n_value * 30
        self.expenditure_m += self.expenditure_p
        self.expenditure_p = self.n_value * 360
        self.expenditure_y += self.expenditure_p
        calculator.refresh_predicts(self)

    def change_expenditures(self, new_data, name_o, value_o, often_o):
        count = 0
        for i in self.expenditures:
            name, value, often = i.split(";")
            if name == name_o:
                if value == value_o:
                    if often == often_o:
                        del self.expenditures[count]
                        self.expenditures.append(new_data)
            count += 1
        calculator.refresh_expenditures(self)

    def delete_expenditures(self, name_o, value_o, often_o):
        count = 0
        for i in self.expenditures:
            name, value, often = i.split(";")
            if name == name_o:
                if value == value_o:
                    if often == often_o:
                        del self.expenditures[count]
            count += 1
        calculator.refresh_expenditures(self)

    def refresh_expenditures(self):
        self.expenditure_p = 0
        self.expenditure_d = 0
        self.expenditure_w = 0
        self.expenditure_m = 0
        self.expenditure_y = 0
        for i in self.expenditures:
            name, value, often = i.split(";")
            if often == "w":
                self.n_value = int(value)/7
            elif often == "m":
                self.n_value =  int(value)/30
            elif often == "d":
                self.n_value =  int(value)
            elif often == "y":
                self.n_value =  int(value)/360

            self.expenditure_d += self.n_value
            self.expenditure_p = self.n_value * 7
            self.expenditure_w += self.expenditure_p
            self.expenditure_p = self.n_value * 30
            self.expenditure_m += self.expenditure_p
            self.expenditure_p = self.n_value * 360
            self.expenditure_y += self.expenditure_p
            calculator.refresh_predicts(self)

    def add_savings_goal(self, value, title):
        self.savings_goals.append(f"{title};{value}")
        self.savings_goal_value += value

    def refresh_savings_goals(self):
        self.savings_goal_value = 0
        for i in self.savings_goals:
            name, value = i.split(";")
            self.savings_goal_value += int(value)

    def delete_savings_goal(self, name_o, value_o):
        count = 0
        for i in self.savings_goals:
            name, value = i.split(";")
            if name == name_o:
                if value == value_o:
                    del self.savings_goals[count]
            count += 1
        calculator.refresh_savings_goals(self)

    def change_savings_goals(self, new_data, name_o, value_o):
        count = 0
        for i in self.savings_goals:
            name, value = i.split(";")
            if name == name_o:
                if value == value_o:
                    del self.savings_goals[count]
                    self.savings_goals.append(new_data)
            count += 1
        calculator.refresh_savings_goals(self)
