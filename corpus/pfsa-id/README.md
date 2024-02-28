# PFSA-ID Corpus

From the 1168 selected articles, during the annotation process, some of the articles were flagged to be excluded from the corpus, for example, articles about obituary, opinion, international news, and news that did not have any direct quote, and the final number is 1018 articles. The 1018 news articles consist of 247 articles in the political and law categories, 245 articles in the economic category, 253 articles in the metro category, and 273 articles in the nusantara category. The final corpus has 811174 tokens. The distribution of each label is shown in the Table below.

Label	| Total
--- | ---
PERSON	| 2514
PERSONCOREF	|	2421
ROLE	|	2586
AFFILIATION	|	1861
CUE	|	2738
CUECOREF	|	1429
STATEMENT	|	4160
ISSUE	|	1018
DATETIME	|	712
LOCATION	|	385
EVENT	|	767



## :books: How to Cite
If you extend or use this work, please cite the paper where it was introduced:
```
@article{PURNOMOWP2022,
	title = {PFSA-ID: an annotated Indonesian corpus and baseline model of public figures statements attributions},
	journal = {Global Knowledge, Memory and Communication},
	volume = {ahead-of-print},
	pages = {ahead-of-print},
	year = {2022},
	issn = {2514-9342},
	doi = {https://doi.org/10.1108/GKMC-04-2022-0091},
	url = {https://www.emerald.com/insight/content/doi/10.1108/GKMC-04-2022-0091/full/html},
	author = {Yohanes Sigit {Purnomo W.P.} and Yogan Jaya Kumar and Nur Zareen Zulkarnain},
	keywords = {Indonesian corpus, Public figures, Statement attribution, News article, Baseline model, Named entity recognition},
	abstract = {Purpose By far, the corpus for the quotation extraction and quotation attribution tasks in Indonesian is still limited in quantity and depth. This study aims to develop an Indonesian corpus of public figure statements attributions and a baseline model for attribution extraction, so it will contribute to fostering research in information extraction for the Indonesian language. Design/methodology/approach The methodology is divided into corpus development and extraction model development. During corpus development, data were collected and annotated. The development of the extraction model entails feature extraction, the definition of the model architecture, parameter selection and configuration, model training and evaluation, as well as model selection. Findings The Indonesian corpus of public figure statements attribution achieved 90.06% agreement level between the annotator and experts and could serve as a gold standard corpus. Furthermore, the baseline model predicted most labels and achieved 82.026% F-score. Originality/value To the best of the authors’ knowledge, the resulting corpus is the first corpus for attribution of public figures’ statements in the Indonesian language, which makes it a significant step for research on attribution extraction in the language. The resulting corpus and the baseline model can be used as a benchmark for further research. Other researchers could follow the methods presented in this paper to develop a new corpus and baseline model for other languages.}
}
```