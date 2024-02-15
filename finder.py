
import sys
import argparse

HOME_DATABASE = """shoes,floor,8/23/23,10:00am
papers,cubbard,7/23/23,1:00am
picture frames,wall,6/23/23,10:00pm
tshirts,cubbard,1/13/23,9:00am
soccer balls,basket,2/9/22,12:00pm
kitchen tables,floor,3/23/23,4:00pm
cabinets,corner,5/30/23,10:30pm"""


def main(database, name):
    # This code will split the database string into an array of strings and will create new lines for the function
    string_array = database.split('\n')

    # This code will iterate through each line in the array
    for line_number, line in enumerate(string_array, start=1):
        # This code is going to split the line on commas so that the sentences are separated
        line_parts = line.split(',')

        if len(line_parts) >= 4:
            item_name = line_parts[0].strip()
            location = line_parts[1].strip()
            date_last_moved = line_parts[2].strip()
            time_last_moved = line_parts[3].strip()

            if item_name == name:
                return f"The {item_name} were found in the {location} and were placed there on {date_last_moved} at {time_last_moved}"
            
    return None

        # # This code will check to see if the line has enough elements
        # if len(line_parts) >= 4:
        #     # This code will assign values to variables
        #     item_name = line_parts[0]
        #     location = line_parts[1]
        #     date_last_moved = line_parts[2]
        #     time_last_moved = line_parts[3]

        #     # This code will print out the variables assigned with the values
        #     print(f"Item Name: {item_name}")
        #     print(f"Location: {location}")
        #     print(f"Date Last Moved: {date_last_moved}")
        #     print(f"Time Last Moved: {time_last_moved}")
        # else:
        #     print(f"Skipping line {line_number} with an unexpected format: {line}")

# This code will call the HOME_DATABASE
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error try again, not right")
        sys.exit(1)


name_to_find = sys.argv[1]

result = main(HOME_DATABASE, name_to_find)

if result:
    print(result)
else:
    print(f"ValueError: Sorry, could not find your item named {name_to_find} within the database")






def create_argument_parser():
    """
    This code will Takes a list of strings from the command prompt and passes them through as
arguments 
Args:
args_list (list) : the list of strings from the command prompt
    Returns:
        parser (argparse.ArgumentParser): An ArgumentParser object with added arguments.
    """
    parser = argparse.ArgumentParser(description="My Command Line Tool")

    # This code will add arguments to the parser
    parser.add_argument('arguments', nargs='+', type=str, help="List of arguments")

    return parser

# Example usage:
if __name__ == "__main__":
    # This argument will create an argument parser, then it will parse through the 
    #command line and access the arguments as a list and then process the list of arguments
    argument_parser = create_argument_parser()

    args = argument_parser.parse_args()

    argument_list = args.arguments

    for arg in argument_list:
        pass
        # print("Argument:", arg)

