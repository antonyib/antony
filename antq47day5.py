def roman_to_int(s):
    roman_dict={
       '|':1,
       'V':5,
       'X':10,
       'L':50,
       'C':100,
       'D':500,
       'M':1000
     }
total=o
i=0
while i<len(s):
    if i+1<len(s)and roman_dict[s[i]]<roman_dict[s[i+1]]:
        total +=roman_dict[s[i+1]]-roman_dict[s[i]]
        i+= 2
    else:
        total +=roman_dict[s[i]]
        i+= 1

        
  return total 

print(roman_to_int("|||"))
print(roman_to_int("LV|||"))
print(roman_to_int("MCMXC|V"))
print(roman_to_int("LV"))
    
                
