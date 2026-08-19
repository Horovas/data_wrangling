import json

filename = "data.json"

events_list = []
events_set = {}
timer_tick_list = []
timer_tick_set = {}
driver_list = []
driver_set = {}


with open(filename, encoding="utf-8") as file:
	dictionary = json.load(file)

for data_point in dictionary["data_points"]:
    events_list.append(data_point["id"])

events_set = set(events_list)


for timer_tick in dictionary["timer_ticks"]:
    timer_tick_list.append(timer_tick["id"])

timer_tick_set = set(timer_tick_list)


for driver in dictionary["drivers"]:
    driver_list.append(driver["id"])

organizer_set = set(organizer_list)

print(f"Events_list count: {len(events_list)}")
print(f"Events_set count: {len(events_set)}")
print()
print(f"timer_tick_list: {len(timer_tick_list)}")
print(f"timer_tick_set count: {len(timer_tick_set)}")
print()
print(f"driver_list count: {len(driver_list)}")
print(f"driver_set count: {len(driver_set)}")
print("--------------------------------")

unique_id_list = []

for driver in dictionary["drivers"]:
    unique_id_list.append(driver["unique_id"])

unique_id_set = set(unique_id_list)
print(f"unique_id_list: {len(unique_id_list)}")
print(f"unique_id_set: {len(unique_id_set)}")

for unique_id in unique_id_list:
    if len(unique_id) < 10:
        print(f"< 10 unique_id {unique_id}")
    elif len(unique_id) == 10:
        print(f"== 10 unique_id {unique_id}")
    elif len(unique_id) == 11:
        print(f"== 11 unique_id {unique_id}")
    elif len(unique_id) == 12:
        print(f"== 12 unique_id {unique_id}")
    elif len(unique_id) > 12:
        print(f"> 12 unique_id {unique_id}")
    else:
        print(f"some crazy-ass case unique_id {unique_id}")
