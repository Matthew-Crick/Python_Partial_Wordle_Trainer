import unittest
import partial_wordle_trainer


class MyTestCase(unittest.TestCase):

    def test_one(self):
        #  example 01
        test_wordlist_1 = ['limes', 'spare', 'store', 'loser', 'aster', 'pares',
                           'taser', 'pears', 'stare', 'spear', 'parse', 'reaps', 'rates',
                           'tears', 'losts']
        test_word_1 = 'pares'
        test_marker_1 = [0, 0, 0, 0, 1]

        self.assertEqual(partial_wordle_trainer.trainer(test_wordlist_1, test_word_1, test_marker_1), ['reaps'])

    def test_two(self):
        #  example 02
        test_wordlist_2 = ['limes', 'spare', 'store', 'loser', 'aster', 'pares',
                           'taser', 'pears', 'stare', 'spear', 'parse', 'reaps', 'rates',
                           'tears', 'losts']
        test_word_2 = 'pares'
        test_marker_2 = [1, 0, 0, 0, 1]
        self.assertEqual(partial_wordle_trainer.trainer(test_wordlist_2, test_word_2, test_marker_2), ['pears'])

    def test_three(self):
        #  example 03
        test_wordlist_3 = ['limes', 'spare', 'store', 'loser', 'aster', 'pares',
                           'taser', 'pears', 'stare', 'spear', 'parse', 'reaps', 'rates',
                           'tears', 'losts']
        test_word_3 = 'pares'
        test_marker_3 = [0, 0, 0, 0, 0]
        self.assertEqual(partial_wordle_trainer.trainer(test_wordlist_3, test_word_3, test_marker_3),
                         ['spare', 'spear'])

    def test_four(self):
        #  example 04
        test_wordlist_4 = ['limes', 'spare', 'store', 'loser', 'aster', 'pares',
                           'taser', 'pears', 'stare', 'spear', 'parse', 'reaps', 'rates',
                           'tears', 'losts']
        test_word_4 = 'spare'
        test_marker_4 = [1, 1, 0, 0, 1]
        self.assertEqual(partial_wordle_trainer.trainer(test_wordlist_4, test_word_4, test_marker_4), [])

    def test_five(self):
        #  example 05
        test_wordlist_5 = ['limes', 'spare', 'store', 'loser', 'aster', 'pares',
                           'taser', 'pears', 'stare', 'spear', 'parse', 'reaps', 'rates',
                           'tears', 'losts']
        test_word_5 = 'sprae'
        test_marker_5 = [1, 1, 0, 0, 1]
        self.assertEqual(partial_wordle_trainer.trainer(test_wordlist_5, test_word_5, test_marker_5), ['spare'])

    def test_six(self):
        #  example 06
        test_wordlist_6 = ['limes', 'spare', 'store', 'loser', 'aster', 'pares',
                           'taser', 'pears', 'stare', 'spear', 'parse', 'reaps', 'rates',
                           'tears', 'losts']
        test_word_6 = ['spare']
        test_marker_6 = [1, 1, 1, 1, 1]
        self.assertEqual(partial_wordle_trainer.trainer(test_wordlist_6, test_word_6, test_marker_6), ['spare'])

    def test_seven(self):
        test_wordlist_7 = ['costar', 'carets', 'recast', 'traces', 'reacts',
                           'caster', 'caters', 'crates', 'actors', 'castor']
        test_word_7 = 'catrse'
        test_marker_7 = [1, 1, 0, 0, 0, 0]
        self.assertEqual(partial_wordle_trainer.trainer(test_wordlist_7, test_word_7, test_marker_7),
                         ['carets', 'caster'])


if __name__ == '__main__':
    unittest.main()
