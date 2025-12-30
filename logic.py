import mta_api

green_trains = mta_api.green_trains
yellow_trains = mta_api.yellow_trains
yellow_union_time = 3
green_union_time = 5

yellow = ["r","q","w","n"]
green = ["4","5","6"]
def get_train_times(line, direction):
    train_times = []
    if line in green:
        for train in green_trains:
            counter = 0
            if train["route_id"] == line and train["stop_id"].endswith(direction):
                train_times.append(train[counter]["arrival_time"])
            counter += 1
    elif line in yellow:
        for train in yellow_trains:
            counter = 0
            if train["route_id"] == line and train["stop_id"].endswith(direction):
                train_times.append(train[counter]["arrival_time"])
            counter += 1
    return train_times

print(get_train_times("4","N"))
# input the train line and direction
# iterete through the array and find next time
# if time is less than current time plus commute time, move onto next time
# if time is greater than current time plus commute time, 
#   print that time and when to leave station

