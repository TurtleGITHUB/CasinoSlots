"""
Program: casinoslotGUI.py
Author: Robert 4/27/2021
"""

from breezypythongui import EasyFrame
import math
import random

class CasinoSlot(EasyFrame):
	def __init__(self):
		EasyFrame.__init__(self, title = "Slot Machine", width = 400, height = 300)
		self.addLabel(text = "Slot Machine", row = 0, column = 0, background = "lightgreen")
		self.field1 = self.addIntegerField(value = 0, row = 1, column = 1)
		self.field2 = self.addIntegerField(value = 0, row = 1, column = 2)
		self.field3 = self.addIntegerField(value = 0, row = 1, column = 3)

		self.button1 = self.addButton(text = "Spin!", row = 4, column = 2, command = self.spinNum)

		self.button2 = self.addButton(text = "Play again?", row = 4, column = 4, command = self.resetGame)

		self.resultArea = self.addLabel(text = "Total Tally", row = 2, column = 2, background = "lightblue")

		self.scoreField = self.addIntegerField(value = 50, row = 3, column = 2)

	def spinNum(self):
		"""Spin the numbers"""
		
		
		num1 = random.randint(1, 9)
		num2 = random.randint(1, 9)
		num3 = random.randint(1, 9)
		result = ""
		points = self.scoreField.getNumber()

		if num1 == num2 and num2 == num3:
			result = "JackPot!!"
			points += 30
		elif num1 == num2 or num2 == num3 or num1 == num3:
			result = "Two of a Kind!"
			points += 10
		else:
			result = "No Combination"
			points -= 10
		
		self.field1.setNumber(num1)
		self.field2.setNumber(num2)
		self.field3.setNumber(num3)
		self.resultArea["text"] = result
		self.scoreField.setNumber(points)

		if points == 0:
			result = "GAME OVER"
			self.button1["state"] = "disabled"
		

		
		
		

		

		
	
		 




	def resetGame(self):
		"""Reset the game"""






def main():
	CasinoSlot().mainloop()
main()