def log_transaction(func):
    def wrapper():
        print("1. Logging transaction...")
        func()
        print("3. log terminado...")
    return wrapper

@log_transaction
def process_payment():
    print("2. Processing payment...")

process_payment()