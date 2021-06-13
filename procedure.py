def P():
	A +=1
	B +=1

def Q():
	def procedureR():
		A = 16
		P()
		print(A,B)

B = 11
procedureR()

