import random
from collections import deque

class VitalSignsGenerator:
    """
    A class to generate and print sets of random vital signs including temperature, SpO2, and pulse rate.
    """

    @staticmethod
    def generate_vital_signs():
        """
        Generates 50 sets of random vital signs including temperature, SpO2, and pulse rate.

        Each set of vital signs is represented as a string in the format "temperature|spo2|pulse_rate".
        The ranges for the random values are:
        - Temperature: 36.0 to 37.5 degrees Celsius
        - SpO2: 95 to 100 percent
        - Pulse rate: 60 to 100 beats per minute

        Returns:
            list: A list of 50 strings, each representing a set of vital signs.
        """
        vital_signs = []
        for _ in range(50):
            temperature = round(random.uniform(36.0, 37.5), 1)
            spo2 = random.randint(95, 100)
            pulse_rate = random.randint(60, 100)
            vital_signs.append(f"{temperature}|{spo2}|{pulse_rate}")
        return vital_signs

    @staticmethod
    def print_vital_range_on_console():
        """
        Generates and prints 50 sets of random vital signs to the console.
        """
        vital_signs = VitalSignsGenerator.generate_vital_signs()
        print("\ntemperature|spo2|pulse_rate")
        for vs in vital_signs:
            print(vs)
        return vital_signs
    
    @staticmethod
    def process_vital_signs_from_generated_data(vital_signs):
        """
        Processes the given vital sign data to compute:
        - Maximum and minimum values in the incoming stream for temperature, SpO2, and pulse rate.
        - Simple moving average of the last 5 values for each vital sign.

        Args:
            vital_signs (list): A list of vital sign strings in the format "temperature|spo2|pulse_rate".
        """
        temperatures = deque(maxlen=5)
        spo2_values = deque(maxlen=5)
        pulse_rates = deque(maxlen=5)

        max_temp = min_temp = None
        max_spo2 = min_spo2 = None
        max_pulse = min_pulse = None

        print("\nProcessing vital signs data...")

        for vital_sign in vital_signs:
            try:
                temperature, spo2, pulse_rate = map(float, vital_sign.split('|'))
            except ValueError:
                print(f"Invalid data format: {vital_sign}")
                continue

            # Update deque
            temperatures.append(temperature)
            spo2_values.append(spo2)
            pulse_rates.append(pulse_rate)

            # Calculate min/max
            if max_temp is None or temperature > max_temp:
                max_temp = temperature
            if min_temp is None or temperature < min_temp:
                min_temp = temperature

            if max_spo2 is None or spo2 > max_spo2:
                max_spo2 = spo2
            if min_spo2 is None or spo2 < min_spo2:
                min_spo2 = spo2

            if max_pulse is None or pulse_rate > max_pulse:
                max_pulse = pulse_rate
            if min_pulse is None or pulse_rate < min_pulse:
                min_pulse = pulse_rate

            # Calculate simple moving averages
            sma_temp = sum(temperatures) / len(temperatures)
            sma_spo2 = sum(spo2_values) / len(spo2_values)
            sma_pulse = sum(pulse_rates) / len(pulse_rates)

            # Print results
            print(f"Max temperature: {max_temp}, Min temperature: {min_temp}")
            print(f"Max SpO2: {max_spo2}, Min SpO2: {min_spo2}")
            print(f"Max pulse rate: {max_pulse}, Min pulse rate: {min_pulse}")
            print(f"SMA of last 5 temperatures: {sma_temp:.2f}")
            print(f"SMA of last 5 SpO2 values: {sma_spo2:.2f}")
            print(f"SMA of last 5 pulse rates: {sma_pulse:.2f}")

if __name__ == '__main__':
    print("Process generated vital signs...")
    vital_signs_data = VitalSignsGenerator.print_vital_range_on_console()
    VitalSignsGenerator.process_vital_signs_from_generated_data(vital_signs_data)
    