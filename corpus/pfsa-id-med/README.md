# PFSA-ID-MED Corpus

The bigger-size corpus (PFSA-ID-MED) comprises 1889 annotated news articles, 46.11% bigger than the size of the PFSA-ID corpus (1018 articles). This table shows the label distribution of the PFSA-ID-MED corpus. 

Label	| Total
--- | ---
PERSON	|	4555
PERSONCOREF	|	4510
ROLE	|	4668
AFFILIATION	|	3405
CUE	|	5052
CUECOREF	|	2770
STATEMENT	|	7817
ISSUE	|	1830
DATETIME	|	1360
LOCATION	|	776
EVENT	|	1485


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