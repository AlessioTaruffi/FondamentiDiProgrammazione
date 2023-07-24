import testlib
import random
from ddt import file_data, ddt, data, unpack

# change this variable to True to disable timeout and enable print
DEBUG=True
DEBUG=False

@ddt
class Test(testlib.TestCase):

    def do_test(self, poetry_file, e_prosody, e_module, e_lengths, e_finals):
        """Test implementation
        - poetry_file: the file containing the poem
        - e_prosody : the expected prosody
        - e_module  : the expected module
        - e_lengths : the expected lengths
        - e_finals  : the expected finals
        TIMEOUT: 0.1 seconds for each test
        """
        if DEBUG:
                import program01 as program
                result   = program.ex1(poetry_file)
        else:
            with    self.ignored_function('builtins.print'), \
                    self.ignored_function('pprint.pprint'), \
                    self.forbidden_function('builtins.input'), \
                    self.forbidden_function('builtins.eval'), \
                    self.check_open(allowed_filenames_modes={poetry_file: ['r']}), \
                    self.check_imports(allowed=['program01', '_io', 'encodings.utf_8']), \
                    self.timeout(0.1), \
                    self.timer(0.1):
                import program01 as program
                result   = program.ex1(poetry_file)
        self.assertEqual(type(result),  tuple,
                         "The result should be a tuple / Il risultato prodotto deve essere una tupla")
        self.assertEqual(len(result), 4, 
                        "The result should be a tuple of 4 elements / Il risultato deve essere una tupla di 4 elementi")
        prosody, module, lengths, finals = result
        self.assertEqual(type(prosody),  list,
                         "The first element should be a list of integers / Il primo elemento deve essere una lista di interi")
        self.assertEqual(type(prosody[0]),  int,
                         "The firts element should be a list of integers / Il terzo elemento deve essere una lista di interi")
        self.assertEqual(type(module),   int,
                         "The second element should be an integer / Il secondo elemento deve essere un intero")
        self.assertEqual(type(lengths),  list,
                         "The third element should be a list of integers / Il terzo elemento deve essere una lista di interi")
        self.assertEqual(type(lengths[0]),  int,
                         "The third element should be a list of integers / Il terzo elemento deve essere una lista di interi")
        self.assertEqual(type(finals),   list,
                         "The last element should be a list of strings / L'ultimo elemento deve essere una lista di stringhe")
        self.assertEqual(type(finals[0]),   str,
                         "The last element should be a list of strings / L'ultimo elemento deve essere una lista di stringhe")
        self.assertEqual(prosody,   e_prosody,
                         "The returned prosody is incorrect / La prosodia restituita non e' corretta")
        self.assertEqual(module,    e_module,
                         "The returned module is incorrect / Il modulo restituito non e' corretto")
        self.assertEqual(lengths,   e_lengths,
                         "The returned verse lengths are incorrect / Le lunghezze dei versi restituite non sono corrette")
        self.assertEqual(finals,    e_finals,
                         "The returned verse finals are incorrect / Le finali dei versi restituite non sono corrette")
        return 1

    @file_data("examples.json")
    def test_examples(self, filename, prosody, module, lengths, finals):
        return self.do_test(filename, prosody, module, lengths, finals)

    @file_data("random-10-ita.json")
    def test_random_10(self, filename, prosody, module, lengths, finals):
        return self.do_test(filename, prosody, module, lengths, finals)

    @file_data("random-10-rnd.json")
    def test_random_10(self, filename, prosody, module, lengths, finals):
        return self.do_test(filename, prosody, module, lengths, finals)

    @file_data("random-180-ita.json")
    def test_random_180(self, filename, prosody, module, lengths, finals):
        return self.do_test(filename, prosody, module, lengths, finals)

    @file_data("random-270-eng.json")
    def test_random_270(self, filename, prosody, module, lengths, finals):
        return self.do_test(filename, prosody, module, lengths, finals)

    @file_data("random-558-eng.json")
    def test_random_558(self, filename, prosody, module, lengths, finals):
        return self.do_test(filename, prosody, module, lengths, finals)

    @file_data("random-840-ita.json")
    def test_random_840(self, filename, prosody, module, lengths, finals):
        return self.do_test(filename, prosody, module, lengths, finals)

    @file_data("random-2754-eng.json")
    def test_random_2754(self, filename, prosody, module, lengths, finals):
        return self.do_test(filename, prosody, module, lengths, finals)

    @file_data("random-102-rnd.json")
    def test_random_102(self, filename, prosody, module, lengths, finals):
        return self.do_test(filename, prosody, module, lengths, finals)

    @file_data("random-1024-rnd.json")
    def test_random_1024(self, filename, prosody, module, lengths, finals):
        return self.do_test(filename, prosody, module, lengths, finals)

    @file_data("random-1173-rnd.json")
    def test_random_1173(self, filename, prosody, module, lengths, finals):
        return self.do_test(filename, prosody, module, lengths, finals)

    @file_data("random-2048-rnd.json")
    def test_random_2048(self, filename, prosody, module, lengths, finals):
        return self.do_test(filename, prosody, module, lengths, finals)

    @file_data("random-2592-rnd.json")
    def test_random_2592(self, filename, prosody, module, lengths, finals):
        return self.do_test(filename, prosody, module, lengths, finals)

if __name__ == '__main__':
    Test.main()

