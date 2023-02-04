import copy
import random
import math


def swap(state, i, j):
    new_state = copy.deepcopy(state)
    temp = new_state[j]
    new_state[j] = new_state[i]
    new_state[i] = temp
    # print(new_state)
    return new_state

# def up(state):
# 	zero_index = state.index(0)
# 	if zero_index > 3:
# 	    return swap(state, zero_index, zero_index - 4)
# 	else:
# 	    return None

# def down(state):
# 	zero_index = state.index(0)
# 	if zero_index < 12:
# 	    return swap(state, zero_index, zero_index + 4)
# 	else:
# 	    return None

# def left(state):
# 	zero_index = state.index(0)
# 	if zero_index % 4 != 0:
# 	    return swap(state, zero_index, zero_index - 1)
# 	else:
# 	    return None

# def right(state):
# 	zero_index = state.index(0)
# 	if (zero_index + 1) % 4 != 0:
# 	    return swap(state, zero_index, zero_index + 1)
# 	else:
# 	    return None

def up(state):
	zero_index = state.index(0)
	length = int(math.sqrt(len(state)))
	if zero_index > (length - 1):
	    return swap(state, zero_index, zero_index - length)
	else:
	    return None

def down(state):
	zero_index = state.index(0)
	length = int(math.sqrt(len(state)))
	if zero_index < length * (length - 1):
	    return swap(state, zero_index, zero_index + length)
	else:
	    return None

def left(state):
	zero_index = state.index(0)
	length = int(math.sqrt(len(state)))
	if zero_index % length != 0:
	    return swap(state, zero_index, zero_index - 1)
	else:
	    return None

def right(state):
	zero_index = state.index(0)
	length = int(math.sqrt(len(state)))
	if (zero_index + 1) % length != 0:
	    return swap(state, zero_index, zero_index + 1)
	else:
	    return None

def random_generate(state):
	new_state = None
	random_step = random.randint(0, 3)
	if random_step == 0:
		new_state = up(state)
	elif random_step == 1:
		new_state = down(state)
	elif random_step == 2:
		new_state = left(state)
	else:
		new_state = right(state)
	return new_state


print("start generating ...")


size = 8
step = 1000
number_of_samples = 50

samples_8 = []
while len(samples_8) < number_of_samples:
	state = [1,2,3,4,5,6,7,8,0]
	new_state = [1,2,3,4,5,6,7,8,0]
	count = 0
	while count < (step + 1):
		temp = random_generate(new_state)
		while (temp == None):
			temp = random_generate(state)
		new_state = copy.deepcopy(temp)
		count += 1

	if (new_state not in samples_8) and (new_state != state):
		samples_8.append(new_state)

for s in samples_8:
	s.reverse()

output = open("samples_for_8_puzzle.txt", "w", buffering=1)
header = str(size) + " " + str(number_of_samples)
output.write(header)
for s in samples_8:
	sample =  "\n" + "".join(str(n) for n in s)
	output.write(sample)
output.close()


print("Samples for 8-puzzle are generated")


size = 15

samples_15 = []
while len(samples_15) < number_of_samples:
	state = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
	new_state = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
	count = 0
	while count < (step + 1):
		temp = random_generate(new_state)
		while (temp == None):
			temp = random_generate(state)
		new_state = copy.deepcopy(temp)
		count += 1

	if (new_state not in samples_15) and (new_state != state):
		samples_15.append(new_state)

# print(samples_15)

output = open("samples_for_15_puzzle.txt", "w", buffering=1)
header = str(size) + " " + str(number_of_samples)
output.write(header)
for s in samples_15:
	sample =  "\n" + " ".join(str(n) for n in s)
	output.write(sample)
output.close()



print("Samples for 15-puzzle are generated")

