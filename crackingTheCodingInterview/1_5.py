string1 = "strog bem massa"
string2 = "string bem massa"

def one_away():
    edits = 0
    length_diff = len(string1) - len(string2) 
    if(abs(length_diff) > 1):
        print("not one away")
        return

    elif(length_diff<0):
        j = 0
        for i in range(len(string2)):
            if string2[i] != string1[j]:
                edits += 1
            else:
                j+=1

    elif(length_diff>0):
        j = 0
        for i in range(len(string1)):
            print(str(i) +' and ' +str(j))
            if string1[i] != string2[j]:
                edits += 1
            else: 
                j+=1
           

    elif(length_diff == 0):
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                edits += 1

    if(edits > 1):
        print("not one away")
    else:
        print("one away")

one_away()

# well, it works...