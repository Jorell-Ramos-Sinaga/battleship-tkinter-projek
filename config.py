import json

class Config:

	def __init__(self):

		self.app_title = "Battleship"

		#GAME CONFIG
		self.row = 5
		self.column = 5

		#WINDOW CONFIG
		base = 160
		ratio = 5
		self.side = base*ratio
		self.screen = f"{self.side}x{self.side}+500+500"


		#IMG BUTTON PATH
		self.init_img_btn = "img/init_img.jpg"
		self.final_img_btn = "img/final_img.png"
		self.win_img_btn = "img/win_img.jpg"

		#LOGO PATH
		self.logo_path = "img/logo.jfif"

		#DATA CONFIG
		self.users_path = "json/users.json"
		self.leaderboard_path = "json/leaderboard.json"

	def load_userData(self, users_path):
		with open(users_path, "r") as json_data:
			userData = json.load(json_data)
		return userData

	def load_gameData(self):
		with open(leaderboard_path, "r") as json_data:
			gameData = json.load(json_data)
		return gameData

	def save_gameData(self):
		pass

	def login(self, username, password):
		users = self.load_userData(self.users_path)
		if username in users:
			if password == users[username]["password"]:
				return True
			else:
				return False
		else:
			return False

