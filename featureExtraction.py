# Feature Extraction


# importing all relevant libraries

import numpy as np
from skimage import measure
from  skimage.measure import label,regionprops_table
from skimage.color import rgb2gray



# Creating a function 


def ShapeSizeFeature(thresh):
    
    #area
    #
    props = regionprops_table(thresh, properties=('area','major_axis_length',
                                                  'minor_axis_length','centroid','local_centroid',
                                                'coords','eccentricity','equivalent_diameter',
                                                  'orientation','perimeter','perimeter',
                                                  'solidity'))
    temparea = props['area']
    tempperimeter = props['perimeter']
    Roundness = (4 * np.pi *temparea)/(tempperimeter ** 2)
    props['Roundness']=Roundness
    tempmajoraxis=props['major_axis_length']
    Compactness=np.sqrt((4*temparea)/np.pi)/tempmajoraxis
    props['Compactness']=Compactness
    tempminoraxis=props['minor_axis_length']
    SF3=temparea/((tempmajoraxis/2)*(tempminoraxis/2)*np.pi)
    props['SF3'] = SF3
    return props
    
    
    
    
