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
  Run `./ProgramTester.py testprogram.py test.xml python` where `testprogram.py` takes input of the format number of testcases followed by `m` and `n`. Each of the next m lines (given by repeat="m") contains n integers between 0 and 10. After this there are two lines(repeat="2") containing `n` uppercase strings, each of length 10.
 

## Writing the XML file
The following tags are available for use:
1. `<file>...</file>` This is the topmost or root tag. Each input XML file must have this tag, and the contents must be enclosed inside this.
2. `<testcase min="..." max="..." />` This tag represent the number of test cases each file contains. The range of possible values of test cases is mentioned with the help of `max` and `min` attributes. To fix the number of testcases for each file make the value of max equal to the value of min. If these attributes are ignored, their values are assumed to be 1.
3. `<element name="..." type="..." max="..." min="..."/>` This tag represent a single element.
    1. `type` attribute specifies the type of the element. It can be `real` for integers, `float` for floating point numbers, `string_u` for uppercase strings, `string_l` for lowercase strings and `string` for mixed case strings.
    2. `name` attribute is like variable name. The value of this attribute is used to refer to this element later. For example in `test.xml` we use in `<elements>` tag we use `repeat="m"` where `m` is name of variable in `element` tag.
    3. `max` attribute is the maximum value that this element can take. In case of strings, `max` determines the maximum allowed length of the string element.
    4. `min` attribute is the minimum value that this element can take. In case of strings, `min` determines the minimum allowed length of the string element.

    *NB: The element is generated randomly between `max` and `min`. However we can generate a particular value all the time by making the values of `max` and `min` same. Similarly, in case of strings the length of string is chosen randomly between `max` and `min`, and if they are equal then string of same length is generated every time*

4. `<line>...</line>` This tag defines a single line in the input file. It has only `element` tags as its contents. Thus it helps to define a line of elements represented by `<element .../>`, where each of the elements can be of different type. For example, in `test.xml` file the `line` tag defines two elements of integer type named `m` and `n`. Both of them have a minimum value of `1` and maximum value of `10`.
5. `<elements type="..." repeat="..." max="..." min="..." len="..." minlen="..." maxlen="..."/>`
This tag is an alternative to `line` tag. When we need inputs where each line has large number of elements of the same type, and also the same line is repeated couple of time, for example, when we need inputs for arrays or matrices, often we repeat lines of inputs having the same format (each line having large number of elements). In such cases using `line` tag can be tedious.
    1. `type` attribute specifies the type of the element. It can be `real` for integers, `float` for floating point numbers, `string_u` for uppercase strings, `string_l` for lowercase strings and `string` for mixed case strings.
    2. `repeat` attribute defines how many times a single line is to be repeated. The value of the attribute can be a integer value or can be a previously named `element` as in `text.xml` where `repeat="m"`. Here the line would be repeated `m` times where value of `m` is determined randomly.
    3. `max` attribute specifies the maximum allowed value of a single element in the line. In case of string types, `max` determines the maximum allowed length of each individual string element in the line.
    4. `min` attribute specifies the minimum allowed value of a single element in the line. In case of string types, `min` determines the minimum allowed length of each individual string element in the line.
    
    *NB: The value is chosen randomly from a range between `max` and `min`. A fixed value can be generated every time by making `max` equal to `min`. In case of strings, the length of the string is chosen randomly between `min` and `max`. If `max` and `min` are made equal then every string will be of fixed length.*
    
    5. `len` attribute defines the number of elements there will be in a single line. When `len` is specified, it defines a fixed number of elements, whereas
    6. `maxlen` attributes defines the maximum possible number of elements in a line. In this case, the number of elements in a line is chosen randomly between `maxlen` and `minlen` which is assumed to be `1` if not specified.
    
    *NB: `len`,`maxlen` and `minlen` can be variables also. If their values are refer to previously `name`-ed variables then that value will be taken. For example,in `test.xml` we see that `len="n"` which means that value of `len` here will be value chosen for the element named `n`*
    
## Contributing
 Anyone is open to contributing but please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.
