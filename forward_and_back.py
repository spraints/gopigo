# Go forward. When we're about to hit something, stop and go backwards to the starting point.
from gopigo import *
import signal, sys

us_port = 15
distance_to_stop = 30

def main():
  dist = move_forward()
  move_backward(dist)

def move_forward():
  start = time.time()
  fwd()
  while True:
    dist = us_dist(us_port)
    sys.stdout.write(str.format("\rDist: {0}   ", dist))
    if dist < distance_to_stop:
      stop()
      break
    time.sleep(0.1)
  return time.time() - start

def move_backward(dist):
  bwd()
  time.sleep(dist)
  stop()

def done(sig, stackframe):
  stop()
  sys.stdout.write("\n")

signal.signal(signal.SIGINT, done)

main()
done(False, False)
