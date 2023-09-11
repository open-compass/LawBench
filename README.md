# LawBench

Task List

| Cognitive Level                                | ID | Tasks                      | Data Sources | Metrics |
|---------------------------------------------------------|-------------|-------------------------------------|-----------------------|------------------|
|    **Legal Knowledge  Memorization**  | 1-1 <br> 1-2        | Article Recitation   <br>    Knowledge Question Answering           | FLK     <br>   JEC\_QA             | ROUGE-L   <br>  Accuracy     |
|    **Legal Knowledge Understanding**  | 2-1 <br> 2-2 <br> 2-3 <br> 2-4 <br> 2-5 <br> 2-6 <br> 2-7 <br> 2-8   | Document Proofread<br>Dispute Focus Identification <br> Marital Disputes Identification<br> Issue Topic Identification <br> Reading Comprehension <br>Name Entity Recognition <br>Opinion Summarization <br> Argument Mining | CAIL<br>LAIC<br>AIStudio<br>CrimeKgAssitant<br>CAIL<br>CAIL<br>CAIL<br>CAIL                  | F0.5<br>F1<br>F1<br>Accuracy<br>F1<br>F1<br>ROUGE-L<br>Accuracy              |                                                       
| **Legal knowledge Application**| 3-1 <br> 3-2 <br> 3-3 <br> 3-4 <br> 3-5 <br> 3-6 <br> 3-7 <br> 3-8   | Fact-based Article Prediction <br> Scene-based Article Prediction <br> Charge Prediction <br> Prison Term Prediction w.o Article <br> Prison Term Prediction w. Article <br> Case Analysis  <br> Crime Amount Calculation <br>Consultation | CAIL-2018 <br> ChatGPT <br> CAIL-2018 <br> CAIL-2018 <br> CAIL-2018 <br> JEC\_QA <br> LAIC <br> 66law| F1<br> ROUGE-L <br> F1 <br> log-distance <br> log-distance <br> Accuracy<br> ROUGE-L                                                      | 3-2         | Scene-based Article Prediction      | ChatGPT               | Rouge-L          |



Zero-Shot Performance

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

One-Shot Performance
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
