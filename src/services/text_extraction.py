from langchain_community.llms import Ollama

class Understanding:
    llm = Ollama(model="llama2")
    """
    list of function:
    Understanding query and reply it based on several states
    Extracting info and send it to db
    """
        
    def req_extract(self, text):
        pass
    
    def main_extract(self, text):
        pass
    
    def instruc_extract(self, text):
        pass