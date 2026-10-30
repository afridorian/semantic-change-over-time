import argparse

def main(args):

    if args.task == "data":
        # Data calls

    if args.task == "embedding":
        # embedding calls

    if args.task == "1a":
        # subtask 1a functions/code

    if args.task == "1b":
        # subtask 1b functions/code

    if args.task == "2":
        # subtask 2 functions/code

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--task",choices=("data","embedding","1a", "1b", "2"), nargs="+",required=True,help="Choose which task(s) to run.",)
