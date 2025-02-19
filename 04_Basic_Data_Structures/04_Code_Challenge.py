def encodeString(stringVal):
    letters = [character for character in stringVal]
    b=[]
    x=0
    for i in range(len(letters)):
        if (letters[i] == letters[i-1] or i == 0) and (i < len(letters)-1):
            x += 1
            continue
        elif i == len(letters)-1:
            x +=1
            ch = letters[i-1]
            b.append((ch, x))
        else:
            ch = letters[i-1]
            b.append((ch, x))
            x=1
            continue
    return b

def decodeString(encodedList):
    a = []
    string =''
    for key,value in encodedList:
        a.append(key*value)
    for i in range(len(a)):
        string += a[i]
    return string

a1 = encodeString('''
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                    %%%%%%%%                         %%%%%%%%                   
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%             
           %%%%%%                                               %%%%%           
          %%%%%                                                   %%%%%         
        %%%%%                                                       %%%%%       
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%     
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%   
    %%%%                    %%%%%              %%%%%                     %%%%   
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%   
    %%%%       %%%%%%                                        %%%%%       %%%%   
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%     
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%         
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                   %%%%%%%%%%%%                                 
''')
a2 = encodeString('AAAAABBBBCCC')

print(a1)
print(decodeString(a1))
print(a2)
print(decodeString(a2))