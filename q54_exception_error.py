try:
    5/0
except ZeroDivisionError:
    print("division by zero!")
except Exception:
    print("Caught an exception")
finally:
    print("In finally block for cleanup")
    
