# Mice Protein Expression: data dictionary

**Source:** UCI Machine Learning Repository, dataset 342, released under CC BY 4.0.
**Paper:** Higuera C, Gardiner KJ, Cios KJ. *Self-organizing feature maps identify proteins critical to learning in a mouse model of Down syndrome.* PLoS ONE 10(6): e0129126.

## Biological background
Down syndrome is caused by trisomy of human chromosome 21. The **Ts65Dn** mouse carries an extra copy of a large segment of mouse chromosome 16 and is the most widely used mouse model: it shows learning and memory deficits. **Memantine** (an NMDA-receptor antagonist) has been tested as a treatment to improve learning in this model.

Mice were assessed with **contextual fear conditioning**:
- **C/S (context-shock):** the mouse is first allowed to explore the cage and is then given a mild shock. These mice are stimulated to learn the association.
- **S/C (shock-context):** the mouse is shocked immediately and only then exposed to the context. These mice are not expected to learn the association.

Expression levels of 77 proteins or protein modifications that gave detectable signals in the **nuclear fraction of the cortex** were measured.

## Layout
One row = one measurement of all 77 proteins. **Each mouse contributes 15 rows** (replicate measurements from the same animal).

| Column | Meaning |
|--------|---------|
| `MouseID` | `<animal number>_<replicate number>`, for example `309_1` is the first measurement of animal 309 |
| 77 columns ending in `_N` | Expression level of one protein or modification (for example `DYRK1A_N`, `SOD1_N`, `pERK_N`); numeric, arbitrary units, may be missing |
| `Genotype` | `Control` or `Ts65Dn` (trisomic) |
| `Treatment` | `Memantine` or `Saline` |
| `Behavior` | `C/S` (context-shock, stimulated to learn) or `S/C` (shock-context, not stimulated) |
| `class` | Genotype, behaviour and treatment combined into 8 groups |

## The 8 classes
Letter code: genotype (`c` control, `t` Ts65Dn) - behaviour (`CS`, `SC`) - treatment (`m` memantine, `s` saline).

| Class | Mice | Class | Mice |
|-------|------|-------|------|
| `c-CS-s` | 9 | `t-CS-s` | 7 |
| `c-CS-m` | 10 | `t-CS-m` | 9 |
| `c-SC-s` | 9 | `t-SC-s` | 9 |
| `c-SC-m` | 10 | `t-SC-m` | 9 |

72 mice in total (38 control, 34 Ts65Dn), 1080 rows.

## Known data issues
Several proteins have missing values, a few of them for a large share of rows. Some missingness may be related to the experimental group. Treat missingness as part of the analysis.
