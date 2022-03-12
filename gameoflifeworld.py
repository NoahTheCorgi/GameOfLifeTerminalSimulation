import random, time

n = 60 #different_worlds_physics.n
N=n*n #total number of cells

def determine_new_world():
	wworld = []
	i = 0
	while i < N:
		wworld.append(random.choice([" ","*"])) #random.choice([" ","*"])
		i+=1
	return wworld

def show_world(world):
	j=0
	L = []
	the_word = ""
	while j < N:
		L.append(world[j:n+j])
		j+=n

	k = 0
	while k < n:
		l = 0
		while l < n:
			the_word = the_word + L[k][l] + ' '
			l+=1
		k += 1
		the_word += '\n'

	print(the_word)


#Idea: first need to create a double array,,,,, in order to index efficiently...
def create_next_state_original(previous):

	dbllist = []
	nbhr_count = []

	i = 0
	while i < N:
		nbhr_count.append(0) #random.choice([" ","*"])
		i+=1

	j=0
	while j < N:
		dbllist.append(previous[j:n+j])
		j+=n

	#'b' represents the width 'a' represents the height all starting from the top left corner....
	a = 1
	while a < n-1:
		b = 1
		while b < n-1:
			if dbllist[a][b] == "*":
				nbhr_count[(b) + (a)*n + 1 -n ] +=1
				nbhr_count[(b) + (a)*n -n] +=1
				nbhr_count[(b) + (a)*n - 1 -n] +=1

				nbhr_count[(b) + (a)*n + 1] +=1
				nbhr_count[(b) + (a)*n - 1] +=1

				nbhr_count[(b) + (a)*n + 1 + n] +=1
				nbhr_count[(b) + (a)*n + n] +=1
				nbhr_count[(b) + (a)*n - 1 + n] +=1
			b+=1
		a+=1

	#addressing the corners:
	#top left corner
	if dbllist[0][0] == "*":
		nbhr_count[(0) + (0)*n + 1] +=1
		nbhr_count[(0) + (0)*n + n] +=1
		nbhr_count[(0) + (0)*n + 1 + n] +=1

	#top right corner
	if dbllist[0][n-1] == "*":
		nbhr_count[(n-1) + (0)*n - 1] +=1
		nbhr_count[(n-1) + (0)*n + n] +=1
		nbhr_count[(n-1) + (0)*n - 1 + n] +=1

	#bottom left corner
	if dbllist[n-1][0] == "*":
		nbhr_count[(0) + (n-1)*n + 1 ] +=1
		nbhr_count[(0) + (n-1)*n - n ] +=1
		nbhr_count[(0) + (n-1)*n + 1 - n] +=1

	#bottom right corner
	if dbllist[n-1][n-1] == "*":
		nbhr_count[(n-1) + (n-1)*n -1] +=1
		nbhr_count[(n-1) + (n-1)*n - n] +=1
		nbhr_count[(n-1) + (n-1)*n - 1 - n] +=1

	#addressing the edges without the corners....
	#e1. addressing the top horizontal edge
	b = 1
	while b < n-1:
		if dbllist[0][b] == "*":
			nbhr_count[(b) + (0)*n + 1] +=1
			nbhr_count[(b) + (0)*n - 1] +=1
			nbhr_count[(b) + (0)*n + n] +=1
			nbhr_count[(b) + (0)*n +1 + n] +=1
			nbhr_count[(b) + (0)*n - 1 + n] +=1
		b+=1
	#e2. addressing the bottom horizontal edge
	b = 1
	while b < n-1:
		if dbllist[n-1][b] == "*":
			nbhr_count[(b) + (n-1)*n + 1] +=1
			nbhr_count[(b) + (n-1)*n - 1] +=1
			nbhr_count[(b) + (n-1)*n - n] +=1
			nbhr_count[(b) + (n-1)*n +1 - n] +=1
			nbhr_count[(b) + (n-1)*n - 1 - n] +=1
		b+=1
	#e3. addresssing the left vertical edge
	a = 1
	while a < n-1:
		if dbllist[a][0] == "*":
			nbhr_count[(0) + (a)*n -n] +=1
			nbhr_count[(0) + (a)*n -n + 1] +=1
			nbhr_count[(0) + (a)*n +1] +=1
			nbhr_count[(0) + (a)*n +n] +=1
			nbhr_count[(0) + (a)*n +n + 1] +=1
		a+=1

	#e4. addressing the right vertical edge
	a = 1
	while a < n-1:
		if dbllist[a][n-1] == "*":
			nbhr_count[(n-1) + (a)*n -n] +=1
			nbhr_count[(n-1) + (a)*n -n - 1] +=1
			nbhr_count[(n-1) + (a)*n -1] +=1
			nbhr_count[(n-1) + (a)*n +n] +=1
			nbhr_count[(n-1) + (a)*n +n - 1] +=1
		a+=1

	#Now...... all relevant neighborhood details are updated...

	i = 0
	while i < N:
		m = nbhr_count[i]

		if previous [i] == "*":
			if m < 2 or m > 3: # should be m<2 or m>3 for original conway's set of rules.
				previous[i] = " "
		else:
			if m == 3: # should be m == 3 for original conway's set of rules
				previous[i] = "*"

		i+=1
	#time.sleep(1)
	return previous


####################################################################################
####################################################################################
####################################################################################
def run_terminal_visualization():
	The_World = []
	counter = 0
	x = 0
	while x < 500:
		if counter == 0:
			The_World = determine_new_world()
			show_world(The_World)
			counter+=1
		else:
			The_World = create_next_state_original(The_World)
			show_world(The_World)
			counter+=1
		x+=1
		time.sleep(.1)
	print(counter, "number of states went by.")

######################
run_terminal_visualization()
######################
