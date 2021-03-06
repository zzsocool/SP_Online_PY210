#!/usr/bin/env python3
import tempfile
import time
import sys


donors = {
    "STEVE JOBS":
        {"name": "Steve Jobs", "total_don": 1002.40, "donations": 2, "avg": 501.20},
    "JEFF BEZOS":
        {"name": "Jeff Bezos", "total_don": 877.33, "donations": 1, "avg": 877.33},
    "BILL GATES":
        {"name": "Bill Gates", "total_don": 653784.49, "donations": 2, "avg": 326892.24},
    "MARK ZUCKERBERG":
        {"name": "Mark Zuckerberg", "total_don": 16396.10, "donations": 3, "avg": 5465.37},
    "PAUL ALLEN":
        {"name": "Paul Allen", "total_don": 708.42, "donations": 3, "avg": 236.14}
}


def menu_input():
    return input(
        "\nSelect an option number:"
        "\n1. Send a Thank You"
        "\n2. Create a Report"
        "\n3. Send letters to all donors"
        "\n4. Quit\n"
    )


def thank_you():
    thank_you_options = {
        "MENU": False,
        "LIST": list_donors
    }
    while True:
        user_selection = (
            input("\nPlease provide a full name to send thank you note to (options 'list' and 'menu'): ")
        )
        action = thank_you_options.get(user_selection.upper())
        if action is False:
            break
        elif action is None:  # Write letter to user selection if an action option wasn't selected
            write_letter(user_selection)
        else:
            action()


def list_donors():
    for name in donors:
        print(name)


def write_letter(person):
    if person.upper() in donors:
        current_donor = donors[person.upper()]
    else:
        current_donor = add_donor(person)

    while True:  # Loop until a valid amount is provided
        donation_amount = input("\nHow much did {} donate?: ".format(person))
        try:
            donation_amount = round(float(donation_amount), 2)
        except ValueError:
            print("Please provide a valid amount")
        else:
            break
    add_donation(current_donor, donation_amount)
    print(thank_you_text(current_donor, str(donation_amount)))


def add_donor(new_name):
    donors[new_name.upper()] = {"name": new_name, "total_don": 0, "donations": 0, "avg": 0}
    return donors[new_name.upper()]


def add_donation(donor, donation_value):
    donor["donations"] += 1
    donor["total_don"] = round(donor["total_don"] + float(donation_value), 2)
    donor["avg"] = round(donor["total_don"]/donor["donations"], 2)


def create_report():
    the_report = generate_report()
    print(the_report)


def print_line(line_format, info, width):
    row_string = (line_format.format(*info, w1=width[0], w2=width[1], w3=width[2], w4=width[3]))
    return row_string


def find_widths(seq):
    return [max(len(str(row[i])) for row in seq) for i in range(len(seq[0]))]


def generate_report():
    header = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    header_string = "{0:<{w1}} | {1:>{w2}} | {2:>{w3}} | {3:>{w4}}"
    data_string = "{0:<{w1}}  ${1:>{w2}}   {2:>{w3}}  ${3:>{w4}}"
    width_dict = donors.copy()  # width dictionary is used only to find column widths
    width_dict["HEADER"] = {
        "name": "Donor Name", "total_don": "Total Given", "donations": "Num Gifts", "avg": "Average Gift"
    }
    width_list = [v2 for k, v in width_dict.items() for k2, v2 in v.items()]
    width_list = [width_list[i * 4:(i + 1) * 4] for i in range((len(width_list) + 4 - 1) // 4)]  # list of lists
    w = find_widths(width_list)
    header_to_print = print_line(header_string, header, w)
    report = '\n' + header_to_print + '\n' + ('-' * len(header_to_print)) + '\n'
    for key, value in sorted(donors.items(), reverse=True, key=lambda x: x[1]['total_don']):
        report += (print_line(data_string, value.values(), w) + '\n')
    return report


def print_all():
    file_location = tempfile.gettempdir()
    print("letters stored at: " + file_location)
    for key, value in donors.items():
        file_path_name = "{}{}{}".format(file_location, "\\", value["name"])
        file = file_creation(file_path_name)
        file.write(thank_you_text(value))
        file.close()


def file_creation(file_name):
    return open("{}{}{}".format(file_name, time.strftime("%Y%m%d-%H%M%S"), ".txt"), "w")


def thank_you_text(donor_dict, amount="{total_don:.2f}"):
    string_to_format = ("Dear {name},"
                        "\n\nThank you for your kind donation of $" + amount + "."
                        "\nIt will be put to very good use."
                        "\n\nSincerely,"
                        "\n-The Team")
    return string_to_format.format(**donor_dict)


def main():
    menu_switch = {
        "1": thank_you,
        "2": create_report,
        "3": print_all,
        "4": sys.exit
    }
    while True:
        user_selection = menu_input()
        action = menu_switch.get(user_selection)
        try:
            action()
        except TypeError:
            print("Please provide a valid option \n")


if __name__ == '__main__':
    main()
