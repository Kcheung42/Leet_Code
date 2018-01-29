import os
os.system("clear")

class Board:
	def __init__(self):
		self.winner = None
		self.winPath = set([
			int('000000111',2),
			int('000111000',2),
			int('111000000',2),
			int('001001001',2),
			int('010010010',2),
			int('100100100',2),
			int('100010001',2),
			int('001010100',2),
		])

	def display(self, p1, p2):
		cells = [' '] * 9
		if p1 is not None and p2 is not None:
			for i in range(9):
				cell = 2 ** i
				if p1.board & cell == cell:
					cells[i] = p1.symb
				elif p2.board & cell == cell:
					cells[i] = p2.symb
		print("===Tic====")
		print("{} | {} | {}".format(cells[6], cells[7], cells[8]))
		print("----------")
		print("{} | {} | {}".format(cells[3], cells[4], cells[5]))
		print("----------")
		print("{} | {} | {}".format(cells[0], cells[1], cells[2]))
		print("===Next===")
		print("Layout: Use NumberPad")
	
	def isWinner(self, player):
		for s in self.winPath:
			self.winner = player if player.board & s == s else None
			if self.winner:
				print("We have a Winner!! Player {}".format(player.symb))
				return
	
	def play(self, p1, p2):
		self.display(p1, p2)
		player_now, player_wait = p1, p2
		while(self.winner is None):
			player_now.board = player_now.update(player_wait)
			self.display(player_now, player_wait)
			self.isWinner(player_now)
			if player_now.board | player_wait.board == 511:
				print("No one Wins: Tie!")
				return
			player_now, player_wait = player_wait, player_now

class HumanPlayer(Board):
	def __init__(self, char, board):
		super().__init__()
		self.board = 0
		self.symb = char

	def update(self, otherPlayer):
		while True:
			try:
				move = int(input("Player1 Please Choose Cell [1-9]:"))
			except ValueError:
				print("ERROR:Please choose correct Cell format")
				continue
			if 1 <= move <= 9: 
				move = move - 1
				cell = 2 ** move
				if otherPlayer.board & cell == cell or self.board & cell == cell:
					print("Oops! that cell is already filled. Please Choose Again")
				else:
					return (self.board | cell)
			else:
					print("ERROR:Please choose correct Cell format")

class AI(Board):
	def __init__(self, char, board):
		super().__init__()
		self.board = 0
		self.symb = char

	def isBlock(self, board):
		for s in self.winPath:
			if board & s == s:
				return True
		return False

	def update(self, otherPlayer):
		possible_moves = []
		board = self.board | otherPlayer.board
		board = ~board
		for i in range(0, 9):
			cell = 2 ** i
			if board & cell == cell:
				possible_moves.append(i + 1)
		print("hmmmm.....")
		print("possible moves:{}".format(possible_moves))

		for i,val in enumerate(possible_moves):
			cell = 2 ** (val-1)
			if self.isBlock(self.board | cell):
				return self.board | cell

		for i,val in enumerate(possible_moves):
			cell = 2 ** (val-1)
			if self.isBlock(otherPlayer.board | cell):
				return self.board | cell

		for i,val in enumerate(possible_moves):
			cell = 2 ** (val-1)
			return self.board | cell

def main():
	b = Board()
	human1 = HumanPlayer('X', b)
	human2 = HumanPlayer('O', b)
	comp = AI('@', b)
	while True:
		try:
			val = int(input("Choose Opponent: (1)Computer (2)Human:"))
		except ValueError:
			print("Please choose correct Opponent")
			continue
		if val == 1:
			b.play(human1, comp)
			break
		elif val == 2:
			b.play(human1, human2)
			break
		else:
			print("Please choose correct Opponent")

if __name__ == "__main__":
	main()
