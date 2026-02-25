import random
import time
def get_random_date():
    year = random.randint(2010,2012)
    month= random.randint(1,12)
    day = random.randint(1,28)
    timestamp = int(time.time())
    print("random date:",day,"/",month,"/",year)
    print("timestamp:",timestamp)
get_random_date()