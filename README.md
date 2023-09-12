# LawBench

Large language models (LLMs) have demonstrated strong capabilities in various aspects. However, when applying them to the highly-specialized, safe-critical legal domain, it is unclear how much legal knowledge they possess and whether they can reliably perform law-related tasks. To address this gap, we propose a comprehensive evaluation benchmark LawBench. 

## Introduction
LawBench has been meticulously crafted to have precise assessment of the LLMs’ legal capabilities.
In designing the testing task, we simulated three dimensions of judicial cognition and selected 18 tasks to evaluate the ability of the large model. Compared to some existing benchmarks with only multiple-choice questions, we include more diverse types of tasks closely related to real-world applications, such as legal entity recognition, reading comprehension, crime amount calculation and consultation.
We recognize that the security policies of current large models may decline to respond to certain legal queries or experience difficulty in comprehending instructions, leading to a lack of response. Therefore, we have developed
a separate evaluation metric "anstantion rate" to measure how often the model refuses to provide the answer, or fail to understand the instructions properly.
We report the performances of 46 large language models on LawBench, including a wide range of multilingual/Chinese-specific, general/legal-specific, open/closed sourced large language models.

## Dataset
Our dataset include 18 diverse tasks covering 3 cognitive levels: 
- **Legal knowledge memorization**: whether large language models can memorize legal knowledge in their parameters.
- **Legal knowledge understandin**: whether large language models can comprehend entities, events, and relationships within legal texts, so as to understand the content of the text.
- **Legal knowledge application**: whether large language models can utilize their legal knowledge to solve realistic legal tasks in downstream applications.

### Task List
THe following is the included task list. Every task has 500 examples.

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Cognitive Level</th>
    <th class="tg-0pky">ID</th>
    <th class="tg-0pky">Tasks</th>
    <th class="tg-0pky">Data Sources</th>
    <th class="tg-0pky">Metrics</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-lboi" rowspan="2"><b>Legal Knowledge Memorization</b>></td>
    <td class="tg-qdov">1-1</td>
    <td class="tg-qdov">Article Recitation</td>
    <td class="tg-qdov">FLK</td>
    <td class="tg-qdov">ROUGE-L</td>
  </tr>
  <tr>
    <td class="tg-0pky">1-2</td>
    <td class="tg-qdov">Knowledge Question Answering</td>
    <td class="tg-0pky">JEC_QA</td>
    <td class="tg-0pky">Accuracy</td>
  </tr>
  <tr>
    <td class="tg-lboi" rowspan="8"><b>Legal Knowledge Understanding</b></td>
    <td class="tg-0pky">2-1</td>
    <td class="tg-0pky">Document Proofread</td>
    <td class="tg-0pky">CAIL</td>
    <td class="tg-0pky">F0.5</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-2</td>
    <td class="tg-0pky">Dispute Focus Identification</td>
    <td class="tg-0pky">LAIC</td>
    <td class="tg-0pky">F1</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-3</td>
    <td class="tg-0pky">Marital Disputes Identification</td>
    <td class="tg-0pky">AIStudio</td>
    <td class="tg-0pky">F1</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-4</td>
    <td class="tg-0pky">Issue Topic Identification</td>
    <td class="tg-0pky">CrimeKgAssitant</td>
    <td class="tg-0pky">Accuracy</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-5</td>
    <td class="tg-0pky">Reading Comprehension</td>
    <td class="tg-0pky">CAIL</td>
    <td class="tg-0pky">F1</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-6</td>
    <td class="tg-0pky">Name Entity Recognition</td>
    <td class="tg-0pky">CAIL</td>
    <td class="tg-0pky">F1</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-7</td>
    <td class="tg-0pky">Opinion Summarization</td>
    <td class="tg-0pky">CAIL</td>
    <td class="tg-0pky">ROUGE-L</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-8</td>
    <td class="tg-qdov">Argument Mining</td>
    <td class="tg-0pky">CAIL</td>
    <td class="tg-0pky">Accuracy</td>
  </tr>
  <tr>
    <td class="tg-lboi" rowspan="8"><b>Legal Knowledge Application</b></td>
    <td class="tg-0pky">3-1</td>
    <td class="tg-0pky">Fact-based Article Prediction</td>
    <td class="tg-0pky">CAIL-2018</td>
    <td class="tg-0pky">F1</td>
  </tr>
  <tr>
    <td class="tg-0pky">3-2</td>
    <td class="tg-0pky">Scene-based Article Prediction</td>
    <td class="tg-0pky">ChatGPT</td>
    <td class="tg-0pky">ROUGE-L</td>
  </tr>
  <tr>
    <td class="tg-0pky">3-3</td>
    <td class="tg-0pky">Charge Prediction</td>
    <td class="tg-0pky">CAIL-2018</td>
    <td class="tg-0pky">F1</td>
  </tr>
  <tr>
    <td class="tg-0pky">3-4</td>
    <td class="tg-0pky">Prison Term Prediction w.o Article</td>
    <td class="tg-0pky">CAIL-2018</td>
    <td class="tg-0pky">Normalized log-distance</td>
  </tr>
  <tr>
    <td class="tg-0pky">3-5</td>
    <td class="tg-0pky">Prison Term Prediction w. Article</td>
    <td class="tg-0pky">CAIL-2018</td>
    <td class="tg-0pky">Normalized log-distance</td>
  </tr>
  <tr>
    <td class="tg-0lax">3-6</td>
    <td class="tg-0lax">Case Analysis</td>
    <td class="tg-0lax">JEC_QA</td>
    <td class="tg-0lax">Accuracy</td>
  </tr>
  <tr>
    <td class="tg-0lax">3-7</td>
    <td class="tg-0lax">Crime Amount Calculation</td>
    <td class="tg-0lax">LAIC</td>
    <td class="tg-0lax">Accuracy</td>
  </tr>
  <tr>
    <td class="tg-0lax">3-8</td>
    <td class="tg-0lax">Consultation</td>
    <td class="tg-0lax">66law</td>
    <td class="tg-0lax">ROUGE-L</td>
  </tr>
