# Day 10: *Neural Networks & Deep Learning: From Theory to Biomedical Applications*

## Overview
This day covers the foundations and applications of deep learning for biomedical research. We explore neural network architectures from feedforward networks to transformers, with emphasis on practical implementation and real-world neuroscience applications:

1. **Introduction to Deep Learning** - History, motivation, core concepts, and why deep learning matters for neuroscience
2. **Feedforward Neural Networks** - Architecture, training, regularization, and applications to tabular biomedical data
3. **Convolutional Neural Networks** - Image analysis, classic architectures (ResNet, U-Net), medical imaging applications
4. **Recurrent Neural Networks** - Sequence modeling, LSTM/GRU, time series analysis, EEG/clinical data applications
5. **Transformers & Attention** - Modern architectures, self-attention, protein language models, AlphaFold case study
6. **Advanced Architectures** - Graph Neural Networks, Variational Autoencoders, Generative Adversarial Networks
7. **Practical Considerations** - Training strategies, hyperparameter tuning, debugging, interpretability
8. **Framework Comparisons** - PyTorch vs TensorFlow vs JAX, when to use each

## Lecture Materials
- **Slides**: Available from [this link](https://slides.com/renatocfduarte/scientific-programming-10-neural-networks-and-deep-learning/scroll?token=5L6W9MWn&chrome=hidden)
- **PDF**: Download from [this link](https://drive.google.com/file/d/1hYNG6j4uS6yVJXOew2-fULCB-_W22TD9/view?usp=sharing)
- **Notebooks**: Interactive demonstrations in the [`notebooks/`](notebooks/) directory
- **Detailed Handout**: [day10_handout.md](day10_handout.md), also available as [PDF](https://drive.google.com/file/d/1a6Ihrxs08OaswQx_QEVMTvB9YEBUpxXj/view?usp=sharing). Comprehensive reference material covering all concepts.

**NOTE:** due to the depth and complexity of the subject, this material is quite extensive. We recommend working through it systematically and not trying to cover everything in one session. We did not incorporate exercises, as it makes more sense for you to explore the complete examples provided in the notebooks and handout.

## Learning Objectives

By the end of this day, you will be able to:
- Understand the fundamental principles of deep learning and backpropagation
- Choose appropriate architectures for different data types (tabular, images, sequences)
- Implement feedforward, convolutional, and recurrent neural networks in PyTorch
- Apply transfer learning with pre-trained models to biomedical tasks
- Train and evaluate deep learning models with proper validation strategies
- Use U-Net for medical image segmentation
- Build LSTM/GRU models for time series and sequence analysis
- Understand attention mechanisms and transformer architectures
- Apply protein language models (ESM-2) to sequence analysis
- Implement regularization techniques (dropout, batch normalization, weight decay)
- Debug training issues (vanishing/exploding gradients, overfitting)
- Interpret model predictions and understand what networks learn
- Navigate the PyTorch ecosystem and use pre-trained models

## Session Structure
The day combines theoretical foundations with extensive hands-on practice. Work through the handout material first to understand the concepts, then implement the examples in the notebooks to build practical skills. 


## Additional Resources
- **PyTorch Tutorials**: pytorch.org/tutorials
- **Deep Learning Book**: deeplearningbook.org (Goodfellow, Bengio, Courville)
- **ESM Protein Models**: github.com/facebookresearch/esm
- **Medical Imaging Datasets**: medicaldecathlon.com
- **Papers with Code**: paperswithcode.com (implementations of latest research)
