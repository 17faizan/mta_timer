import requests
from google.transit import gtfs_realtime_pb2
import time
from datetime import datetime
from zoneinfo import ZoneInfo

green_line_url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs"
yellow_line_url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw"

def format_time(ts):
    return datetime.fromtimestamp(
        ts,
        tz=ZoneInfo("America/New_York")
    ).strftime("%I:%M %p")

def fetch_realtime_data():
    response = requests.get(green_line_url)
    
    if response.status_code == 200:
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(response.content)
        return feed
    else:
        print(f"Error: {response.status_code}")
        return None
    
green_trains = []
yellow_trains = []
green_line_prefix = "635"
yellow_line_prefix = "R20"

def display_train_updates(feed):
    for entity in feed.entity:
        if entity.HasField("trip_update"):
            trip_update = entity.trip_update
            for stop_time_update in trip_update.stop_time_update:   
                if stop_time_update.stop_id.startswith(green_line_prefix):
                    green_trains.append({
                        "trip_id": trip_update.trip.trip_id,
                        "route_id": trip_update.trip.route_id,
                        "stop_id": stop_time_update.stop_id,
                        "arrival_time": format_time(int(stop_time_update.arrival.time)),
                        "departure_time": format_time(int(stop_time_update.departure.time))
                    })
                    # print(f"Trip ID: {trip_update.trip.trip_id}")
                    # print(f"  Route ID: {trip_update.trip.route_id}")
                    # print(f"  Stop ID: {stop_time_update.stop_id}")
                    # print(f"  Arrival Time: {format_time(int(stop_time_update.arrival.time))}")
                    # print(f"  Departure Time: {format_time(int(stop_time_update.departure.time))}")
                if stop_time_update.stop_id.startswith(yellow_line_prefix):
                    yellow_trains.append({
                        "trip_id": trip_update.trip.trip_id,
                        "route_id": trip_update.trip.route_id,
                        "stop_id": stop_time_update.stop_id,
                        "arrival_time": stop_time_update.arrival.time,
                        "departure_time": stop_time_update.departure.time
                    })    
                    
                    
if __name__ == "__main__":
    feed = fetch_realtime_data()
    if feed:
        display_train_updates(feed)
print()
print(green_trains)
