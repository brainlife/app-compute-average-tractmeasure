<h1 align="center">Compute average measures per tract</h1>

<p align="center">
  One value per tract and measure, averaged over the nodes of along-tract profiles in a tractmeasures CSV.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.706"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.706-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT license"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Averages along-tract measures across nodes to give one value per tract and measure, from a tractmeasures CSV, with pandas.**

Groups the input tractmeasures.csv by structureID, averages every numeric column over nodes, drops nodeID, and writes output/tractmeasures.csv. Use it to turn tract profiles into per-tract summaries for statistics.

| | |
|---|---|
| **Inputs** | `neuro/tractmeasures` |
| **Outputs** | `neuro/tractmeasures` |
| **Container** | `brainlife/freesurfer-stats:1.2` |
| **Resources** | 1 CPUs · 14 GB memory · 0.5 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.706](https://doi.org/10.25663/brainlife.app.706) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `tractmeasures` | `neuro/tractmeasures` (macro_micro) | yes | Tractmeasures CSV with structureID and nodeID columns (macro- and microstructural profiles along tracts). |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `output` | `neuro/tractmeasures` | tractmeasures.csv with one row per tract: the mean of each measure across nodes. |

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.706](https://doi.org/10.25663/brainlife.app.706), choose a `neuro/tractmeasures` dataset tagged `macro_micro` (a CSV with `structureID` and `nodeID` columns, such as tract profiles) and press **Execute**. The App groups the rows by `structureID`, averages every numeric column over nodes and drops `nodeID`. The result is archived to your project as a `neuro/tractmeasures` dataset tagged `average`, ready for per-tract statistics.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/). pandas runs inside the container.

1. Clone this repository and check out the branch brainlife.io runs: `git checkout v1.0` (the averaging step on `main` does not reduce over nodes).
2. Create `config.json` with the path to your CSV:

   ```json
   {
       "input": "/input/tractmeasures/tractmeasures.csv"
   }
   ```

3. Run the App:

   ```bash
   ./main
   ```

## Outputs

```text
output/
└── tractmeasures.csv   one row per tract: the mean of each measure across nodes
```

## Citing

> [!TIP]
> If you use this App in your work, please cite the App, the software it builds on and brainlife.io (below). GitHub's **Cite this repository** button gives the App citation in APA and BibTeX.

- Compute average measures per tract. brainlife.io App. [doi:10.25663/brainlife.app.706](https://doi.org/10.25663/brainlife.app.706)
- Fischl. FreeSurfer. *NeuroImage* 62:774-781 (2012). [doi:10.1016/j.neuroimage.2012.01.021](https://doi.org/10.1016/j.neuroimage.2012.01.021)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Franco Pestilli (project director)
- Brad Caron

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io is publicly funded, and acknowledging that support helps keep it running. This App was developed with support from Wellcome, the U.S. National Institutes of Health (including the BRAIN Initiative BRAIN CONNECTS program: The Axonal Projectome EXchange, U24NS140384, and the Center for Mesoscale Connectomics, UM1NS132207) and the U.S. National Science Foundation.</sub>

## License

[MIT](LICENSE).
