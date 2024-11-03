
class Response:
    def __init__(self):
        pass           
    def firstime(self, state):
        msg = """
        👋 Welcome to Trackio!
        
        I'm your friendly expense tracker, here to help you manage your finances with ease. Whether you want to log a new expense, check your spending trends, or set budget alerts, I’ve got you covered.

        To get started, simply tell me what you'd like to do! Please provide some information:
            -What's your budget ?
            -How much money you want to save ?
            -What's your budget peer day ?

        Let’s take control of your expenses together! 💰
        """
        if state == 0:
            return msg
    
    def main_opener(self, state):
        query= "How much you just spend and what is the category?"
        if state == 1:
            return query
        
    def remaining_budget (self, state):
        pass
