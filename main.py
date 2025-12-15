"""
CLI to create, list and complete tasks in an sqlite3 database.
"""
import argparse
from datetime import datetime
import tasktracker

def _parse_datetime(date_string):
    try:
        return datetime.strptime(date_string, '%Y-%m-%d').date()
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"Invalid date format: {date_string}. Use 'YYYY-MM-DD'.") from exc

# NOTE: Take arguments by flags with argpars
parser = argparse.ArgumentParser(
                            prog="tasktracekrcli",
                            description="Create tasks that are marked unique by name and date in a sqlite3 database.",
                            epilog="")
# NOTE: change this, go by dates.
parser.add_argument("-l", "--list",
                type=bool,
                help="List tasks in the data base, -d will specify a date.")
# NOTE: change to task name.
parser.add_argument("-a", "--add",
                type=str,
                help="Name of task to add, -d is optional, assumed today.")
parser.add_argument("-d", "--due_date",
                type=_parse_datetime,
                help="Optional flag to -a, -l, -c.")
parser.add_argument("-c", "--complete",
                action="store_true",
                help="Completes a task, requires -a and -d is option")
args = parser.parse_args()

if any(vars(args).values()):
    temp_name = tasktracker.TaskTracker("real_task_database.db","task_table")
    temp_name.check()
else:
    parser.print_help()

if args.add:
    if args.due_date:
        temp_name.add(args.add, args.due_date)
    else:
        temp_name.add(args.add)
if (args.add and args.complete):
    if args.due_date:
        temp_name.complete(args.add, args.due_date)
    else:
        temp_name.complete(args.add)
if args.list is not None:
    print(args.list)
    for i in temp_name.list_task(args.list):
        print(i)
