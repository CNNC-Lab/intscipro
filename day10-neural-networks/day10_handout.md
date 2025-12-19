# Lecture 10: Neural Networks and Deep Learning
## Theory, Implementation, and Biomedical Applications
*PhD Course in Integrative Neurosciences - Introduction to Scientific Programming*

---

## Table of Contents

1. [Introduction to Deep Learning](#1-introduction-to-deep-learning)
2. [Feedforward Neural Networks](#2-feedforward-neural-networks)
3. [Convolutional Neural Networks](#3-convolutional-neural-networks)
4. [Recurrent Neural Networks](#4-recurrent-neural-networks)
5. [Transformers and Attention Mechanisms](#5-transformers-and-attention-mechanisms)
6. [Advanced Architectures](#6-advanced-architectures)
7. [Practical Considerations](#7-practical-considerations)
8. [Case Study: AlphaFold](#8-case-study-alphafold)
9. [Framework Comparisons](#9-framework-comparisons)
10. [Resources and Further Reading](#10-resources-and-further-reading)

---

## 1. Introduction to Deep Learning

### 1.1 What is Deep Learning?

Deep learning is a subset of machine learning that uses artificial neural networks with multiple layers (hence "deep") to automatically learn hierarchical representations from data. Unlike traditional machine learning methods that require manual feature engineering, deep learning models can automatically discover relevant features from raw data.

**Key Characteristics:**
- **Hierarchical learning:** Early layers learn simple features, deeper layers learn complex patterns
- **End-to-end learning:** Learns directly from inputs to outputs without manual feature extraction
- **Scalability:** Performance improves with more data and computation
- **Flexibility:** Same architecture can be adapted to different tasks

### 1.2 Why Deep Learning?

Deep learning has transformed scientific research in several ways:

1. **Data Analysis:** Automated analysis of imaging data, electrophysiology recordings
2. **Pattern Recognition:** Identifying patterns in complex datasets across all scientific domains
3. **Predictive Modeling:** Forecasting outcomes from high-dimensional data
4. **Hypothesis Generation:** Discovering unexpected relationships in complex datasets
5. **Tool Development:** Building automated analysis pipelines for scientific data

**Examples across domains:**
- Automatic segmentation of neurons from microscopy images (Neuroscience)
- Decoding mental states from fMRI data (Neuroscience)
- Predicting epileptic seizures from EEG (Neuroscience)
- Classifying cell types from gene expression profiles (Biology)
- Protein structure prediction (AlphaFold) for understanding synaptic proteins (Biochemistry)
- Drug discovery and molecular property prediction (Chemistry/Pharmacology)
- Climate pattern analysis and weather forecasting (Environmental Science)

### 1.3 The Deep Learning Revolution

**Timeline:**
- **1943:** McCulloch-Pitts neuron (first computational model)
- **1958:** Perceptron (Rosenblatt)
- **1986:** Backpropagation popularized (Rumelhart, Hinton, Williams)
- **1989:** Convolutional Neural Networks (LeCun - LeNet)
- **1997:** LSTM for sequence modeling (Hochreiter & Schmidhuber)
- **2012:** AlexNet wins ImageNet (deep learning breakthrough)
- **2017:** Transformers introduced (Vaswani et al.)
- **2020:** AlphaFold 2 solves protein folding
- **2022:** ChatGPT brings transformers to mainstream
- **2024:** AlphaFold 3, multimodal models dominate

### 1.4 Core Concepts

#### 1.4.1 Neural Network Basics

A neural network consists of:
- **Input layer:** Receives raw data
- **Hidden layers:** Transform inputs through learned representations
- **Output layer:** Produces predictions

Each layer contains **neurons** (nodes) connected by **weights** that are learned during training.

#### 1.4.2 Forward Propagation

Data flows through the network:
```
Input → Layer 1 → Layer 2 → ... → Layer N → Output
```

At each layer:
1. Weighted sum: z = Wx + b
2. Activation function: a = σ(z)

#### 1.4.3 Backpropagation

Learning happens by:
1. Computing loss (error) on training examples
2. Computing gradients of loss w.r.t. weights (chain rule)
3. Updating weights to reduce loss (gradient descent)

**Mathematical Foundation:**

Given loss L, weight w, we update:
```
w_new = w_old - learning_rate × ∂L/∂w
```

Gradients are computed efficiently using the **chain rule**:
```
∂L/∂w_layer1 = ∂L/∂output × ∂output/∂layer2 × ∂layer2/∂layer1 × ∂layer1/∂w_layer1
```

#### 1.4.4 Activation Functions

Activation functions introduce non-linearity, allowing networks to learn complex patterns.

**Common Activation Functions:**

1. **ReLU (Rectified Linear Unit):**
   - Formula: f(x) = max(0, x)
   - Most popular for hidden layers
   - Fast to compute, helps avoid vanishing gradients
   - Dead ReLU problem: neurons can get stuck at 0

2. **Sigmoid:**
   - Formula: σ(x) = 1 / (1 + e^(-x))
   - Output range: (0, 1)
   - Used for binary classification outputs
   - Suffers from vanishing gradients for large |x|

3. **Tanh (Hyperbolic Tangent):**
   - Formula: tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))
   - Output range: (-1, 1)
   - Zero-centered (better than sigmoid)
   - Still has vanishing gradient problem

4. **Softmax:**
   - Formula: softmax(x_i) = e^(x_i) / Σ_j e^(x_j)
   - Converts logits to probability distribution
   - Used for multi-class classification outputs

5. **Leaky ReLU:**
   - Formula: f(x) = x if x > 0, else α*x (typically α=0.01)
   - Addresses dead ReLU problem
   - Small gradient for negative values

6. **GELU (Gaussian Error Linear Unit):**
   - Formula: f(x) = x × Φ(x), where Φ is standard normal CDF
   - Smooth, non-monotonic
   - Popular in transformers

#### 1.4.5 Loss Functions

Loss functions measure prediction error and guide learning.

**For Classification:**

1. **Binary Cross-Entropy:**
   ```
   L = -[y log(ŷ) + (1-y) log(1-ŷ)]
   ```
   Used for binary classification (y ∈ {0,1})

2. **Categorical Cross-Entropy:**
   ```
   L = -Σ_i y_i log(ŷ_i)
   ```
   Used for multi-class classification (one-hot encoded labels)

3. **Sparse Categorical Cross-Entropy:**
   Same as above but with integer labels instead of one-hot

**For Regression:**

1. **Mean Squared Error (MSE):**
   ```
   L = (1/n) Σ_i (y_i - ŷ_i)²
   ```
   Standard for regression, sensitive to outliers

2. **Mean Absolute Error (MAE):**
   ```
   L = (1/n) Σ_i |y_i - ŷ_i|
   ```
   More robust to outliers than MSE

3. **Huber Loss:**
   Combines MSE and MAE, robust to outliers

#### 1.4.6 Optimization Algorithms

**Gradient Descent Variants:**

1. **Stochastic Gradient Descent (SGD):**
   ```python
   w = w - learning_rate * gradient
   ```
   - Updates weights after each example
   - Noisy but can escape local minima
   - Often enhanced with momentum:
     ```python
     velocity = beta * velocity + gradient
     w = w - learning_rate * velocity
     ```

2. **Adam (Adaptive Moment Estimation):**
   ```python
   m = beta1 * m + (1-beta1) * gradient  # First moment
   v = beta2 * v + (1-beta2) * gradient²  # Second moment
   m_hat = m / (1 - beta1^t)  # Bias correction
   v_hat = v / (1 - beta2^t)
   w = w - learning_rate * m_hat / (sqrt(v_hat) + epsilon)
   ```
   - Adapts learning rate per parameter
   - Combines momentum and RMSProp
   - Default choice for most tasks
   - Typical values: beta1=0.9, beta2=0.999, lr=1e-3

3. **AdamW (Adam with Weight Decay):**
   - Fixes weight decay implementation in Adam
   - Better generalization than standard Adam
   - Recommended for transformers

**Learning Rate Scheduling:**

1. **Step Decay:** Reduce LR by factor every N epochs
2. **Exponential Decay:** LR = LR₀ × e^(-kt)
3. **Cosine Annealing:** Smooth cosine decrease
4. **ReduceLROnPlateau:** Reduce when validation loss plateaus

---

## 2. Feedforward Neural Networks

### 2.1 Architecture

Feedforward Neural Networks (FFNs), also called **Multi-Layer Perceptrons (MLPs)**, are the simplest deep learning architecture. Information flows in one direction: input → hidden layers → output (no cycles).

**Structure:**
```
Input Layer (features)
    ↓
Hidden Layer 1 (neurons with activation)
    ↓
Hidden Layer 2 (neurons with activation)
    ↓
    ...
    ↓
Output Layer (predictions)
```

**Mathematical Formulation:**

For a network with L layers:
```
Layer 1: h₁ = σ(W₁x + b₁)
Layer 2: h₂ = σ(W₂h₁ + b₂)
...
Layer L: ŷ = σ(W_L h_(L-1) + b_L)
```

Where:
- x: input vector
- W_i: weight matrix for layer i
- b_i: bias vector for layer i
- σ: activation function
- h_i: hidden layer activations
- ŷ: output predictions

### 2.2 When to Use FFNs

**✓ Best For:**
- Tabular data (structured features)
- Feature-based inputs (already engineered features)
- Classification or regression tasks
- Small to medium datasets
- When interpretability is important (with proper techniques)

**✗ Not Ideal For:**
- Images (use CNNs instead)
- Sequences/time series (use RNNs/Transformers)
- Graph-structured data (use GNNs)
- Very high-dimensional raw data

### 2.3 Biomedical Applications

1. **Gene Expression Analysis:**
   - Input: Gene expression levels (RNA-seq, microarray)
   - Task: Classify cell types, disease states, or predict drug response
   - Architecture: Input (genes) → Hidden layers → Output (classes)

2. **Clinical Prediction:**
   - Input: Patient features (age, lab results, vitals)
   - Task: Predict disease risk, mortality, treatment response
   - Example: ICU mortality prediction from electronic health records

3. **Drug Discovery:**
   - Input: Molecular descriptors, fingerprints
   - Task: Predict drug-target binding, toxicity, bioactivity
   - Often combined with more complex architectures

### 2.4 Implementation in PyTorch

```python
import torch
import torch.nn as nn
import torch.optim as optim

class FeedforwardNN(nn.Module):
    def __init__(self, input_dim, hidden_dims, output_dim, dropout=0.3):
        """
        Feedforward neural network with multiple hidden layers.
        
        Args:
            input_dim: Number of input features
            hidden_dims: List of hidden layer sizes [128, 64, 32]
            output_dim: Number of output classes/values
            dropout: Dropout probability for regularization
        """
        super().__init__()
        
        # Build layers dynamically
        layers = []
        prev_dim = input_dim
        
        for hidden_dim in hidden_dims:
            layers.append(nn.Linear(prev_dim, hidden_dim))
            layers.append(nn.BatchNorm1d(hidden_dim))  # Normalize activations
            layers.append(nn.ReLU())
            layers.append(nn.Dropout(dropout))
            prev_dim = hidden_dim
        
        # Output layer (no activation here, applied externally)
        layers.append(nn.Linear(prev_dim, output_dim))
        
        self.network = nn.Sequential(*layers)
    
    def forward(self, x):
        return self.network(x)

# Example: Gene expression classification
input_dim = 2000  # 2000 genes
hidden_dims = [512, 256, 128]
output_dim = 5  # 5 cell types

model = FeedforwardNN(input_dim, hidden_dims, output_dim)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-4)

# Training loop
model.train()
for epoch in range(num_epochs):
    for batch_x, batch_y in dataloader:
        # Forward pass
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)
        
        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

### 2.5 Key Techniques

#### 2.5.1 Regularization

**Prevents overfitting** (memorizing training data instead of learning general patterns)

1. **Dropout:**
   - Randomly set fraction of neurons to 0 during training
   - Forces network to learn redundant representations
   - Typical values: 0.2-0.5
   ```python
   nn.Dropout(p=0.3)  # Drop 30% of neurons
   ```

2. **L1/L2 Weight Regularization:**
   - Add penalty to loss based on weight magnitudes
   - L1: Encourages sparsity (many weights → 0)
   - L2: Encourages small weights (weight decay)
   ```python
   optimizer = optim.AdamW(model.parameters(), weight_decay=1e-4)  # L2
   ```

3. **Early Stopping:**
   - Stop training when validation loss stops improving
   - Prevents overfitting to training set
   ```python
   if val_loss < best_val_loss:
       best_val_loss = val_loss
       patience_counter = 0
   else:
       patience_counter += 1
       if patience_counter >= patience:
           break  # Stop training
   ```

4. **Batch Normalization:**
   - Normalizes layer inputs to mean=0, std=1
   - Stabilizes training, allows higher learning rates
   - Acts as mild regularizer
   ```python
   nn.BatchNorm1d(hidden_dim)
   ```

#### 2.5.2 Architecture Design

**Depth vs Width Trade-off:**

- **Deep (many layers):** Better at learning hierarchical features
  - Example: 5 layers of 128 neurons each
  - Good for: Complex patterns, large datasets
  
- **Wide (large layers):** More parameters per layer
  - Example: 2 layers of 512 neurons each
  - Good for: Feature-rich tabular data

**Tapering Architecture:**
Common pattern: gradually reduce layer sizes
```
Input (2000) → 512 → 256 → 128 → 64 → Output (5)
```
Intuition: Compress information into increasingly abstract representations

### 2.6 Common Issues and Solutions

| Issue | Symptoms | Solutions |
|-------|----------|-----------|
| **Vanishing Gradients** | Training stalls, early layers don't learn | Use ReLU, batch normalization, residual connections |
| **Exploding Gradients** | Loss becomes NaN, unstable training | Gradient clipping, lower learning rate |
| **Overfitting** | High training accuracy, low validation accuracy | Dropout, L2 regularization, more data, early stopping |
| **Underfitting** | Low training and validation accuracy | Larger model, more layers, train longer, reduce regularization |
| **Class Imbalance** | Model predicts majority class only | Weighted loss, oversampling, SMOTE |

---

## 3. Convolutional Neural Networks

### 3.1 Architecture and Motivation

Convolutional Neural Networks (CNNs) are designed for data with **spatial structure**, especially images. Unlike FFNs that treat each pixel independently, CNNs exploit:

1. **Local connectivity:** Nearby pixels are related
2. **Translation invariance:** Features (edges, textures) appear anywhere in image
3. **Hierarchical patterns:** Simple features (edges) → Complex patterns (objects)

**Key Advantages:**
- **Parameter efficiency:** Share weights across spatial locations
- **Feature learning:** Automatically discover visual patterns
- **Scalability:** Handle high-resolution images

### 3.2 Core Components

#### 3.2.1 Convolutional Layers

**Concept:** Slide a small filter (kernel) across the image, computing dot products.

**Mathematical Operation:**
```
Output(i,j) = Σ_m Σ_n Input(i+m, j+n) × Kernel(m, n) + bias
```

**Key Parameters:**
- **Kernel size:** 3×3, 5×5, 7×7 (odd numbers preferred)
- **Stride:** Step size when sliding (1 = slide by 1 pixel)
- **Padding:** Add zeros around borders to maintain dimensions
  - Same padding: Output size = Input size
  - Valid padding: Output size < Input size (no padding)
- **Number of filters:** How many different patterns to detect

**Example:**
```python
# Detect edges, textures, patterns
conv1 = nn.Conv2d(in_channels=3,    # RGB input
                  out_channels=64,   # Learn 64 different filters
                  kernel_size=3,     # 3×3 filters
                  stride=1,
                  padding=1)         # Same padding
```

**What Filters Learn:**
- **Layer 1 (early):** Edges, colors, simple textures
- **Layer 2-3 (middle):** Shapes, patterns, parts of objects
- **Layer 4+ (late):** Object parts, complete objects, complex patterns

#### 3.2.2 Pooling Layers

**Purpose:** Reduce spatial dimensions, increase receptive field, provide translation invariance.

**Types:**

1. **Max Pooling:**
   - Takes maximum value in each window
   - Most common, preserves strongest activations
   ```python
   pool = nn.MaxPool2d(kernel_size=2, stride=2)  # Halves H and W
   ```

2. **Average Pooling:**
   - Takes average value in window
   - Smoother, less aggressive downsampling
   ```python
   pool = nn.AvgPool2d(kernel_size=2, stride=2)
   ```

3. **Global Average Pooling:**
   - Average entire feature map to single value
   - Replaces fully connected layers, reduces parameters
   ```python
   pool = nn.AdaptiveAvgPool2d((1, 1))  # Output: 1×1 per channel
   ```

**Effect:**
- Input: 128×128 → MaxPool(2×2) → Output: 64×64
- Reduces computation, increases receptive field

#### 3.2.3 Fully Connected Layers

After convolutional and pooling layers extract features, fully connected (FC) layers perform classification/regression.

**Typical Pattern:**
```
Convolutional Backbone (feature extraction)
    ↓
Flatten (convert 3D to 1D)
    ↓
Fully Connected Layers (classification)
    ↓
Output (predictions)
```

### 3.3 Classic CNN Architectures

#### 3.3.1 LeNet-5 (1998)

- First successful CNN for digit recognition (MNIST)
- Architecture: Conv → Pool → Conv → Pool → FC → FC
- Historical importance, now outdated

#### 3.3.2 AlexNet (2012)

- ImageNet winner, sparked deep learning revolution
- Innovations: ReLU, Dropout, GPU training, Data augmentation
- 8 layers: 5 convolutional + 3 fully connected

#### 3.3.3 VGGNet (2014)

- Very deep (16-19 layers), simple design
- Stacks many 3×3 conv layers
- Shows depth is important
- Large parameter count

#### 3.3.4 ResNet (2015)

**Revolutionary Innovation:** Residual connections (skip connections)

**Problem Solved:** Vanishing gradients in very deep networks

**Residual Block:**
```
       Input
         |
    [Conv-BN-ReLU-Conv-BN]
         |
         ↓ (add)
       Output = F(x) + x
```

**Mathematical Formulation:**
```
H(x) = F(x) + x
```
where F(x) is learned residual mapping

**Why It Works:**
- If identity mapping is optimal, network just needs to learn F(x) = 0
- Easier to learn residuals than full mapping
- Gradients flow directly through skip connections

**Variants:**
- ResNet-18, ResNet-34: Shallower, faster
- ResNet-50, ResNet-101, ResNet-152: Deeper, more accurate

**Code:**
```python
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv1 = nn.Conv2d(channels, channels, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(channels)
        self.conv2 = nn.Conv2d(channels, channels, 3, padding=1)
        self.bn2 = nn.BatchNorm2d(channels)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        residual = x
        out = self.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out += residual  # Skip connection
        out = self.relu(out)
        return out
```

#### 3.3.5 U-Net (2015)

**Designed for:** Medical image segmentation

**Architecture:** Encoder-decoder with skip connections

**Structure:**
```
Encoder (contracting path):
  Conv → Conv → MaxPool → ... (down-sample, learn features)
  
Decoder (expanding path):
  UpConv → Conv → Conv → ... (up-sample, refine localization)
  
Skip Connections:
  Encoder features → Decoder (preserve spatial detail)
```

**Why Important:**
- Combines global context (encoder) with precise localization (decoder)
- Skip connections recover spatial information lost in pooling
- State-of-the-art for medical image segmentation

**Applications:**
- Cell segmentation in microscopy
- Tumor segmentation in MRI/CT
- Neuron tracing in electron microscopy

### 3.4 Biomedical Applications

#### 3.4.1 Medical Image Analysis

1. **Cell/Nucleus Segmentation:**
   - Input: Microscopy images
   - Output: Pixel-wise masks of cells
   - Architecture: U-Net
   - Enables automated cell counting, morphology analysis

2. **Tumor Detection:**
   - Input: MRI, CT, X-ray images
   - Output: Tumor location and boundaries
   - Architecture: ResNet + U-Net
   - Clinical impact: Faster diagnosis, second opinion

3. **Brain MRI Analysis:**
   - Tissue segmentation (gray/white matter, CSF)
   - Lesion detection (MS, stroke, tumors)
   - Disease classification (Alzheimer's staging)

#### 3.4.2 Microscopy Image Analysis

1. **Neuron Reconstruction:**
   - Trace neuron morphology from confocal/2-photon microscopy
   - Architecture: U-Net variants
   - Application: Understand neural circuit structure

2. **Calcium Imaging Analysis:**
   - Detect active neurons from fluorescence videos
   - Architecture: 3D CNNs (Conv3D) for spatiotemporal data
   - Application: Decode neural population activity

3. **Synaptic Counting:**
   - Identify and count synapses in electron microscopy
   - Architecture: Object detection networks (Faster R-CNN)
   - Application: Study synaptic plasticity, disease

#### 3.4.3 Histopathology

1. **Cancer Grading:**
   - Classify tumor aggressiveness from tissue slides
   - Architecture: ResNet-50 pre-trained on ImageNet
   - Clinical workflow integration

2. **Cell Type Classification:**
   - Identify different cell types in tissue samples
   - Transfer learning from natural images

### 3.5 Implementation Example: U-Net

```python
class UNet(nn.Module):
    """U-Net for image segmentation."""
    
    def __init__(self, in_channels=1, out_channels=1):
        super().__init__()
        
        # Encoder (contracting path)
        self.enc1 = self.conv_block(in_channels, 64)
        self.pool1 = nn.MaxPool2d(2)
        
        self.enc2 = self.conv_block(64, 128)
        self.pool2 = nn.MaxPool2d(2)
        
        self.enc3 = self.conv_block(128, 256)
        self.pool3 = nn.MaxPool2d(2)
        
        # Bottleneck
        self.bottleneck = self.conv_block(256, 512)
        
        # Decoder (expanding path)
        self.upconv3 = nn.ConvTranspose2d(512, 256, 2, stride=2)
        self.dec3 = self.conv_block(512, 256)  # 512 = 256 (upconv) + 256 (skip)
        
        self.upconv2 = nn.ConvTranspose2d(256, 128, 2, stride=2)
        self.dec2 = self.conv_block(256, 128)
        
        self.upconv1 = nn.ConvTranspose2d(128, 64, 2, stride=2)
        self.dec1 = self.conv_block(128, 64)
        
        # Output
        self.out = nn.Conv2d(64, out_channels, 1)
    
    def conv_block(self, in_ch, out_ch):
        return nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True)
        )
    
    def forward(self, x):
        # Encoder
        enc1 = self.enc1(x)
        enc2 = self.enc2(self.pool1(enc1))
        enc3 = self.enc3(self.pool2(enc2))
        
        # Bottleneck
        bottleneck = self.bottleneck(self.pool3(enc3))
        
        # Decoder with skip connections
        dec3 = self.upconv3(bottleneck)
        dec3 = torch.cat([dec3, enc3], dim=1)  # Skip connection
        dec3 = self.dec3(dec3)
        
        dec2 = self.upconv2(dec3)
        dec2 = torch.cat([dec2, enc2], dim=1)
        dec2 = self.dec2(dec2)
        
        dec1 = self.upconv1(dec2)
        dec1 = torch.cat([dec1, enc1], dim=1)
        dec1 = self.dec1(dec1)
        
        return self.out(dec1)
```

### 3.6 Data Augmentation

**Critical for CNNs:** Increases effective dataset size, improves generalization

**Common Augmentations:**

```python
from torchvision import transforms

train_transforms = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomVerticalFlip(p=0.5),
    transforms.RandomRotation(degrees=15),
    transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.RandomResizedCrop(size=224, scale=(0.8, 1.0)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],  # ImageNet stats
                        std=[0.229, 0.224, 0.225])
])
```

**Biomedical-Specific Augmentations:**
- Elastic deformations (simulate tissue variations)
- Gaussian noise (simulate imaging artifacts)
- Intensity variations (simulate staining differences)

### 3.7 Transfer Learning

**Concept:** Use knowledge learned on one task to improve performance on another

**Why It Works:**
- Early CNN layers learn general features (edges, textures)
- Transfer these to new domains

**Typical Workflow:**

1. **Load Pre-trained Model:**
   ```python
   import torchvision.models as models
   
   # Load ResNet-50 pre-trained on ImageNet
   model = models.resnet50(pretrained=True)
   ```

2. **Freeze Early Layers:**
   ```python
   for param in model.parameters():
       param.requires_grad = False  # Don't update these weights
   ```

3. **Replace Final Layer:**
   ```python
   # Original: 1000 ImageNet classes
   # New: num_classes for our task
   model.fc = nn.Linear(model.fc.in_features, num_classes)
   ```

4. **Fine-tune:**
   ```python
   # Only train the new final layer initially
   optimizer = optim.Adam(model.fc.parameters(), lr=1e-3)
   
   # Later, optionally unfreeze and fine-tune all layers
   for param in model.parameters():
       param.requires_grad = True
   optimizer = optim.Adam(model.parameters(), lr=1e-4)  # Lower LR
   ```

**Transfer Learning Strategies:**

| Strategy | When to Use | Trainable Layers |
|----------|-------------|------------------|
| **Feature Extraction** | Small dataset, similar domain | Only final classifier |
| **Fine-tuning (late layers)** | Medium dataset | Last few layers + classifier |
| **Fine-tuning (all layers)** | Large dataset | All layers (low LR for early) |
| **Train from Scratch** | Very large dataset, very different domain | All layers |

---

## 4. Recurrent Neural Networks

### 4.1 Motivation and Architecture

Recurrent Neural Networks (RNNs) are designed for **sequential data** where order matters. Unlike FFNs/CNNs that process inputs independently, RNNs maintain a "memory" of previous inputs.

**Applications:**
- Time series (EEG, stock prices, weather)
- Text (language modeling, translation)
- Speech (recognition, synthesis)
- Video (action recognition)
- Biological sequences (DNA, protein sequences)

**Key Idea:** Hidden state carries information from previous time steps

**Architecture:**
```
Input sequence: x₁, x₂, x₃, ..., x_T

At each time step t:
  h_t = σ(W_h h_(t-1) + W_x x_t + b)
  y_t = W_y h_t + b_y
  
where:
  h_t: hidden state at time t
  x_t: input at time t
  y_t: output at time t
```

**Visualization:**
```
x₁ → [RNN] → h₁ → y₁
       ↓
x₂ → [RNN] → h₂ → y₂
       ↓
x₃ → [RNN] → h₃ → y₃
```

### 4.2 The Vanishing Gradient Problem

**Challenge:** Standard RNNs struggle with long sequences

**Cause:** Gradients become exponentially small when backpropagating through many time steps

**Mathematical Explanation:**
```
∂L/∂h_1 = ∂L/∂h_T × ∂h_T/∂h_(T-1) × ... × ∂h_2/∂h_1
```

If each gradient term < 1, product → 0 (vanishing)
If each gradient term > 1, product → ∞ (exploding)

**Consequences:**
- Long-term dependencies not learned
- Early sequence information forgotten
- Training becomes unstable

**Solutions:**
1. **LSTM (Long Short-Term Memory):** Designed to avoid vanishing gradients
2. **GRU (Gated Recurrent Unit):** Simplified LSTM variant
3. **Gradient clipping:** Prevent exploding gradients
4. **Better initialization:** Xavier/He initialization

### 4.3 Long Short-Term Memory (LSTM)

**Key Innovation:** Cell state with gating mechanisms to control information flow

**Architecture Components:**

1. **Cell State (C_t):** Long-term memory highway
2. **Hidden State (h_t):** Short-term memory / output
3. **Three Gates:**
   - **Forget Gate (f_t):** What to remove from cell state
   - **Input Gate (i_t):** What new information to add
   - **Output Gate (o_t):** What to output from cell state

**Mathematical Formulation:**

```python
# At time step t:

# Forget gate: decides what to forget from C_(t-1)
f_t = σ(W_f [h_(t-1), x_t] + b_f)

# Input gate: decides what new information to store
i_t = σ(W_i [h_(t-1), x_t] + b_i)
C_tilde_t = tanh(W_C [h_(t-1), x_t] + b_C)  # Candidate values

# Update cell state
C_t = f_t ⊙ C_(t-1) + i_t ⊙ C_tilde_t

# Output gate: decides what to output
o_t = σ(W_o [h_(t-1), x_t] + b_o)
h_t = o_t ⊙ tanh(C_t)

where:
  σ: sigmoid (outputs 0-1, acts as gate)
  tanh: hyperbolic tangent (outputs -1 to 1)
  ⊙: element-wise multiplication
  [h, x]: concatenation
```

**Intuition:**

- **Forget Gate:** "Should I forget that the subject is plural?"
- **Input Gate:** "Should I remember this new subject?"
- **Output Gate:** "Should I output verb agreement information?"

**Why LSTMs Work:**

- Cell state provides uninterrupted gradient flow
- Gates learn what to remember/forget
- Sigmoid outputs (0-1) act as differentiable switches
- Can learn dependencies over 100+ time steps

### 4.4 Gated Recurrent Unit (GRU)

**Simplified LSTM variant** with fewer parameters

**Key Differences:**
- Combines forget and input gates into single "update gate"
- Merges cell state and hidden state
- Fewer parameters, faster training
- Often comparable performance to LSTM

**Mathematical Formulation:**

```python
# Update gate: how much of past to keep
z_t = σ(W_z [h_(t-1), x_t])

# Reset gate: how much of past to forget when computing new content
r_t = σ(W_r [h_(t-1), x_t])

# New content (candidate hidden state)
h_tilde_t = tanh(W [r_t ⊙ h_(t-1), x_t])

# Final hidden state (interpolation between old and new)
h_t = (1 - z_t) ⊙ h_(t-1) + z_t ⊙ h_tilde_t
```

**LSTM vs GRU:**

| Aspect | LSTM | GRU |
|--------|------|-----|
| Parameters | More (3 gates + cell state) | Fewer (2 gates) |
| Training Speed | Slower | Faster |
| Memory | Separate cell/hidden states | Combined state |
| Performance | Slightly better on complex tasks | Comparable on most tasks |
| When to Use | Default choice, complex sequences | Limited data, faster training needed |

### 4.5 Bidirectional RNNs

**Motivation:** Sometimes future context is important

**Examples:**
- "The bank" → financial institution or river bank? (need future words)
- Protein secondary structure depends on both upstream and downstream residues
- Named Entity Recognition benefits from full sentence context

**Architecture:**

```
Forward RNN:  x₁ → x₂ → x₃ → ... → x_T
               ↓    ↓    ↓         ↓
              h₁→  h₂→  h₃→       h_T→

Backward RNN: x_T ← x₃ ← x₂ ← ... ← x₁
               ↓    ↓    ↓         ↓
              h_T← h₃← h₂←       h₁←

Output: Concatenate forward and backward hidden states
y_t = [h_t→; h_t←]
```

**Mathematical Formulation:**

```python
# Forward pass
h_t→ = LSTM_forward(x_t, h_(t-1)→)

# Backward pass
h_t← = LSTM_backward(x_t, h_(t+1)←)

# Combine
h_t = [h_t→; h_t←]  # Concatenation
```

**Implementation:**

```python
lstm = nn.LSTM(input_size, hidden_size, 
               num_layers=2,
               bidirectional=True,  # This makes it bidirectional
               batch_first=True)

# Note: output hidden size is 2 * hidden_size (forward + backward)
```

**When to Use Bidirectional:**

✓ **Use when:**
- Complete sequence is available (not real-time)
- Context from both directions is useful
- Tasks: NER, protein structure prediction, sentiment analysis

✗ **Don't use when:**
- Real-time prediction needed
- Causal relationships must be preserved
- Online/streaming data
- Tasks: Stock prediction, real-time speech recognition

### 4.6 Biomedical Applications

#### 4.6.1 Clinical Time Series Analysis

**1. EEG Seizure Prediction:**
- **Input:** Multi-channel EEG signals (time series)
- **Architecture:** Bidirectional LSTM with attention
- **Output:** Probability of seizure in next 5-10 minutes
- **Impact:** Early warning system for epilepsy patients

```python
class EEGSeizurePredictor(nn.Module):
    def __init__(self, n_channels=16, hidden_size=128):
        super().__init__()
        self.lstm = nn.LSTM(n_channels, hidden_size, 
                            num_layers=2,
                            bidirectional=True,
                            batch_first=True)
        self.fc = nn.Linear(hidden_size * 2, 1)  # Binary classification
        
    def forward(self, x):
        # x: [batch, time_steps, n_channels]
        lstm_out, _ = self.lstm(x)
        # Take last time step output
        final_hidden = lstm_out[:, -1, :]
        output = torch.sigmoid(self.fc(final_hidden))
        return output
```

**2. ICU Mortality Prediction:**
- **Input:** Time series of vital signs, lab results from ICU stay
- **Architecture:** LSTM with attention mechanism
- **Output:** Risk of mortality in next 24-48 hours
- **Data:** MIMIC-III dataset (Medical Information Mart for Intensive Care)

**3. ECG Arrhythmia Detection:**
- **Input:** ECG signal (heart rhythm time series)
- **Architecture:** 1D CNN + LSTM hybrid
- **Output:** Classification of heart rhythm abnormalities

#### 4.6.2 Biological Sequence Analysis

**1. Protein Secondary Structure Prediction:**

- **Task:** Predict α-helix, β-sheet, or coil from amino acid sequence
- **Input:** Protein sequence (20 amino acids = 20-dimensional one-hot encoding)
- **Architecture:** Bidirectional LSTM (captures dependencies from both directions)
- **Performance:** 80-84% accuracy for 3-state prediction

```python
class ProteinStructureLSTM(nn.Module):
    def __init__(self, vocab_size=20, hidden_size=256):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, 128)
        self.lstm = nn.LSTM(128, hidden_size,
                            num_layers=3,
                            bidirectional=True,
                            batch_first=True,
                            dropout=0.3)
        # 3 classes: helix, sheet, coil
        self.fc = nn.Linear(hidden_size * 2, 3)
        
    def forward(self, x):
        # x: [batch, seq_len] with amino acid indices
        embedded = self.embedding(x)
        lstm_out, _ = self.lstm(embedded)
        # Predict for each position
        logits = self.fc(lstm_out)
        return logits  # [batch, seq_len, 3]
```

**Why Bidirectional?**
- Structure depends on both upstream and downstream residues
- Local interactions and long-range contacts both matter

**2. Clinical Named Entity Recognition (NER):**

- **Task:** Extract medical entities from clinical text
- **Entities:** Diseases, symptoms, medications, procedures
- **Input:** Electronic health records, clinical notes (text sequences)
- **Architecture:** Bi-LSTM + CRF (Conditional Random Field)
- **Why Bi-LSTM:** Word meaning depends on context from both directions
- **Why CRF:** Ensures valid label sequences (e.g., "B-Disease" must be followed by "I-Disease" or "O", not "I-Medication")

**Example:**
```
Text: "Patient diagnosed with type 2 diabetes, prescribed metformin"

Desired Output:
Patient -> O
diagnosed -> O
with -> O
type -> B-Disease
2 -> I-Disease
diabetes -> I-Disease
, -> O
prescribed -> O
metformin -> B-Medication
```

### 4.7 Implementation Example

```python
import torch
import torch.nn as nn

class BiLSTMClassifier(nn.Module):
    """
    Bidirectional LSTM for sequence classification.
    Suitable for: EEG classification, sentiment analysis, etc.
    """
    def __init__(self, input_size, hidden_size, num_layers, num_classes, dropout=0.3):
        super().__init__()
        
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            bidirectional=True,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0
        )
        
        # Attention mechanism (optional but improves performance)
        self.attention = nn.Linear(hidden_size * 2, 1)
        
        # Classification head
        self.fc = nn.Sequential(
            nn.Linear(hidden_size * 2, 128),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(128, num_classes)
        )
    
    def forward(self, x):
        # x: [batch_size, seq_len, input_size]
        
        # LSTM processing
        lstm_out, (h_n, c_n) = self.lstm(x)
        # lstm_out: [batch, seq_len, hidden_size*2]
        
        # Attention mechanism
        attention_weights = torch.softmax(self.attention(lstm_out), dim=1)
        # attention_weights: [batch, seq_len, 1]
        
        # Weighted sum of LSTM outputs
        context = torch.sum(attention_weights * lstm_out, dim=1)
        # context: [batch, hidden_size*2]
        
        # Classification
        output = self.fc(context)
        return output

# Usage example
model = BiLSTMClassifier(
    input_size=16,      # 16 EEG channels
    hidden_size=128,
    num_layers=2,
    num_classes=2,      # Seizure / No seizure
    dropout=0.3
)

# Example forward pass
x = torch.randn(32, 1000, 16)  # batch=32, time=1000, channels=16
output = model(x)               # output: [32, 2]
```

### 4.8 Training Tips for RNNs

**1. Gradient Clipping:**
Prevents exploding gradients
```python
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=5.0)
```

**2. Proper Initialization:**
```python
for name, param in model.named_parameters():
    if 'weight' in name:
        nn.init.xavier_uniform_(param)
    elif 'bias' in name:
        nn.init.constant_(param, 0)
```

**3. Learning Rate Scheduling:**
```python
scheduler = optim.lr_scheduler.ReduceLROnPlateau(
    optimizer, mode='min', factor=0.5, patience=5
)
```

**4. Handling Variable-Length Sequences:**
```python
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

# Pack sequences (ignore padding in computation)
packed = pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
packed_output, hidden = lstm(packed)
output, _ = pad_packed_sequence(packed_output, batch_first=True)
```

---

## 5. Transformers and Attention Mechanisms

### 5.1 The Attention Revolution

**Problem with RNNs:**
- Sequential processing (slow, can't parallelize)
- Long sequences still challenging despite LSTM/GRU
- Information bottleneck (entire sequence compressed into single vector)

**Solution: Attention Mechanism**

**Core Idea:** Allow model to "attend" to different parts of input when producing each output

**"Attention is All You Need" (Vaswani et al., 2017):**
- Eliminated recurrence entirely
- Relied solely on attention mechanisms
- Massive parallelization (faster training)
- State-of-the-art performance on NLP tasks
- Foundation for GPT, BERT, AlphaFold, and modern AI

### 5.2 Self-Attention Mechanism

**Goal:** Compute representation of sequence by relating different positions

**Mathematical Formulation:**

Given input sequence X = [x₁, x₂, ..., x_n]:

1. **Create Query, Key, Value matrices:**
   ```
   Q = XW_Q  (queries: what I'm looking for)
   K = XW_K  (keys: what I have)
   V = XW_V  (values: what I'll return if you attend to me)
   ```

2. **Compute attention scores:**
   ```
   Scores = QK^T / √d_k
   ```
   where d_k is dimension of keys (prevents large values)

3. **Apply softmax to get attention weights:**
   ```
   Attention_Weights = softmax(Scores)
   ```

4. **Weighted sum of values:**
   ```
   Output = Attention_Weights × V
   ```

**Complete Formula:**
```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

**Intuition:**

Consider sentence: "The animal didn't cross the street because it was too tired"

When processing "it":
- Attention mechanism looks at all previous words
- Computes similarity (QK^T) between "it" and each word
- High attention to "animal" (it refers to animal)
- Low attention to "street" (less relevant)
- Weighted combination captures meaning

### 5.3 Multi-Head Attention

**Motivation:** Different attention patterns capture different relationships

**Idea:** Learn multiple attention functions in parallel

**Architecture:**

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model=512, num_heads=8):
        super().__init__()
        assert d_model % num_heads == 0
        
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads  # Dimension per head
        
        # Linear layers for Q, K, V
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        
        # Output projection
        self.W_o = nn.Linear(d_model, d_model)
        
    def forward(self, Q, K, V, mask=None):
        batch_size = Q.size(0)
        
        # Linear projections in batch
        Q = self.W_q(Q)  # [batch, seq_len, d_model]
        K = self.W_k(K)
        V = self.W_v(V)
        
        # Split into multiple heads
        Q = Q.view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        K = K.view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        V = V.view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        # Now: [batch, num_heads, seq_len, d_k]
        
        # Scaled dot-product attention
        scores = torch.matmul(Q, K.transpose(-2, -1)) / torch.sqrt(torch.tensor(self.d_k, dtype=torch.float32))
        
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
        
        attention_weights = torch.softmax(scores, dim=-1)
        context = torch.matmul(attention_weights, V)
        
        # Concatenate heads
        context = context.transpose(1, 2).contiguous().view(batch_size, -1, self.d_model)
        
        # Output projection
        output = self.W_o(context)
        return output, attention_weights
```

**Why Multiple Heads?**
- Head 1: Captures syntactic relationships
- Head 2: Captures semantic relationships
- Head 3: Captures positional relationships
- Each head learns different aspects

### 5.4 Transformer Architecture

**Complete Transformer Block:**

```
Input
  ↓
Multi-Head Self-Attention
  ↓
Add & Norm (Residual connection + Layer Normalization)
  ↓
Feed-Forward Network (2-layer MLP)
  ↓
Add & Norm
  ↓
Output
```

**Full Architecture:**

1. **Encoder (e.g., BERT):**
   ```
   Input Embeddings + Positional Encoding
   ↓
   [Transformer Block] × N layers
   ↓
   Output representations
   ```

2. **Decoder (e.g., GPT):**
   ```
   Input Embeddings + Positional Encoding
   ↓
   [Transformer Block with Masked Attention] × N layers
   ↓
   Output tokens (autoregressively)
   ```

3. **Encoder-Decoder (e.g., Translation):**
   ```
   Encoder: Process source sequence
   ↓
   Decoder: Generate target sequence (attends to encoder outputs)
   ```

**Key Components:**

1. **Positional Encoding:**
   - Transformers have no inherent notion of position
   - Add position information via sinusoidal functions or learned embeddings
   ```python
   PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
   PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
   ```

2. **Layer Normalization:**
   - Stabilizes training
   - Applied after each sub-layer
   ```python
   LayerNorm(x + Sublayer(x))
   ```

3. **Feed-Forward Network:**
   - Applied position-wise (same network for each position)
   - Usually: Linear → ReLU → Linear
   ```python
   FFN(x) = max(0, xW_1 + b_1)W_2 + b_2
   ```

### 5.5 Biomedical Applications

#### 5.5.1 Protein Language Models

**ESM-2 (Evolutionary Scale Modeling 2):**

- **Architecture:** Transformer encoder (like BERT)
- **Training:** 250M+ protein sequences from UniRef database
- **Pre-training Task:** Masked language modeling (predict missing amino acids)
- **Sizes:** 8M to 15B parameters

**What ESM-2 Learns:**
- Evolutionary patterns
- Structural constraints
- Functional relationships
- Without ever seeing 3D structures!

**Applications:**
1. **Protein Function Prediction:**
   - Extract embeddings from ESM-2
   - Train classifier on top
   - Achieves state-of-the-art with limited labels

2. **Variant Effect Prediction:**
   - Score mutations by comparing ESM-2 likelihood
   - Predicts pathogenic vs. benign variants

3. **Protein Design:**
   - Generate novel protein sequences
   - Optimize for desired properties

**Usage:**
```python
import esm

# Load pre-trained model
model, alphabet = esm.pretrained.esm2_t33_650M_UR50D()
batch_converter = alphabet.get_batch_converter()

# Prepare data
data = [("protein1", "MKTAYIA...")]
batch_labels, batch_strs, batch_tokens = batch_converter(data)

# Extract embeddings
with torch.no_grad():
    results = model(batch_tokens, repr_layers=[33])
embeddings = results["representations"][33]

# Use embeddings for downstream tasks
```

#### 5.5.2 Clinical Natural Language Processing

**ClinicalBERT:**
- BERT fine-tuned on clinical notes (MIMIC-III)
- Understands medical terminology
- Applications: Clinical NER, ICD coding, outcome prediction

**BioBERT:**
- BERT fine-tuned on PubMed abstracts
- Biomedical entity recognition
- Relation extraction (drug-disease relationships)

#### 5.5.3 Drug Discovery

**MolTrans (Molecular Transformers):**
- Represent molecules as SMILES strings or graphs
- Transformer learns chemical properties
- Applications: Drug-target binding prediction, toxicity prediction, molecule generation

### 5.6 AlphaFold: Case Study in Transformers for Structure

**Problem:** Predict 3D protein structure from sequence

**Why Transformers?**
- Protein structure depends on long-range interactions
- Attention can model contacts between distant residues
- Self-attention on sequence and evolutionary data

**AlphaFold 2 Architecture:**

1. **Input Processing:**
   - Multiple Sequence Alignment (MSA) from evolutionary data
   - Template structures (if available)

2. **Evoformer (Core Innovation):**
   - Alternating attention on MSA rows and columns
   - Pair representation for residue-residue relationships
   - Triangular update operations

3. **Structure Module:**
   - Invariant Point Attention (IPA)
   - Predicts 3D coordinates
   - Iterative refinement

4. **Confidence Prediction:**
   - pLDDT: Per-residue confidence
   - PAE: Predicted aligned error matrix

**Key Innovation: Invariant Point Attention (IPA)**

- Standard attention not aware of 3D geometry
- IPA incorporates 3D frame transformations
- Respects geometric structure

**Impact:**
- Solved 50-year protein folding problem
- 200M+ structures predicted
- Accelerated drug discovery, structural biology

**AlphaFold 3 (2024):**
- Diffusion model architecture
- Predicts protein-ligand, protein-nucleic acid complexes
- Broader biomolecular applications

### 5.7 Implementation Example: Simplified Transformer

```python
class TransformerBlock(nn.Module):
    """Single Transformer encoder block."""
    
    def __init__(self, d_model=512, num_heads=8, d_ff=2048, dropout=0.1):
        super().__init__()
        
        # Multi-head attention
        self.attention = nn.MultiheadAttention(d_model, num_heads, dropout=dropout)
        
        # Feed-forward network
        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(d_ff, d_model)
        )
        
        # Layer normalization
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        
        # Dropout
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x):
        # Multi-head attention with residual connection
        attn_out, _ = self.attention(x, x, x)
        x = self.norm1(x + self.dropout(attn_out))
        
        # Feed-forward with residual connection
        ffn_out = self.ffn(x)
        x = self.norm2(x + self.dropout(ffn_out))
        
        return x

