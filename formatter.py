""""
Formatter project by Andrew Li
Description: given a txt file, replace string with the start of the line 
to the first replacement string for a set number of times
"""
# import os to get file path
import os


def main():

    # input file name here
    #  - file name = file name in this dir
    #  - new_file = new file to write to
    #  - replace_string = string to be replaced
    #  - single_char = the single of char
    #  - times = number of times to be copied
    file_ = 'lab2a'
    new_file = 'lab2a_new'
    replace_string = '""'
    single_char = '"'
    times = 51

    # get path to current dir
    current_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(current_folder, file_ + '.txt')
    new_file = os.path.join(current_folder, new_file + '.txt')

    # with the file open, for every line in file,
    # if line = '""' in the line,
    # for every single char replace with number or whatever at the start of line
    # in the end, join char and multiply by length plus line break
    with open(my_file, 'r+') as fp:
        data = fp.readlines()
        for index, line in enumerate(data):
            if replace_string in line:
                number = []
                for char in line:
                    if char != single_char:
                        number.append(char)
                    else:
                        break
                number = ''.join(number)

                data[index] = str(number * times) + '\n '

        # print data and write to new_file
        new_data = ''.join(data)
        print('Data:\n', new_data)

        with open(new_file, 'w') as fp:
            fp.write(''.join(new_data))


    return 0

# system calls main
if __name__ == "__main__":
    main()