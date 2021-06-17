import tkinter as tk

class MainMenu(tk.Frame):
	
	def __init__(self, parent, Game):
		
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="PaleGreen1")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)


		#CREATE MAIN FRAME
		self.main_frame = tk.Frame(self, width=self.config.side, height=self.config.side, bg="PaleGreen1")
		self.main_frame.pack(expand=True)

		self.btn_play = tk.Button(self.main_frame, text="Play", font=("GOUDY STOUT", 18,), bg="thistle1", command=lambda:self.game.create_board())
		self.btn_play.pack(padx=10, side="left" , anchor="sw")

		self.btn_info = tk.Button(self.main_frame, text="Info", font=("GOUDY STOUT", 18), bg="thistle1", command=lambda:self.game.change_page('infoPage'))
		self.btn_info.pack(padx=10, side="left", anchor="s")

		self.btn_exit = tk.Button(self.main_frame, text="Exit", font=("GOUDY STOUT", 18), bg="thistle1", command=lambda:self.game.exit())
		self.btn_exit.pack(padx=10, side="left", anchor="se")