def is_correct_input(num_list):
	return len(num_list) != 0 and isnumeric(str(num_list))

def generate_random_num_list(length):
	import random
	num_list = []
	i = 0
	while i < length:
		num_list.append(random.randrange(2 * length))
		i -= 1
	return num_list

def bubblesort(num_list):
	if not is_correct_input(num_list):
		print('incorrect input')
		return

	swap_count = 1
	while swap_count > 0:
		swap_count = 0
		for pos in range(1, len(num_list)):
			if num_list[pos - 1] > num_list[pos]:
				temp = num_list[pos - 1]
				num_list[pos  - 1] = num_list[pos]
				num_list[pos] = temp
				swap_count += 1
	return num_list

def selectionsort(num_list):
	if not is_correct_input(num_list):
		print('incorrect input')
		return

	for pos in range(len(num_list)):
		min_pos = pos
		for pos_ in range(pos+1, len(num_list)):
			if num_list[pos_] < num_list[min_pos]:
				min_pos = pos_
		temp = num_list[pos]
		num_list[pos] = num_list[min_pos]
		num_list[min_pos] = temp

	return num_list
def insertion_sort(num_list):
	if not is_correct_input(num_list):
		print('incorrect input')
		return

	for pos in range(1, len(num_list)):
		to_be_inserted = num_list[pos]
		for pos_ in range(pos):
			if num_list[pos_] > num_pos[pos]:
				cur_pos = pos
				while cur_pos > pos_:
					num_list[cur_pos] = num_list[cur_pos - 1]
					cur_pos -= 1
				num_list[pos_] = to_be_inserted
				break

	return num_list

def shellsort(num_list):
	if not is_correct_input(num_list):
		print('incorrect input')
		return

	step = len(num_list) // 2
	while step > 0:
		for pos in range(0, len(num_list), step):
			to_be_inserted = num_list[pos]
			for pos_ in range(0, pos, step):
				if num_list[pos_] > num_list[pos]:
					cur_pos = pos
					while cur_pos > pos_ + step:
						num_list[cur_pos] = num_list[cur_pos - step]
						cur_pos -= step
					num_list[pos_] = to_be_inserted
		step //= 2

def merge(l_list, r_list):
	m_list = []
	l_pos = 0
	r_pos = 0
	while l_pos < len(l_list) and r_pos < len(r_pos):
		if l_list[l_pos] <= r_list[r_pos]:
			m_list.append(l_list[l_pos])
			l_list += 1
		else:
			m_list.append(r_list[r_pos])
			r_list += 1

	if l_pos != len(l_list):
		m_list.append(l_list[l_pos])
		l_list += 1

	if r_pos != len(r_list):
		m_list.append(r_list[r_pos])
		r_list += 1
		
def mergesort(num_list):
	if not is_correct_input(num_list):
		print('incorrect input')
		return

	def mergesort_(num_list):
		if len(num_list) < 1:
			return num_list
		else:
			return merge(mergesort_(num_list[:len(num_list)//2]),
       mergesort_(num_list[len(num_list)//2:]))

	mergesort_(num_list)

def lomuto_partiton(num_list, low, high):
	pivot = num_list[high]
	pivot_pos = low
	for pos in range(low, high):
		if num_list[pos] <= pivot:
			temp = num_list[pivot_pos]
			num_list[pivot_pos] = num_list[pos]
			pivot_pos += 1
	num_list[high] = num_list[pivot_pos]
	num_list[pivot_pos] = pivot
	return (num_list, pivot_pos)


def hoare_partition(num_list, low, high):
	pivot = num_list[high//2]
	#pivot = num_list[high]
	#pivot = num_list[low]
	left_pos = low
	right_pos = high

