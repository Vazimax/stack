class Stack:
    
    def __init__(self,capacity):

        self.capacity = capacity
        self.data = [None] * capacity
        self.top = -1

    def is_full(self):

        return self.top == self.capacity - 1
    
    def is_empty(self):

        return self.top == -1

    def push(self,element):

        if self.is_full():
            print("Sorry, the stack is full")
            return None 
        
        self.top = self.top + 1 
        self.data[self.top] = element

    def pop(self):

        if self.is_empty():
            print("Sorry, the stack is empty")
            return None
        
        to_pop = self.data[self.top]
        self.top -= 1
        return to_pop

    def peek(self):

        if self.is_empty():
            print("Sorry, the stack is empty")
            return None

        return self.data(self.top)
        

def is_balanced(expression):

    s = Stack(capacity=len(expression))
    for char in expression:
        if char == "(":
            s.push(char)
        elif char == ")":
            if s.is_empty():
                return False

            s.pop()

    return s.is_empty()


assert is_balanced("bakr") == True
assert is_balanced("(a + b)") == True
assert is_balanced("((a + b) + (v + c)) + (a + b)") == True
assert is_balanced("((a + b) + (v + c)) + a + b)") == True

