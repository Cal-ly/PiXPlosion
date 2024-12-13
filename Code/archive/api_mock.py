from datetime import datetime, timedelta

# Mock backend responses
def fetch_drinking_plan(desired_bac, time_period):
    print(f"Fetching drinking plan for BAC {desired_bac} and time {time_period} hours.")
    
    # Current time
    start_time = datetime.now()
    
    # Generate time intervals
    time_intervals = [
        (start_time + timedelta(seconds=30)).strftime("%H:%M:%S"),
        (start_time + timedelta(seconds=90)).strftime("%H:%M:%S"),  # 30s + 1m
        (start_time + timedelta(seconds=180)).strftime("%H:%M:%S"),  # 30s + 1m + 1m30s
    ]
    
    # Mock drinks
    drinks = ["Beer", "Wine", "Whiskey"]
    
    # Mock response
    return {
        "timeIntervals": time_intervals,
        "drinks": drinks
    }

def fetch_current_bac():
    print("Fetching current BAC...")
    # Mock BAC
    return {"currentBAC": round(random.uniform(0.03, 0.1), 2)}

def update_drinking_plan(current_bac):
    print(f"Updating drinking plan based on current BAC {current_bac}...")
    # Mock updated plan
    return {
        "timeIntervals": [
            (datetime.now() + timedelta(seconds=60)).strftime("%H:%M:%S"),  # 1 minute later
            (datetime.now() + timedelta(seconds=120)).strftime("%H:%M:%S"), # 2 minutes later
            (datetime.now() + timedelta(seconds=180)).strftime("%H:%M:%S"), # 3 minutes later
        ],
        "drinks": ["Whiskey", "Beer", "Wine"]
    }
