from EmotionDetection.emotion_detection import emotion_detector
import unittest
from io import StringIO
import sys

class TestEmotionDetection(unittest.TestCase):
    ## TEST 1 ##
    def test_emotion_detection1(self):
        captured_output = StringIO() #capture the printed output
        sys.stdout = captured_output 
        emotion_detector("I am glad this happened") #call function that prints output
        output = captured_output.getvalue() #redirect output 
        self.assertIn("'dominant_emotion': 'joy'", output) #Assert expected output
    ## TEST 2 ##
    def test_emotion_detection2(self):        
        captured_output = StringIO() #capture the printed output
        sys.stdout = captured_output 
        emotion_detector("I am really mad about this") #call function that prints output
        output = captured_output.getvalue() #redirect output
        self.assertIn("'dominant_emotion': 'anger'", output) #Assert expected output
    ## TEST 3 ##
    def test_emotion_detection3(self):
        captured_output = StringIO() #capture the printed output
        sys.stdout = captured_output 
        emotion_detector("I feel disgusted just hearing about this") #call function that prints output
        output = captured_output.getvalue() #redirect output
        self.assertIn("'dominant_emotion': 'disgust'", output) #Assert expected output
    ## TEST 4 ##
    def test_emotion_detection4(self):
        captured_output = StringIO() #capture the printed output
        sys.stdout = captured_output 
        emotion_detector("I am so sad about this") #call function that prints output
        output = captured_output.getvalue() #redirect output
        self.assertIn("'dominant_emotion': 'sadness'", output) #Assert expected output
    ## TEST 5 ##    
    def test_emotion_detection5(self):
        captured_output = StringIO() #capture the printed output
        sys.stdout = captured_output
        emotion_detector("I am really afraid that this will happen") #call function that prints output
        output = captured_output.getvalue() #redirect output
        self.assertIn("'dominant_emotion': 'fear'", output) #Assert expected output  

if __name__ == '__main__':
    unittest.main()