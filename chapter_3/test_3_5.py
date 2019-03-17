invitees = ['Huang Yongqing', 'Li Qingchang', 'Huang Diming']
absent = invitees.pop(1)
print(absent + " is absent.")
invitees.append("Su Tianbo")
for i in range(3):
    print('Would you like to have supper with me tonight? ' + invitees[i] + ".")