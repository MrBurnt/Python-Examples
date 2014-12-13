def incrementBit(hex):
    hex = hex +1
    return hex



def increment(macAddress):
    #increment part of the address
    newMacAddress = [0,0,0,0,0,0]
    carryBit = True
    i = 5

    #while there is a number to add/carry bit
    while(carryBit):
        macAddress[i] = incrementBit(macAddress[i])
        #if the hex number is still below where it ticks over to a higher significant place
        if macAddress[i] <= 255: #15: #255:
            #this is the last time a value will be incremented
            carryBit = False
        #if the hex number ticks over to the next significant bit
        else:
            #the hex number goes to zero and the carry bit is set to indicate that the next level should be incremented
             macAddress[i] = 0
             carryBit = True
        #the position we are looking at the mac address is moved to the next significant place
        i = i - 1

        #if the next significant place is out of range the process ends and an error is show, continues from 0
        if i < 1:
            carryBit = False
            print("")
            print("Error Encountered, it seems like the mac address has gone out of range:")
            print(macAddress)
            print("")
            macAddress[i] = 0
    return macAddress

#prints mac addresses as they are
def printMacAddress(macAddress):
    #print(hex(macAddress[0]) +":"+ hex(macAddress[1]) +":"+ hex(macAddress[2]) +":"+ hex(macAddress[3]) +":"+ hex(macAddress[4]) +":"+hex(macAddress[5]))
    print('{:02x}'.format(macAddress[0]) +":"+'{:02x}'.format(macAddress[1]) +":"+'{:02x}'.format(macAddress[2]) +":"+'{:02x}'.format(macAddress[3]) +":"+'{:02x}'.format(macAddress[4]) +":"+'{:02x}'.format(macAddress[5]))

#prints mac addresses with a leading #, needed for my application
def printMacAddress2(macAddress):
    #print(hex(macAddress[0]) +":"+ hex(macAddress[1]) +":"+ hex(macAddress[2]) +":"+ hex(macAddress[3]) +":"+ hex(macAddress[4]) +":"+hex(macAddress[5]))
    print("#          "+'{:02x}'.format(macAddress[0]) +":"+'{:02x}'.format(macAddress[1]) +":"+'{:02x}'.format(macAddress[2]) +":"+'{:02x}'.format(macAddress[3]) +":"+'{:02x}'.format(macAddress[4]) +":"+'{:02x}'.format(macAddress[5]))


#Top of program header
print("This program generates the number of mac addresses entered,")
print("starting at the value entered.")
print("")

print("There are almost no safety nets in this program so please check")
print("that your mac addresses make sense.")
print("")

print("The mac address should contain six hex numbers (0 to F)")
print("each with two characters separated by :, for example AA:BB:CC:11:22:33,")
print("a:b:c:1:2:3 or aa:bb:cc:11:22:33.")
print("")

#user input
inputMacAddress = input("Please enter the starting mac address:")
print(inputMacAddress + " entered")

inputJ = input("Please enter the number of mac addresses to generate:")
print(inputJ + " mac addresses will be generated")
print("")

#convert input to program usable data
userMacAddress = inputMacAddress.split(":")

macAddress = [0,0,0,0,0,0]

for i in range(0,6):
    macAddress[i] = int(userMacAddress[i], 16)

j = 0

#loop as many time neccissary to generate the mac addresses
while(j <int(inputJ)):
    j = j+1
    macAddress = increment(macAddress)
    printMacAddress2(macAddress)



                
