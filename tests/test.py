
from src.algo import invert, strMatch, makeQuestion, selectWord
import json

class Testing:
    def test_invert(self):
        assert '' == invert('')
        assert '1' == invert('1')
        assert '1234567890' == invert('0987654321')

    def test_strMatch(self):
        assert strMatch('', '')
        assert strMatch(' ', ' ')
        assert not strMatch('Hello', 'World')
        assert strMatch('HellO', 'hello')

    def test_makeQuestion(self):
        assert ' '.join(['1', '2', '3']) == makeQuestion(['1','2','3'])

    def test_selectWord(self):
        words_ordered_by_len = None

        with open('data.json', 'r') as file:
            words_ordered_by_len = json.load(file)
        
        assert selectWord(5) in words_ordered_by_len['5']



if __name__ == "__main__":
    entity = Testing()
    entity.test_invert()
    entity.test_makeQuestion()
    entity.test_selectWord()
    entity.test_strMatch()
    print('Tests passed!')