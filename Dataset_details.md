# Dataset Details for GC Content Analysis

## Dataset Overview
The dataset used in this project contains genomic sequences in FASTA format. Each sequence represents a segment of DNA, and the GC content for each sequence is calculated.

### Data Characteristics
- **File Format**: FASTA
- **Organism**: *Lampyris noctiluca* (Common Glow-worm)
- **Number of Sequences**: 10

### Example FASTA File Structure
```fasta
>MZ265787.1
ATGCGTACGTAGCTAG
>MZ265786.1
CGCGATCGATCGATCG
>MZ265784.1
AATTGCCATTGCCATT
>MZ265782.1
ATATGCCATTGCCATT
>MZ265783.1
GCCATTGGCATTGGCA
>MZ265781.1
GCGGCGATCGATCGGC
>MZ265779.1
ATTGCCATTGCCATTA
>MZ265778.1
GCCATTGGCCATTGGA
>MZ265776.1
ATGCGCCTGCGCCTGC
>MZ265774.1
ATTGCCATTGCCATTA
```

### Sequence Details
| **Sequence ID** | **Clone Name**              | **Number of Base Pairs (bp)** |
|------------------|-----------------------------|-------------------------------|
| MZ265787.1       | Ln_828167                  | 200                           |
| MZ265786.1       | Ln_491643                  | 209                           |
| MZ265784.1       | Ln_825696                  | 149                           |
| MZ265782.1       | Ln_683928                  | 222                           |
| MZ265783.1       | Ln_769417                  | 101                           |
| MZ265781.1       | Ln_599464                  | 192                           |
| MZ265779.1       | Ln_494378                  | 198                           |
| MZ265778.1       | Ln_289123                  | 144                           |
| MZ265776.1       | Ln_27108                   | 183                           |
| MZ265774.1       | Ln_589048                  | 94                            |

### Total Base Pairs
- **Value**: 1,692 bp

---

## Analysis Workflow
1. **Input Data**:
   - The dataset is provided in a single FASTA file (`sequence.fasta`).

2. **Processing Steps**:
   - GC content for each sequence is calculated using a Python script.
   - The results are saved to an output file (`results.txt`) for visualization and analysis.

3. **Output Example**:
   - Individual GC content for each sequence.
   - Average GC content across all sequences.

---

## Notes
- The dataset is specifically tailored for demonstrating GC content analysis.
- The number of sequences and their base pairs may vary based on the input file.

---

## File Information
- **FASTA File Name**: `sequence.fasta`
- **Output File Name**: `results.txt`

---