</tbody>
</table>

### Data Format
The data is stored under the data folder.

## Model List
We test 46 models

## Model Performance
We test the  model performance under 2 scenarios: (1) zero-shot, where only instructions are provided in the prompt, and (2) one-shot, where instructions and one-shot examples are concatenated in the prompt.

### Zero-shot Performance
We show the performances of top-5 models with the highest average scores.

**Note: gpt-3.5-turbo is version 2023.6.13, and all gpt-3.5-turbo results below are for this version**

| Task ID   |   GPT4 |   GPT-3.5-turbo      |   freewilly2_70b    |   qwen-7b-chat    |   internlm-chat-7b-8k    |
|:----------|-------:|---------------------:|--------------------:|------------------:|-------------------------:|
| AVG       |  52.39 |                42.84 |               39.41 |             38.45 |                    35.77 |
| 1-1       |  15.38 |                15.86 |               14.58 |             18.54 |                    15.45 |
| 1-2       |  55.2  |                36    |               34.6  |             34    |                    40.4  |
| 2-2       |  41.65 |                32.37 |               25.57 |             27.42 |                    35.46 |
| 2-3       |  69.79 |                51.73 |               44.2  |             31.42 |                    28.96 |
| 2-4       |  44    |                41.2  |               39    |             35    |                    35.6  |
| 2-5       |  56.5  |                53.75 |               52.03 |             48.48 |                    54.13 |
| 2-6       |  76.6  |                69.55 |               65.54 |             37.88 |                    17.95 |
| 2-7       |  37.92 |                33.49 |               39.07 |             36.04 |                    27.11 |
| 2-8       |  61.2  |                36.4  |               45.8  |             24    |                    36.2  |
| 3-1       |  52.47 |                29.5  |               16.41 |             44.62 |                    34.86 |
| 3-2       |  27.54 |                31.3  |               24.52 |             33.5  |                    19.11 |
| 3-3       |  41.99 |                35.52 |               22.82 |             40.67 |                    41.05 |
| 3-4       |  82.62 |                78.75 |               76.06 |             76.74 |                    63.21 |
| 3-5       |  81.91 |                76.84 |               65.35 |             77.19 |                    67.2  |
| 3-6       |  48.6  |                27.4  |               34.4  |             26.8  |                    34.2  |
| 3-7       |  77.6  |                61.2  |               56.6  |             42    |                    43.8  |
| 3-8       |  19.65 |                17.45 |               13.39 |             19.32 |                    13.37 |

