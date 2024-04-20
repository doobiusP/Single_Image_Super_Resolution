# Repository for Image SR Project for the NITK Chapter of ACM, 2023-2024
## Abstract
We leverage a GAN-based architecture to tackle the issue of constructing high-resolution images from low-resolution images while preserving image structure and simultaneously improving image fidelity and sharpness.
<p align="center">
  
![image](https://github.com/doobiusP/Single_Image_Super_Resolution/assets/36434536/e1faf3e4-75c6-4127-8255-1d9c22719930?raw=True)
![image](https://github.com/doobiusP/Single_Image_Super_Resolution/assets/36434536/67cdd0d3-2438-44a3-9b76-52b0c0de46e6?raw=True)
</p>
<p> Note that: 
  <font size="-2">
  * An SSIM (Structural Similarity Index Measure) closer to 1 is considered perfect]
  * Note that a higher PSNR indicates a higher quality reconstruction but studies have shown that it is a poor indicator compared to other metrics
  </font>
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
<p align="center>
![image](https://github.com/doobiusP/Single_Image_Super_Resolution/assets/36434536/18949d5a-5ea8-4333-aa2f-2f36f4674803)

*<p align="center"> Fig 1. Generator </p>*

![image](https://github.com/doobiusP/Single_Image_Super_Resolution/assets/36434536/f6edd6e8-43a5-4e8f-ae4a-9c0aca0c8584)

*<p align="center">Fig 2. Discriminator</p>*
</p>
The main block of the generator lies in the list of residual blocks connected sequentially. Upscaling is done via Pixel Shuffling layers. Bicubically upscaling the original input image as a baseline for the output allows for color-correct output images. Optional post-processing such as sharpening can be done.


### Technologies/Libraries used:
* Numpy
* PyTorch
* Matplotlib
* Pillow

### Associated links:
* <a href="https://www.kaggle.com/code/doobiusp/srgan">Kaggle Code</a>
