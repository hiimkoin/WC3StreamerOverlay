from player_data import *
from runner import *

matchups = [[[p1, p2], [p3, p4]], [[p1, p2, p3], [p4, p5, p6]], [[p1, p2, p3, p4], [p5, p6, p7, p8]]]

runner = TestRunner(matchups)
runner.start()
