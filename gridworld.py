grid_cols = 10
grid_rows = 10
things = {
	1: ["Raj",[2,5],"Alive"],
	2: ["Pav",[1,2],"Alive"], 
	3: ["Mark",[9,7],"Alive"]        
}

def status():
	print("Step "+str(current_step)+":")
	for item in things.values():
		print(item[0]+" is "+item[2]+ " at " +str(item[1]))
	print("----------------------------------------------------------------")
	
steps = 20
current_step = 0
while current_step < steps:
	if current_step  == 4:
		things[1][1] = things[2][1]
	elif current_step == 6:
		things[1][1]  = [1,1]
		things[2][1]  = [1,1]
	elif current_step == 10:
		things[3][1]  = [4,8]
	elif current_step == 12:
		things[1][1] = [3,3]
		things[3][1] = [3,3]
	elif current_step == 13:
		things[1][2] = "Napping"
	elif current_step == 16:
		things[3][1] = things[2][1]
	elif current_step == 17:
		things[3][2] = "Napping"
	status()
	current_step+=1

