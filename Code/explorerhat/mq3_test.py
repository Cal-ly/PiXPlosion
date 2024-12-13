import explorerhat as eh
import time

# Calibration constants (update with actual calibration data)
VOLTAGE_TO_BRAC_MULTIPLIER = 50  # Placeholder multiplier
BASELINE_VOLTAGE = 0.26          # Sensor baseline voltage in clean air (adjust as needed)

def calibrate_voltage_to_brac(voltage):
    """
    Convert voltage to Breath Alcohol Concentration (BrAC) in mg/L.
    Adjusts for baseline voltage.
    """
    adjusted_voltage = max(voltage - BASELINE_VOLTAGE, 0)  # Remove baseline
    brac = adjusted_voltage * VOLTAGE_TO_BRAC_MULTIPLIER
    return brac

def voltage_to_bac(brac):
    """
    Convert Breath Alcohol Concentration (BrAC) in mg/L to BAC (‰ promille).
    """
    bac = (brac * 2100 / 1e6) * 10  # Convert to promille (‰)
    return bac

def analog_to_voltage(analog_value):
    """
    Convert analog value to voltage (5V reference).
    """
    return (analog_value * 5.0) / 1023

def read_sensor():
    """
    Continuously read from the MQ3 sensor, calculate BrAC and BAC, and display results.
    """
    try:
        while True:
            # Read analog value from ADC0 (connected to MQ3 OUT)
            analog_value = eh.analog.one.read()
            voltage = analog_to_voltage(analog_value)
            brac = calibrate_voltage_to_brac(voltage)
            bac = voltage_to_bac(brac)
            print(f"Analog Value: {analog_value:.6f} | BrAC: {brac:.2f} mg/L | Estimated BAC: {bac:.4f} ‰ promille")
            time.sleep(2)
    except KeyboardInterrupt:
        print("Exiting.")

if __name__ == "__main__":
    read_sensor()
