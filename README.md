# Feature_Extraction_ImageFeatures_Conversion

 - Here in this img_path path you have to replaced with  your path
- In this Project Create two files One for Extracting Features from Image 
-  another Excel_conversion.py to Extract Features from Extracted festures to Convert into excel
- Here you will get live Example Converted Features into Excel that image_features.xlsx

FeatureExtraction:

Documentation:

This is a Python script that defines a function named `ShapeSizeFeature` which takes a grayscale thresholded image as input and returns a dictionary of shape and size features of objects in the input image.

The script uses the following libraries:
- `cv2` (OpenCV): for computer vision and image processing functions.
- `numpy` (Numerical Python): for numerical operations and array manipulations.
- `skimage` (Scikit-Image): for image processing and analysis functions.

The `ShapeSizeFeature` function takes a single argument `thresh`, which is a thresholded image, i.e., a binary image where white pixels represent objects of interest and black pixels represent the background. The function first labels the objects in the input image using the `label` function from Scikit-Image. The `label` function assigns a unique integer label to each connected component in the input image.

The function then uses the `regionprops_table` function from Scikit-Image to compute various shape and size features of the labeled objects. The function computes the following features for each object:
- area: the number of pixels in the object.
- perimeter: the perimeter length of the object.
- major_axis_length: the length of the major axis of the ellipse that best fits the object.
- minor_axis_length: the length of the minor axis of the ellipse that best fits the object.
- centroid: the centroid (center of mass) of the object.
- local_centroid: the centroid of the object relative to its bounding box.
- coords: the coordinates of all pixels in the object.
- eccentricity: the eccentricity of the ellipse that best fits the object.
- equivalent_diameter: the diameter of a circle with the same area as the object.
- orientation: the angle between the major axis of the object and the x-axis.
- solidity: the ratio of the object's area to the area of its convex hull.

The function then computes three additional features based on the above properties:
- Roundness: a measure of how closely an object resembles a circle, defined as `(4 * pi * area) / (perimeter^2)`.
- Compactness: a measure of how compact an object is, defined as `sqrt((4 * area) / pi) / major_axis_length`.
- SF3: a measure of how elongated an object is, defined as `area / ((major_axis_length/2) * (minor_axis_length/2) * pi)`.

The function returns a dictionary `props` containing all the computed features, along with their corresponding values for each labeled object in the input image.


# youtube link:
https://youtu.be/v5UrfsQgBXM
