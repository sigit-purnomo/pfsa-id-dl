# Extraction and attribution of public figures statements for journalism in Indonesia using deep learning

This is the official repository for the [Extraction and attribution of public figures statements for journalism in Indonesia using deep learning](https://doi.org/10.1016/j.knosys.2024.111558) paper published in Knowledge-Based System journal.


![RNN-based Model Architecture.](https://ars.els-cdn.com/content/image/1-s2.0-S095070512400193X-gr2.jpg)

## 🌟 Highlight from this research
- Public figures' statements in news articles are valuable.
- Named entity recognition could be used to extract and attribute the public figure's statements.
- RNN and transformer-based extraction models performed well with the highest F1 score 81.34 % and 81.01 %.
- The size of the corpus affects the performance of the model.

## 🛠️ Overview of this repository
This repository is structured as follows:
- `corpus/` contains the corpus used in the paper.
- `model/` contains the best model for each of the deep learning architecture.

## 🚀 Getting Started

1. Run the python main file <br />
   Notes: Please check the path of the corpus, model, and testing result output.
   ```sh
   python main.py
    ```
2. Check the testing result in the testing-result folder

## :pray: Acknowledgments 

Acknowledgments

The authors are grateful to **[Universitas Atma Jaya Yogyakarta](https://www.uajy.ac.id)** and the **[Center for Advanced Computing Technology (C-ACT), Fakulti Teknologi Maklumat Dan Komunikasi, Universiti Teknikal Malaysia Melaka](https://ftmk.utem.edu.my)** for supporting this publication.

	
## :books: How to Cite
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