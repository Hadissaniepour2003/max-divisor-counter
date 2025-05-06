def nums():
    best_div_count=0
    best_num=None
    for i in range(5):
        num1=int(input("please enter your number:")) 
        current_divisor_count=0  
        for j in range(1,num1+1):
            if num1%j==0:
                current_divisor_count+=1
            if current_divisor_count>best_div_count:
                best_div_count=current_divisor_count
                best_num=num1
            elif current_divisor_count==best_div_count: 
                if best_num==None or num1>best_num:
                    best_num=num1
    return best_num, best_div_count
best_num, best_div_count = nums()
print("Best number:", best_num, "with divisor count:", best_div_count)              
                
                      
                   
                
            
                    
                
                
                                
                
                
                
                
            
            