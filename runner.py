import scheduler
import sys
import os

def main():

    scheduler.run(os.environ['BARCODE'], os.environ['PIN'], os.environ['SESSION_CODE'], os.environ['REQUEST_TIME'])

if __name__ == "__main__":
    main()