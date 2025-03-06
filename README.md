[![GitHub license](https://img.shields.io/github/license/materialsvirtuallab/matpes)](https://github.com/materialsvirtuallab/matpes/blob/main/LICENSE)
[![Linting](https://github.com/materialsvirtuallab/matpes/workflows/Linting/badge.svg)](https://github.com/materialsvirtuallab/matpes/workflows/Linting/badge.svg)

### Aims

MatPES is an initiative by the [Materials Virtual Lab] and the [Materials Project] to address
[critical deficiencies](http://matpes.ai/about) in potential energy surface (PES) datasets for materials.

1. **Accuracy.** MatPES is computed using static DFT calculations with stringent converegence criteria.
   Please refer to the `MatPESStaticSet` in [pymatgen] for details.
2. **Comprehensiveness.** MatPES structures are sampled using a 2-stage version of DImensionality-Reduced
   Encoded Clusters with sTratified ([DIRECT]) sampling from a greatly expanded configuration of MD structures.
3. **Quality.** MatPES includes computed data from the PBE functional, as well as the high fidelity r2SCAN meta-GGA
   functional with improved description across diverse bonding and chemistries.

The initial v2025.1 release comprises ~400,000 structures from 300K MD simulations. This dataset is much smaller
than other PES datasets in the literature and yet achieves comparable or, in some cases,
[improved performance and reliability](http://matpes.ai/benchmarks).

### Software

The `matpes` python package, which provides tools for working with the MatPES datasets, can be installed via pip:

```shell
pip install matpes
```

Some command line usage examples:

```shell
# Download the PBE dataset to the current directory
matpes download pbe

# You should see a MatPES-PBE-20240214.json.gz file in your directory.

# Extract all entries in the Fe-O chemical system
matpes data -i MatPES-PBE-20240214.json.gz --chemsys Fe-O -o Fe-O.json.gz
```

The `matpes.db` module provides functionality to create your own MongoDB database with the MatPES downloaded data,
which is extremely useful if you are going to be working with the data (e.g., querying, adding entries, etc.) a lot.

### Models

We have released a set of MatPES-trained universal machine learning interatomic potentials (UMLIPs) in the [M3GNet],
[CHGNet], [TensorNet] architectures in the [MatGL] package.

### Tutorials

We have provided a series of Jupyter notebooks demonstrating how to load the MatPES dataset, train a model and perform
fine-tuning.

### Citing

If you use MatPES, please cite the following work:

```txt
Aaron Kaplan, Runze Liu, Ji Qi, Tsz Wai Ko, Bowen Deng, Gerbrand Ceder, Kristin A. Persson, Shyue Ping Ong.
A foundational potential energy surface dataset for materials. Submitted.
```

[Materials Virtual Lab]: http://materialsvirtuallab.org
[Materials Project]: https://materialsproject.org
[MatGL]: https://matgl.ai
[M3GNet]: http://dx.doi.org/10.1038/s43588-022-00349-3
[CHGNet]: http://doi.org/10.1038/s42256-023-00716-3
[TensorNet]: https://arxiv.org/abs/2306.06482
[DIRECT]: https//doi.org/10.1038/s41524-024-01227-4
