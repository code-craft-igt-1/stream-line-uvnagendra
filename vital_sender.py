import random

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

# Example usage
vital_signs = generate_vital_signs()
for vs in vital_signs:
    print(vs)