#
#
# 

# 
    
# asks for how far you need to go and how fast you will be going roughly
# responds with the estimated time to get there
# estimate traffic based on time of day asking the user what time and day it is,
# if its a friday is going to be longer than a 2am on a tuesday because of traffic
# prints the response in days, hours, minutes format

def travel_time():
    print("Welcome to the Travel Time Estimator!")
    distance = float(input("Enter the distance you need to travel (in miles): "))
    speed = float(input("Enter your estimated average speed (in miles per hour): "))
    estimated_time = distance / speed
    time_of_day = input("What time of day will you be traveling? (morning/afternoon/evening/night): ").strip("!.,;:?/']").lower()
    day_of_week = input("What day of the week will you be traveling? (weekday/weekend): ").strip("!.,;:?/']").lower()

    traffic_delay = 0
    if time_of_day in ["morning", "evening"] and day_of_week == "weekday":
        traffic_delay = 0.5 
    elif time_of_day == "afternoon" and day_of_week == "weekday":
        traffic_delay = 0.25 
    elif day_of_week == "weekend":
        traffic_delay = 0.1  

    total_time = estimated_time + traffic_delay

    if speed <= 0:
        print("Speed must be greater than zero.")
        return
    
    days = int(total_time // 24)
    hours = int(total_time % 24)
    minutes = int((total_time * 60) % 60)

    print(f"Estimated travel time: {days} days, {hours} hours, and {minutes} minutes.")

travel_time()
