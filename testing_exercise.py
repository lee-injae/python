import unittest
import testing_exercise_script 

class TestGuessGame(unittest.TestCase):
    def test_input(self):
        answer = 5 
        guess = 5
        result = testing_exercise_script.guess_game(answer, guess)
        self.assertTrue(result)
    
    def test_input_wrong_guess(self):
        result = testing_exercise_script.guess_game(5, 0)
        self.assertFalse(result)
    
    def test_input_wrong_number(self):
        result = testing_exercise_script.guess_game(5, 11)
        self.assertFalse(result)
    
    def test_input_wrong_type(self):
        result = testing_exercise_script.guess_game(5, '11')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()


