# GC Content Analysis of *Lampyris noctiluca* Clones

## Overview
This project focuses on analyzing the GC content of genomic sequences from *Lampyris noctiluca* (common glow-worm). By studying the GC content across different sequences, we aim to understand genome characteristics, including coding and noncoding regions, evolutionary adaptations, and potential functional elements like bioluminescence-related genes.

---

## Data Summary
The dataset contains four genomic sequences with varying GC content:
| **Sequence ID** | **GC Content (%)** | **Description** |
|------------------|--------------------|------------------|
| MZ265787.1       | 28.50%            | AT-rich; likely noncoding or regulatory region. |
| MZ265786.1       | 32.06%            | Slightly higher GC content; may represent mixed coding/noncoding region. |
| MZ265784.1       | 41.61%            | GC-rich; possibly a protein-coding region or GC-rich gene. |
| MZ265782.1       | 27.93%            | Strong AT bias; likely a noncoding or repetitive region. |
| MZ265783.1       | 29.70%            | Near average GC content; potential regulatory or intergenic region. |
| MZ265781.1       | 27.08%            | AT-dominant region; possibly noncoding or repetitive. |
| MZ265779.1       | 34.34%            | GC-enriched; likely indicative of coding sequences. |
| MZ265778.1       | 33.33%            | Moderate GC content; could represent coding DNA. |
| MZ265776.1       | 27.87%            | AT-rich; likely a noncoding or repetitive region. |
| MZ265774.1       | 29.79%            | Close to average GC content; potential regulatory region or intergenic DNA. |
---

## Objectives
1. **Analyze GC Content**:
   - Calculate and compare GC content across sequences.
   - Identify regions with significant AT or GC biases.

2. **Functional Implications**:
   - Explore potential coding and noncoding regions based on GC content.
   - Investigate links between GC-rich regions and protein-coding genes.

3. **Evolutionary Insights**:
   - Understand genome organization and potential adaptations of *Lampyris noctiluca*.

---

## Tools and Technologies
- **Programming Language**: Python
- **Libraries**: Biopython, Matplotlib

---

## Methodology
1. **Data Input**:
   - DNA sequences are provided in a single FASTA file (`sequence.fasta`).

2. **GC Content Calculation**:
   - Developed a Python script to calculate GC content for each sequence.

3. **Visualization**:
   - Bar charts to illustrate GC content variations across sequences.

4. **Interpretation**:
   - Correlated GC content with potential genomic functions and evolutionary traits.

---

## Results
- **Average GC Content**:
  - The dataset has an average GC content of 32.52%, indicating an AT-rich genome.
- **Sequence Variability**:
  - GC content ranges from 27.93% to 41.61%, highlighting differences in genomic regions.

---

## Key Findings
- **Functional Regions**:
  - GC-rich regions (e.g., 41.61%) likely represent protein-coding genes.
  - AT-rich regions may correspond to noncoding or regulatory sequences.

- **Bioluminescence Genes**:
  - Further analysis could focus on identifying genes related to *luciferase*, a key enzyme for bioluminescence.

- **Evolutionary Insights**:
  - The AT-rich genome aligns with known characteristics of many insect species.

---

## How to Use
### Requirements
- Python 3.6+
- Required Libraries:
  ```bash
  pip install biopython matplotlib
  ```

### Run the Script
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/gc-content-analysis.git
   cd gc-content-analysis
   ```

2. Run the script:
   ```bash
   python gc_calculator.py --input sequence.fasta
   ```

3. Output:
   - GC content for each sequence.
   - Average GC content for the dataset.

---

## Future Work
- Extend analysis to larger datasets.
- Functional annotation of GC-rich regions.
- Investigate bioluminescence-related genes and their evolutionary significance.

---

## Author
- **Sravya Sri Mallampalli**
  - [GitHub Profile](https://github.com/Sravz2433)
  - [LinkedIn](https://www.linkedin.com/in/sravya-sri-mallampalli)

---

## License
This project is licensed under the MIT License.