class ProteinTransformer(nn.Module):
    """Transformer for protein sequence analysis."""
    
    def __init__(self, vocab_size=20, d_model=512, num_heads=8, 
                 num_layers=6, max_seq_len=1000, num_classes=10):
        super().__init__()
        
        # Embeddings
        self.token_embedding = nn.Embedding(vocab_size, d_model)
        self.positional_encoding = nn.Parameter(torch.randn(1, max_seq_len, d_model))
        
        # Transformer blocks
        self.transformer_blocks = nn.ModuleList([
            TransformerBlock(d_model, num_heads)
            for _ in range(num_layers)
        ])
        
        # Classification head
        self.fc = nn.Linear(d_model, num_classes)
        
    def forward(self, x):
        # x: [batch, seq_len] with amino acid indices
        
        # Embeddings with positional encoding
        seq_len = x.size(1)
        embedded = self.token_embedding(x) + self.positional_encoding[:, :seq_len, :]
        
        # Pass through transformer blocks
        for block in self.transformer_blocks:
            embedded = block(embedded)
        
        # Global average pooling
        pooled = embedded.mean(dim=1)
        
        # Classification
        output = self.fc(pooled)
        return output
```

### 5.8 Advantages and Limitations

**Advantages:**

✅ **Parallelization:** No sequential dependencies, much faster training
✅ **Long-range dependencies:** Attention directly connects distant positions
✅ **Interpretability:** Attention weights show what model focuses on
✅ **Transfer learning:** Pre-trained models (BERT, GPT, ESM-2) excel at downstream tasks
✅ **Scalability:** Performance improves with model size and data

**Limitations:**

⚠️ **Computational cost:** Attention is O(n²) in sequence length
⚠️ **Memory requirements:** Large models need significant GPU memory
⚠️ **Data hungry:** Need large datasets for pre-training (less so for fine-tuning)
⚠️ **Positional encoding:** Not as natural as RNN's inherent sequential processing
⚠️ **Over-parameterization:** Easy to overfit on small datasets without pre-training

**When to Use Transformers vs RNNs:**

| Use Transformers | Use RNNs |
|------------------|----------|
| Large datasets available | Small datasets |
| Pre-trained models exist (ESM-2, BERT) | Custom sequential tasks |
| Long-range dependencies critical | Real-time streaming data |
| Computational resources available | Resource-constrained environments |
| State-of-the-art performance needed | Simple sequential patterns |

---

## 6. Advanced Architectures

### 6.1 Graph Neural Networks (GNNs)

**Motivation:** Many biological systems are naturally graph-structured

**Examples:**
- Molecular graphs (atoms = nodes, bonds = edges)
- Protein structure (residues = nodes, contacts = edges)
- Brain connectivity (regions = nodes, connections = edges)
- Metabolic pathways
- Gene regulatory networks

**Key Idea:** Learn representations of nodes by aggregating information from neighbors

**Message Passing Framework:**

```python
# For each layer:
for node v in graph:
    # 1. Aggregate messages from neighbors
    message = AGGREGATE({h_u for u in neighbors(v)})
    
    # 2. Update node representation
    h_v_new = UPDATE(h_v, message)
