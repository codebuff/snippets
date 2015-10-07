import timeit
"""
----setup----
 text = "sample string" # executed once
 char = "g" # executed once
 --- statement -----
 char in text # executed %number% times
 -------
 timeit method takes number argument
 number defaults to 10^6 , statement(char in text) executed number times
"""

# direct function call
timeit.timeit('char in text', setup='text = "sample string"; char = "g"')
timeit.timeit('"g" in "sample string"')

# using Timer class
t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')
run_time = t.timeit(number=100000)
print(str(run_time) + " seconds")

# command line
# -m timeit -s 'text = "sample string"; char = "g"'  'char in text'


# gives inconsistent values

"""import time
start_time = time.time()
print(time.time() - start_time)
print('{:f}'.format(time.time() - start_time))
print("--- %s seconds ---" % (time.time() - start_time))
"""

# print('g' in "sample string")
