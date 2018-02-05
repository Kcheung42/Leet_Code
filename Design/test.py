
class Board:
	#initialize board
	def __init__(self, p1, p2):
		self.winner = None
		self.winPath = [
			int("000000111",2),
			int("000111000",2),
			int("111000000",2),
			int("001001001",2),
			int("010010010",2),
			int("100100100",2),
			int("100010100",2),
			int("001010001",2),
		]
		pass

	def display(self, p1, p2):
		cells = [' '] * 9
		if p1 is not None and p2 is not None:
			for i in range(9):
				cell = 2 ** i
				if p1.board & cell == cell:
					cells[i] = p1.symb
				elif p2.board & cell == cell:
					cells[i] = p2.symb
		print("{} | {} | {}".format(cells[6], cells[7], cells[8]))
		print("-----------")
		print("{} | {} | {}".format(cells[3], cells[4], cells[5]))
		print("-----------")
		print("{} | {} | {}".format(cells[0], cells[1], cells[2]))
		pass

	def isWinner(self, player):
		for w in self.winPath:
			self.winner = player if (player.board & w == w) else None
			if self.winner:
				print("we have a winner")
				return

	def play(self, p1, p2):
		self.display(p1,p2)
		player_now = p1
		player_wait = p2
		while self.winner is None:
			player_now.board = player_now.update(player_wait)
			self.isWinner(player_now)
			self.display(player_now, player_wait)
			if player_now.board + player_wait.board == 511:
				print('We have a tie')
				break
			player_now, player_wait = player_wait, player_now
		pass

class Player:
	def __init__(self, symb):
		super().__init__()
		self.symb = symb
		self.board = 0
	
	def update(self, otherPlayer):
		while(True):
			move = input("Please Choose a move [0-9]")
			try:
				move = int(move)
			except ValueError:
				print("Please choose the right format")
				continue 
			if 1 <= move <= 9:
				move = move -1
				cell = 2 ** move
				if otherPlayer.board & cell == cell or self.board & cell == cell:
					print("OOps already chosen")
				else:
					return (self.board | cell)
			else:
				print("Please choose the right range")

	
def main():
	p1 = Player('X')
	p2 = Player('O')
	b = Board(p1, p2)
	b.play(p1,p2)

if __name__ == "__main__":
	main()