```

#### 6.1.1 Graph Convolutional Networks (GCN)

**Mathematical Formulation:**

```
H^(l+1) = σ(D^(-1/2) A D^(-1/2) H^(l) W^(l))

where:
  H^(l): Node features at layer l
  A: Adjacency matrix (with self-loops)
  D: Degree matrix
  W^(l): Learnable weights
  σ: Activation function
```

**Intuition:**
- Each node's new representation is weighted average of neighbors
- Stacking layers increases receptive field (multi-hop neighbors)

**Implementation:**

```python
import torch
import torch.nn as nn
import torch_geometric.nn as gnn

class ProteinGCN(nn.Module):
    """GCN for protein structure analysis."""
    
    def __init__(self, node_features=20, hidden_dim=64, num_classes=3):
        super().__init__()
        
        # GCN layers
        self.conv1 = gnn.GCNConv(node_features, hidden_dim)
        self.conv2 = gnn.GCNConv(hidden_dim, hidden_dim)
        self.conv3 = gnn.GCNConv(hidden_dim, hidden_dim)
        
        # Graph-level pooling
        self.pool = gnn.global_mean_pool
        
        # Classification
        self.fc = nn.Linear(hidden_dim, num_classes)
        
    def forward(self, x, edge_index, batch):
        # x: [num_nodes, node_features]
        # edge_index: [2, num_edges]
        # batch: [num_nodes] indicating which graph each node belongs to
        
        # GCN layers with ReLU
        x = torch.relu(self.conv1(x, edge_index))
        x = torch.relu(self.conv2(x, edge_index))
        x = torch.relu(self.conv3(x, edge_index))
        
        # Graph-level pooling
        x = self.pool(x, batch)
        
        # Classification
        output = self.fc(x)
        return output