### One-Shot Performance
We show the performances of top-5 models with the highest average scores.
| Task ID   |   GPT4 |   GPT-3.5-turbo      |   qwen-7b-chat    |   freewilly2_70b    |   internlm-chat-7b-8k    |
|:----------|-------:|---------------------:|------------------:|--------------------:|-------------------------:|
| 0         |  53.93 |                45.25 |             40.16 |               39.06 |                    37.64 |
| 1-1       |  17.21 |                16.15 |             17.73 |               15.03 |                    15.16 |
| 1-2       |  54.8  |                37.2  |             28.6  |               36    |                    40.6  |
| 2-2       |  46    |                40.6  |             27.4  |               15    |                    36.6  |
| 2-3       |  69.99 |                54.01 |             32.96 |               41.76 |                    30.91 |
| 2-4       |  44.4  |                41.4  |             31.2  |               38    |                    33.2  |
| 2-5       |  64.8  |                61.98 |             46.71 |               53.55 |                    54.35 |
| 2-6       |  79.96 |                74.04 |             57.34 |               64.99 |                    26.86 |
| 2-7       |  40.52 |                40.68 |             42.58 |               45.06 |                    30.56 |
| 2-8       |  59    |                37.4  |             26.8  |               37.6  |                    30.6  |
| 3-1       |  53.2  |                30.81 |             52.86 |               16.87 |                    38.88 |
| 3-2       |  33.15 |                34.49 |             34.49 |               32.44 |                    28.7  |
| 3-3       |  41.3  |                34.55 |             39.91 |               23.07 |                    42.25 |
| 3-4       |  83.21 |                77.12 |             78.47 |               75.8  |                    67.74 |
| 3-5       |  82.74 |                73.72 |             73.92 |               63.59 |                    71.1  |
| 3-6       |  49.6  |                31.6  |             26.8  |               33    |                    36.2  |
| 3-7       |  77    |                66.4  |             44.6  |               56    |                    44    |
| 3-8       |  19.9  |                17.17 |             20.39 |               16.24 |                    12.11 |


## How to Evaluate Model
### Steps
The steps to evaluate the model predictions are as below:
1. Put prediction results from all systems under a folder F. Every system has one subfolder.
2. Under the subfolder of every system, every task has a prediction file. The name of every task is the task id.
3. Enter the evaluation folder and run "python main.py -i F -o <metric_result>"

The data format is as below:
```
data/
├── system-1
│   ├── 1-1.json
│   ├── 1-2.json
│   ├── ...
├── system-2
│   ├── 1-1.json
│   ├── 1-2.json
│   ├── ...
├── ...
```

The result is a csv file with four columns: task, model_name, score and abstention_rate. 
It will be saved in <metric_result>.

For example, the zero-shot predictions from the 46 tested models are saved in predictions/zero_shot.
You can run
   ```
   cd evaluation
   python main.py -i ../predictions/zero_shot -o ../predictions/zero_shot/results.csv
   ```
to get their evaluation results.

### Requirement

```
rouge_chinese
cn2an
ltp
OpenCC
python-Levenshtein
pypinyin
tqdm
```
