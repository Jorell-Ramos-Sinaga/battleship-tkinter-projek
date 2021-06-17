import tkinter as tk
import sys

from config import Config
from ship import Ship
from player import Player
from board import Board
from main_menu import MainMenu
from info import InfoPage

class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game
		self.config = Game.config

		super().__init__()
		self.title(self.config.app_title)
		self.geometry(self.config.screen)
		self.create_container()
		self.pages = {}
		self.create_board()
		self.create_infoPage()
		self.create_mainMenu()
		#self.create_loginPage()


	def create_container(self):
		self.container = tk.Frame(self, bg="white")
		self.container.pack(fill="both", expand=True)

	def create_board(self):
		self.pages["board"] = Board(self.container, self.game)
		self.game.generate_answer()

	def create_mainMenu(self):
		self.pages['mainMenu'] = MainMenu(self.container, self)

	def create_infoPage(self):
		self.pages['infoPage'] = InfoPage(self.container, self)


	def change_page(self, page):
		page = self.pages[page]
		page.tkraise()

	def exit(self):
		sys.exit()


class Battleship:

	def __init__(self):
		self.config = Config()
		self.ship = Ship(self)
		self.player = Player()
		self.window = Window(self)

	def check_answer(self):
		ship = self.ship.location
		player = self.player.location
		if ship == player:
			return True
		return False

	def button_clicked(self, pos_x, pos_y):
		#print(pos_x, pos_y)
		self.player.current_location(pos_x, pos_y)
		win = self.check_answer()
		self.window.pages['board'].change_img_button(pos_x, pos_y, win)
		if win:
			print("You Win!!!")
			self.window.change_page('mainMenu')

	def run(self):
		self.window.mainloop()

	def generate_answer(self):
		self.ship.setup_location()


if __name__ == '__main__':
	my_battleship = Battleship()
	my_battleship.run()