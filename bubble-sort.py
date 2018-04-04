import random
import time

start_time = time.time()
print "Bubble Sort Start."

random_list = []
for i in range(10000):
	random_list.append(random.randint(100, 1000))

round_number = 1
pointer_a = 0
pointer_b = 1
flag_success = False
print random_list

while not flag_success:	
	flag_success = True
	# print "Buble Sort Round ", round_number	
	for i in range(0, len(random_list)-1):		
		# print random_list		

		if random_list[pointer_a] > random_list[pointer_b]:
			random_list[pointer_b], random_list[pointer_a] = random_list[pointer_a], random_list[pointer_b]
			flag_success = False

		pointer_a = pointer_a + 1
		pointer_b = pointer_b + 1		

	# Reset pointer
	pointer_a = 0
	pointer_b = 1
	round_number = round_number + 1

print "Success bubble sort"
print random_list
print("--- %s seconds ---" % (time.time() - start_time))
