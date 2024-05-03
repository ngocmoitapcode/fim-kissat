def convert(input_file, output_file):
    try:
        with open(input_file, 'r') as input:
            with open(output_file, 'w') as output:
                for line in input:
                    values = line.strip().split()
                    convert_values = [str(int(value) % 2) for i, value in enumerate(values)] 
                    output.write(' '.join(convert_values) + '\n')
        print("Output file created successfully!")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))

input_file = 'input/data.txt'
output_file = 'input/converted_data.txt'
convert(input_file, output_file)
