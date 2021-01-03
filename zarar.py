import Human from human


class Zarar(Human):

	def __init__(self, dna, history=None):

		self.dna = dna 
		self.history = history or []

	def act(self, state):

		action = self.model.predict(state)
		
		return action

	def observe(self, state):
	
		while True:
			pass

		return None
	
	def solve(self, problem):
	
		return solution
	
	def update(self, data):
		
		self.model.update(data)

	def learn(self, data):

		knowledge = compress(data)
		self.knowledgeGraph.update(knowledge)

		
