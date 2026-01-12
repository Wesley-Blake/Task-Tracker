"""
CLI to create, list and complete tasks in an sqlite3 database.
"""
import sys
import argparse
from datetime import datetime
import tasktracker

def _parse_datetime(date_string: str) -> datetime:
    try:
        return datetime.strptime(date_string, '%Y-%m-%d').date() # type: ignore
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"Invalid date format: {date_string}. Use 'YYYY-MM-DD'.") from exc

parser = argparse.ArgumentParser(
    prog="tasktracekrcli",
    description="Create tasks that are marked unique by name and date in a sqlite3 database.",
    epilog="")
# Important flags
parser.add_argument("-a", "--add",
    action="store_true",
    help="Name of task to add, -d is optional, assumed today.")
parser.add_argument("-l", "--list",
    action="store_true",
    help="List tasks in the data base, -d will specify a date.")
parser.add_argument("-c", "--complete",
    action="store_true",
    help="Completes a task, requires -a and -d is option")
parser.add_argument("-n", "--name",
    type=str,
    help="Name of task to modify or add.")

# Optional flags
parser.add_argument("-d", "--due_date",
    type=_parse_datetime,
    help="Optional flag to -a, -l, -c.")

# Parse arguments
args = parser.parse_args()

if __name__ == "__main__":
    if not (args.add or args.list or args.complete):
        parser.print_help()
        sys.exit(1)
    else:
        tasks = tasktracker.TaskTracker("task_database.db", "task_table")
        tasks.check()

    if args.add:
        tasks.add(task=args.name, due_date=args.due_date)
    if args.list:
        for task in tasks.list_task():
            print(task)
    if args.complete:
        tasks.complete(args.name, due_date=args.due_date)

    tasks.close()