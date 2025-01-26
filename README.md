### Conservation of protein-protein interactions (PPIs)

Lim, C.S., Mace, P., Fineran P.C. Gardner, P.P. (2024) Towards a phylogenetically-informed approach to solving protein-protein interactions. Manuscript in preparation.

- All figures for the manuscript can be found in [`figs`](https://github.com/lcscs12345/ppi_conservation/tree/main/figs).
- [ppi_conservation.ipynb](https://github.com/lcscs12345/ppi_conservation/blob/main/jupyter_notebooks/ppi_conservation.ipynb) demonstrates the heterogeneity between eight PPI databases, revealing that most PPI entries have been not been validated across species. Related to Fig 1, 2 and 3.
- The list of PPIs that remain to be structurally solved is available [`here`](https://github.com/lcscs12345/ppi_conservation/tree/main/data/unsolved.csv).
- [wnt_ror.ipynb](https://github.com/lcscs12345/ppi_conservation/blob/main/jupyter_notebooks/wnt_ror.ipynb) and [`scripts`](https://github.com/lcscs12345/ppi_conservation/tree/main/scripts) showcase an example of protein complex prediction, i.e. the highly conserved WNT-ROR ligand-receptor complex. Related to Fig 4.
- To reproduce the results, please download the [files](https://doi.org/10.5281/zenodo.14020181) and move them to [`data`](https://github.com/lcscs12345/ppi_conservation/tree/main/data).

```
📦ppi_conservation
 ┣ 📂data
 ┃ ┣ 📂dbs
 ┃ ┃ ┣ 📜biogrid_.pkl.gz
 ┃ ┃ ┣ 📜bioplex_.pkl.gz
 ┃ ┃ ┣ 📜db_cons.pkl.gz
 ┃ ┃ ┣ 📜db_cons_ids.pkl.gz
 ┃ ┃ ┣ 📜dip_.pkl.gz
 ┃ ┃ ┣ 📜dstack.pkl.gz
 ┃ ┃ ┣ 📜dstack_species.pkl.gz
 ┃ ┃ ┣ 📜idmapping.pkl.gz (available on 10.5281/zenodo.14020181)
 ┃ ┃ ┣ 📜intact_.pkl.gz
 ┃ ┃ ┣ 📜mentha_.pkl.gz
 ┃ ┃ ┣ 📜mint_.pkl.gz
 ┃ ┃ ┣ 📜overlap_coefs.pkl.gz
 ┃ ┃ ┣ 📜overlap_coefs_rand.pkl.gz
 ┃ ┃ ┣ 📜pdb_ppi.pkl.gz
 ┃ ┃ ┣ 📜signor_.pkl.gz
 ┃ ┃ ┣ 📜solved_KEGG.pkl.gz
 ┃ ┃ ┣ 📜solved_complexes.pkl.gz
 ┃ ┃ ┣ 📜solved_keggpath.pkl.gz
 ┃ ┃ ┣ 📜solved_keggpath_ids.pkl.gz
 ┃ ┃ ┣ 📜string_.pkl.gz (available on 10.5281/zenodo.14020181)
 ┃ ┃ ┣ 📜unsolved.pkl.gz
 ┃ ┃ ┣ 📜unsolved_KEGG.pkl.gz
 ┃ ┃ ┣ 📜unsolved_KEGG2.pkl.gz
 ┃ ┃ ┣ 📜unsolved_complexes.pkl.gz
 ┃ ┃ ┣ 📜unsolved_keggpath.pkl.gz
 ┃ ┃ ┣ 📜unsolved_keggpath2.pkl.gz
 ┃ ┃ ┗ 📜unsolved_keggpath_ids.pkl.gz
 ┃ ┗ 📂wnt_ror
 ┃ ┃ ┗ 📂esmflow_out (available on 10.5281/zenodo.14020181)
 ┃ ┃ ┣ 📜contacts_x.pkl.gz
 ┃ ┃ ┣ 📜dist_mats.pkl.gz
 ┃ ┃ ┣ 📜idmapping_2024_05_13.fasta.gz
 ┃ ┃ ┣ 📜ipr.pkl.gz
 ┃ ┃ ┣ 📜lineages.pkl.gz
 ┃ ┃ ┣ 📜pro.domtblout
 ┃ ┃ ┣ 📜pro.pkl.gz
 ┃ ┃ ┣ 📜ror.hmm
 ┃ ┃ ┣ 📜selected.csv
 ┃ ┃ ┣ 📜selected.pkl.gz
 ┃ ┃ ┣ 📜uniprotkb_ROR1_2024_04_15.fasta.gz
 ┃ ┃ ┣ 📜uniprotkb_ROR2_2024_04_15.fasta.gz
 ┃ ┃ ┣ 📜uniprotkb_WNT5A_2024_04_15.fasta.gz
 ┃ ┃ ┣ 📜uniprotkb_WNT5B_2024_04_15.fasta.gz
 ┃ ┃ ┣ 📜unsolved.csv
 ┃ ┃ ┣ 📜wnt.hmm
 ┃ ┃ ┣ 📜wnt_ror.csv
 ┃ ┃ ┗ 📜wnt_ror.hmm
 ┣ 📂figs
 ┃ ┣ 📜barplot_counts_conserved_ppi.pdf
 ┃ ┣ 📜barplot_unsolved_complexes.pdf
 ┃ ┣ 📜contact_map.pdf
 ┃ ┣ 📜esmflow_tmscores.pdf
 ┃ ┣ 📜keggpath_counts.pdf
 ┃ ┣ 📜keggpath_unsolved_counts.pdf
 ┃ ┣ 📜networks_og.pdf
 ┃ ┣ 📜overlap_coefs_delta.pdf
 ┃ ┣ 📜overlap_coefs_heatmap_tri.pdf
 ┃ ┣ 📜overlap_coefs_ident.pdf
 ┃ ┣ 📜rmsf_ROR2.pdf
 ┃ ┣ 📜rmsf_WNT5A.pdf
 ┃ ┣ 📜species_counts.pdf
 ┃ ┣ 📜upset_conserved_ppi.pdf
 ┃ ┗ 📜upset_min_subset_size_ppi_idmapping.pdf
 ┣ 📂jupyter_notebooks
 ┃ ┣ 📜ppi_conservation.ipynb
 ┃ ┗ 📜wnt_ror.ipynb
 ┣ 📂scripts
 ┃ ┣ 📜alphaflow_SLURM.sh
 ┃ ┣ 📜usalign_SLURM.sh
 ┃ ┗ 📜usalign_multimodels.py
 ┗ 📜README.md
```