```

#### 6.1.2 Biomedical Applications

**1. Molecular Property Prediction:**
- Input: Molecular graph (SMILES → graph)
- Task: Predict solubility, toxicity, binding affinity
- Architecture: GCN or Graph Attention Networks (GAT)

**2. Protein Function Prediction:**
- Input: Protein structure as graph (residue contact map)
- Task: Predict enzyme class, GO terms
- Architecture: GCN with residue-level and graph-level tasks

**3. Brain Network Analysis:**
- Input: Brain connectivity graphs from fMRI
- Task: Disease classification (healthy vs. diseased)
- Nodes: Brain regions, Edges: Functional connectivity

**4. Drug-Target Interaction:**
- Input: Drug graph + Protein graph
- Task: Predict binding
- Architecture: GNN encoder for each + interaction prediction

### 6.2 Variational Autoencoders (VAEs)

**Motivation:** Learn meaningful latent representations and generate new data

**Architecture:**

```
Input → Encoder → Latent Space (μ, σ) → Decoder → Reconstruction
                      ↓
                   Sample z ~ N(μ, σ)
```

**Key Components:**

1. **Encoder:** Maps input x to latent distribution parameters (μ, σ)
2. **Reparameterization Trick:** Sample z = μ + σ ⊙ ε, where ε ~ N(0, 1)
3. **Decoder:** Maps latent z back to reconstructed x̂
4. **Loss Function:**
   ```
   L = Reconstruction_Loss(x, x̂) + KL_Divergence(q(z|x) || p(z))
   
   where:
     Reconstruction: How well x̂ matches x
     KL Divergence: How close latent distribution is to prior N(0,1)
   ```

**Why VAE over Regular Autoencoder?**
- Regular AE: Latent space can have "holes" (interpolation fails)
- VAE: Continuous, smooth latent space (good for generation)

#### 6.2.1 Biomedical Applications

**1. Single-Cell RNA-seq Analysis:**
- Input: Gene expression profiles
- Latent space: Meaningful cell state representation
- Applications: Cell clustering, trajectory inference, batch correction
- Tool: scVI (single-cell Variational Inference)

**2. Drug Design:**
- Input: Molecular structures
- Latent space: Chemical space
- Generate new molecules by sampling/interpolating in latent space

**3. Medical Image Synthesis:**
- Generate synthetic medical images for data augmentation
- Privacy-preserving (generate realistic images without real patients)

### 6.3 Generative Adversarial Networks (GANs)

**Architecture:** Two networks compete

1. **Generator (G):** Creates fake data
2. **Discriminator (D):** Distinguishes real from fake

**Training:**
```
D tries to maximize: log D(x_real) + log(1 - D(G(z)))
G tries to minimize: log(1 - D(G(z)))

