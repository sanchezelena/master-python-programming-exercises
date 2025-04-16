def hours_minutes(seconds):
  # Your code here
  hours = seconds // 3600
  minutes = (seconds % 3600) // 60
  return f"{hours}, {minutes}" 


# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))
