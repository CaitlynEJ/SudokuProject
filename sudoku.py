class Sudoku():
	"""A class to hold the Sudoku Gamea and it's methods."""
	def __init__(self):
		"""A method that initiates the board with a hardcoded puzzle. It also sets the status as 'Unfinished' """
		self.board = [
			["*", 8, 4, "*", 5, "9", 2, "*", "*"], 				#row 1
			[6, "*", "*", 1, "*", 3, 7, "*", 8],				#row 2
			["*", "*", "*", 7, "*", "*", 4, "*", "*"],			#row 3
			[1, "*", 2, "*", "*", "*", 3, "*", "*"],			#row 4
			["*", "*", "*", "*", "*", "*", "*", "*", "*"],		#row 5
			["*", "*", 7, "*", "*", "*", 6, "*", 5],			#row 6
			["*", "*", 1, "*", "*", 6, "*", "*", "*"],			#row 7
			[4, "*", 6, 9, "*", 5, "*", "*", 1],				#row 8
			["*", "*", 9, "*", 8, "*", 5, 6, "*"]]				#row 9
		self.status = "Unfinished"
		
	
	def getBoard(self):
		"""Returns the game board."""
		return self.board
		
	def getStatus(self):
		"""Returns the status of the game."""
		return self.status
		
	def setStatus(self, value):
		"""Sets the game status."""
		self.status = value
		
	def giveRules(self):
		""" Prints the rules of Sudoku."""
		rules1 = "Every row, every column, and every 3x3 section must contain the numbers 1 to 9, with no duplications."
		rules1a = "A '*' represents a blank space that needs to be filled in."
		rules2 = "Once you have filled out the entire grid, the program will check your attempt with it’s encoded algorithm,"
		rules3 = "checkSolution(), to see if that solution is valid."
		print(rules1)
		print(rules1a)
		print(rules2)
		print(rules3)
			
					
	def uniqueRow(self, row):
		"""
		A method to make sure that a list of given numbers (or a row) is unique and no numbers are repeated.
		"""
		copy = 0
	 
		for i in range(len(row)): 
			for x in range(len(row)): 
				if i != x: 
					if row[i] == row[x]: 
						copy = 1
	
		if(not copy):
			return True
		else:  
			return False
			
			
	def checkRows(self, list):
		"""A method that checks if rows are unique by calling uniqueRow method"""
		for x in list:
			result = self.uniqueRow(x)
			if result == True:
				solution = True
				continue
			else:
				solution = False
				break
				
		return solution
			
	def checkColumns(self, list):
		""" a method that checks if the Columns are unique by calling the checkRows method"""
		return self.checkRows(list)
		
		
	def gatherColumns(self, board):
		""" a method that creates "columns" as "rows" and returns a new list"""
		columnsList=[[], [], [], [], [], [], [], [], []]
		start = 0
		while start < 9:
			for x in board:
				columnsList[start].append(x[start])
			start += 1
			
		return columnsList
		
			
	def gatherSections(self, board):
		""" a method that creates a 3x3 sections as a 'row' and returns a new list of sections """
		#newList for sections
		sectionList = [[], [], [], [], [], [], [], [], []]
		
		#rowCounter
		rowCounter = 3
		currentRow = 0
		
		#columnCounter
		columnCounter = 3
		currentColumn = 0
		
		section = 0
		
		#while # of sections is less than 9
		while section < 9:
			#count 3 rows at a time and make sure it's not our of range
			while currentRow < rowCounter and currentRow !=9:
				#get section
				if columnCounter == 12:
					break
				else:
					sectionList[section] = self.getOneSection(board, rowCounter, columnCounter)
					#increase section number
					section += 1
					#move to next 3 columns
					columnCounter += 3
			#drop out of while loop and get next 3 rows
			currentRow += 3
			rowCounter += 3
			# start from column 0 and set the Max column to 3
			columnCounter = 3
			
		return sectionList
		
	def checkSections(self, board):
		""" checks if each section (one row) is has unique numbers"""
		return self.checkRows(board)
		
				
	def getOneSection(self, board, rowMax, columnMax):
		"""a method that returns one 3x3 section of a board"""
		section = []
		
		
		for x in range(rowMax-3, rowMax):
			for y in range(columnMax-3, columnMax):
				section.append(board[x][y])
				
		return section	
		
	def checkSolution(self):
		"""
		This is the algorithm to solve the decision problem of a sudoku problem: if a players solution is correct.
		a method that creates if an inputted solution on a board is correct by calling 3 checking methods:
		checkRows, checkColumns, checkSections. If all three return true, then the solution is correct. Otherwise, it returns false. 
		"""
		board = self.getBoard()
		
		columnList = self.gatherColumns(board)
		sectionList = self.gatherSections(board)
		
		solution = self.checkRows(board) and self.checkColumns(columnList) and self.checkSections(sectionList)
		
		if solution == True:
			print("Your solution is correct! Congratulations!")
		else:
			print("Your solution is incorrect. Please try again.")
			
			
			
	def printBoard(self):
		"""Prints the sudoku board"""
		list = self.getBoard()

		currentRow = 0

		print("    A  B  C     D  E  F     G  H  I")
		print()
		
		#for each section:
		for section in range (0, 3):

			#for each row
			for k in range(currentRow, currentRow+3):
				currentColumn = 0
				
				print(k, " ", end=" ")
				
				#for each section row
				for x in range (0, 3):
				
					#colum count 3
					for y in range(currentColumn, currentColumn+3):
						value = list[k][y]
						print(value, end = " ")
						print("", end =" ")
						
					# print a |
					if x != 2:
						print("| ", end =" ")
					else:
						print("")
					
					currentColumn += 3
						
			currentRow += 3
				
			if section != 2:
				print("    _______________________________")
				print("")
		print("")
	
				
	def convertCol(self, column):
		"""Coverts a Alpha character into the matching column number. """
		colList = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]	

		for x in range(len(colList)): 
			if column == colList[x]:
				return x

			# if column value is invalid
			elif column not in colList:
				
				return None
					
				
	def insert(self, column, row, value):
		"""A method to insert a value into a square."""
		board = self.getBoard()
		
		column = self.convertCol(column)
		if column == None:
			print("That is not a valid Column input. Please try again.")
			return

		# an attempt to catch if input is invalid.
		if value < 0 or value > 10:
			print("That is not a valid number input. Please try again")

		# inserts value into the 9X9 matrix.
		self.board[row][column] = value
		

		self.checkBoard()
		self.checkStatus()
		self.printBoard()
		
		
	def checkBoard(self):
		"""A method that checks is the board is filled in or not."""
		board = self.getBoard()
		boxesFilled = 0
		
		
		for x in board:
			for y in x:
				if y == "*":		# if the value is equal to a blank square.
					break
					
				else:
					boxesFilled += 1
					
		if boxesFilled == 81:
			self.setStatus("Finished")
		
		
	def checkStatus(self):
		"""A method to check if the game is finished or not."""
		status = self.getStatus()
		
		if status == "Unfinished":
			pass
			
		else:
			self.checkSolution()
			
	def start(self):
		"""A method to be called by 'main()' to start the game."""
		# Welcome player and give rules
		print("Welcome to Sudoku!")
		self.giveRules()
		ready = input("Type 'yes' when you are ready. ")

		#start game
		if ready.lower() == 'yes':
			status = self.getStatus()
			self.printBoard()

			# a loop to continue to prompt for a value.
			while status == "Unfinished":
				print("Please type the column, row, and number you wish to insert.")
				columnVal = input("Column: ")
				columnVal = columnVal.upper()
				rowVal = int(input("Row: "))
				value = int(input("Number: "))


				else:
					#input value:
					self.insert(columnVal, rowVal, value)

		
def main():
	"""A main function to be used if the file is run as a script."""
	game = Sudoku()
	game.start()		
			
if __name__ == '__main__':
	main()