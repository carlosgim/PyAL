#**************************************************************************************************
__copyright__ = "in revision"
__credits__ = ["PyTL"]
__license__ = "in revision"
__version__ = "1.0.1"
__maintainer__ = "Carlos A. Gimenez"
__status__ = "Testing"
#**************************************************************************************************


def vis_corr():

    import seaborn as sns   
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt


    print "Please type the file name to the correlation (Example: xxx.csv)"
    
    filename = raw_input()

    print "Please type the separator text"
    print "1 = ,"
    print "2 = |"                          
    print "3 = tab"
    separator = raw_input()    


    if separator > "3":
    
       print "Invalid option"
    
    else:


        if separator == "1":

            df = pd.read_table(filename, sep=",",nrows=500, low_memory=False)

        elif separator=="2":

            df = pd.read_table(filename, sep="|",nrows=500, low_memory=False)   

        elif separator=="3":

            df = pd.read_table(filename, sep="\t",nrows=500, low_memory=False)  


        corr = df.corr()

        # Generate a mask for the upper triangle
        mask = np.zeros_like(corr, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True

        # Set up the matplotlib figure
        f, ax = plt.subplots(figsize=(30, 30))

        # Generate a custom diverging colormap
        cmap = sns.diverging_palette(220, 10, as_cmap=True)

        # Draw the heatmap with the mask and correct aspect ratio
        sns.heatmap(corr, mask=mask, cmap=cmap, 
            square=True, xticklabels=2, yticklabels=2,
            linewidths=.5, cbar_kws={"shrink": .7}, ax=ax)

        plt.yticks(rotation=0)
        plt.xticks(rotation=90)
        plt.title("Correlation of "+filename)
        plt.savefig(filename+".pdf")
        plt.title("Correlation of "+filename)
        plt.show()


vis_corr()
