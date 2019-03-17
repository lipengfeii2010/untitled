invitees = ['Huang Yongqing', 'Li Qingchang', 'Huang Diming']
absent = invitees.pop(1)
print(absent + " is absent.")
invitees.append("Su Tianbo")
print("I find a bigger desk. We can have supper with more friends!")
invitees.insert(0, "Chen Songhui")
invitees.insert(2, "Huang Minghui")
invitees.append("Tang Fei")
for i in range(len(invitees)):
    print('Would you like to have supper with me tonight? ' + invitees[i] + ".")
print("I'm sorry that there are only two friends can be invited " +
      "because the new desk can't be serviced on time.\n")
for i in range(len(invitees) - 2):
    print(invitees.pop() + ", we have a date next time.")
for i in range(2):
    print(invitees[i] + "Would you still like to have supper with me tonight?")
print()
del invitees[:]
print(invitees)