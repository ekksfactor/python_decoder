import re

#defines the decoding function, where "message_file" is a string with the name of the .txt file that contains the encoded message
def decode(message_file):
    #open the file, declare the empty decoder dictionary, and declare an empty list that will be populated with the code numbers
    file = open(message_file, "r")
    nums = []
    decode_dict = {}

    #load the code number from each line into the list, and populate the decoder dictionary. Each code number and corresponding code word are used as the key/value pairs
    for line in file:
        nums.append(int(re.match("[0-9]+", line).group()))
        decode_dict[int(re.match("[0-9]+", line).group())] = re.search("[a-zA-Z]+",line).group()
    nums.sort()

    #declare the empty pyramid, row_counter that will be used to determine the length of each row, and an empty list that will be used to form the rows and append them to the pyramid
    pyramid = []
    row_counter = 1
    append_list = []

    #go through the list of numbers, split it into smaller lists, and populate the pyramid with them
    for i in nums:
        if i == max(nums):
            append_list.append(i)
            pyramid.append(append_list)
        elif len(append_list) < row_counter:
            append_list.append(i)
        else:
            pyramid.append(append_list)
            row_counter = row_counter + 1
            append_list = [i]

    #create an empty return string that will be used to populate the decoded message. Get the last number in each row in the pyramid, use it to look up the code word, and add the code word to the return string
    decoded_msg = ""
    for pyramid_row in pyramid:
        decoded_msg = decoded_msg + decode_dict[pyramid_row[-1]] + " "

    #return the decoded message
    return decoded_msg.rstrip()

#run the function with the test file and print the decoded message
output = decode("test_file.txt")
print(output)
