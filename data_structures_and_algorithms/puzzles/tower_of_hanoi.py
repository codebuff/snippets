
def move_disk(disk_num, from_pole, to_pole):
    print('move disk no', disk_num, 'from', from_pole, 'to', to_pole)

def toh(height, start_pole, intermediate_pole, end_pole):
    if height >= 1:
        toh(height-1, start_pole, end_pole, intermediate_pole)
        move_disk(height, start_pole, end_pole)
        toh(height-1, intermediate_pole, start_pole, end_pole)
        
toh(int(input('enter no of disks ')), 'A', 'B', 'C')

"""
for iterative solution
start by taking height into consideration ie 
if odd
        move least_numbered disk to end_pole
if even
        move least_numbered disk to intermeidate_node

After that direction plays important part
if started with even > right
 a - c > a - b > c - b
if started with odd > left
 a - b > a - c > b - c

optimal number of steps = 2^height - 1
"""

