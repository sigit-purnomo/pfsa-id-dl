# Extraction and attribution of public figures statements for journalism in Indonesia using deep learning

This is the official repository for the [Extraction and attribution of public figures statements for journalism in Indonesia using deep learning](https://doi.org/10.1016/j.knosys.2024.111558) paper published in Knowledge-Based System.

## Overview of this repository
This repository is structured as follows:
- `corpus/` contains the corpus used in the paper.
- `model/` contains the best model for each of the deep learning architecture.

## How to Cite
If you extend or use this work, please cite the paper where it was introduced:
```
@article{PURNOMOWP2024111558,
	title = {Extraction and attribution of public figures statements for journalism in Indonesia using deep learning},
	journal = {Knowledge-Based Systems},
	volume = {289},
	pages = {111558},
	year = {2024},
	issn = {0950-7051},
	doi = {https://doi.org/10.1016/j.knosys.2024.111558},
	url = {https://www.sciencedirect.com/science/article/pii/S095070512400193X},
	author = {Yohanes Sigit {Purnomo W.P.} and Yogan Jaya Kumar and Nur Zareen Zulkarnain and Basit Raza},
	keywords = {Statement extraction and attribution, Named-entity recognition, Knowledge-based, Indonesian language, Deep learning},
	abstract = {News articles are usually written by journalists based on statements taken from interviews with public figures. Attribution from such statements provides important information and it can be extracted from news articles to build a knowledge base by developing a sequential tagging scheme such as entity recognition. This research applies two deep learning architectures: recurrent neural networks-based and transformer-based, to establish public figures statement attribution and extraction models in the Indonesian Language. The experiments are conducted using five deep-learning model architectures with two different corpus sizes to investigate the impact of corpus size on each model's performance. The experiments show that the best model for the RNN-based architecture is PFSA-ID-BLWCA which achieves 81.34 % F1 score, and the best model for the transformer-based is PFSA-ID-TWCA which obtains 81.01 % F1 score. This research also discovers that the size of the corpus influences the model performances. Furthermore, the study lays a foundation to overcome the attribution extraction in another language, especially low-resource languages, with some necessary adjustments.}
}
```