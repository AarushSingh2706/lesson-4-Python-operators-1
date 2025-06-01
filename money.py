Amount = (int(input("give money for withdrawing")))
notes_1 = Amount//500
notes_2 = (Amount%500)//100
notes_3 = (Amount%500)%100//50
notes_4 = (Amount%500)%100%50//10
print("500 notes are",notes_1)
print("100 notes are",notes_2)
print("50 notes are",notes_3)
print("10 notes are",notes_4)
