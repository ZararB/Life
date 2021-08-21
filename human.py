import Animal 

class Human(Animal):

	def __init__(self, dna, history=None):

		self.dna = dna 
                self.history = history or [] 

	def observe(self, state):
	
		while True:
			pass

		return None
	
	def learn(self, data):

		knowledge = compress(data)
		self.knowledgeGraph.update(knowledge)

        def act(self, state):

                action = self.knowledgeGraph.evaluate(state) 

                return action 
