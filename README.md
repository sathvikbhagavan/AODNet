# AODNet

## All in one Dehazing net

End to end Deep Learning Model to remove haze from images written in Tensorflow 2.1

Requirements:
Tensorflow, OpenCV, Numpy, Streamlit, Pillow

To test, download the code, install all requirements and run the streamlit web application as:

#### streamlit run aod_webapp.py 

you can upload your image and get the haze free image and download it


Dataset used was : https://sites.google.com/site/boyilics/website-builder/project-page

### Examples 

![Exmaple-1](/test_images/test-1.jpg)  ![Exmaple-1](/test_images/test-1-output.jpeg) 

![Exmaple-2](/test_images/test-2.jpg)  ![Exmaple-2](/test_images/test-2-output.jpeg)

![Exmaple-3](/test_images/test-3.jpg)  ![Exmaple-1](/test_images/test-3-output.jpeg) 

![Exmaple-1](/test_images/test-4.jpg)  ![Exmaple-1](/test_images/test-4-output.jpeg) 

### References

```
@InProceedings{Li_2017_ICCV,
author = {Li, Boyi and Peng, Xiulian and Wang, Zhangyang and Xu, Jizheng and Feng, Dan},
title = {AOD-Net: All-In-One Dehazing Network},
booktitle = {The IEEE International Conference on Computer Vision (ICCV)},
month = {Oct},
year = {2017}
}
```


