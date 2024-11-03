import regex as re
class Staging:
    def __init__(self, cmd: str):
        if cmd == "main":
            pass
    def opening(self):
        pass
    
    def register(self):
        #get username
        
        #get password
        if self.check_pswd(input) == False:
            self.check_pswd(input)
    
    def check_pswd(self, input:str):
        # Check for at least one uppercase letter
        has_uppercase = re.search(r'[A-Z]', input) is not None
        # Check for at least one digit
        has_digit = re.search(r'[0-9]', input) is not None
        # Check for at least one symbol (non-alphanumeric)
        has_symbol = re.search(r'[^\w]', input) is not None
        
        return has_uppercase and has_digit and has_symbol
    
    def check_username(self, input:str):
        