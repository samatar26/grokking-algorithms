# 3.1
# The greet function is called first, with name = maggie
#  Then greet function calls the greet2 function with name = maggie
#  At that point the greet function is in a partially completed/suspended state
#  The current funciton call is greet2 and when it finishes, the greet function will resume


# 3.2
# If a recursive function runs forever, this mean that a function call, i.e. a box of memory allocated for a function call keeps being pushed onto the call stack.
# And the call stack grows forever. Each program only has a limited amount of space on the call stack and when it runs out it'll exit with a stack overflow error.
