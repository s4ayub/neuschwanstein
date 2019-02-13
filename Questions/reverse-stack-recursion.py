def insertAtBottom(stack, item): 
    if isEmpty(stack): 
        push(stack, item) 
    else: 
        temp = pop(stack) 
        insertAtBottom(stack, item) 
        push(stack, temp) 

# reverses the given stack 
# using insertAtBottom() 
def reverse(stack): 
    if not isEmpty(stack): 
        temp = pop(stack) 
        reverse(stack) 
        insertAtBottom(stack, temp)

# temp = 5, stack = [4, 3]
# temp = 4, stack = [4, 3]
# temp = 3, stack = []

# insertAtBottom
# stack = [3] 

# Function to check if  
# the stack is empty 
def isEmpty(stack): 
    return len(stack) == 0
  
# Function to push an  
# item to stack 
def push( stack, item ): 
    stack.append( item ) 

def pop( stack ): 

    if(isEmpty( stack )): 
        print("Stack Underflow ") 
        exit(1) 

    return stack.pop() 

s = [3, 4, 5]
reverse(s)

print(s)


def insertAtBottom(stack, val):
    if len(stack) == 0:
        stack.append(val)
    else:
        temp = stack.pop()
        insertAtBottom(stack, val)
        stack.append(temp)
    
def reverse(stack):
    if not len(stack):
        temp = stack.pop()
        revserse(stack)
        insertAtBottom(stack, val)
        




