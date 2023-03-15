import lasanga
from lasanga import elapsed_time_in_minutes
from lasanga import preparation_time_in_minutes
from lasanga import bake_time_remaining
lasanga.EXPECTED_BAKE_TIME
bake_time_remaining(int(input("How many minutes has your lasagna been in the oven?\n")))
preparation_time_in_minutes(int(input("How many layers is your lasagna?\n")))
totalTime = elapsed_time_in_minutes(3, 20)
print("The total time you've spent on this lasagna is " + str(totalTime))