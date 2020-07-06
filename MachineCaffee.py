class MC:
    def __init__(self):
        self.money = 550
        self.agua = 400
        self.leche = 540
        self.cafe = 120
        self.cups = 9

    def cafe(self, opcion):
        self.opcion = opcion
        while self.opcion != "exit":
            if self.opcion == "buy":
                self.buy()
            elif self.opcion == "fill":
                self.fill()
            elif self.opcion == "take":
                self.dinero()
            elif self.opcion == "remaining":
                self.remaining()
            self.opcion = input("Write action (buy, fill, take, remaining, exit):")

    def buy(self):
        tipo_cafe = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if tipo_cafe == "back":
            return
        else:
            tipo_cafe = int(tipo_cafe)
            if tipo_cafe == 1:
                self.money += 4
                self.agua -= 250
                self.cafe -= 16
                self.cups -= 1
                if self.agua >= 0 and self.cafe >= 0 and self.cups >= 0:
                    print("I have enough resources, making you a coffee!")
                else:
                    if self.agua < 0:
                        print("Sorry, not enough water!")
                    elif self.cafe < 0:
                        print("Sorry, not enough cafe!")
                    else:
                        print("Sorry, not enough cups!")
                    self.money -= 4
                    self.agua += 250
                    self.cafe += 16
                    self.cups += 1
            elif tipo_cafe == 2:
                self.money += 7
                self.agua -= 350
                self.leche -= 75
                self.cafe -= 20
                self.cups -= 1
                if self.agua >= 0 and self.cafe >= 0 and self.cups >= 0:
                    print("I have enough resources, making you a coffee!")
                else:
                    if self.agua < 0:
                        print("Sorry, not enough water!")
                    elif self.cafe < 0:
                        print("Sorry, not enough cafe!")
                    else:
                        print("Sorry, not enough cups!")
                    self.money -= 7
                    self.agua += 350
                    self.leche += 75
                    self.cafe += 20
                    self.cups += 1
            else:
                self.money += 6
                self.agua -= 200
                self.leche -= 100
                self.cafe -= 12
                self.cups -= 1
                if self.agua >= 0 and self.cafe >= 0 and self.cups >= 0:
                    print("I have enough resources, making you a coffee!")
                else:
                    if self.agua < 0:
                        print("Sorry, not enough water!")
                    elif self.cafe < 0:
                        print("Sorry, not enough cafe!")
                    else:
                        print("Sorry, not enough cups!")
                    self.money -= 6
                    self.agua += 200
                    self.self.leche += 100
                    self.cafe += 12
                    self.cups += 1

    def fill(self):
        self.agua += int(input("Write how many ml of water do you want to add:"))
        self.leche += int(input("Write how many ml of milk do you want to add:"))
        self.cafe += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    def dinero(self):
        print("I gave you", self.money)
        self.money *= 0

    def remaining(self):
        print("The coffee machine has:")
        print(self.agua, "of water")
        print(self.leche, "of milk")
        print(self.cafe, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")

    def __str__(self):
        return f"{self.cafe}, {self.leche}, {self.agua}, {self.cups}, {self.money}"

resultado = MC()
print(resultado.__str__())
resultado.cafe("buy")

