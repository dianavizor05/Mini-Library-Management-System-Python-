def action_info(func):
    def wrapper(*args, **kwargs):
        print("Wykonywanie akcji...")
        return func(*args, **kwargs)
    return wrapper