In practice, G maximizes: log D(G(z))  (better gradients)
```

**Intuition:**
- D learns to be better at detecting fakes
- G learns to fool D
- At equilibrium, G generates realistic data, D can't tell real from fake

#### 6.3.1 Biomedical Applications

**1. Medical Image Synthesis:**
- Generate high-resolution MRI from low-resolution
- Cross-modality synthesis (MRI → CT)
- Data augmentation for rare diseases

**2. Histopathology:**
- Generate synthetic tissue images
- Stain normalization (standardize staining variations)
- CycleGAN for unpaired image-to-image translation

**3. Drug Discovery:**
- Generate novel molecular structures
- Conditional generation (generate molecules with desired properties)

**4. Microscopy Super-Resolution:**
- Generate high-resolution images from low-resolution microscopy
- Reduce imaging time while maintaining quality

---

## 7. Practical Considerations

### 7.1 Data Preparation

#### 7.1.1 Handling Limited Data

**Common in Biomedical Research:**
- Expensive data collection (patient studies, experiments)
- Privacy concerns (limited data sharing)
- Rare diseases (few samples)

**Solutions:**

1. **Transfer Learning:**
   - Start with pre-trained model (ImageNet, ESM-2, etc.)
   - Fine-tune on your small dataset
   - Often works with 100-1000 labeled examples

2. **Data Augmentation:**
   ```python
   # For images
   transforms.Compose([
       transforms.RandomHorizontalFlip(),
       transforms.RandomRotation(15),
       transforms.ColorJitter(brightness=0.2, contrast=0.2),
       transforms.RandomResizedCrop(224)
   ])
   
   # For biological sequences
   - Random mutations (simulate natural variation)
   - Subsequence extraction
   - Reverse complement (DNA)
   ```

3. **Synthetic Data Generation:**
   - Use GANs or VAEs to generate additional training data
   - Validate that synthetic data is realistic

4. **Multi-Task Learning:**
   - Train on related tasks simultaneously
   - Share representations across tasks

#### 7.1.2 Handling Class Imbalance

**Problem:** Rare diseases, rare events (e.g., 1% seizures in EEG data)

**Solutions:**

1. **Weighted Loss:**
   ```python
   class_weights = torch.tensor([1.0, 10.0])  # Weight rare class more
   criterion = nn.CrossEntropyLoss(weight=class_weights)
   ```

2. **Oversampling Minority Class:**
   ```python
   from imblearn.over_sampling import SMOTE
   X_resampled, y_resampled = SMOTE().fit_resample(X, y)
   ```

3. **Focal Loss:**
   - Down-weights easy examples, focuses on hard ones
   - Especially effective for extreme imbalance

4. **Evaluation Metrics:**
   - Don't use accuracy alone!
   - Use: Precision, Recall, F1-score, AUROC, AUPRC

#### 7.1.3 Missing Data

**Common in Clinical Data:**
- Lab results not always collected
- Patients miss follow-up visits
- Sensor malfunctions

**Strategies:**

1. **Simple Imputation:**
   - Mean/median for numerical
   - Most frequent for categorical
   ```python
   from sklearn.impute import SimpleImputer
   imputer = SimpleImputer(strategy='mean')
   X_imputed = imputer.fit_transform(X)
   ```

2. **Model-Based Imputation:**
   - KNN imputation
   - Iterative imputation (MICE)

3. **Indicator Variables:**
   - Add binary "missingness" indicator
   - Let model learn importance of missing vs. present

4. **Embeddings for Missing:**
   - Special embedding for "missing" category
   - Common in NLP, applicable to other domains

### 7.2 Training Best Practices

#### 7.2.1 Monitoring Training

**Essential Metrics:**

```python
# Track during training
metrics = {
    'train_loss': [],
    'train_acc': [],
    'val_loss': [],
    'val_acc': [],
    'learning_rate': []
}

