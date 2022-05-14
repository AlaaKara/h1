from csv import reader

result = 0
name = input("enter your name: ")
# skip the first line(the header)
with open('questions.csv', 'r') as my_file:
    file_csv = reader(my_file)
    head = next(file_csv)

    # check if the file is empty or not
    if head is not None:
        # Iterate over each row
        for row in file_csv:
            # print the rows
            cols = row[0].split(';')
            answer = input(cols[0]+"?")
            if answer == cols[1]:
                result += 1

output = open("result.txt", "w")
output.write("name: "+name+"\n")
output.write("result: " + str(result)+" from 20")
