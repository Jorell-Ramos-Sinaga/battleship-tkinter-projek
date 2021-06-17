import tkinter as tk

class InfoPage(tk.Frame):
	
	def __init__(self, parent, Game):
		
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="orchid")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		#CREATE MAIN FRAME
		self.main_frame = tk.Frame(self, width=self.config.side, height=self.config.side, bg="orchid")
		self.main_frame.pack(expand=True)

		self.frame_howToPlay = tk.Frame(self.main_frame, width=self.config.side, height=3*self.config.side//8, bg="orchid")
		self.frame_howToPlay.pack(side="top", fill="x")

		self.label_howToPlay = tk.Label(self.frame_howToPlay, text="How to Play", font=("Blackadder ITC", 30, "bold"), bg="LightSteelBlue4", fg="gold")
		self.label_howToPlay.pack(side="top", anchor="nw", pady=5)

		self.scroll_howToPlay = tk.Scrollbar(self.frame_howToPlay)
		self.scroll_howToPlay.pack(side="right", fill="y")

		self.text_howToPlay = tk.Text(self.frame_howToPlay, width=100, height=12, font=("Comic Sans MS", 14))
		self.howToPlay = """-This game is a single player game  \n-The board consists of 5x5 squares \n-Your goal is to find the one correct random square and win the game"""
		self.text_howToPlay.insert(tk.END, self.howToPlay)
		self.text_howToPlay.pack(pady=5)

		self.text_howToPlay.configure(yscrollcommand=self.scroll_howToPlay.set)
		self.scroll_howToPlay.configure(command=self.text_howToPlay.yview)

		self.frame_aboutGame = tk.Frame(self.main_frame, width=self.config.side, height=3*self.config.side//8, bg="orchid")
		self.frame_aboutGame.pack(side="top", fill="x")

		self.label_aboutGame = tk.Label(self.frame_aboutGame, text="About Game", font=("Blackadder ITC", 30, "bold"), bg="LightSteelBlue4", fg="gold")
		self.label_aboutGame.pack(side="top", anchor="nw", pady=5)

		self.scroll_aboutGame = tk.Scrollbar(self.frame_aboutGame)
		self.scroll_aboutGame.pack(side="right", fill="y")

		self.text_aboutGame = tk.Text(self.frame_aboutGame, width=100, height=12, font=("Comic Sans MSmai", 14))
		self.aboutGame = """Battleship is the classic naval combat game that brings together competition, strategy, and excitement. In head-to-head battle, you search for the enemy's fleet of ships and destroy them one by one. No ship is safe in this game of stealth and suspense. Try to protect your own fleet while you annihilate your opponent's. It's a battle that you must win!

You sank my battleship!

Feel the authentic thrill of the battle when you wage war on the high seas in the game of Battleship. Take charge and command your own fleet to defeat the enemy. With convenient portable battle cases and realistic naval crafts, Battleship puts you right in the middle of the action. It's a full-out assault. Position your ships strategically to survive the relentless strikes. Then target your opponent's ships and wipe them out. You know you can do it!"""

		self.text_aboutGame.insert(tk.END, self.aboutGame)
		self.text_aboutGame.pack(pady=5)

		self.text_aboutGame.configure(yscrollcommand=self.scroll_aboutGame.set)
		self.scroll_aboutGame.configure(command=self.text_aboutGame.yview)

		self.btn_mainMenu = tk.Button(self.main_frame, text="Main Menu", font=("Arial", 18, "bold"), command=lambda:self.game.change_page('mainMenu'))
		self.btn_mainMenu.pack(side="bottom", pady=5)