import os


loop_count = 15

for row in range(loop_count):
    print("TESTING!!!!", row)




files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print(f)