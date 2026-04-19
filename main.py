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
            base_value = (1/10) * self.rounds  #  this was the base value we use to start the game in the college


        normalised = np.random.normal(loc=5,  scale=1, size=self.rounds)

        print(normalised)



a = Auctioneer(rounds=5, init_cash=10, players=5)
a.make_account(name="raakin")
a.make_account(name="khan")
a.make_account(name="cha")
a.make_account(name="chi")
a.make_account(name="gota")

a.generate_normalised()




class GUI:
    def __init__(self, accounts):
        self.accounts = accounts
        self.main_window = tkinter.Tk()
        self.main_window.title("Dominator")
        self.MAIN_FRAME = tkinter.Frame(self.main_window)
        self.MAIN_FRAME.pack()
        self.generate_frames()
        tkinter.mainloop()

    def generate_frames(self):
        for player in self.accounts:
            print(player)
            id_ = self.accounts[player]["id"]
            name = self.accounts[player]["name"]
            player_frame = tkinter.LabelFrame(text=name, master=self.MAIN_FRAME, width=int(1920/len(self.accounts)))
            player_frame.grid(row=0, column=id_)
            tkinter.Label(master=player_frame, text=name).pack()



print(a.accounts)
GUI(accounts=a.accounts)




