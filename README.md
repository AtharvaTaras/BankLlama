### Note
This repository contains part of the original code developed during research for the paper [Fine Tuned Large Langage Model in Banking](https://drive.google.com/file/d/1q1qkZpqGH9PeMqnwh8O0-U9gmCLDWU-e/view?usp=sharing)  

This code has been ported from Colab and several other sources, and may not work directly out of the box. Please download the model directly from Huggingface for inferencing, or contact the authors if you wish to recreate the training code.

Credits - [Soham Name](https://www.linkedin.com/in/soham-nale/), [Shreyash Darade](https://www.linkedin.com/in/shreyash-darade-3366b1213/), [Ashwin Choudhari](https://www.linkedin.com/in/ashwin-chaudhari-623627244/)

# BankLlama

This project fine-tunes the LLaMA 2 7B model on banking-related queries to create a specialized banking assistant. The implementation uses PEFT (Parameter Efficient Fine-Tuning) techniques and is optimized to run on Google Colab with T4 GPU.

## Overview

The project consists of two main components:
1. Model fine-tuning pipeline
2. Inference application

The model is trained on a custom banking dataset (Banking.csv) containing various banking-related questions and their detailed responses.

## Requirements

- Google Colab with T4 GPU
- Python 3.10+
- PyTorch
- Transformers
- PEFT
- Accelerate
- Bitsandbytes
- Gradio

## Model Details

- Base Model: LLaMA 2 7B (Guanaco Instruct variant)
- Training Method: LoRA (Low-Rank Adaptation)
- Quantization: 4-bit quantization using bitsandbytes
- Training Parameters:
  - LoRA rank: 64
  - LoRA alpha: 16
  - Dropout: 0.1
  - Learning rate: 2e-4
  - Batch size: 4
  - Max sequence length: 512

## Usage

After starting the Gradio interface (load_demo.ipynb), simply:
1. Enter your banking-related question in the text input
2. Click submit
3. Get a detailed, context-aware response from the model

## Limitations

- Requires T4 GPU or better for reasonable performance
- Model responses are limited to banking domain knowledge

## Acknowledgments

- Meta AI for LLaMA 2
- Hugging Face for the Transformers library
- Microsoft for LoRA implementation
