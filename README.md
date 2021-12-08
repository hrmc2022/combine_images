# Combine images

## Introduction
We can combine images of the same size by this program.

## Requirements
> pip install numpy  
> pip install opencv-python

## Input parameters
-  in_path : set a path where contains images. 
- out_path : an output path name or directory
- save_name : name of a combined image
- horizontal_num : set horizontal number of images to combine
-  config : set 0 for combining images from right to left, or 1 for combining images from left to right.

## Demo
### Example 1
- input 
> python combine_images.py --in_path=data --out_path=results --save_name=combine --horizontal_num=4 --config=1

In the example input, the output file is generated in the output path. We can combine images from right to left and the horizontal number of images is 4, and the blank is filled with black.

- output image
![demo1](/results/combine.png)

#### Example 2
- input
> python combine_images.py --in_path=data --out_path=results --save_name=combine2 --horizontal_num=2 --config=0

In the example input, the output file is generated in the output path. We can combine images from left to right and the horizontal number of images is 2, and the blank is filled with black.

- output image
![demo1](/results/combine2.png)