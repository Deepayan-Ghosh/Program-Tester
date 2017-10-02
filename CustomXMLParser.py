from __future__ import print_function
import xml.etree.ElementTree as ET
import random, string


class CustomXMLParser:
    def __init__(self, xmlFileName):
        self.tree = None
        self.root = None
        self.xmlFileName = xmlFileName
        self.testcase_string = None
        self.variable_names = None
        self.lower_letters = string.ascii_lowercase
        self.upper_letters = string.ascii_uppercase
        self.letters = string.ascii_letters
        self.initialise()

    def initialise(self):
        # the XML file is parsed and the root is initialised
        # variable_names is a dictionary which stores named variables from XML for future reference
        try:
            self.tree = ET.parse(self.xmlFileName)
            self.root = self.tree.getroot()
            self.variable_names = {}
            self.testcase_string = ''
        except Exception as e:
            print(e)

    def gen_test_cases(self):
        # the immediate children of root are obtained and parsed
        direct_children = list(self.root)
        self.create_test_case(direct_children)

    def create_test_case(self, remaining_children):
        # the list of children is iterated and each child is checked
        # if the child is a testcase tag, then the following tags are to be repeated for all the testcases
        # all tags are handled seperately
        for child in remaining_children:
            if child.tag == 'testcases':
                self.handle_test_case_tag(child, remaining_children)
                break
            elif child.tag == 'line':
                self.handle_line_tag(child, list(child))
            elif child.tag == 'element':
                self.handle_element_tag(child)
            elif child.tag == 'elements':
                self.handle_elements_tag(child)

    def handle_test_case_tag(self, child, children):
        # lower limit of testcases is assumed to be 1
        # since the program must run once and calculate random number
        test_cases_upper_bound = child.attrib.get('max', 1)
        test_cases_lower_bound = child.attrib.get('min', 1)
        random_number_of_test_cases = random.randint(
            int(test_cases_lower_bound), int(test_cases_upper_bound)
        );
        print(random_number_of_test_cases)
        # add the test case number to the string
        self.testcase_string += str(random_number_of_test_cases) + '\n'

        # iterate to produce individual test cases

        for _ in range(random_number_of_test_cases):
            # print('In testcase:')
            self.create_test_case(children[children.index(child) + 1:])

    def handle_line_tag(self, child, children):

        # if the testcase_string is not empty and the last character is not newline then add a newline
        # this newline marks the beginning of  a new line
        if self.testcase_string != '' and self.testcase_string[-1] != '\n':
            self.testcase_string += '\n'

        # produce the contents of the line
        # a line can have only element tags, not elements tag
        for child in children:
            tag_name = child.tag
            if tag_name == 'testcases':
                self.handle_test_case_tag(child, children)
            elif tag_name == 'element':
                self.handle_element_tag(child)

        # add ending newline
        self.testcase_string += '\n'

    def handle_element_tag(self, child):
        # determine type of element, real, floating or string(uppercase, lowercase, mixed)
        content_type = child.attrib.get('type')

        # determine the maximum(element_upper_bound) and minimum(element_lower_bound) allowed values of the element
        element_upper_bound = child.attrib.get('max', 1)
        element_lower_bound = child.attrib.get('min', 1)

        # obtain the random element
        value = self.handle_content(
            element_lower_bound, element_upper_bound, content_type
        )
        print(value)
        # determine if there is name of the element or not, if it is there, add to dictionary for later reference
        var_name = child.attrib.get('name')
        if var_name:
            self.variable_names[var_name] = value
        self.testcase_string += value + ' '

    def handle_elements_tag(self, child):
        # elements tag represent a matrix of values of a particular type
        # the number of rows is given by 'repeat'
        # the number of columns is given by 'len' (fixed length) or 'maxlen' (determined random number)
        repeat = child.attrib.get('repeat', 1)

        # if the number of elements in line is obtained from another named element, then obtain value
        if repeat in self.variable_names:
            repeat = self.variable_names[repeat]

        # a loop runs 'repeat' times and generates individual element of a particular type
        for _ in range(int(repeat)):
            x = []

            # determine type and max(element_upper_bound) and min(element_lower_bound) allowed value of each element in matrix
            content_type = child.attrib.get('type')
            element_upper_bound = int(child.attrib.get('max', 1))
            element_lower_bound = int(child.attrib.get('min', 1))

            # determine how many elements will be there in one line
            # if 'len' is mentioned then the length is fixed
            # else if 'maxlen' is mentioned then random length is chosen every time
            length = child.attrib.get('len', None)
            if length is None:
                length = child.attrib.get('maxlen', 1)
                length = random.randint(1, int(length))
            elif length in self.variable_names:
                length = self.variable_names.get(length, length)

            length = int(length)

            # produce a list of elements, integers, floats, or strings(upper,lower or mixed case)
            # for numbers, a number is chosen between the min(element_lower_bound) and max(element_upper_bound)
            # for strings, max and min serve as max and min allowed length of each string in a row, and
            # a random length is selected between element_upper_bound and element_lower_bound
            if content_type == 'real':
                x = [random.randint(int(element_lower_bound), int(element_upper_bound)) for _ in range(length)]
            elif content_type == 'float':
                x = [random.uniform(int(element_lower_bound), int(element_upper_bound)) for _ in range(length)]

            elif content_type == 'string_u':
                str_length = random.randint(int(element_lower_bound), int(element_upper_bound))
                for _ in range(length):
                    x.append(''.join([random.choice(self.upper_letters) for _ in range(str_length)]))
            elif content_type == 'string_l':
                str_length = random.randint(int(element_lower_bound), int(element_upper_bound))
                for _ in range(length):
                    x.append(''.join([random.choice(self.lower_letters) for _ in range(str_length)]))
            elif content_type == 'string':
                str_length = random.randint(int(element_lower_bound), int(element_upper_bound))
                for _ in range(length):
                    x.append(''.join([random.choice(self.letters) for _ in range(str_length)]))

            x = map(str, x)
            self.testcase_string += ' '.join(x) + '\n'

    def handle_content(self, lower_bound, upper_bound, content_type):
        if content_type == 'real':
            return str(random.randint(int(lower_bound), int(upper_bound)))
        elif content_type == 'float':
            return str(random.uniform(int(lower_bound), int(upper_bound)))
        elif content_type == 'string_u':
            len = random.randint(int(lower_bound), int(upper_bound))
            x = [random.choice(self.upper_letters) for _ in range(len)]
            return ''.join(x)
        elif content_type == 'string_l':
            len = random.randint(int(lower_bound), int(upper_bound))
            x = [random.choice(self.lower_letters) for _ in range(len)]
            return ''.join(x)
        elif content_type == 'string':
            len = random.randint(int(lower_bound), int(upper_bound))
            x = [random.choice(self.letters) for _ in range(len)]
            return ''.join(x)

    def get_testcase_string(self):
        return self.testcase_string

    def reset(self):
        self.initialise()
