#  This is the game which i designed and i used to play in school and college days with my friends group


import tkinter
import numpy as np
import random





class Auctioneer:
    def __init__(self, rounds, init_cash, players):
        self.rounds = rounds  #  total rounds to gen
        self.init_cash = init_cash  #  total cash at begining
        self.players = players  #  total players
        self.player_id = 0
        self.accounts = {}


    def make_account(self, name):
        """

        :param name: name of the player
        :return: makes an account with "id", "name", "cash":total cash left*, "company":total company owned *
        """
        if self.player_id <= self.rounds:
            account_info = {
                "id":self.player_id,
                "name":name,
                "cash":self.init_cash,
                "company":0,
            }
            self.accounts[self.player_id] = account_info
            self.player_id += 1
        else:
            print(f"max player limit reached {self.players}")


    def generate_normalised(self, company_ratio=0.7):  #  company_ratio, is basically how much company to be given
        #  70 % companies and 30 % stocks by default
        #  but the company and stock provided must be normalised based on number of rounds and init cash
        def generate_normal_company():
            MULTIPLIER = [0.7, 0.5, *[1]*2 , 2, 1.5]  #  this will reduce random structure, and also create normalisation, what this does - it makes the company x times the base value
            base_value = (1/10) * self.rounds  #  this was the base value we use to start the game in the college, refined through years and came up with this
            normalised_company = random.Random().choice(MULTIPLIER) * base_value
            return round(normalised_company, 3)

        def generate_normal_stock():
            MULTIPLIER = [*[1]*2, 1.3, 1.5]  # same logic
            base_value = (1 / 3) * self.rounds  # based on auctioneer experience, as we used to give 5 bil stock as of 15 rounds
            normalised_stock = random.Random().choice(MULTIPLIER) * base_value
            return round(normalised_stock,3)

        asset_list = []
        company_freq = int(company_ratio*self.rounds)  #  how many number of companies as per total number of rounds
        stock_freq = self.rounds - company_freq  #  how many number of stocks as per total number of rounds
        print(f"the number of companies: {company_freq}")
        print(f"the number of stocks: {stock_freq}")

        for company in range(company_freq):
            asset_list.append({"type":"company", "earn":generate_normal_company()})
        for stock in range(stock_freq):
            asset_list.append({"type":"stock", "earn":generate_normal_stock()})



        asset_list_random_ = random.Random().choices(asset_list, k=self.rounds)  #  it gives randomised stuff from the asset list
        return asset_list_random_





a = Auctioneer(rounds=5, init_cash=10, players=5)
a.make_account(name="raakin")
a.make_account(name="khan")
a.make_account(name="cha")
a.make_account(name="chi")
a.make_account(name="gota")

# a.generate_normalised()



class GUI:
    def __init__(self, accounts):
        self.accounts = accounts
        self.main_window = tkinter.Tk()
        self.main_window.title("Dominator")
        self.main_window.state("zoomed")  #  learning:  it starts the windows with full screen
        self.main_window.columnconfigure(0, weight=1)  #  learning: this tells the inner widgets that your allowed to grow or shrink
        self.main_window.rowconfigure(0, weight=1)  # same
        self.container = tkinter.Frame(self.main_window)
        self.container.pack(fill="both", expand=True, pady=10, padx=10)
        self.generate_frames()
        tkinter.mainloop()






    def generate_frames(self):
        def container_equaliser():  # basically configs each columns to share same space b/w
            for cont in range(len(self.accounts)):
                self.container.columnconfigure(cont, weight=1,
                                               uniform="col")  # make each container equally spaced through columns
            self.container.rowconfigure(0, weight=1)  # we could change this in future


        container_equaliser()
        for player in self.accounts:
            print(player)
            id_ = self.accounts[player]["id"]
            name = self.accounts[player]["name"]
            player_frame = tkinter.LabelFrame(text=name, master=self.container, width=int(1920 / len(self.accounts)))
            player_frame.grid(row=0, column=id_, sticky="nsew", padx=5, pady=5)  # sticky=nsew is the key, it tells its hammered to 4 corners of the label, so it streaches to fill it up
            tkinter.Label(master=player_frame, text=name).pack()



print(a.accounts)
GUI(accounts=a.accounts)




