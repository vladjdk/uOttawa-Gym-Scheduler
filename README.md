# uOttawa Gym Scheduler Usage

## Getting Started
This is a simple program, and it only requires Python and Docker.

When you have installed docker, run the following command to set up your image using the Dockerfile:

```docker build --tag scheduler .```

After the image has been built, run the command 

```docker run --env BARCODE=your_barcode --env PIN=your_pin --env SESSION_CODE=desired_gym_slot_code --env REQUEST_TIME=time_between_requests_ms --name scheduler scheduler```

For example, this might look like:

```docker run --env BARCODE=1234567890 --env PIN=12345 --env SESSION_CODE=15403 --env REQUEST_TIME=10000 --name scheduler scheduler```

The Python stdout is flushed at every print statement, so to view the output, use the command

```docker logs scheduler```

The session code for every gym slot can be found here:
![alt text](https://github.com/photonized/uOttawa-Gym-Scheduler/blob/main/barcode.png "session code example")

# PSA
Make sure you choose a future gym slot barcode that doesn't have a waitlist on it for this bot to work.

//TODO: add info.json info and change up README