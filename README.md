# Single Image Super Resolution
## Abstract
### Repository for Image SR Project for the NITK Chapter of ACM, 2023-2024
We leverage a GAN-based architecture to tackle the issue of constructing high-resolution images from low-resolution images while preserving image structure and simultaneously improving image fidelity and sharpness.
<p align="center">
  
![image](https://github.com/doobiusP/Single_Image_Super_Resolution/assets/36434536/e1faf3e4-75c6-4127-8255-1d9c22719930?raw=True)
![image](https://github.com/doobiusP/Single_Image_Super_Resolution/assets/36434536/67cdd0d3-2438-44a3-9b76-52b0c0de46e6?raw=True)
</p>

### Mentors:
* Santosh C
* Prasanna Kumar
### Mentees:
* Aaryan Patil
* Arnav Santosh

### Key Points:
* SRGAN trained on an image dataset consisting of more than **6000** high resolution and low resolution pairs of training images alongside 273 corresponding pairs of validation images (publicly available <a href="https://www.kaggle.com/datasets/doobiusp/various-ordered-images-for-super-resolution-task">here</a>.)
* Performs data augmentation to the training images
* Includes dataset loading, model architecture and the training
* Includes an easy to use upscale function to easily upscale any image given its path

## Report:

### Method
SRGAN

To perform SISO-SR, we use a GAN with a generator and discriminator architecture as shown below.

![image](https://github.com/doobiusP/Single_Image_Super_Resolution/assets/36434536/a5e41898-b3d6-4307-919b-05db2161e4e4)

*<p align="center"> Fig 1. Generator </p>*

![image](https://github.com/doobiusP/Single_Image_Super_Resolution/assets/36434536/dc21acdf-8aa6-4edf-9fbd-2fca38ddfe70)

*<p align="center">Fig 2. Discriminator</p>*

The main block of the generator lies in the list of residual blocks connected sequentially. Upscaling is done via Pixel Shuffling layers. Bicubically upscaling the original input image as a baseline for the output allows for color-correct output images. Optional post-processing such as sharpening can be done.


### Technologies/Libraries used:
* Numpy
* PyTorch
* Matplotlib
* Pillow

### Associated links:
* <a href="https://www.kaggle.com/code/doobiusp/srgan">Kaggle Code</a>
