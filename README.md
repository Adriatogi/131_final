# Segmenting Graffiti in Images
This project was done for CS131: Computer Vision Foundations and Applications, a course at Stanford called.

- Complete research paper for this project can be found here: [LINK TO PAPER](https://drive.google.com/file/d/1eMi7NTLBB8pNiUDSQkmxQzuDKxImdsKw/view?usp=sharing)
- Model can be found here: [LINK TO MODEL](https://huggingface.co/Adriatogi/segformer-b0-finetuned-segments-graffiti)
- Dataset can be found here: [LINK TO DATASET](https://huggingface.co/datasets/Adriatogi/graffiti)

## Files
- [initial_exploration.ipynb](initial_exploration.ipynb): I explored the task of segmenting graffiti through other methods, such as kmeans segmentation, edge and region segmentation, and watershed segmentation. They would prove unsuccesful to adequately segment an image. This file is optional

## Abstract
This paper presents an implementation of SegFormer, a pre-trained segmentation model compromised of Transformer encoders and multi-layer perceptron (MLP) decoders, to segment graffiti from images. To achieve this, we had to first create a dataset of graffiti images with respective labels. We would then use this dataset to train our model to acheive a 92\% test accuracy in segmenting graffiti from images.

## Introduction
Graffiti is art that is written or painted onto a surface, commonly without permission from the owner of said surface. Oftentimes, graffiti is seen as an illegal activity with no substantial impact, but one can't dismiss cultural importance and impact it has on communities worldwide. Separately, image segmentation is when an image is broken up into multiple segments as to further extract important information or to separate parts of the image from each other. This paper seeks to be able to segment graffiti in images such that an image will be segmented into two parts, the graffiti piece and the non-graffiti part. The goal of this paper is to provide means to further engage with graffiti in a meaningful and productive way. Alternative ways of working with graffiti have already been developed, such as using computer vision for the policing of graffiti. 

Furthermore, this paper seeks to explore alternative methods for segmentation, such as the use of SegFormer instead of the CNN standard. As well, SegFormer is a pre-trained model, meaning that complex segmentation is made more accessible and can be leveraged by fine-tuning. 
