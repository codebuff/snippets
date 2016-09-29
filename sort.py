def is_correct_input(num_list):
    return len(num_list) != 0 and ''.join(map(str, num_list)).isnumeric()


def generate_random_num_list(length):
    import random
    num_list = []
    i = 0
    while i < length:
        num_list.append(random.randrange(2 * length))
        i += 1
    print('input ', num_list)
    return num_list


def validate_output(num_list):
    for pos in range(1, len(num_list)):
        if num_list[pos - 1] > num_list[pos]:
            return False
    return True


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
                num_list[pos - 1] = num_list[pos]
                num_list[pos] = temp
                swap_count += 1
    return num_list


def selectionsort(num_list):
    if not is_correct_input(num_list):
        print('incorrect input')
        return

    for pos in range(len(num_list)):
        min_pos = pos
        for pos_ in range(pos + 1, len(num_list)):
            if num_list[pos_] < num_list[min_pos]:
                min_pos = pos_
        temp = num_list[pos]
        num_list[pos] = num_list[min_pos]
        num_list[min_pos] = temp

    return num_list


def insertionsort(num_list):
    if not is_correct_input(num_list):
        print('incorrect input')
        return

    for pos in range(1, len(num_list)):
        to_be_inserted = num_list[pos]
        for pos_ in range(pos):
            if num_list[pos_] > num_list[pos]:
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

    return num_list


def merge(l_list, r_list):
    m_list = []
    l_pos = 0
    r_pos = 0
    while l_pos < len(l_list) and r_pos < len(r_list):
        if l_list[l_pos] <= r_list[r_pos]:
            m_list.append(l_list[l_pos])
            l_pos += 1
        else:
            m_list.append(r_list[r_pos])
            r_pos += 1

    while l_pos != len(l_list):
        m_list.append(l_list[l_pos])
        l_pos += 1

    while r_pos != len(r_list):
        m_list.append(r_list[r_pos])
        r_pos += 1

    return m_list


def mergesort(num_list):
    if not is_correct_input(num_list):
        print('incorrect input')
        return

    def mergesort_(num_list):
        if len(num_list) <= 1:
            return num_list
        else:
            return merge(mergesort_(num_list[:len(num_list) // 2]),
                         mergesort_(num_list[len(num_list) // 2:]))

    return mergesort_(num_list)


def lomuto_partition(num_list, low, high):
    pivot = num_list[high]
    pivot_pos = low
    for pos in range(low, high):
        if num_list[pos] <= pivot:
            temp = num_list[pivot_pos]
            num_list[pivot_pos] = num_list[pos]
            num_list[pos] = temp
            pivot_pos += 1
    num_list[high] = num_list[pivot_pos]
    num_list[pivot_pos] = pivot
    return pivot_pos


def hoare_partition(num_list, low, high):
    pivot = num_list[high]
    left_pos = low
    right_pos = high - 1

    while True:
        while num_list[left_pos] <= pivot and left_pos <= right_pos:
            left_pos += 1
        while num_list[right_pos] >= pivot and left_pos <= right_pos:
            right_pos -= 1

        if left_pos > right_pos:
            break

        temp = num_list[left_pos]
        num_list[left_pos] = num_list[right_pos]
        num_list[right_pos] = temp

    num_list[high] = num_list[left_pos]
    num_list[left_pos] = pivot
    return left_pos


# in place sorting (pass by value reference)
def quicksort(num_list):
    if not is_correct_input(num_list):
        print('incorrect input')
        return

    def quicksort_helper(num_list, low, high):
        if low >= high:
            return

        split_point = hoare_partition(num_list, low, high)
        quicksort_helper(num_list, low, split_point - 1)
        quicksort_helper(num_list, split_point + 1, high)

    quicksort_helper(num_list, 0, len(num_list) - 1)

    return num_list


if __name__ == '__main__':
    length = 5
    print('\n\tbubblesort')
    num_list = generate_random_num_list(length)
    output = bubblesort(num_list)
    print('output', output)
    print(validate_output(output))

    print('\n\tselectionsort')
    num_list = generate_random_num_list(length)
    output = selectionsort(num_list)
    print('output', output)
    print(validate_output(output))

    print('\n\tinsertionsort')
    num_list = generate_random_num_list(length)
    output = insertionsort(num_list)
    print('output', output)
    print(validate_output(output))

    print('\n\tshellsort')
    num_list = generate_random_num_list(length)
    output = shellsort(num_list)
    print('output', output)
    print(validate_output(output))

    print('\n\tmergesort')
    num_list = generate_random_num_list(length)
    output = mergesort(num_list)
    print('output', output)
    print(validate_output(output))

    print('\n\tquicksort')
    num_list = generate_random_num_list(length)
    output = quicksort(num_list)
    print('output', output)
    print(validate_output(output))
