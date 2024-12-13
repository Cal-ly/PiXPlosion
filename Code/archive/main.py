from api_mock import fetch_drinking_plan, fetch_current_bac, update_drinking_plan
from sensor_mock import get_mock_sensor_bac
from sensehat_display import display_drinking_plan
from notifications import trigger_notifications

def main():
    print("Starting Promille Partner...")
    
    # Mock user input
    desired_bac = 0.08
    time_period = 4

    # Fetch and display drinking plan
    plan = fetch_drinking_plan(desired_bac, time_period)
    display_drinking_plan(plan)

    # Simulate notifications
    trigger_notifications(plan)

    # Mock sensor and backend integration
    current_bac = get_mock_sensor_bac()
    print(f"Simulated BAC: {current_bac}")
    
    updated_plan = update_drinking_plan(current_bac)
    print("Updated Plan:", updated_plan)
    display_drinking_plan(updated_plan)

if __name__ == "__main__":
    main()
