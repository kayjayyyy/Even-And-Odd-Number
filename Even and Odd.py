# Templanza, Kristine Joy F.
# BSCPE 1-4
# Asignnment no. 3 - Even and Odd numbers

# Greeting and border line
print("")
print("\033[35m※ \033[0m" * 35)
print("")
print("\033[45m ♥ Welcome! ♥ \033[0m".center(78))

# open numbers.txt (read), even.txt (write/append), odd.txt (write/append)
def process():
    with open("numbers.txt") as input_number_file, open("even.txt", "w") as output_even_file, open("odd.txt", "w") as output_odd_file:
        # read the numbers.txt
        for line in input_number_file:
            integers = int(line.strip())
            # check the integers
            if integers % 2 == 0:
                # if even, write/append it in even.txt file
                output_even_file.write(str(integers) + "\n")
            else:
                # if odd, write/append it in odd.txt file
                output_odd_file.write(str(integers) + "\n")
process()