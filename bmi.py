def calculate_bmi(height, weight):
  print("Height = " + str(height))
  print("Weight = " + str(weight))

  bmi = weight/(height*height)
  print(f"Your BMI is {bmi}.")
  if(bmi<18.5):
    print("Under weight.")
    return -1
  elif(18.5<=bmi<=25.0):
    print("Normal weight")
    return 0
  else:
    print("Over weight.")
    return 1
calculate_bmi(weight=57, height=1.73)

