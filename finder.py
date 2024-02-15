
import sys
import argparse

HOME_DATABASE = """shoes,floor,8/23/23,10:00am
papers,cubbard,7/23/23,1:00am
picture frames,wall,6/23/23,10:00pm
tshirts,cubbard,1/13/23,9:00am
soccer balls,basket,2/9/22,12:00pm
kitchen tables,floor,3/23/23,4:00pm
cabinets,corner,5/30/23,10:30pm"""


def main(object_name):
    # Split the HOME_DATABASE string into an array of strings by splitting by new lines
    database_entries = HOME_DATABASE.split('\n')

    # Iterate through the array of strings
    for entry in database_entries:
        # Split the string on commas
        item, location, date_last_moved, time_last_moved = entry.split(',')

        # Check if the name of the item matches the name passed into the function
        if item.strip() == object_name:
            # Return the location, date last moved, and time last moved as a string
            return f"The {item.strip()} were found in the {location.strip()} and were placed there on {date_last_moved.strip()} at {time_last_moved.strip()}"

    # If the item is not found, raise a ValueError
    raise ValueError(f"Sorry, could not find your item named {object_name} within the database")

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


def parse_args(args_list):
    parser = argparse.ArgumentParser()
    parser.add_argument('object', type=str, help="Please enter the name that we are searching for.")
    args = parser.parse_args(args_list)
    return args

# This code will call the HOME_DATABASE
if __name__ == "__main__":
    arguments = parse_args(sys.argv[1:])
    try:
        print(main(arguments.object))
    except ValueError as e:
        print(e)


# name_to_find = sys.argv[1]

# result = main(HOME_DATABASE, name_to_find)

# if result:
#     print(result)
# else:
#     print(f"ValueError: Sorry, could not find your item named {name_to_find} within the database")






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

