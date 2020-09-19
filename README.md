# Interview

This repository contains an interview coding challenge for Avail.  I'm going rogue, and have completed this challenge in
python. As such, I've packaged this up in a docker container so the evaluator(s) should be able to see it "just work" 
without having to know much.  Except maybe a little bit about docker.

## What you would use this for
I'm not exactly sure.  the thing that came to mind was that you could
anonymize ordered interaction  between multiple parties.  You
definately have something in mind, but I cant quite figure it out.

## Setup

Everything is packaged in docker.  I've been using docker pretty exclusively, and love that the local development environment
you have is identical to the production environment.
Some initial setup steps need to be performed in order to pull docker images from
where we store them in AWS.

## Building

Requires docker to be installed.

from the current directory of this file:
docker build .

Note: these instructions are copied from the makefile.
## Running

### Tests
```bash
docker run --rm -t echaz_interview py.test tests.py
```

###  execute encryptor directly

```bash
docker run --rm -t echaz_interview python3 main.py The dog jumped over the fence too
```

### from a bash shell

```bash
docker run --rm -t echaz_interview /bin/bash
% python3 main.py The dog jumped over the fence too
```
