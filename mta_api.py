import requests
from google.transit import gtfs_realtime_pb2

# URL for the subway feed
FEED_URL = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs"

def fetch_realtime_data():
    response = requests.get(FEED_URL)
    
    if response.status_code == 200:
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(response.content)
        return feed
    else:
        print(f"Error: {response.status_code}")
        return None



print(feed.entity[0])

def display_train_updates(feed):
    for entity in feed.entity:
        if entity.HasField("trip_update"):
            trip_update = entity.trip_update
            for stop_time_update in trip_update.stop_time_update:
                if stop_time_update.stop_id.startswith("602"):
                    print(f"Trip ID: {trip_update.trip.trip_id}")
                    print(f"  Stop ID: {stop_time_update.stop_id}")
                    print(f"  Arrival Time: {stop_time_update.arrival.time}")
                    print(f"  Departure Time: {stop_time_update.departure.time}")

if __name__ == "__main__":
    feed = fetch_realtime_data()
    if feed:
        display_train_updates(feed)