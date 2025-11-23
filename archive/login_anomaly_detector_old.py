#########  OLD VERSION  #########

# import csv 

# normal_hours = [8, 9, 10, 11, 12, 13, 14, 15, 16]
# count = 0
# user_suspicious = {}
# repeat_offenders = []
# more_than_1 = set()
# with open("logins.csv", "r") as file:
#   reader = csv.reader(file)
#   next(reader)
  
#   for row in reader:
#     username = row[0]
#     value = row[1]
#     if int(row[1]) not in normal_hours:
#       count += 1
#       if username not in user_suspicious:
#         user_suspicious[username] = 0
#         repeat_offenders.append((username, value))
#       user_suspicious[username] += 1
#       if user_suspicious[username] > 1:
#           more_than_1.add(username)
#       print(f"{username}: suspicious")
#     else:
#       print(f"{username}: normal")

# print(count)
# print(f"Repeat Offenders: {repeat_offenders}")
# print(f"More than one offending count: {more_than_1}")