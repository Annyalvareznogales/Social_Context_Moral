# Enriching Language Models with Network Knowledge for Sentiment and Moral Assessment

This repository contains the code and supporting resources for the paper:  
**"Enriching Language Models with Network Knowledge for Sentiment and Moral Assessment"**  
*Anny Álvarez, Oscar Araque*


## 📁 Repository Structure

This repository is organized as follows:

- **`data/`**  
  Contains the moral lexicons used for annotation, including **MFD** and **LIWC**.  
  ⚠️ *The datasets used in the experiments are not publicly available.*  
  To request access, please contact: [a.anogales@upm.es](mailto:a.anogales@upm.es)

- **`models/`**  
  Stores the user embeddings generated through various node representation learning techniques:
  - SVD
  - DeepWalk
  - Node2Vec
  - TADW

- **`src/`**  
  Contains the main implementation notebooks:
  
  - `Moral_annotation.ipynb`:  
    - Performs moral annotation using fine tuned models:
    - Applies **MoralBERT** from Hugging Face  
    - Applies GSI models based on **RoBERTa** for both moral trait and polarity prediction  
    - Uses lexicons: **MFD** and **LIWC**  
    - Includes a **perspective-based moral model**  
    - Handles label selection (with and without polarity)  
    - Computes inter-annotator agreement: **Cohen’s Kappa** and **Fleiss’ Kappa**  
    - Merges annotated data into `.pkl` format and saves embeddings in `.npy`

  - `Data_exploration_baseline_models.ipynb`:  
    - Explores and visualizes the datasets  
    - Generates user embeddings reflecting social context  
    - Implements baseline classification models (via Hugging Face) using:
      - BERT  
      - RoBERTa  
      - LLaMA  
      - DeepSeek 

  - `Social_context_Adition.ipynb`:  
    - Defines the architecture to integrate social context into the classification process  
    - Fine-tunes models for **sentiment** and **moral value** prediction  
    - Saves the final classification results  


