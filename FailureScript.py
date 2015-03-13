#Author Rashid Berndt
#March 2015
###################################################################################
###################################################################################
###################################################################################

product_name = 'SCR200E'
product_note = 'units that failed oven proofing because of large changes in grids'
product_date = '01/11/2014'

###################################################################################
###################################################################################
###################################################################################

def findStart(file):  #find the start of the next element
    while True:
        line = file.readline()
        if(line == ""): return False #if the line is empty (this happens at the end of the file)
        if('at 0x4D' in line): return True #this is how elements start
    return False

def findGridEnabled(file):
    while True:
        line = file.readline()
        if(line == ""): return False #if the line is empty (this happens at the end of the file)
        if('Grid enabled: ' in line):   #if we read grid enable bit
            if('1' in line):
                return 'Grid Enabled'
            else:
                return 'Grid Not Enabled'
        if('Current' in line):  #gone too far and missed grid enable bit in file
            return 'error reading data'
    return 'error reading data'

def findBattery(file):   #find the condition of the battery, either good or something else, bad?
    while True:
        line = file.readline()
        if(line == ""): return "" #if the line is empty (this happens at the end of the file)
        if('Battery Good' in line): return "Battery Good" #check if battery is dead or alive
        if('Battery Fail' in line): return "Battery Fail" #need to find what string this actually is
        if('Grid Enabled at count' in line): return "No Battery Info" #program should never get to here, if it does it has failed

def findMinMaxStep(file):
    A_min = None
    A_max = None
    A_biggest_step = None

    B_min = None
    B_max = None
    B_biggest_step = None

    while True:
        line = file.readline()
        if('ADC Limits:' in line): #when we reach the line before the grid record appear
            grid_A_found = False #loop until we find the values
            grid_B_found = False
            while not(grid_A_found):
                line = file.readline()
                if('Max change:' in line):
                    grid_A_found = True
                    words = line.split()
                    A_min_index = words.index('far:') + 1
                    A_max_index =  A_min_index + 2
                    
                    A_biggest_step_index = A_min_index + 5

                    
                    A_min = int(float(words[A_min_index]))
                    A_max = int(float(words[A_max_index]))

                    A_biggest_step = int(float(words[A_biggest_step_index]))

                if('MinMax temp seen:' in line): #the exit condition, we have gone too far
                    return A_min, A_max, B_min, B_max


            while not(grid_B_found):
                line = file.readline()
                if('Max change:' in line):
                    grid_B_found = True
                    words = line.split()
                    B_min_index = words.index('far:') + 1
                    B_max_index =  B_min_index + 2
                    B_biggest_step_index = B_min_index + 5

                    B_min = int(float(words[B_min_index]))
                    B_max = int(float(words[B_max_index]))

                    B_biggest_step = int(float(words[B_biggest_step_index]))
                if('MinMax temp seen:' in line): #the exit condition, we have gone too far
                    return A_min, A_max, B_min, B_max

            return A_min, A_max, A_biggest_step, B_min, B_max, B_biggest_step

        if('MinMax temp seen:' in line): #the exit condition, we have gone too far
            return A_min, A_max, A_biggest_step, B_min, B_max, B_biggest_step


def find_off(file):
    while True:
        line = file.readline()
        if('Current ADC values, grid off:' in line):
            words = line.split()
            values = words[5].split(',')

            A_off = int(values[0])
            B_off = int(values[1])
            SEC_off = int(values[3])
            #print(A_off, B_off, SEC_off)
            return A_off, B_off, SEC_off
        if('Current ADC values, grid on:' in line): #early exit criteria
            return None, None, None

def find_current(file):
    while True:
        line = file.readline()
        if('Current ADC values, grid on:' in line):
            words = line.split()
            values = words[5].split(',')

            A_on = int(values[0])
            B_on = int(values[1])
            SEC_on = int(values[3])

            temp_store = values[4].split('(')
            temp = temp_store[1]
            #print(temp_store)
            temp = temp.rstrip(')')
           # print(temp)
            temp_store = int(temp)
           # print(temp)
            return A_on, B_on, SEC_on, temp
        if('Current ADC values, grid on:' in line): #early exit criteria
            return None, None, None

def check_debounce(file):
    A_failed = None
    B_failed = None
    line = file.readline()
    while(not 'IntegrityCheck done:' in line):
        if('Failed grid=AnalogA' in line):
            A_failed = 'Grid A Failed'
           # print('Grid A debounce Failed :' + str(line))

        if('Failed grid=AnalogB' in line):
            B_failed = 'Grid B Failed'
          #  print('Grid B debounce Failed :' + str(line))
            #print(B_
        line = file.readline()
            
    if(A_failed == None):
        A_failed = 'Grid A Good'
        
    if(B_failed == None):
        B_failed = 'Grid B Good'
   # print(str(A_failed) + ' and ' + str(B_failed))
    return A_failed, B_failed

