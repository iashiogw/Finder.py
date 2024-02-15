
import sys
import argparse

HOME_DATABASE = """shoes,floor,8/23/23,10:00am
#papers,cubbard,7/23/23,1:00am
#picture frames,wall,6/23/23,10:00pm
#tshirts,cubbard,1/13/23,9:00am
#soccer balls,basket,2/9/22,12:00pm
#kitchen tables,floor,3/23/23,4:00pm
#cabinets,corner,5/30/23,10:30pm"""

def main(database):
    # This code is going to split the database string into an array 
    string_array = database.split('\n')

    # This code will iterate through each line in the array
    for line in string_array:
        # This code is going to split the line on commas 
        line_parts = line.split(',')

        # This code will check to see if the line has enough elements 
        if len(line_parts) >= 4:
            # This code will assign values to variables
            item_name = line_parts[0]
           
            location = line_parts[1]
           
            date_last_moved = line_parts[2]
            
            time_last_moved = line_parts[3]

            # This code is going to print out the variables assigned with the values
            print(f"Item Name: {item_name}")
           
            print(f"Location: {location}")
           
            print(f"Date Last Moved: {date_last_moved}")
           
            print(f"Time Last Moved: {time_last_moved}")
        else:
            print("Skipping line with an unexpected format:", line)


if __name__ == "__main__":
    HOME_DATABASE = """shoes,floor,8/23/23,10:00am
papers,cubbard,7/23/23,1:00am
picture frames,wall,6/23/23,10:00pm
tshirts,cubbard,1/13/23,9:00am
soccer balls,basket,2/9/22,12:00pm
kitchen tables,floor,3/23/23,4:00pm
cabinets,corner,5/30/23,10:30pm"""

    main(HOME_DATABASE)


    
import argparse
import sys

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
        print("Argument:", arg)

