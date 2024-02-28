import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Example: Retrieve data stored with a specific key
key = "specific.cce61af69c9b465181649d3d5dc03f12!dc4c38bb3bfb47e3a24ccad2e689eb2c"
data = redis_client.get(key)

# Example: Decode and display the retrieved data
if data:
    decoded_data = data.decode('utf-8')  # Assuming the data is encoded as UTF-8
    print("Data stored with key '{}':".format(key))
    print(decoded_data)
else:
    print("No data found for key '{}'.".format(key))