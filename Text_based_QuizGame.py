import time

true = ["T", "t", "True"]
false = ["F", "f", "False"]
correct = 0
name = input ("What's your name?") 

print ("\nOK, " +  name +", let's get started. Remember, the following answers are only True or False.")
time.sleep(2)

print ("\nDelhi is the captial of India.")
choice = input(">>> ")
if choice in true:
  correct += 1 #If correct, the user gets one point
else:
  correct += 0
  
print ("\nCyclones spin in a clockwise direction in the southern hemisphere.")
choice = input(">>> ")
if choice in true:
  correct += 1
else:
  correct += 0  

print ("\nA woman has walked on the moon.")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0 
  
print ("\nAndorra is between France and Spain.")
choice = input(">>> ")
if choice in true:
    correct += 1
else:
  correct += 0  
  
print ("\nThe mathematical name for the shape of a Pringle is hyperbolic paraboloid.")
choice = input(">>> ")
if choice in true:
  correct += 1
else:
  correct += 0
  
print ("\nThe currency of France is the Franc")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0
    
print ("\nYou're finished, " + name +". You got", correct, "out of 6 correct.")