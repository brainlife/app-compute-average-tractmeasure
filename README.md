# app-compute-average-tractmeasures

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

**Averages along-tract measures across nodes to give one value per tract and measure, from a tractmeasures CSV, with pandas.**

Groups the input tractmeasures.csv by structureID, averages every numeric column over nodes, drops nodeID, and writes output/tractmeasures.csv. Use it to turn tract profiles into per-tract summaries for statistics.

Run it on brainlife.io: [https://doi.org/10.25663/brainlife.app.706](https://doi.org/10.25663/brainlife.app.706)

| Input | Datatype | Required | Description |
|---|---|---|---|
| `tractmeasures` | `neuro/tractmeasures` (macro_micro) | yes | Tractmeasures CSV with structureID and nodeID columns (macro- and microstructural profiles along tracts). |

| Output | Datatype | Description |
|---|---|---|
| `output` | `neuro/tractmeasures` | tractmeasures.csv with one row per tract: the mean of each measure across nodes. |

Runtime: container `brainlife/freesurfer-stats:1.2`; 1 CPUs; 14 GB memory; 0.5 h walltime.

<!-- brainlife-app:end -->

