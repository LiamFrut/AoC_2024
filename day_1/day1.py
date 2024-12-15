import csv
from pathlib import Path
location_IDs_1 = []
location_IDs_2 = []
dir = Path(__file__).parent
with open(dir / 'input_list.csv', 'r') as f:
    reader = csv.reader(f)
    for location_1, location_2 in reader:
        location_IDs_1.append(int(location_1))
        location_IDs_2.append(int(location_2))

location_IDs_1.sort()
location_IDs_2.sort()

total_distance = 0
similarity_score = 0
if len(location_IDs_1) == len(location_IDs_2):
    for i in range(len(location_IDs_1)):
        curr_val = location_IDs_1[i]
        total_distance += abs(curr_val - location_IDs_2[i])
        similarity_score += (curr_val * location_IDs_2.count(curr_val))

else:
    raise("Error: Lists lengths are not the same.")

print(total_distance)
print(similarity_score)