# Plot after each epoch
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(metrics['train_loss'], label='Train')
axes[0].plot(metrics['val_loss'], label='Val')
axes[0].set_title('Loss')
axes[1].plot(metrics['train_acc'], label='Train')
axes[1].plot(metrics['val_acc'], label='Val')
axes[1].set_title('Accuracy')
```

**Signs of Problems:**

| Pattern | Diagnosis | Solution |
|---------|-----------|----------|
| Train ↓, Val ↓ (both improving) | Healthy training | Continue |
| Train ↓, Val ↑ (diverging) | Overfitting | More regularization, early stopping |
| Train ↑ or flat | Underfitting or bad hyperparameters | Larger model, lower LR, longer training |
| Loss = NaN | Exploding gradients or numerical instability | Gradient clipping, lower LR, check data |
| Val bouncing around | Batch size too small or LR too high | Increase batch size, reduce LR |

#### 7.2.2 Hyperparameter Tuning

**Key Hyperparameters:**

1. **Learning Rate:** Most important
   - Too high: Training unstable, loss explodes
   - Too low: Training too slow, gets stuck
   - Typical range: 1e-5 to 1e-2
   - Try: 1e-3 first, then adjust

2. **Batch Size:**
   - Larger: Faster training, more stable gradients, worse generalization
   - Smaller: Noisier gradients, better generalization, slower
   - Typical: 16-256
   - Limited by GPU memory

3. **Number of Layers / Hidden Size:**
   - More parameters: Can fit more complex patterns, but risk overfitting
   - Start small, increase if underfitting

4. **Dropout Rate:**
   - 0.1-0.5 typical
   - Higher for larger models / more overfitting

5. **Weight Decay (L2 regularization):**
   - 1e-5 to 1e-2 typical
   - Prevents large weights

**Tuning Strategies:**

1. **Grid Search:**
   ```python
   from sklearn.model_selection import GridSearchCV
   
   param_grid = {
       'learning_rate': [1e-4, 1e-3, 1e-2],
       'hidden_size': [64, 128, 256],
       'dropout': [0.2, 0.3, 0.5]
   }
   ```

2. **Random Search:**
   - More efficient than grid search
   - Sample hyperparameters randomly

3. **Bayesian Optimization:**
   - Smart search using previous results
   - Tools: Optuna, Ray Tune
   ```python
   import optuna
   
   def objective(trial):
       lr = trial.suggest_float('lr', 1e-5, 1e-2, log=True)
       hidden_size = trial.suggest_categorical('hidden_size', [64, 128, 256])
       
       model = MyModel(hidden_size=hidden_size)
       # Train and return validation loss
       return val_loss
   
   study = optuna.create_study(direction='minimize')
   study.optimize(objective, n_trials=50)
   ```

4. **Learning Rate Finder:**
   - Increase LR exponentially during training
   - Plot loss vs. LR
   - Choose LR where loss decreases fastest
   ```python
   from torch_lr_finder import LRFinder
   
   lr_finder = LRFinder(model, optimizer, criterion)
   lr_finder.range_test(train_loader, end_lr=1, num_iter=100)
   lr_finder.plot()
   ```

#### 7.2.3 Optimization Tricks

**1. Learning Rate Scheduling:**

```python
# ReduceLROnPlateau: Reduce when validation plateaus
scheduler = optim.lr_scheduler.ReduceLROnPlateau(
    optimizer, mode='min', factor=0.5, patience=5
)
scheduler.step(val_loss)

