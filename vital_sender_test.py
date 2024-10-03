from vital_sender import VitalSignsGenerator
import unittest

class TestGenerateVitalSigns(unittest.TestCase):
    """
    Unit tests for the generate_vital_signs function.
    
    This class contains tests to ensure that the generate_vital_signs function
    generates the correct number of sets and that each set contains valid values
    within the specified ranges.
    """
    
    def test_generate_vital_signs_length(self):
        """
        Test that the generate_vital_signs function generates exactly 50 sets of vital signs.
        """
        vital_signs = VitalSignsGenerator.generate_vital_signs()
        self.assertEqual(len(vital_signs), 50, "Should generate 50 sets of vital signs")
    
    def test_generate_vital_signs_values(self):
        """
        Test that each set of vital signs contains valid values within the specified ranges.
        
        The ranges are:
        - Temperature: 36.0 to 37.5 degrees Celsius
        - SpO2: 95 to 100 percent
        - Pulse rate: 60 to 100 beats per minute
        """
        vital_signs = VitalSignsGenerator.generate_vital_signs()
        for vs in vital_signs:
            temperature, spo2, pulse_rate = map(float, vs.split('|'))
            self.assertTrue(36.0 <= temperature <= 37.5, "Temperature out of range")
            self.assertTrue(95 <= spo2 <= 100, "SpO2 out of range")
            self.assertTrue(60 <= pulse_rate <= 100, "Pulse rate out of range")

if __name__ == '__main__':
    unittest.main()