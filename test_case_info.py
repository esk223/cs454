class TestCaseInfo(object):
    def __init__(self, file_name, classification=-1):
        self._file_name = file_name
        self._classification = classification
        self._term_info = {}            # dictionary (ex: {'void': 3, 'test_main': 1, 'msg': 1, 'SOME_STRING': 2})
        self._vector = []               # list or vector (ex: [3, 0, 1, 1, 0, 0, ..., 2, 0])

    def __repr__(self):
        return "{0}({1}) {2}".format(self._file_name, self._classification, self._term_info)

    def get_file_name(self):
        return self._file_name

    def get_term_info(self):
        return self._term_info

    def get_classification(self):
        return self._classification

    def set_classification(self, classification):
        self._classification = classification

    def update_term_info(self, term):
        if term in self._term_info:
            self._term_info[term] += 1
        else:
            self._term_info[term] = 1

    def get_vector(self):
        return self._vector

    def set_vector(self, vector):
        self._vector = vector
