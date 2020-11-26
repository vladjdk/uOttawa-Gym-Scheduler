# uOttawa Gym Scheduler Usage

## Dependencies
REQUIRES PYTHON 3
- Pandas
- BS4
- Requests

If you do not have any of the above, run the following script in your terminal/command prompt.

```
pip install requests
pip install bs4
pip install pandas
```

## Usage
In a terminal, navigate to the cloned directory and run the following:
```
python scheduler.py
```

Then, input your account barcode, your account PIN, the barcode of the gym slot you want to reserve, and the time in MS between each request (recommended is 5000).

The barcode for every gym slot can be found here:
![alt text](https://github.com/photonized/uOttawa-Gym-Scheduler/blob/main/barcode.png "barcode example")

# PSA
Make sure you choose a future gym slot barcode that doesn't have a waitlist on it for this bot to work.
