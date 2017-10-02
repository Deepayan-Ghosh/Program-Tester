# Program Tester
This is a program that tests another program written in Python, Java or C++ for errors by feeding random input to that program. The input fed to the program is generated according to a XML file which describes the input format for a program which is to-be-tested.

## Prerequisites
Python must be installed on the host system.

## Getting Started
1. Download the folder
2. Use `chmod a+x ProgramTester.py` to make it executable.
3. Run the program using `./ProgramTester.py arg1 arg2 arg3` where
    1. `arg1` is the path to the program to-be-tested
    2. `arg2` is the path to the XML file
    3. `arg3` is the language in which the to-be-tested program is written. Currently only Java, python and C++ is supported.
       C++ means g++ compiler only.
  
  #### For example
  There are testprograms given, and pre-written XML files as example files.
  Run `./ProgramTester.py testprogram.py test.xml python` where `testprogram.py` takes input of the format number of testcases followed by `m` and `n`. Each of the next m lines contains n integers between 0 and 10. After this there are two lines containing `n` uppercase strings, each of length 10.
 

## Writing the XML file
The following tags are available for use:
1. `<file>...</file>` This is the topmost or root tag. Each input XML file must have this tag, and the contents must be enclosed inside this.
2. `<testcase min="..." max="..." />` This tag represent the number of test cases each file contains. The range of possible values of test cases is mentioned with the help of `max` and `min` attributes. To fix the number of testcases for each file make the value of max equal to the value of min. If these attributes are ignored, their values are assumed to be 1.
3. `<element name="..." type="..." max="..." min="..."/>` This tag represent a single element.
    1. `type` attribute specifies the type of the element. It can be `real` for integers, `float` for floating point numbers, `string_u` for uppercase strings, `string_l` for lowercase strings and `string` for mixed case strings.
    2. `name` attribute is like variable name. The value of this attribute is used to refer to this element later. For example in `test.xml` we use in `<elements>` tag we use `repeat="m"` where `m` is name of variable in `element` tag.
    3. `max` attribute is the maximum value that this element can take.
    4. `min` attribute is the minimum value that this element can take.

*NB: The element is generated randomly between `max` and `min`. However we can generate a particular value all the time by making the values of `max` and `min` same*
