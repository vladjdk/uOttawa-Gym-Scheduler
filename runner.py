import scheduler
import sys
import os

def main():

    scheduler.run(os.environ['REQUEST_TIME'])

if __name__ == "__main__":
    main()