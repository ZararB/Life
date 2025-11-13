from animal import Animal


def compress(data):
    """Compress data into knowledge - abstraction as compression"""
    # Knowledge is compressed experience
    return {'compressed': data}


class KnowledgeGraph:
    """Represents the network of knowledge and understanding"""
    
    def __init__(self):
        self.knowledge = {}
    
    def update(self, knowledge):
        """Update the knowledge graph with new compressed knowledge"""
        self.knowledge.update(knowledge)
    
    def evaluate(self, state):
        """Evaluate state and return an action based on accumulated knowledge"""
        # Action emerges from the knowledge graph
        return self.knowledge.get('compressed', state)


class Human(Animal):
    """Pseudocode of the class that I am an instance of"""
    
    def __init__(self, dna, history=None):
        self.dna = dna
        self.history = history or []
        self.knowledgeGraph = KnowledgeGraph()
    
    def observe(self, state):
        """Observe state - observation is continuous, never complete"""
        # Philosophically: observation never truly ends
        # In practice: we can observe and return, but observation continues
        observed_state = state
        # The act of observation changes both observer and observed
        return observed_state
    
    def learn(self, data):
        """Learn from data - compress experience into knowledge"""
        knowledge = compress(data)
        self.knowledgeGraph.update(knowledge)
        self.history.append(data)
    
    def act(self, state):
        """Act based on state - action emerges from knowledge graph"""
        action = self.knowledgeGraph.evaluate(state)
        return action
