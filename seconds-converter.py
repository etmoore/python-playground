total_seconds = input("How many seconds would you like to convert? ")

hours = total_seconds // 3600
seconds_remaining = total_seconds % 3600

minutes = seconds_remaining // 60
seconds_remaining = seconds_remaining % 60

print(str(hours) + " hours, " + str(minutes) + " minutes, " +
      str(seconds_remaining) + " seconds")
