[![License: LGPL-2.1](https://img.shields.io/badge/license-LGPL--2.1-lightgrey.svg)](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html)

# Sleeping Beauties in Case Law

This repository contains the code to reproduce the computational study from the [paper](https://cris.maastrichtuniversity.nl/en/publications/sleeping-beauties-in-case-law) by [Pedro Hernández Serrano](https://cris.maastrichtuniversity.nl/en/persons/pedro-hern%C3%A1ndez-serrano), [Kody Moodley](https://cris.maastrichtuniversity.nl/en/persons/kody-moodley), [Gijs van Dijck](https://cris.maastrichtuniversity.nl/en/persons/gijs-van-dijck), and [Michel Dumontier](https://cris.maastrichtuniversity.nl/en/persons/michel-dumontier)

![](figures/CorrelationsV2.jpg)

One of the challenges in computational legal research is trying to quantitatively assess “relevance” in a network of court decisions. In Scientometrics, the phenomena of “delayed recognition” for scientific publications has been studied. In this connection, the term "sleeping beauty" (SB) was coined to denote an article that received almost no attention immediately after publication, but suddenly receives a burst of citations many years later, these publications can be identified by calculating their so-called Beauty coefficient (B-coefficient). In this contribution, we apply approaches used for identifying SBs to the context of European case law, more specifically to decisions arising from the Court of Justice of the European Union (CJEU). We compared B-coefficients of CJEU cases with their centrality scores using classical algorithms from network analysis, finding that these measures tend to correlate. This makes the B-coefficient a potential candidate for an additional measure of case relevance or significance. We discuss the implications of this that are interesting for legal scholars, acknowledging that future work is required to calibrate the scale of the time variable in the B-coefficient formula for finer-grained application to case law. The setup of our study provides a template and foundation for a set of methodologies for case law analytics that extends the power of traditional network analysis techniques for answering questions about the behavior of European court systems.

![](figures/subjects_SB.png)
![](figures/top10SBs.png)

## Citation

For attribution in academic contexts, please cite this work as:

```latex
@inproceedings{serrano2020sleeping,
  title = {Sleeping Beauties in Case Law},
  author = {{Hern{\'a}ndez Serrano}, Pedro and Kody Moodley and {van Dijck}, Gijs and Michel Dumontier},
  booktitle = {International Conference on Legal Knowledge and Information Systems, JURIX},
  month = dec,
  year = {2020},
  address = {Prague, Czech Republic}
}
```

## License

This repository is licensed under the terms of the [LGPL-2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html) license.
