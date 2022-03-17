# These are the imports we're going to use in all scripts.
import sys
import os
import matplotlib.pyplot as plt
# Use relative paths so this works on any computer
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import utility
# Use relative paths so this works on any computer
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../ext/gpytoolbox')))
import gpytoolbox