# uOttawa Gym Scheduler Usage

## Getting Started
This is a simple program, and it only requires Python and Docker.

When you have installed docker, run the following command to set up your image using the Dockerfile:

```docker build --tag scheduler .```

After the image has been built, run the command 

```docker run --env REQUEST_TIME=time_between_requests_ms --name scheduler scheduler```

For example, this might look like:

```docker run --env REQUEST_TIME=10000 --name scheduler scheduler```

The Python stdout is flushed at every print statement, so to view the output, use the command

```docker logs scheduler```

//TODO: add info.json info and change up README
