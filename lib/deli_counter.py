katz_deli=[]

def line(deli_line:list):
    line_num=len(deli_line)
    if line_num == 0:
        print (f"The line is currently empty.")
    else:
        #print (type(deli_line))
        # i=1
        # namelist = ''
        # for person in deli_line:
        #     namelist+=f"{i}. {person} "
        #     print(f"{i}. {person}" )
        #     i+=1
        print(f"The line is currently:", end ='')
        for i,person in enumerate (deli_line):  
        # joined_names = {i}. {person}
            print(f" {i+1}. {person}", end ='') 
        
        print('') 
        #print(f"The line is currently: {namelist}" )
line(katz_deli)


def take_a_number(deli_line:list, name:str):
    deli_line.append(name)
    print ( f"Welcome, {name}. You are number {len(deli_line)} in line.")
take_a_number(katz_deli, 'Yiran')

def now_serving(deli_line:list):
    if len(deli_line)>0:
        print(f"Currently serving {deli_line[0]}.")
        deli_line.pop(0)
        # print(  "katz_deli: ", katz_deli)
    else:
        print("There is nobody waiting to be served!")
now_serving(katz_deli)

take_a_number(katz_deli, "Ada")
take_a_number(katz_deli, "Grace")
take_a_number(katz_deli, "Kent")
print(  "katz_deli: ", katz_deli)