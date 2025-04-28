<div align="center">
VIETNAM NATIONAL UNIVERSITY, HO CHI MINH CITY
<br />
UNIVERSITY OF TECHNOLOGY
<br />
FACULTY OF COMPUTER SCIENCE AND ENGINEERING
<br />
<br />

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/HCMUT_official_logo.png/238px-HCMUT_official_logo.png)](https://www.hcmut.edu.vn/vi)
<br />
<br />
**Machine Learning / Semester 242**
<br/>

</div>

# Project: AI Detector for distinguishing real and AI-generated images
## Team members
| No. | Name             | Student ID | Email                          | Contact                                                                                                                                                                                                                     |
| :-: | ---------------- | :--------: | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  1  | Nguyễn Hữu Huy Thịnh     |  2213291   | thinh.nguyenhuuhuy@hcmut.edu.vn        |  [<img src="https://cdn-icons-png.flaticon.com/512/733/733609.png" align="left" width=20px style="margin-left:5px" />][git1]|
|  2  | Nguyễn Anh Khoa  |   2211612   | khoa.nguyenanh0807@hcmut.edu.vn   | [<img src="https://cdn-icons-png.flaticon.com/512/733/733609.png" align="left" width=20px style="margin-left:5px" />][git2]|

[git1]: https://github.com/shInNei/
[git2]: https://github.com/Khoawawa/

## Introduction to Problem
The rapid advancement of generative models like GANs and diffusion models has made it difficult to distinguish real images from AI-generated ones. This poses challenges in areas such as misinformation and digital trust. Our project aims to develop an AI detector that can accurately classify images as real or synthetic, helping to promote authenticity in digital media.
## Data Analysis
In this section, we analyze the dataset to better understand its structure and quality. A thorough analysis helps in identifying potential issues and guides preprocessing and modeling strategies.

The following key aspects are covered:
* **File Integrity**: Check for missing values and ensure all referenced image files exist.
* **Dataset Properties**: Study basic attributes such as image dimensions, file count, and formats.
* **Class Balance**: Examine the distribution between real and AI-generated images to ensure a balanced dataset.
* **Pairing Violations Check**: Verify if image pairs are correctly paired according to the expected labels.
* **Pair Completeness Check**: Ensure every pair should have exactly 2 images.
* **Visual and Metadata Analysis**: Explore metadata like image size and visually inspect sample images.
* **Pixel Intensity Distribution**: Compare pixel value distributions across the classes to understand visual differences.

For a detailed breakdown, refer to the `Analysis.ipynb` notebook — you can find the file in this folder. To run this notebook, simply open the file and execute the cells in sequence. Since this notebook is implemented on Google Colab, the best way to run it is by opening it directly on Colab and executing the cells.
## XGBoost
In this section, we apply the **XGBoost** algorithm — a powerful and efficient gradient boosting framework — to classify images as either real (human-generated) or AI-generated based on extracted features.

For a detailed breakdown, refer to the `XGBoostTraining`.ipynb notebook - you can find the file in this folder. To run this notebook, simply open the file and execute the cells in sequence. Since this notebook is implemented on Google Colab, the best way to run it is by opening it directly on Colab and executing the cells.
## ResNet
In this section, we apply the **ResNet** (Residual Network) architecture — a deep convolutional neural network with residual connections — to classify images as either real (human-generated) or AI-generated. By fine-tuning a pre-trained ResNet model, we adapt it to our binary classification task and leverage its powerful feature extraction capabilities.

For a detailed breakdown, refer to the `CNN.ipynb` notebook — you can find the file in this folder. To run this notebook, simply open the file and execute the cells in sequence. Since this notebook is implemented on Google Colab, the best way to run it is by opening it directly on Colab and executing the cells.

## Models Evaluation
In this section, after applying both the **XGBoost** method and the **ResNet** method to detect real and AI-generated images, we will perform evaluation and comparison between the two models to determine which one performs better.

For a detailed breakdown, refer to the `Evaluation.ipynb` notebook — you can find the file in this folder.  
To run this notebook, simply open the file and execute the cells sequentially. Since this notebook is implemented on Google Colab, the best way to run it is by opening it directly on Colab and executing the cells.

## Conclusion
This project aimed to research effective methods for detecting real versus AI-generated images, addressing the rising concerns of deepfakes and synthetic media. Two models, XGBoost and ResNet, were explored for this task. XGBoost yielded moderate results, while ResNet outperformed it significantly, demonstrating superior ability in accurately classifying images due to its deep learning architecture. The findings underscore the importance of developing reliable systems for identifying synthetic content, particularly as AI-generated images present growing challenges to security and trust. Future work can expand this research to include diverse media types, such as videos, further enhancing the detection of AI-generated content.
