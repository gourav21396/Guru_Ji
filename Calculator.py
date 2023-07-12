import sys

def main():
  A = int(input("Enter first Number:"))
  B = int(input("Enter Second Number:"))

  Opr = input("Please select an operation to perform:")
    

  if Opr == "+":
    print("The result is:", A + B)
  elif Opr == "-":
    print("The result is:",A - B)
  elif Opr == "*":
    print("The result is:",A*B)
  elif Opr == "/":
    try: 
      print("The result is :",A/B)
    except ZeroDivisionError:
      print("Please enter a positive number greater than 0.")
      return main()
  else:
    print("Please enter a valid operation (+,-,*,/).")
    return main()


if __name__ == '__main__':
  main()