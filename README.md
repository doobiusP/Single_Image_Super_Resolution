# Repository for Image SR Project for the NITK Chapter of ACM, 2023-2024
## Abstract
We leverage a GAN-based architecture to tackle the issue of constructing high-resolution images from low-resolution images while preserving image structure and simultaneously improving image fidelity and sharpness.
<p align="center">
  
![image](https://github.com/doobiusP/Single_Image_Super_Resolution/assets/36434536/e1faf3e4-75c6-4127-8255-1d9c22719930?raw=True)

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
### Introduction
Classical image enhancement techniques such as nearest-neighbor, bilinear and bicubic interpolation produce poor results for upscaling given images, often leading to blurred edges and low image contrast. So in recent years, through the general development of generative models, artificial intelligence has applied itself naturally to the task of image super-resolution. 

Generative Adversarial Networks rose to popularity around five years after their introduction in a research paper published in 2014, eventually seeing a rise in popularity in 2019. In recent years, the trend has begun to shift into using diffusion-based models which offer more stability and higher quality outputs in classical image processing tasks, primarily image upscaling. 

Nevertheless, this project looks to explore and apply known deep learning techniques that have been known to achieve superior visual fidelity and sharpness in upscaled images and videos using state-of-the-art algorithms such as Generative Adversarial Networks and other deep learning models (such as RNNs) for the task of Super Resolution.

### Method

To perform SISO-SR (Single-Image-Single-Output Super Resolution), we use a GAN with a generator and discriminator architecture as shown below.
<p align="center>
  
![image](https://github.com/doobiusP/Single_Image_Super_Resolution/assets/36434536/18949d5a-5ea8-4333-aa2f-2f36f4674803)

*<p align="center"><font size="-2"> Fig 1. Generator </font></p>*

![image](https://github.com/doobiusP/Single_Image_Super_Resolution/assets/36434536/f6edd6e8-43a5-4e8f-ae4a-9c0aca0c8584)

*<p align="center"><font size="-2"> Fig 2. Discriminator</font></p>*
</p>
The main block of the generator lies in the list of residual blocks connected sequentially. Upscaling is done via Pixel Shuffling layers. Bicubically upscaling the original input image as a baseline for the output allows for color-correct output images. Optional post-processing such as sharpening can be done.

### Results:
<p align="center">
![image](https://github.com/doobiusP/Single_Image_Super_Resolution/assets/36434536/eb82c8e3-ebcf-4896-bc59-bff5dd6a3a4a)
![image](https://github.com/doobiusP/Single_Image_Super_Resolution/assets/36434536/8e11d509-4eed-4021-bc63-8d06c21da190)
*<p><font size="-2"> Fig 3. Website developed for the model using Flask.</font></p>*

![image](https://github.com/doobiusP/Single_Image_Super_Resolution/assets/36434536/67cdd0d3-2438-44a3-9b76-52b0c0de46e6?raw=True)
*<p><font size="-2"> Fig 4. Example output image. Note the high SSIM value.</font></p>*
</p>

The SRGAN model was tested using a completely new dataset consisting of about 76 images, of various objects, animals, places and people. The model was then fed the test dataset and the evaluation metrics (PSNR and SSIM) were calculated and printed between the upscaled image and the original high resolution image.
* Average PSNR value: 23.048
* Average SSIM value: 0.9438

### Conclusion:

SRGAN was successfully implemented with results surpassing that of the original research paper on which the project was based owing to custom modifications made. With a larger dataset and more training time, the model can be deployed for use in commercial image editing software.

### Technologies/Libraries/Frameworks used:
* Numpy
* PyTorch
* Matplotlib
* Pillow
* Flask
* HTML
* CSS

### Associated links:
* <a href="https://www.kaggle.com/code/doobiusp/srgan">Kaggle Code</a>
* <a href="https://www.kaggle.com/datasets/doobiusp/various-ordered-images-for-super-resolution-task">Kaggle Dataset </a>

### References:
* <a href="https://arxiv.org/abs/1609.04802">Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network</a>
* <a href="https://youtu.be/1HqjPqNglPc?si=ezqEiYBfKW1Wtv_I">256 - Super resolution GAN (SRGAN) in keras </a>
* <a href="https://medium.com/@neetu.sigger/a-comprehensive-guide-to-understanding-and-implementing-bottleneck-residual-blocks-6b420706f66b">More information on bottlenecked residual blocks</a>