class Unit:
    
    def __init__(self): #this is called when an object of class Unit is created
        self.product = product_name
        self.note = product_note
        self.date = product_date

        self.grid_state = None

        self.battery_record = None
        
        self.grid_A_Min = None
        self.grid_A_Max  = None
        self.grid_A_Step = None
        self.grid_A_off = None
        self.grid_A_current = None
        
        self.grid_B_Min = None
        self.grid_B_Max = None
        self.grid_B_Step = None
        self.grid_B_off = None
        self.grid_B_current = None

        self.SEC_off = None
        self.SEC_on = None

        self.temp_current = None

        self.grid_A_debounce = None
        self.grid_B_debounce = None

    def __str__(self): #this is called when the class is converted to string using str(instance)
        return (str(self.grid_state) + ';' + str(self.battery_record) +';' + str(self.grid_A_Min)  +';' + str(self.grid_A_Max) +';' + str(self.grid_A_Step) +';'+ str(self.grid_B_Min)  + ';'+ str(self.grid_B_Max) + ';'+ str(self.grid_B_Step) + ';' +  str(self.grid_A_off)  +';'+ str(self.grid_B_off)  + ';'+ str(self.SEC_off) + ';' + str(self.grid_A_current) + ';' +  str(self.grid_B_current) + ';'  + str(self.SEC_on) +';' +str(self.temp_current) + ';' + str(self.grid_A_debounce) + ';' + str(self.grid_B_debounce)+';' + str(self.product) + ';' + str(self.note) + ';'+ str(self.date)) + ';'

read_file = open('fails.txt', 'r', encoding='utf8')
write_file = open('semicolon_delimited_fails.txt', 'w')
#print(read_file.name)

# Write Header
current_unit = Unit() #there is a garbage collector, not too sure how this works but I am hoping that this instance will be freed entering the next cycle of the loop
 
current_unit.grid_state = 'Grid State'

current_unit.battery_record = 'Battery State'

current_unit.grid_A_Min = 'Grid A Min'
current_unit.grid_A_Max = 'Grid A Max'
current_unit.grid_A_Step = 'Grid A Biggest Step'

current_unit.grid_B_Min = 'Grid B Min'
current_unit.grid_B_Max = 'Grid B Max'
current_unit.grid_B_Step = 'Grid B Biggest Step'

current_unit.grid_A_off = 'Grid A Off'
current_unit.grid_B_off = 'Grid B Off'
current_unit.SEC_off = 'SEC Off'

current_unit.grid_A_current = 'Grid A Current'
current_unit.grid_B_current = 'Grid B Current'
current_unit.SEC_on = 'SEC Current'

current_unit.grid_A_debounce = 'Historic A Failure'
current_unit.grid_B_debounce = 'Historic B Failure'

current_unit.temp_current = 'Current Temperature'

current_unit.product = 'Product'
current_unit.note = 'Note'
current_unit.date = 'Date'

write_file.write(str(current_unit) + '\n')
#print(current_unit)

del current_unit #finished with header so destroy it




while(findStart(read_file)):
    current_unit = Unit() #there is a garbage collector, not too sure how this works but I am hoping that this instance will be freed entering the next cycle of the loop
 
    current_unit.grid_state = findGridEnabled(read_file)

    current_unit.battery_record = findBattery(read_file)

    grid_min_max_values = findMinMaxStep(read_file)     #find min max grid values
    current_unit.grid_A_Min = grid_min_max_values[0]
    current_unit.grid_A_Max = grid_min_max_values[1]
    current_unit.grid_A_Step = grid_min_max_values[2]

    current_unit.grid_B_Min = grid_min_max_values[3]
    current_unit.grid_B_Max = grid_min_max_values[4]
    current_unit.grid_B_Step = grid_min_max_values[5]


    grid_off_values = find_off(read_file)
    current_unit.grid_A_off = grid_off_values[0]
    current_unit.grid_B_off = grid_off_values[1]
    current_unit.SEC_off = grid_off_values[2]

    grid_on_values = find_current(read_file)
    current_unit.grid_A_current = grid_on_values[0]
    current_unit.grid_B_current = grid_on_values[1]
    current_unit.SEC_on = grid_on_values[2]
    current_unit.temp_current = grid_on_values[3]
    
    debounce = check_debounce(read_file)
    current_unit.grid_A_debounce = str(debounce[0])
    current_unit.grid_B_debounce = str(debounce[1])

    #print('Actual grid A: ' + str(debounce[0]))
    #print('Recorded grid A: ' + str(current_unit.grid_A_debounce))

   # print('Recorded grid B: ' + str(current_unit.grid_B_debounce))
   # print('Actual grid B: ' + str(debounce[1]))

    write_file.write(str(current_unit) + '\n')
  #  print(current_unit)
    

read_file.close()
write_file.close()
