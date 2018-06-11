# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))

# There is package name scipy.io which can load the mat file in the system and return the <dict> out of it.