# Cosine Annealing: Smooth decrease
scheduler = optim.lr_scheduler.CosineAnnealingLR(
    optimizer, T_max=n_epochs
)

# Step Decay: Drop by factor every N epochs
scheduler = optim.lr_scheduler.StepLR(
    optimizer, step_size=10, gamma=0.5
)
```

**2. Gradient Clipping:**

```python
# Prevent exploding gradients (especially important for RNNs)
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=5.0)
```

**3. Mixed Precision Training:**

```python
# Faster training, lower memory usage
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()

for batch in dataloader:
    optimizer.zero_grad()
    
    with autocast():
        outputs = model(inputs)
        loss = criterion(outputs, labels)
    
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

**4. Gradient Accumulation:**

```python
# Simulate larger batch size when GPU memory is limited
accumulation_steps = 4

for i, batch in enumerate(dataloader):
    outputs = model(inputs)
    loss = criterion(outputs, labels) / accumulation_steps
    loss.backward()
    
    if (i + 1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

### 7.3 Computational Resources

#### 7.3.1 Hardware Options

| Option | Cost | Speed | Best For |
|--------|------|-------|----------|
| **CPU** | Included | Slow | Small models, prototyping |
| **Google Colab (Free)** | Free | Medium | Learning, small projects |
| **Google Colab Pro** | $10/month | Fast | Regular use, medium projects |
| **Local GPU (RTX 3090/4090)** | $1500-2000 | Very Fast | Frequent use, full control |
| **Cloud (AWS, GCP, Azure)** | $0.50-3/hr | Fast | Large-scale, temporary needs |
| **HPC Cluster** | Varies | Very Fast | Academic research |

#### 7.3.2 Memory Management

**GPU Out of Memory? Try:**

1. **Reduce Batch Size:**
   ```python
   batch_size = 32  # Try 16, 8, 4, ...
   ```

2. **Gradient Accumulation:**
   ```python
   # Simulate batch_size=128 with 4 steps of 32
   accumulation_steps = 4
   ```

3. **Mixed Precision (FP16):**
   ```python
   # Halves memory usage
   with autocast():
       outputs = model(inputs)
   ```

4. **Gradient Checkpointing:**
   ```python
   # Trade computation for memory
   from torch.utils.checkpoint import checkpoint
   output = checkpoint(module, input)
   ```

5. **Use Smaller Model:**
   - Fewer layers, smaller hidden size
   - Or use model quantization

### 7.4 Interpretability and Validation

#### 7.4.1 Model Interpretability

**Why Important in Biomedicine:**
- Trust from clinicians and researchers
- Regulatory approval (FDA, EMA)
- Scientific insight (what features matter?)
- Debugging (is model learning right patterns?)

**Techniques:**

1. **Attention Visualization (Transformers):**
   ```python
   # Extract attention weights
   _, attention_weights = model(input, return_attention=True)
   
   # Visualize
   plt.imshow(attention_weights[0].detach().cpu(), cmap='viridis')
   plt.xlabel('Key Position')
   plt.ylabel('Query Position')
   plt.colorbar()
   ```

2. **Grad-CAM (CNNs):**
   - Highlights regions of image important for prediction
   - Shows where model is "looking"
   ```python
   from pytorch_grad_cam import GradCAM
   
   cam = GradCAM(model=model, target_layers=[model.layer4])
   grayscale_cam = cam(input_tensor=image)
   ```

3. **SHAP Values:**
   - Game-theory based feature importance
   - Works for any model
   ```python
   import shap
   
   explainer = shap.DeepExplainer(model, background_data)
   shap_values = explainer.shap_values(test_data)
   shap.summary_plot(shap_values, test_data)
   ```

4. **Saliency Maps:**
   - Gradient of output w.r.t. input
   - Shows which input features model is sensitive to

#### 7.4.2 Validation Strategies

**1. Cross-Validation:**
```python
from sklearn.model_selection import KFold

