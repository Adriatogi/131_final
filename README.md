# Segmenting Graffiti in Images
This project was done for CS131: Computer Vision Foundations and Applications, a course at Stanford called.

- Complete research paper for this project can be found here: [LINK TO PAPER](https://drive.google.com/file/d/1eMi7NTLBB8pNiUDSQkmxQzuDKxImdsKw/view?usp=sharing)
- Model can be found here: [LINK TO MODEL](https://huggingface.co/Adriatogi/segformer-b0-finetuned-segments-graffiti)
- Dataset can be found here: [LINK TO DATASET](https://huggingface.co/datasets/Adriatogi/graffiti)

## Files
- [cs131_final_model.ipynb](cs131_final_model.ipynb): This file contains the loading of the dataset, the training, evaluation, and uploading of the fine-tuned model. It was made to run on colab. 
- [data/](data/): data directory for images and labels. Annotations/ are taken and turned into respective masks/ for imgs/. New_imgs/ are images that can be tested that arent in the hugging face dataset.
- [dataset_creation.ipynb](dataset_creation.ipynb): Process annotations and images to create a dataset that is uploaded to hugging face
- [initial_exploration.ipynb](initial_exploration.ipynb): I explored the task of segmenting graffiti through other methods, such as kmeans segmentation, edge and region segmentation, and watershed segmentation. They would prove unsuccesful to adequately segment an image. This file is optional
- [get_data.ipynb](get_data.ipynb): This notebook was made to live in https://huggingface.co/datasets/artificialhoney/graffiti. It is meant to page through the graffiti dataset so I can pick out suitable images for my dataset.


## Abstract
This paper presents an implementation of SegFormer, a pre-trained segmentation model compromised of Transformer encoders and multi-layer perceptron (MLP) decoders, to segment graffiti from images. To achieve this, we had to first create a dataset of graffiti images with respective labels. We would then use this dataset to train our model to acheive a 92\% test accuracy in segmenting graffiti from images.

## Introduction
Graffiti is art that is written or painted onto a surface, commonly without permission from the owner of said surface. Oftentimes, graffiti is seen as an illegal activity with no substantial impact, but one can't dismiss cultural importance and impact it has on communities worldwide. Separately, image segmentation is when an image is broken up into multiple segments as to further extract important information or to separate parts of the image from each other. This paper seeks to be able to segment graffiti in images such that an image will be segmented into two parts, the graffiti piece and the non-graffiti part. The goal of this paper is to provide means to further engage with graffiti in a meaningful and productive way. Alternative ways of working with graffiti have already been developed, such as using computer vision for the policing of graffiti. 

Furthermore, this paper seeks to explore alternative methods for segmentation, such as the use of SegFormer instead of the CNN standard. As well, SegFormer is a pre-trained model, meaning that complex segmentation is made more accessible and can be leveraged by fine-tuning. 
