# Letting python know where to look for the module which we are testing
import sys
sys.path.append(r'C:/Users/devgo/OneDrive/Desktop/Local_Projects/Word-Extractor/lib/')


import unittest
from word_extractor import WordExtractor

# TODO: - Write test for French and Spanish characters

class TestEnglishWords(unittest.TestCase):
    
    def setUp(self) -> None:
        self.word_extractor = WordExtractor()
    
    
    
    
    
    def test_period(self):
        """
        Extract words from a sentence with Period mark.
        """
        sentence = "I got this pouch embossed."
        result = self.word_extractor.extract_words(sentence)
        expected = ['I', 'got', 'this', 'pouch', 'embossed']
        self.assertEqual(result, expected)
 
 
    
    def test_question_mark(self):
        """
        Extract words from a sentence with a Question mark.
        """
        sentence = "How many toy trains does he have?"
        result = self.word_extractor.extract_words(sentence)
        expected = ['How', 'many', 'toy', 'trains', 'does', 'he', 'have']
        self.assertEqual(result, expected)
 
 
    
    def test_exclamation_mark(self):
        """
        Extract words from a sentence with a Exclamation mark.
        """
        sentence = "Wow! You're a good driver."
        result = self.word_extractor.extract_words(sentence)
        expected = ['Wow', 'You\'re', 'a', 'good', 'driver']
        self.assertEqual(result, expected)
    
 
 
    
    def test_comma(self):
        """
        Extract words from a sentence with a Comma.
        """
        sentence = "I like the film, but the color grading is poor."
        result = self.word_extractor.extract_words(sentence)
        expected = ['I', 'like', 'the', 'film', 'but', 'the', 'color', 'grading', 'is', 'poor']
        self.assertEqual(result, expected)
    
 
 
    
    def test_colon(self):
        """
        Extract words from a sentence with a Colon.
        """
        sentence = "Here are some fun ideas for the party: dance-off, board games, scavenger hunt."
        result = self.word_extractor.extract_words(sentence)
        expected = ['Here', 'are', 'some', 'fun', 'ideas', 'for', 'the', 'party', 'dance-off', 'board', 'games', 'scavenger', 'hunt']
        self.assertEqual(result, expected)
    
 
 
    
    def test_semicolon(self):
        """
        Extract words from a sentence with a Semicolon.
        """
        sentence = "I'll visit you once I finish work; that's a promise."
        result = self.word_extractor.extract_words(sentence)
        expected = ['I\'ll', 'visit', 'you', 'once', 'I', 'finish','work', 'that\'s', 'a', 'promise']
        self.assertEqual(result, expected)
    
 
 
    
    def test_hyphen(self):
        """
        Extract words from a sentence with a Hyphen.
        """
        sentence = "I have ninety-nine problems, but chicken tenders can solve all of them."
        result = self.word_extractor.extract_words(sentence)
        expected = ['I', 'have', 'ninety-nine', 'problems', 'but', 'chicken', 'tenders', 'can', 'solve', 'all', 'of', 'them']
        self.assertEqual(result, expected)
    
 
 
    
    def test_en_dash(self):
        """
        Extract words from a sentence with a En dash.
        """
        sentence = "How long is a Tokyo–LA flight?"
        result = self.word_extractor.extract_words(sentence)
        expected = ['How', 'long', 'is', 'a', 'Tokyo–LA', 'flight']
        self.assertEqual(result, expected)
    
 
 
    
    def test_em_dash(self):
        """
        Extract words from a sentence with a Em dash.
        """
        sentence = "The cat—and I'm afraid of four-legged animals—was so adorable."
        result = self.word_extractor.extract_words(sentence)
        expected = ['The', 'cat', 'and', 'I\'m', 'afraid', 'of', 'four-legged', 'animals', 'was', 'so', 'adorable']
        self.assertEqual(result, expected)
    
 
 
    
    def test_parentheses(self):
        """
        Extract words from a sentence with a pair of Parentheses.
        """
        sentence = "His favorite team (Los Angeles Clippers) has a chance to win the title. "
        result = self.word_extractor.extract_words(sentence)
        expected = ['His', 'favorite', 'team', 'Los', 'Angeles', 'Clippers', 'has', 'a', 'chance', 'to', 'win', 'the', 'title']
        self.assertEqual(result, expected)
    
 
 
    
    def test_square_brackets(self):
        """
        Extract words from a sentence with a pair of Square brackets.
        """
        sentence = "The staff writer said the \"[head] of basketball operations was disappointed.\""
        result = self.word_extractor.extract_words(sentence)
        expected = ['The', 'staff', 'writer', 'said', 'the', 'head', 'of', 'basketball', 'operations', 'was', 'disappointed']
        self.assertEqual(result, expected)
    
 
 
    
    def test_curly_brackets(self):
        """
        Extract words from a sentence with a pair of Curly brackets.
        """
        sentence = "The colors {red, green, lilac, red} are for the accent wall."
        result = self.word_extractor.extract_words(sentence)
        expected = ['The', 'colors', 'red', 'green', 'lilac', 'red', 'are', 'for', 'the', 'accent', 'wall']
        self.assertEqual(result, expected)
    
 
 
    
    def test_angle_brackets(self):
        """
        Extract words from a sentence with a pair of Angle brackets.
        """
        sentence = "Angle brackets see more usage in fields such as mathematics or computer programming than they do in writing. In math, for example, a single angle bracket is commonly used to mean that something is “less than” (<) or “greater than” (>) something else."
        result = self.word_extractor.extract_words(sentence)
        expected = ['Angle', 'brackets', 'see', 'more', 'usage', 'in', 'fields', 'such', 'as', 'mathematics', 'or', 'computer', 'programming', 'than', 'they', 'do', 'in', 'writing', 'In', 'math', 'for', 'example', 'a', 'single', 'angle', 'bracket', 'is', 'commonly', 'used', 'to', 'mean', 'that', 'something', 'is', 'less', 'than', 'or', 'greater', 'than', 'something', 'else']
        self.assertEqual(result, expected)
    
 
 
    
    def test_quotation_marks(self):
        """
        Extract words from a sentence with a pair of Quotation marks.
        """
        sentence = "Dylan called it a “splendid affair.”"
        result = self.word_extractor.extract_words(sentence)
        expected = ['Dylan', 'called', 'it', 'a', 'splendid', 'affair']
        self.assertEqual(result, expected)
    
 
 
    
    def test_apostrophe(self):
        """
        Extract words from a sentence with a Apostrophe.
        """
        sentence = "Some of Jerry’s gadgets are missing."
        result = self.word_extractor.extract_words(sentence)
        expected = ['Some', 'of', 'Jerry’s', 'gadgets', 'are', 'missing']
        self.assertEqual(result, expected)
    
 
 
    
    def test_slash_or_virgule(self):
        """
        Extract words from a sentence with a Slash or Virgule.
        """
        sentence = "I’m getting a lipstick/phone case/necklace for her birthday."
        result = self.word_extractor.extract_words(sentence)
        expected = ['I’m', 'getting', 'a', 'lipstick', 'phone', 'case', 'necklace', 'for', 'her', 'birthday']
        self.assertEqual(result, expected)
    
 
 
    
    def test_ellipses(self):
        """
        Extract words from a sentence with a Ellipses.
        """
        sentence = "According to the staff writer, the “president… was disappointed.”"
        result = self.word_extractor.extract_words(sentence)
        expected = ['According', 'to', 'the', 'staff', 'writer', 'the', 'president', 'was', 'disappointed']
        self.assertEqual(result, expected)
    
 
 
    
    def test_asterisk(self):
        """
        Extract words from a sentence with a Asterisk.
        """
        sentence = "*Data from The Journal of Acting Ethics."
        result = self.word_extractor.extract_words(sentence)
        expected = ['Data', 'from', 'The', 'Journal', 'of', 'Acting', 'Ethics']
        self.assertEqual(result, expected)
    
 
 
    
    def test_ampersand(self):
        """
        Extract words from a sentence with a Ampersand.
        """
        sentence = "Tiffany & Co."
        result = self.word_extractor.extract_words(sentence)
        expected = ['Tiffany', 'Co']
        self.assertEqual(result, expected)
    
 
 
    
    def test_pound_symbol(self):
        """
        Extract words from a sentence with a Pound symbol.
        """
        sentence = "#1 Bestselling."
        result = self.word_extractor.extract_words(sentence)
        expected = ['Bestselling']
        self.assertEqual(result, expected)
    
    
 
 
    
    def test_tilde(self):
        """
        Extract words from a sentence with a Tilde.
        """
        sentence = "I think Govine owns ~10 pairs of shoes."
        result = self.word_extractor.extract_words(sentence)
        expected = ['I', 'think', 'Govine', 'owns', 'pairs', 'of', 'shoes']
        self.assertEqual(result, expected)
    
    
 
 
    
    def test_backslash(self):
        """
        Extract words from a sentence with a Backslash.
        """
        sentence = "In Python strings, the backslash \\ is a special character, also called the 'escape' character. "
        result = self.word_extractor.extract_words(sentence)
        expected = ['In', 'Python', 'strings', 'the', 'backslash', 'is', 'a', 'special', 'character', 'also', 'called', 'the', '\'escape\'', 'character']
        self.assertEqual(result, expected)
    
    
 
 
    
    def test_at_symbol(self):
        """
        Extract words from a sentence with a At symbol.
        """
        sentence = "Report bugs to devgovine.apps@gmail.com"
        result = self.word_extractor.extract_words(sentence)
        expected = ['Report', 'bugs', 'to', 'devgovine', 'apps', 'gmail', 'com']
        self.assertEqual(result, expected)
    
    
 
 
    
    def test_pipe_symbol(self):
        """
        Extract words from a sentence with a Pipe symbol.
        """
        sentence = "A pipe symbol is a typographical mark that resembles a vertical line ( | )."
        result = self.word_extractor.extract_words(sentence)
        expected = ['A', 'pipe', 'symbol', 'is', 'a', 'typographical', 'mark', 'that', 'resembles', 'a', 'vertical', 'line']
        self.assertEqual(result, expected)
    




if __name__ == '__main__':
    unittest.main()