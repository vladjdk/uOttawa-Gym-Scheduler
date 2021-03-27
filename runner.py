import scheduler
import sys

def main(argv):
    scheduler.run(argv[1], argv[2], argv[3], argv[4])

if __name__ == "__main__":
    main(sys.argv)