import subprocess

def parse_vitals(output):
    """
    Parses the vitals from the executable output.
    """
    vitals = output.split(':')[2].split('[')[0].split(',')
    vital_list = []
    for vital in vitals:
        values = vital.split()
        if len(values) >= 3:
            temperature, spo2, pulse_rate = values[:3]
            vital_list.append((float(temperature), float(spo2), float(pulse_rate)))
    return vital_list

def calculate_moving_average(vitals, window_size=5):
    """
    Calculates the simple moving average for the last `window_size` entries.
    """
    if len(vitals) < window_size:
        return None, None, None

    last_vitals = vitals[-window_size:]
    temperatures = [v[0] for v in last_vitals]
    spo2s = [v[1] for v in last_vitals]
    pulse_rates = [v[2] for v in last_vitals]

    avg_temperature = sum(temperatures) / window_size
    avg_spo2 = sum(spo2s) / window_size
    avg_pulse_rate = sum(pulse_rates) / window_size

    return avg_temperature, avg_spo2, avg_pulse_rate

def run_sender_exe():
    """
    Runs the sender.exe executable and captures its output.
    """
    try:
        result = subprocess.run(
            [r'Sasikala_Sender\sender.exe'],
            capture_output=True, text=True, check=True
        )

        # Print the entire output from the executable
        print("Executable Output:")
        vitals = parse_vitals(result.stdout)
        for temperature, spo2, pulse_rate in vitals:
            print(f"Temperature: {temperature}, SpO2: {spo2}, Pulse Rate: {pulse_rate}")

        # Calculate and print moving averages
        avg_temperature, avg_spo2, avg_pulse_rate = calculate_moving_average(vitals)
        if avg_temperature is not None:
            print(f"Average Temperature: {avg_temperature:.2f}")
            print(f"Average SpO2: {avg_spo2:.2f}")
            print(f"Average Pulse Rate: {avg_pulse_rate:.2f}")

        # Print any errors
        if result.stderr:
            print("Errors:")
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running sender.exe: {e}")

if __name__ == '__main__':
    run_sender_exe()