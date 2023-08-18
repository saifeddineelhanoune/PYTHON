   # Addition
   num1 = 10
   num2 = 5
   result = num1 + num2
   print("Addition:", result)

   # Subtraction
   result = num1 - num2
   print("Subtraction:", result)

   # Multiplication
   result = num1 * num2
   print("Multiplication:", result)

   # Division
   result = num1 / num2
   print("Division:", result)

   def and_gate(a, b):
       if a == 1 and b == 1:
           return 1
       else:
           return 0

   # Testing the AND gate
   print(and_gate(0, 0))  # Output: 0
   print(and_gate(0, 1))  # Output: 0
   print(and_gate(1, 0))  # Output: 0
   print(and_gate(1, 1))  # Output: 1
