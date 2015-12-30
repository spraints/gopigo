# Go forward. When we're about to hit something, stop and go backwards to the starting point.
from gopigo import *

us_port = 15
distance_to_stop = 100

def main():
  dist = move_forward()
  move_backward(dist)

def move_forward():
  fwd()
  while True:
    dist = us_dist(us_port)
    sys.stdout.write("\rDist: " + dist + "    ")
    if dist < distance_to_stop
      stop()
      return 0
    time.sleep(0.1)

def move_backward(dist):
  # No-op

main()
