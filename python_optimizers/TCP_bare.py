# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 14:52:30 2021

@author: 359167
"""
import socket, json, csv, numpy as np
from scipy import optimize

# %%%%% ----------------------- connections -----------------------------%%%%%

def conns(HOST1, PORT1):
    
    ''' Connect to host port. '''
 
    socket_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket_1.connect((HOST1,PORT1))
    
    return (socket_1) 
 
def start():
    
    ''' Initialize connection. '''

    receiver = conns('localhost', 62358)
    
    return (receiver) 

def cleanup(): 

    ''' Close communication with port and end VI. '''
    
    receiver = conns('localhost', 62358)
    receiver.close()
    
    return ()  

# %%%%% ------------------------- send data -----------------------------%%%%%        

def send_params(conn, params_dict, mode):
    
    ''' Send inputs to LV. '''
    
    params_list = np.array(params_dict).tolist()
    params = [mode] + params_list # 1 = run cmd

    conn.send(json.dumps(params).encode())          
    conn.send('\r\n'.encode())   
               
    while True:  # listening for confirmation
    
        conf_msg = conn.recv(1024)  
        
        if len(conf_msg) > 0:
            
            conf_msg = conf_msg.decode()
                        
            break

    return (conf_msg)

# %%%%% ----------------------- receive data ----------------------------%%%%%

def receive_value(conn, params_dict, mode):
    
    ''' Output return value from LV. '''
    
    send_params(conn, params_dict, mode) # Send params to LV

    while True: # Listen for return from LV
        
        returning_value_bytes = conn.recv(10240)
        
        if len(returning_value_bytes) > 0:
            
            returning_value_json = returning_value_bytes.decode()
            
            break

    returning_value_dict = json.loads(returning_value_json)
    
    val_list = list(map(float, returning_value_dict.values())) 

    returning_val = val_list[0] 

    return (returning_val)

# %%%%% ----------------------- run optimizer ---------------------------%%%%%

def opt() :

    '''Minimize error between LabVIEW output and max return set by cap. '''
    
    print('')
    print('------------------------------------------------')
    print('')
    print('Running optimization . . .')
    print('')
    print('------------------------------------------------')
    print('')
    
    cap = 80 # max return value
    
    def comm(params_dict) :
    
        ''' Send multiple inputs to LabVIEW and recieve a single output. 
        Return difference, or error, between the output and cap. '''
        
        return (receive_value(start(),params_dict, 1) - cap)
    
    
    def initial_guess() :
        
        ''' Set first optimizer guess as starting position. '''
        
        file = 'saved_position.csv'
    
        with open(file, mode = 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            for row in csv_reader:
                    guess_list = list(map(float, row.values())) # dict to floats
            
            return (guess_list)
        

    x_g = initial_guess()
    b = (0,12.7)
    bnds = (b,) * len(x_g) 
    
    res = optimize.minimize(fun = comm, x0 = x_g, method = 'L-BFGS-B', bounds=bnds)
    
    elem = [res.x[0],res.x[1],res.x[2],res.x[3]]
    
    print("Final inputs:", elem)
    print('')
    print("Final output:" , (comm(elem) + cap))
    print('')
    print('------------------------------------------------')
    print('') 
    
# %%%%% ----------------------- choose mode -----------------------------%%%%%

def pick_mode():
    
    ''' Choose whether to run the optimizer, home all channels,
    test TCP communication, or quit. '''
    
    print('')
    print('------------------- MODES ----------------------')
    print('')
    print(' [1] Minimize            [3] Home')
    print(' [2] Test                [4] Exit')

    mode = int(input('Please choose and enter: '))
    
    if mode == 4:
        KeyboardInterrupt()
    
    else:
        if mode == 1:
            opt()
        
        elif mode == 2:
            print('')
            print('------------------------------------------------')
            print('')
            print('Please separate elements with spaces and enter. ')
            
            array_in = input('Input data: ')
            
            array = list(map(float, array_in.split()))
            to_send = np.array(array, dtype = float)
            
            comm(to_send, 1)
            
        elif mode == 3:
            with open('saved_position_2.csv', mode = 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
        
                for row in csv_reader:
                    val_list = list(row.values())
                    home = [0,] *len(val_list)
                    
            comm(home, 3)
        
        print(' [1] Main Menu')
        print(' [2] Exit')
        
        choice = int(input('Please choose and enter: '))
    
        if choice == 1:
            pick_mode()
            
        if choice == 2:
            cleanup()
            
# %%%%% --------------------------- comms test --------------------------%%%%%
    
def comm(vals, mode): 

    ''' Send and recieve data once. '''

    print('')
    print('Returned from LV:', receive_value(start(), vals, mode))
    print('')
    print('------------------------------------------------')
    print('') 
    
    return receive_value(start(), vals, mode)
        
# %%%%% ----------------------------- main ------------------------------%%%%%

def main():
    
    pick_mode()
    
try: main()

except KeyboardInterrupt :
    print('')
    print('')
    print('------------------------------------------------')
    print('')
    print('Program force quit by Client. ')

except ConnectionRefusedError : 
    print('------------------------------------------------')
    print('')
    print('Please start running LabVIEW. ')

except ConnectionResetError : 
    print ('Program force quit by Server. ')
    
print('')
print('------------------------------------------------')       
        
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    