# Thanks to our context.py file, we only need this in the header:
from context import utility 
from context import gpytoolbox
from context import plt

# Test something
a = 4
# Call the functions we wrote in utility/
b = utility.sample_fun_one(a)
print(b)

c = utility.sample_fun_two(a)
print(c)

# We can also call functions in other libraries without more imports We make the
# consistent choice that paths of files we use start at the github repo main
# directory, since we are going to run these scripts from the main directory,
# i.e., `python scripts/sample_script.py`, not `cd scripts` and then `python
# sample_script.py`
filename = "data/illustrator.png"
poly = gpytoolbox.png2poly(filename)
plt.plot(poly[0][:,0],poly[0][:,1])
plt.plot(poly[1][:,0],poly[1][:,1])
plt.plot(poly[2][:,0],poly[2][:,1])
plt.plot(poly[3][:,0],poly[3][:,1])
plt.show()