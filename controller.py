class ExpenseTracker:
    def __init__(self, user: str, flow):
        self.user = user
        self.request = flow
        
    def handle_msg(self, question: str):
        self.request = data
        self.add_expense(float(data))
        
    def create_msg(self, answer):
        

    def add_expense(self, amount: float):
        # Add an expense for the user
        self.daily_spent += amount
        self.monthly_spent += amount

        # Check if limits are exceeded
        self.check_limits()

    def check_limits(self):
        # Check if daily limit is exceeded
        if self.daily_spent > self.daily_limit:
            self.alert("daily")

        # Check if monthly limit is exceeded
        if self.monthly_spent > self.monthly_limit:
            self.alert("monthly")

    def alert(self, limit_type: str):
        # Trigger an alert when a limit is exceeded
        print(f"Alert: {limit_type} spending limit exceeded!")

    def generate_vis(self):
        # Logic to generate visualization for the user
        pass

    def generate_report(self):
        # Logic to generate a report for the user
        pass

    def generate_response(self, interval: str, category: str):
        # Logic to generate a response based on interval and category
        pass

