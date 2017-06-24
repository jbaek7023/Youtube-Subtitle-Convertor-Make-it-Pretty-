import re
if __name__ == '__main__':
    paragraph = []
    cleanr = re.compile('<.*?>')

    # open the file
    file_name = '[DownSub.com] DL 43 Backpropagation V2 (1).txt'
    with open(file_name, 'r') as myfile:
        data=myfile.read()
    # get every line index
    # loop through the line
        next_skip_line=False
        for line in data.splitlines():
            if len(line)>=4 and not line[0].isdigit():
                new_line = re.sub(cleanr, '', line)
                for word in new_line.split(" "):
                    paragraph.append(word)
        output = ''
        for word in paragraph:
            output = output + " " + word
        print output
    #write it
    with open(file_name, 'w') as myfile:
        myfile.write(output)






    # if the line has 3 letters, skip

    # if the line starts with number, skip
    # if the line is empty skip

    # if the line starts with NOT number (character),

        # replace <> <> to '', then split and append them to paragraph ' '

    # print out paragraph