kfold = KFold(n_splits=5, shuffle=True, random_state=42)

for fold, (train_idx, val_idx) in enumerate(kfold.split(X)):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]
    
    # Train model on this fold
    model = MyModel()
    # ... training code ...
    
    # Evaluate on fold
    fold_performance = evaluate(model, X_val, y_val)
```

**2. Stratified Splits:**
```python
# Maintain class distribution in train/val/test
from sklearn.model_selection import train_test_split

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=42
)
```

**3. External Validation:**
- Test on completely different dataset
- Different hospital, different time period
- Critical for clinical deployment

**4. Evaluation Metrics:**

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, average_precision_score, confusion_matrix
)

# For classification
acc = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='weighted')
recall = recall_score(y_true, y_pred, average='weighted')
f1 = f1_score(y_true, y_pred, average='weighted')
auroc = roc_auc_score(y_true, y_prob, multi_class='ovr')
auprc = average_precision_score(y_true, y_prob, average='weighted')

# Confusion matrix
cm = confusion_matrix(y_true, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
```

**Metric Selection Guide:**

| Task | Recommended Metrics |
|------|---------------------|
| Balanced classification | Accuracy, F1-score |
| Imbalanced classification | AUROC, AUPRC, F1 (weighted) |
| Multi-class | Macro/Weighted F1, AUROC (OvR) |
| Regression | MAE, RMSE, R² |
| Segmentation | Dice coefficient, IoU |

---

## 8. Case Study: AlphaFold

(Covered extensively in previous sections, see Section 5.6 and Notebook 05)

---

## 9. Framework Comparisons

### 9.1 PyTorch vs TensorFlow/Keras

| Aspect | PyTorch | TensorFlow/Keras |
|--------|---------|------------------|
| **Philosophy** | Pythonic, dynamic | Production-oriented |
| **Ease of Learning** | More intuitive | Keras: Easy, TF: Harder |
| **Debugging** | Native Python debugging | More challenging |
| **Research** | Dominant in academia | More in industry |
| **Production** | Growing support | Mature ecosystem |
| **Mobile/Edge** | Limited | TensorFlow Lite excellent |
| **Pre-trained Models** | Hugging Face ecosystem | TensorFlow Hub |
| **Performance** | Excellent | Excellent |

**Recommendation:** Learn PyTorch for this course and research. Explore TensorFlow for production deployment.

### 9.2 JAX: The Future?

**What is JAX?**
- NumPy + Automatic Differentiation + XLA Compilation
- Functional programming paradigm
- Composable transformations

**Key Features:**

```python
import jax
import jax.numpy as jnp

# Automatic differentiation
grad_fn = jax.grad(loss_fn)

# JIT compilation (10x speedup)
fast_fn = jax.jit(slow_fn)

# Automatic vectorization
batched_fn = jax.vmap(single_example_fn)

# Parallel computation
parallel_fn = jax.pmap(fn, devices=jax.devices())
```

**When to Use JAX:**
- Scientific computing (physics simulations, ODEs)
- Custom algorithms needing gradient control
- Maximum performance
- Research prototypes

**When NOT to Use JAX:**
- Standard deep learning (PyTorch better supported)
- Production deployment (less mature)
- Beginners (steeper learning curve)

---

## 10. Resources and Further Reading

### 10.1 Textbooks

1. **Deep Learning (Goodfellow, Bengio, Courville)**
   - Comprehensive theoretical foundation
   - Free online: deeplearningbook.org

2. **Dive into Deep Learning (d2l.ai)**
   - Interactive, code-first approach
   - PyTorch and TensorFlow implementations

3. **Neural Networks and Deep Learning (Nielsen)**
   - Beginner-friendly introduction
   - Free online: neuralnetworksanddeeplearning.com

### 10.2 Online Courses

1. **Fast.ai Practical Deep Learning for Coders**
   - Top-down, practical approach
   - Free, excellent for getting started quickly

2. **Stanford CS230 Deep Learning**
   - Andrew Ng, solid theoretical and practical balance
   - Course notes freely available

3. **MIT 6.S191 Introduction to Deep Learning**
   - Lecture videos on YouTube
   - Covers modern architectures

### 10.3 Code & Tutorials

1. **PyTorch Tutorials:** pytorch.org/tutorials
2. **Hugging Face Learn:** huggingface.co/learn
3. **Papers with Code:** paperswithcode.com
4. **Kaggle Learn:** kaggle.com/learn

### 10.4 Biomedical-Specific Resources

1. **ESM Protein Models:** github.com/facebookresearch/esm
2. **AlphaFold:** github.com/deepmind/alphafold
3. **Medical Segmentation Decathlon:** medicaldecathlon.com
4. **MIMIC-III (Clinical Data):** physionet.org/content/mimiciii

### 10.5 Key Papers

**CNNs:**
- LeNet: LeCun et al. (1998) - Gradient-based learning applied to document recognition
- AlexNet: Krizhevsky et al. (2012) - ImageNet classification with deep CNNs
- ResNet: He et al. (2015) - Deep residual learning for image recognition
- U-Net: Ronneberger et al. (2015) - Convolutional networks for biomedical image segmentation

**RNNs:**
- LSTM: Hochreiter & Schmidhuber (1997) - Long short-term memory
- Attention: Bahdanau et al. (2014) - Neural machine translation by jointly learning to align and translate

**Transformers:**
- Vaswani et al. (2017) - Attention is all you need
- BERT: Devlin et al. (2018) - Pre-training of deep bidirectional transformers
- GPT-3: Brown et al. (2020) - Language models are few-shot learners

**GNNs:**
- Kipf & Welling (2016) - Semi-supervised classification with graph convolutional networks

**Biomedical:**
- AlphaFold 2: Jumper et al. (2021) - Highly accurate protein structure prediction with AlphaFold
- AlphaFold 3: Abramson et al. (2024) - Accurate structure prediction of biomolecular interactions
- ESM-2: Lin et al. (2023) - Language models of protein sequences at scale

### 10.6 Communities

- **PyTorch Forums:** discuss.pytorch.org
- **r/MachineLearning:** reddit.com/r/MachineLearning
- **ML Twitter:** Follow researchers and practitioners
- **Conferences:** NeurIPS, ICML, ICLR (AI), RECOMB, ISMB (Computational Biology)

---

## Conclusion

Deep learning has revolutionized how we analyze biological data. From protein structure prediction with AlphaFold to medical image analysis with CNNs, these techniques have become essential tools for modern neuroscience and biomedical research.

**Key Takeaways:**

1. **Match Architecture to Data:**
   - Tabular → Feedforward
   - Images → CNN (U-Net for segmentation)
   - Sequences → RNN/LSTM or Transformer
   - Graphs → GNN

2. **Transfer Learning is Powerful:**
   - Pre-trained models (ImageNet, ESM-2) dramatically reduce data requirements
   - Fine-tuning often works with 100-1000 labeled examples

3. **Practical Matters:**
   - Always use validation sets
   - Apply proper regularization
   - Monitor training carefully
   - Prioritize interpretability for biomedical applications

4. **Transformers Dominate Modern AI:**
   - State-of-the-art across NLP, protein modeling, and more
   - Attention mechanism is key innovation
   - Pre-trained models (BERT, GPT, ESM-2) available

5. **Tools and Frameworks:**
   - PyTorch recommended for research and learning
   - Transfer to TensorFlow if production deployment needed
   - JAX for specialized scientific computing

**Moving Forward:**

- Practice with real datasets (Kaggle, medical imaging challenges)
- Read recent papers (Papers with Code)
- Implement architectures from scratch (best way to learn)
- Apply to your research problems
- Contribute to open-source (Hugging Face, PyTorch)

Deep learning is a rapidly evolving field. Stay curious, keep learning, and remember: understanding the fundamentals will serve you better than chasing every new architecture.

---
*This handout is part of the "Introduction to Scientific Programming" course at CNC-UC, University of Coimbra. For questions or clarifications, please contact the course instructor.*
**Document Version**: 1.0  
**Last Updated**: December 2025  
**License**: CC BY 4.0
