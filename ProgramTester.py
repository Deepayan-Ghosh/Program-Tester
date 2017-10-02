#!/usr/bin/env python
from CustomXMLParser import CustomXMLParser
import subprocess, sys


# handles the input and output files
# ip --> testcase file handle
# op --> output file handle, the file to which output of a testcase is written and also error if encountered
#        If the program terminates due to an error, the "testcase.txt" contains testcase which caused error
#        and the "output.txt" contains the error which occured

def handle_file(testcase):
    # testcase is written to a file to be fed to another program
    ip = open('testcase.txt', 'w')
    ip.write(testcase)
    ip.close()

    # testcase file is opened in read mode, to be passed to other program through subprocess module
    # output file is opened in write mode, for the output and error to be written
    ip = open('testcase.txt', 'r')
    op = open('output.txt', 'w')

    return ip, op


# sys.argv[1] ---> program to tested for exceptions and errors
# sys.argv[2] ---> xml file which describes the input format
# sys.argv[3] ---> the language in which the program is written
if __name__ == "__main__":

    # initialise the custom parser which parses the metadata xml file
    parser = CustomXMLParser(sys.argv[2])
    count = 100

    # if java, python or c++
    # generate test case, obtain appropriate file handles, compile the program, then run the program passing appropriate
    # files through stdin, stdout and stderr
    if sys.argv[3].lower() == 'java':
        while count:

            # generate test case
            parser.gen_test_cases()
            testcase = parser.get_testcase_string()

            ip, op = handle_file(testcase)

            # compile the program whose name is pass as command line arg
            subprocess.call(['javac', sys.argv[1]])
            # execute the program and set the stdin, stdout and stderr
            return_code = subprocess.call(['java', sys.argv[1].split('.')[0]], stdin=ip, stdout=op,
                                          stderr=subprocess.STDOUT)

            # if return code is not zero, there is an error, so the program prints the test case which caused the
            # error, breaks out of loop and closes the allocated resources
            if return_code is not 0:
                print(testcase)
                break
            ip.close()
            parser.reset()
            op.close()
            count -= 1

    elif sys.argv[3].lower() == 'python':
        while count:
            parser.gen_test_cases()
            testcase = parser.get_testcase_string()

            ip, op = handle_file(testcase)

            return_code = subprocess.call(['python', sys.argv[1]], stdin=ip, stdout=op, stderr=subprocess.STDOUT)
            if return_code is not 0:
                print(testcase)
                break

            ip.close()
            parser.reset()
            op.close()
            count -= 1

    elif sys.argv[3].lower() == 'c++':
        while count:
            parser.gen_test_cases()
            testcase = parser.get_testcase_string()
            ip, op = handle_file(testcase)

            subprocess.call(['g++', sys.argv[1]])
            return_code = subprocess.call(['./a.out'], stdin=ip, stdout=op,
                                          stderr=subprocess.STDOUT)
            if return_code is not 0:
                print(testcase)
                break

            ip.close()
            parser.reset()
            op.close()
            count -= 1
