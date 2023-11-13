<div align = center>
    <img width = '540' height = '160' src = './figs/LawBench Logo.png'>
</div>
<h1 align="center">Benchmarking Legal Knowledge of Large Language Models</h1> </center>
<p align="center">
   🌐 <a href="https://lawbench.opencompass.org.cn/home" target="_blank">Website</a> • 🤗 <a href="https://huggingface.co/opencompass" target="_blank">Hugging Face</a> • ⏬ <a href="https://github.com/open-compass/LawBench/tree/main/data" target="_blank">Data</a> •   📃 <a href="https://arxiv.org/abs/2309.16289" target="_blank">Paper</a> 
</p>

<p align="center">
    📖 <a href="https://github.com/open-compass/LawBench/blob/main/README.md">   中文</a> | <a href="https://github.com/open-compass/LawBench/blob/main/README_EN.md">English</a>
</p>

Large language models (LLMs) have demonstrated strong capabilities in various aspects. However, when applying them to the highly-specialized, safe-critical legal domain, it is unclear how much legal knowledge they possess and whether they can reliably perform law-related tasks. To address this gap, we propose a comprehensive evaluation benchmark **LawBench**. Please refer to our <a href="https://arxiv.org/abs/2309.16289" target="_blank">paper</a> for more details.

**Tasks in LawBench are based on the law system of China. A similar bench based on the American law system is available [here](https://github.com/HazyResearch/legalbench).**

## ✨ Introduction
LawBench has been meticulously crafted to have precise assessment of the LLMs’ legal capabilities.
In designing the testing tasks, we simulated three dimensions of judicial cognition and selected 20 tasks to evaluate the abilities of large models. Compared to some existing benchmarks with only multiple-choice questions, we include more diverse types of tasks closely related to real-world applications, such as legal entity recognition, reading comprehension, criminal damages calculation and consultation.
We recognize that the security policies of current large models may decline to respond to certain legal queries or experience difficulty in comprehending instructions, leading to a lack of response. Therefore, we have developed a separate evaluation metric "abstention rate" to measure how often the model refuses to provide the answer, or fail to understand the instructions properly.
We report the performances of 51 large language models on LawBench, including 20 multilingual LLMs, 22 Chinese-oriented LLMs and 9 legal specific LLMs.

## 📖 Dataset
Our dataset include 20 diverse tasks covering 3 cognitive levels:
- **Legal knowledge memorization**: whether large language models can memorize necessary legal concepts, terminologies, articles and facts in their parameters.
- **Legal knowledge understanding**: whether large language models can comprehend entities, events, and relationships within legal texts, so as to understand the meanings and connotations of legal text.
- **Legal knowledge applying**: whether large language models can properly utilize their legal knowledge, reason over it to solve realistic legal tasks in downstream applications.

### Task List
The following is the included task list. Every task has 500 examples.

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Cognitive Level</th>
    <th class="tg-0pky">ID</th>
    <th class="tg-0pky">Tasks</th>
    <th class="tg-0pky">Data Sources</th>
    <th class="tg-0pky">Metrics</th>
    <th class="tg-0pky">Type</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-lboi" rowspan="2"><b>Legal Knowledge Memorization</b></td>
    <td class="tg-qdov">1-1</td>
    <td class="tg-qdov">Article Recitation</td>
    <td class="tg-qdov"><a href="https://flk.npc.gov.cn/">FLK</a></td>
    <td class="tg-qdov">ROUGE-L</td>
    <td class="tg-qdov">Generation</td>
  </tr>
  <tr>
    <td class="tg-0pky">1-2</td>
    <td class="tg-qdov">Knowledge Question Answering</td>
    <td class="tg-0pky">JEC_QA</td>
    <td class="tg-0pky">Accuracy</td>
    <td class="tg-0pky">SLC</td>
  </tr>
  <tr>
    <td class="tg-lboi" rowspan="10"><b>Legal Knowledge Understanding</b></td>
    <td class="tg-0pky">2-1</td>
    <td class="tg-0pky">Document Proofread</td>
    <td class="tg-0pky">CAIL2022</td>
    <td class="tg-0pky">F0.5</td>
    <td class="tg-0pky">Generation</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-2</td>
    <td class="tg-0pky">Dispute Focus Identification</td>
    <td class="tg-0pky">LAIC2021</td>
    <td class="tg-0pky">F1</td>
    <td class="tg-0pky">MLC</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-3</td>
    <td class="tg-0pky">Marital Disputes Identification</td>
    <td class="tg-0pky">AIStudio</td>
    <td class="tg-0pky">F1</td>
    <td class="tg-0pky">MLC</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-4</td>
    <td class="tg-0pky">Issue Topic Identification</td>
    <td class="tg-0pky"><a href="https://github.com/liuhuanyong/CrimeKgAssitant">CrimeKgAssitant</a></td>
    <td class="tg-0pky">Accuracy</td>
    <td class="tg-0pky">SLC</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-5</td>
    <td class="tg-0pky">Reading Comprehension</td>
    <td class="tg-0pky">CAIL2019</td>
    <td class="tg-0pky">rc-F1</td>
    <td class="tg-0pky">Extraction</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-6</td>
    <td class="tg-0pky">Name Entity Recognition</td>
    <td class="tg-0pky"><a href="https://github.com/china-ai-law-challenge/CAIL2021/tree/main/xxcq">CAIL2021</a></td>
    <td class="tg-0pky">soft-F1</td>
    <td class="tg-0pky">Extraction</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-7</td>
    <td class="tg-0pky">Opinion Summarization</td>
    <td class="tg-0pky">CAIL2022</td>
    <td class="tg-0pky">ROUGE-L</td>
    <td class="tg-0pky">Generation</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-8</td>
    <td class="tg-qdov">Argument Mining</td>
    <td class="tg-0pky">CAIL2022</td>
    <td class="tg-0pky">Accuracy</td>
    <td class="tg-0pky">SLC</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-9</td>
    <td class="tg-qdov">Event Detection</td>
    <td class="tg-0pky">LEVEN</td>
    <td class="tg-0pky">F1</td>
    <td class="tg-0pky">MLC</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-10</td>
    <td class="tg-qdov">Trigger Word Extraction</td>
    <td class="tg-0pky">LEVEN</td>
    <td class="tg-0pky">soft-F1</td>
    <td class="tg-0pky">Extraction</td>
  </tr>
  <tr>
    <td class="tg-lboi" rowspan="8"><b>Legal Knowledge Applying</b></td>
    <td class="tg-0pky">3-1</td>
    <td class="tg-0pky">Fact-based Article Prediction</td>
    <td class="tg-0pky">CAIL2018</td>
    <td class="tg-0pky">F1</td>
    <td class="tg-0pky">MLC</td>
  </tr>
  <tr>
    <td class="tg-0pky">3-2</td>
    <td class="tg-0pky">Scene-based Article Prediction</td>
    <td class="tg-0pky"><a href="https://github.com/LiuHC0428/LAW-GPT">LawGPT_zh Project</a></td>
    <td class="tg-0pky">ROUGE-L</td>
    <td class="tg-0pky">Generation</td>
  </tr>
  <tr>
    <td class="tg-0pky">3-3</td>
    <td class="tg-0pky">Charge Prediction</td>
    <td class="tg-0pky">CAIL2018</td>
    <td class="tg-0pky">F1</td>
    <td class="tg-0pky">MLC</td>
  </tr>
  <tr>
    <td class="tg-0pky">3-4</td>
    <td class="tg-0pky">Prison Term Prediction w.o Article</td>
    <td class="tg-0pky">CAIL2018</td>
    <td class="tg-0pky">Normalized log-distance</td>
    <td class="tg-0pky">Regression</td>
  </tr>
  <tr>
    <td class="tg-0pky">3-5</td>
    <td class="tg-0pky">Prison Term Prediction w. Article</td>
    <td class="tg-0pky">CAIL2018</td>
    <td class="tg-0pky">Normalized log-distance</td>
    <td class="tg-0pky">Regression</td>
  </tr>
  <tr>
    <td class="tg-0lax">3-6</td>
    <td class="tg-0lax">Case Analysis</td>
    <td class="tg-0lax">JEC_QA</td>
    <td class="tg-0lax">Accuracy</td>
    <td class="tg-0lax">SLC</td>
  </tr>
  <tr>
    <td class="tg-0lax">3-7</td>
    <td class="tg-0lax">Crimal Damages Calculation</td>
    <td class="tg-0lax">LAIC2021</td>
    <td class="tg-0lax">Accuracy</td>
    <td class="tg-0lax">Regression</td>
  </tr>
  <tr>
    <td class="tg-0lax">3-8</td>
    <td class="tg-0lax">Consultation</td>
    <td class="tg-0lax"><a href="https://www.66law.cn/">hualv.com</a></td>
    <td class="tg-0lax">ROUGE-L</td>
    <td class="tg-0lax">Generation</td>
  </tr>
</tbody>
</table>

### Data Format
The data is stored under the [data](https://github.com/open-compass/LawBench/tree/main/data) folder. Every task is stored in the <task_id>.json file.
The json file can be loaded via json.load as a list of dictionaries.
The data format is as follows (use task 3-2 as an example):

```json
[
  {
    "instruction": "请根据具体场景与问题给出法律依据，只需要给出具体法条内容，每个场景仅涉及一个法条。",
    "question": "场景:某个地区的三个以上专业农民合作社想要出资设立农民专业合作社联合社，以提高其在市场中的竞争力和规模效应。根据哪条法律，三个以上的农民专业合作社可以出资设立农民专业合作社联合社？",
    "answer": "根据《农民专业合作社法》第五十六条，三个以上的农民专业合作社在自愿的基础上，可以出资设立农民专业合作社联合社。该联合社应当有自己的名称、组织机构和住所，由联合社全体成员制定并承认的章程，以及符合章程规定的成员出资。"
  },
]
```

### Model Output Format
The model outputs are stored under the [predictions/zero_shot](https://github.com/open-compass/LawBench/tree/main/predictions/zero_shot) and [predictions/one_shot](https://github.com/open-compass/LawBench/tree/main/predictions/one_shot) folder. Every system has its own subfolder. Within each subfolder, task predictions are stored in  <task_id>.json file.
The json file can be loaded via json.load as a dictionary.
The data format is as follows (use task 3-2 from GPT-4 zero-shot prediction as an example):

```json
{
    "0": {
        "origin_prompt": [
            {
                "role": "HUMAN",
                "prompt": "请根据具体场景与问题给出法律依据，只需要给出具体法条内容，每个场景仅涉及一个法条。\n场景:某个地区的三个以上专业农民合作社想要出资设立农民专业合作社联合社，以提高其在市场中的竞争力和规模效应。根据哪条法律，三个以上的农民专业合作社可以出资设立农民专业合作社联合社？"
            }
        ],
        "prediction": "根据《中华人民共和国农民专业合作社法》第十七条：“三个以上的农民专业合作社可以出资设立农民专业合作社联合社。”",
        "refr": "根据《农民专业合作社法》第五十六条，三个以上的农民专业合作社在自愿的基础上，可以出资设立农民专业合作社联合社。该联合社应当有自己的名称、组织机构和住所，由联合社全体成员制定并承认的章程，以及符合章程规定的成员出资。"
    },
```

## 📖 Model List
We test 51 popular large language models. We group them as in the following table:
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Model</th>
    <th class="tg-0pky">Parameters</th>
    <th class="tg-0pky">SFT</th>
    <th class="tg-0pky">RLHF</th>
    <th class="tg-0lax">Access</th>
    <th class="tg-0lax">Base Model</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-9wq8" colspan="8"><b>Multilingual LLMs</b></td>
  </tr>
  <tr>
    <td class="tg-za14">MPT</td>
    <td class="tg-za14">7B</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">-</td>
  </tr>
  <tr>
    <td class="tg-za14">MPT-Instruct</td>
    <td class="tg-za14">7B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">MPT-7B</td>
  </tr>
  <tr>
    <td class="tg-za14">LLaMA</td>
    <td class="tg-za14">7/13/30/65B</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">-</td>
  </tr>
  <tr>
    <td class="tg-za14">LLaMA-2</td>
    <td class="tg-za14">7/13/70B</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">-</td>
  </tr>
  <tr>
    <td class="tg-za14">LLaMA-2-Chat</td>
    <td class="tg-za14">7/13/70B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">LLaMA-2-7/13/70B</td>
  </tr>
  <tr>
    <td class="tg-0pky">Alpaca-v1.0</td>
    <td class="tg-0pky">7B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">LLaMA-7B</td>
  </tr>
  <tr>
    <td class="tg-za14">Vicuna-v1.3</td>
    <td class="tg-za14">7/13/33B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">LLaMA-7/13/33B</td>
  </tr>
  <tr>
    <td class="tg-za14">WizardLM</td>
    <td class="tg-za14">7B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">LLaMA-7B</td>
  </tr>
  <tr>
    <td class="tg-za14">StableBeluga2</td>
    <td class="tg-za14">70B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">LLaMA-2-70B</td>
  </tr>
  <tr>
    <td class="tg-za14">ChatGPT</td>
    <td class="tg-za14">N/A</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0lax">API</td>
    <td class="tg-0lax">-</td>
  </tr>
  <tr>
    <td class="tg-za14">GPT-4</td>
    <td class="tg-za14">N/A</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0lax">API</td>
    <td class="tg-0lax">-</td>
  </tr>
  <tr>
    <td class="tg-9wq8" colspan="8"><b>Chinese-oriented LLMs</b></td>
  </tr>
  <tr>
    <td class="tg-7zrl">MOSS-Moon</td>
    <td class="tg-7zrl">16B</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-7zrl">-</td>
  </tr>
  <tr>
    <td class="tg-7zrl">MOSS-Moon-SFT</td>
    <td class="tg-7zrl">16B</td>
    <td class="tg-0lax">&#10003</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-7zrl">MOSS-Moon</td>
  </tr>
  <tr>
    <td class="tg-0lax">TigerBot-Base</td>
    <td class="tg-0lax">7B</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">-</td>
  </tr>
  <tr>
    <td class="tg-0lax">TigerBot-SFT</td>
    <td class="tg-hx86">7B</td>
    <td class="tg-0lax">&#10003</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">TigerBot-Base</td>
  </tr>
  <tr>
    <td class="tg-7zrl">GoGPT</td>
    <td class="tg-7zrl">7B</td>
    <td class="tg-0lax">&#10003</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">LLaMA-7B</td>
  </tr>
  <tr>
    <td class="tg-7zrl">ChatGLM2</td>
    <td class="tg-7zrl">6B</td>
    <td class="tg-0lax">&#10003</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-7zrl">ChatGLM</td>
  </tr>
  <tr>
    <td class="tg-za14">Ziya-LLaMA</td>
    <td class="tg-za14">13B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">LLaMA-13B</td>
  </tr>
  <tr>
    <td class="tg-7zrl">Baichuan</td>
    <td class="tg-7zrl">7/13B</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-7zrl">-</td>
  </tr>
  <tr>
    <td class="tg-7zrl">Baichuan-13B-Chat</td>
    <td class="tg-7zrl">13B</td>
    <td class="tg-0lax">&#10003</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-7zrl">Baichuan-13B</td>
  </tr>
  <tr>
    <td class="tg-7zrl">XVERSE</td>
    <td class="tg-7zrl">13B</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-7zrl">-</td>
  </tr>
  <tr>
    <td class="tg-7zrl">InternLM</td>
    <td class="tg-7zrl">7B</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-7zrl">-</td>
  </tr>
  <tr>
    <td class="tg-7zrl">InternLM-Chat</td>
    <td class="tg-7zrl">7B</td>
    <td class="tg-0lax">&#10003</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-7zrl">InternLM-7B</td>
  </tr>
  <tr>
    <td class="tg-7zrl">InternLM-Chat-7B-8K</td>
    <td class="tg-7zrl">7B</td>
    <td class="tg-0lax">&#10003</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-7zrl">InternLM-7B</td>
  </tr>
  <tr>
    <td class="tg-7zrl">Qwen</td>
    <td class="tg-7zrl">7B</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-7zrl">-</td>
  </tr>
  <tr>
    <td class="tg-7zrl">Qwen-7B-Chat</td>
    <td class="tg-7zrl">7B</td>
    <td class="tg-0lax">&#10003</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-7zrl">Qwen-7B</td>
  </tr>
  <tr>
    <td class="tg-7zrl">Yulan-Chat-2</td>
    <td class="tg-7zrl">13B</td>
    <td class="tg-0lax">&#10003</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-7zrl">LLaMA-2-13B</td>
  </tr>
  <tr>
    <td class="tg-za14">BELLE-LLaMA-2</td>
    <td class="tg-za14">13B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">LLaMA-2-13B</td>
  </tr>
  <tr>
    <td class="tg-7zrl">Chinese-LLaMA-2</td>
    <td class="tg-7zrl">7B</td>
    <td class="tg-0lax">&#10003</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">LLaMA-2-7B</td>
  </tr>
  <tr>
    <td class="tg-za14">Chinese-Alpaca-2</td>
    <td class="tg-za14">7B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">LLaMA-2-7B</td>
  </tr>
  <tr>
    <td class="tg-za14">LLaMA-2-Chinese</td>
    <td class="tg-za14">7/13B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">LLaMA-2-7/13B</td>
  </tr>
  <tr>
    <td class="tg-baqh" colspan="8"><span style="font-weight:400;font-style:normal"><b>Legal Specific LLMs</b></span></td>
  </tr>
  <tr>
    <td class="tg-za14">HanFei</td>
    <td class="tg-za14">7B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">HanFei</td>
  </tr>
  <tr>
    <td class="tg-za14">LaWGPT-7B-beta1.0</td>
    <td class="tg-za14">7B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">Chinese-LLaMA</td>
  </tr>
  <tr>
    <td class="tg-za14">LaWGPT-7B-beta1.1</td>
    <td class="tg-za14">7B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">Chinese-alpaca-plus-7B</td>
  </tr>
  <tr>
    <td class="tg-za14">LexiLaw</td>
    <td class="tg-za14">6B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">ChatGLM-6B</td>
  </tr>
  <tr>
    <td class="tg-za14">Wisdom-Interrogatory</td>
    <td class="tg-za14">7B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">Baichuan-7B</td>
  </tr>
  <tr>
    <td class="tg-za14">Fuzi-Mingcha</td>
    <td class="tg-za14">6B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">ChatGLM-6B</td>
  </tr>
  <tr>
    <td class="tg-za14">Lawyer-LLaMA</td>
    <td class="tg-azeh">13B</td>
    <td class="tg-0pky">&#10003</td>
    <td class="tg-0pky">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-0lax">LLaMA</td>
  </tr>
  <tr>
    <td class="tg-7zrl">ChatLaw</td>
    <td class="tg-7zrl">13/33B</td>
    <td class="tg-0lax">&#10003</td>
    <td class="tg-0lax">&#10007</td>
    <td class="tg-0lax">Weights</td>
    <td class="tg-7zrl">Ziya-LLaMA-13B/Anima-33B</td>
  </tr>
</tbody>
</table>

## 📊 Model Performance
We test the  model performance under 2 scenarios: (1) zero-shot, where only instructions are provided in the prompt, and (2) one-shot, where instructions and one-shot examples are concatenated in the prompt.

### Zero-shot Performance

Average performance (zero-shot) of 51 LLMs evaluated on LawBench.

<div align = center>
    <img src = './figs/0-shot.png'>
</div>

We show the performances of top-5 models with the highest average scores.

**Note: gpt-3.5-turbo is version 2023.6.13, and all gpt-3.5-turbo results below are for this version**

| Task ID | GPT4  | GPT-3.5-turbo | StableBeluga2 | qwen-7b-chat | internlm-chat-7b-8k |
| :-----: | :---: | :-----------: | :-----------: | :----------: | :-----------------: |
|   AVG   | 52.35 |     42.15     |     39.23     |    37.00     |        35.73        |
|   1-1   | 15.38 |     15.86     |     14.58     |    18.54     |        15.45        |
|   1-2   | 55.20 |     36.00     |     34.60     |    34.00     |        40.40        |
|   2-1   | 12.53 |     9.10      |     7.70      |    22.56     |        22.64        |
|   2-2   | 41.65 |     32.37     |     25.57     |    27.42     |        35.46        |
|   2-3   | 69.79 |     51.73     |     44.20     |    31.42     |        28.96        |
|   2-4   | 44.00 |     41.20     |     39.00     |    35.00     |        35.60        |
|   2-5   | 56.50 |     53.75     |     52.03     |    48.48     |        54.13        |
|   2-6   | 76.60 |     69.55     |     65.54     |    37.88     |        17.95        |
|   2-7   | 37.92 |     33.49     |     39.07     |    36.04     |        27.11        |
|   2-8   | 61.20 |     36.40     |     45.80     |    24.00     |        36.20        |
|   2-9   | 78.82 |     66.48     |     65.27     |    44.88     |        62.93        |
|  2-10   | 65.09 |     39.05     |     41.64     |    18.90     |        20.94        |
|   3-1   | 52.47 |     29.50     |     16.41     |    44.62     |        34.86        |
|   3-2   | 27.54 |     31.30     |     24.52     |    33.50     |        19.11        |
|   3-3   | 41.99 |     35.52     |     22.82     |    40.67     |        41.05        |
|   3-4   | 82.62 |     78.75     |     76.06     |    76.74     |        63.21        |
|   3-5   | 81.91 |     76.84     |     65.35     |    77.19     |        67.20        |
|   3-6   | 48.60 |     27.40     |     34.40     |    26.80     |        34.20        |
|   3-7   | 77.60 |     61.20     |     56.60     |    42.00     |        43.80        |
|   3-8   | 19.65 |     17.45     |     13.39     |    19.32     |        13.37        |

### One-Shot Performance

Average performance (one-shot) of 51 LLMs evaluated on LawBench.

<div align = center>
    <img src = './figs/1-shot.png'>
</div>

We show the performances of top-5 models with the highest average scores.
| Task ID | GPT4  | GPT-3.5-turbo | qwen-7b-chat | StableBeluga2 | internlm-chat-7b-8k |
| :-----: | :---: | :-----------: | :----------: | :-----------: | :-----------------: |
|   AVG   | 53.85 |     44.52     |    38.99     |     38.97     |        37.28        |
|   1-1   | 17.21 |     16.15     |    17.73     |     15.03     |        15.16        |
|   1-2   | 54.80 |     37.20     |    28.60     |     36.00     |        40.60        |
|   2-1   | 18.31 |     13.50     |    25.16     |     8.93      |        21.64        |
|   2-2   | 46.00 |     40.60     |    27.40     |     15.00     |        36.60        |
|   2-3   | 69.99 |     54.01     |    32.96     |     41.76     |        30.91        |
|   2-4   | 44.40 |     41.40     |    31.20     |     38.00     |        33.20        |
|   2-5   | 64.80 |     61.98     |    46.71     |     53.55     |        54.35        |
|   2-6   | 79.96 |     74.04     |    57.34     |     64.99     |        26.86        |
|   2-7   | 40.52 |     40.68     |    42.58     |     45.06     |        30.56        |
|   2-8   | 59.00 |     37.40     |    26.80     |     37.60     |        30.60        |
|   2-9   | 76.55 |     67.59     |    50.63     |     65.89     |        63.42        |
|  2-10   | 65.26 |     40.04     |    21.27     |     40.54     |        20.69        |
|   3-1   | 53.20 |     30.81     |    52.86     |     16.87     |        38.88        |
|   3-2   | 33.15 |     34.49     |    34.49     |     32.44     |        28.70        |
|   3-3   | 41.30 |     34.55     |    39.91     |     23.07     |        42.25        |
|   3-4   | 83.21 |     77.12     |    78.47     |     75.80     |        67.74        |
|   3-5   | 82.74 |     73.72     |    73.92     |     63.59     |        71.10        |
|   3-6   | 49.60 |     31.60     |    26.80     |     33.00     |        36.20        |
|   3-7   | 77.00 |     66.40     |    44.60     |     56.00     |        44.00        |
|   3-8   | 19.90 |     17.17     |    20.39     |     16.24     |        12.11        |


## 🛠️ How to Evaluate Model
We design different rule-based parsing to extract answers from model predictions. The evaluation scripts for every task is in [evaluation/evaluation_functions](https://github.com/open-compass/LawBench/tree/main/evaluation/evaluation_functions).
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


The output result will be saved in <metric_result>.

For example, the zero-shot predictions from the 51 tested models are saved in [predictions/zero_shot](https://github.com/open-compass/LawBench/tree/main/predictions/zero_shot).
You can run
   ```
   cd evaluation
   python main.py -i ../predictions/zero_shot -o ../predictions/zero_shot/results.csv
   ```
to get their evaluation results stored as [../predictions/zero_shot/results.csv](https://github.com/open-compass/LawBench/tree/main/predictions/zero_shot/results.csv).

### Result Format
The result file is a csv file with four columns: task, model_name, score and abstention_rate:

| Column   |   Description |
|---------|-------       |
| task       |  Task name. Set as the name of the prediction file |
| model_name       |  Model name. Set as the name of the folder storing the prediction files |
| score       |  Model score for the corresponding task.  |
| abstention_rate       |  Abstention rate for the corresponding task. This rate indicates how often the answer cannot be extracted from the model prediction. |
### Requirement

```
rouge_chinese==1.0.3
cn2an==0.5.22
ltp==4.2.13
OpenCC==1.1.6
python-Levenshtein==0.21.1
pypinyin==0.49.0
tqdm==4.64.1
timeout_decorator==0.5.0
```

## 📌 Licenses
LawBench is a mix of created and transformed datasets. We ask that you follow the license of the dataset creator. Please see the [task list](https://github.com/open-compass/LawBench/blob/main/README_EN.md#task-list) for the original source of each task.

## 🔜 Future Plan
- ROUGE-L is not a good metric to evaluate long-form generation results. We will explore using large language model-based evaluation metrics dedicated to law tasks.
- We will keep updating the task list included in LawBench. We welcome external contributors to collaborate with.

## 🖊️ Citation

```bibtex
@article{fei2023lawbench,
  title={LawBench: Benchmarking Legal Knowledge of Large Language Models},
  author={Fei, Zhiwei and Shen, Xiaoyu and Zhu, Dawei and Zhou, Fengzhe and Han, Zhuo and Zhang, Songyang and Chen, Kai and Shen, Zongwen and Ge, Jidong},
  journal={arXiv preprint arXiv:2309.16289},
  year={2023}
}
```

**If you have law datasets that you would like to include or evaluate your own models. Feel free to contact us**.
