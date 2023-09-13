# LawBench

Large language models (LLMs) have demonstrated strong capabilities in various aspects. However, when applying them to the highly-specialized, safe-critical legal domain, it is unclear how much legal knowledge they possess and whether they can reliably perform law-related tasks. To address this gap, we propose a comprehensive evaluation benchmark **LawBench**. 

**Tasks in LawBench are based on the law system of China. A similar bench based on the American law system is available [here](https://github.com/HazyResearch/legalbench).**

## Introduction
LawBench has been meticulously crafted to have precise assessment of the LLMs’ legal capabilities.
In designing the testing tasks, we simulated three dimensions of judicial cognition and selected 18 tasks to evaluate the abilities of large models. Compared to some existing benchmarks with only multiple-choice questions, we include more diverse types of tasks closely related to real-world applications, such as legal entity recognition, reading comprehension, crime amount calculation and consultation.
We recognize that the security policies of current large models may decline to respond to certain legal queries or experience difficulty in comprehending instructions, leading to a lack of response. Therefore, we have developed
a separate evaluation metric "abstention rate" to measure how often the model refuses to provide the answer, or fail to understand the instructions properly.
We report the performances of 46 large language models on LawBench, including a wide range of multilingual/Chinese-specific, general/legal-specific, open/closed sourced large language models.

## Dataset
Our dataset include 18 diverse tasks covering 3 cognitive levels: 
- **Legal knowledge memorization**: whether large language models can memorize necessary legal knowledge in their parameters.
- **Legal knowledge understanding**: whether large language models can comprehend entities, events, and relationships within legal texts, so as to understand the content of legal text.
- **Legal knowledge application**: whether large language models can properly utilize their legal knowledge to solve realistic legal tasks in downstream applications.

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
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-lboi" rowspan="2"><b>Legal Knowledge Memorization</b></td>
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
    <td class="tg-0pky">[LawGPT_zh Project](https://github.com/LiuHC0428/LAW-GPT)</td>
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

## Model List
We test 46 popular large language models. We group them as in the following table:
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Model</th>
    <th class="tg-0pky">Developers</th>
    <th class="tg-0pky">Parameters</th>
    <th class="tg-0lax">Base Model</th>
    <th class="tg-0pky">SFT</th>
    <th class="tg-0pky">RLHF</th>
    <th class="tg-0lax">max len</th>
    <th class="tg-0lax">Access</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-9wq8" colspan="8"><b>Pretrained with English as Majority Language</b></td>
  </tr>
  <tr>
    <td class="tg-za14">MPT-7B</td>
    <td class="tg-za14">MosaicML</td>
    <td class="tg-za14">7B</td>
    <td class="tg-0lax">MPT-7B</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-za14">MPT-Instruct-7B</td>
    <td class="tg-za14">MosaicML</td>
    <td class="tg-za14">7B</td>
    <td class="tg-0lax">MPT-7B</td>
    <td class="tg-0pky">EN</td>
    <td class="tg-0pky"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-za14">LLaMA</td>
    <td class="tg-za14">Meta</td>
    <td class="tg-za14">7/13/30/65B</td>
    <td class="tg-0lax">LLaMA</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-0pky">Alpaca-7B</td>
    <td class="tg-0pky">Stanford University</td>
    <td class="tg-0pky">7B</td>
    <td class="tg-0lax">LLaMA</td>
    <td class="tg-0pky">EN</td>
    <td class="tg-0pky"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-za14">Vicuna-v1.3</td>
    <td class="tg-za14">UC Berkeley</td>
    <td class="tg-za14">7/13/33B</td>
    <td class="tg-0lax">LLaMA</td>
    <td class="tg-0pky">EN</td>
    <td class="tg-0pky"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-za14">WizardLM-7B</td>
    <td class="tg-za14">Microsoft</td>
    <td class="tg-za14">7B</td>
    <td class="tg-0lax">LLaMA</td>
    <td class="tg-0pky">EN</td>
    <td class="tg-0pky"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-za14">Ziya-LLaMA-13B</td>
    <td class="tg-za14">IDEA-CCNL</td>
    <td class="tg-za14">13B</td>
    <td class="tg-0lax">LLaMA</td>
    <td class="tg-0pky">EN</td>
    <td class="tg-0pky">√</td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-za14">Lawyer-llama</td>
    <td class="tg-za14">Peking University</td>
    <td class="tg-azeh">13B</td>
    <td class="tg-0lax">LLaMA</td>
    <td class="tg-0pky">CN; Law</td>
    <td class="tg-0pky"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-7zrl">ChatLaw-13B</td>
    <td class="tg-7zrl">Peking University</td>
    <td class="tg-7zrl">13B</td>
    <td class="tg-7zrl">Ziya-LLaMA-13B </td>
    <td class="tg-0lax">CN; Law</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-0lax">ChatLaw-33B</td>
    <td class="tg-0lax">Peking University</td>
    <td class="tg-0lax">33B</td>
    <td class="tg-0lax">Anima-33B</td>
    <td class="tg-0lax">CN; Law</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-za14">LLaMA-2</td>
    <td class="tg-za14">Meta</td>
    <td class="tg-za14">7/13/70B</td>
    <td class="tg-0lax">LLaMA2</td>
    <td class="tg-0pky">EN</td>
    <td class="tg-0pky"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-qnro">LLaMA-2-Chat</td>
    <td class="tg-za14">Meta</td>
    <td class="tg-za14">7/13/70B</td>
    <td class="tg-0lax">LLaMA2</td>
    <td class="tg-0pky">EN</td>
    <td class="tg-0pky">√</td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-za14">LLaMA-2-Chinese</td>
    <td class="tg-za14">FlagAlpha</td>
    <td class="tg-za14">7/13B</td>
    <td class="tg-0lax">LLaMA2</td>
    <td class="tg-0pky">CN</td>
    <td class="tg-0pky"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-7zrl">Yulan-Chat-2-13B</td>
    <td class="tg-7zrl">GSAI, Renmin University</td>
    <td class="tg-7zrl">13B</td>
    <td class="tg-7zrl">LLaMA2</td>
    <td class="tg-0lax">CN</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-7zrl">Chinese-LLaMA-2-7B</td>
    <td class="tg-7zrl">iFLYTEK</td>
    <td class="tg-7zrl">7B</td>
    <td class="tg-0lax">LLaMA2</td>
    <td class="tg-0lax">CN</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-za14">BELLE-LLaMA-2</td>
    <td class="tg-za14">LianjiaTech</td>
    <td class="tg-za14">13B</td>
    <td class="tg-0lax">LLaMA2</td>
    <td class="tg-0pky">CN</td>
    <td class="tg-0pky"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-za14">Chinese-Alpaca-2-7B</td>
    <td class="tg-za14">iFLYTEK</td>
    <td class="tg-za14">7B</td>
    <td class="tg-0lax">LLaMA2</td>
    <td class="tg-0pky">CN</td>
    <td class="tg-0pky"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-za14">LLaMA-2-13B-Chinese-Chat</td>
    <td class="tg-za14">shareAI</td>
    <td class="tg-za14">13B</td>
    <td class="tg-0lax">LLaMA2</td>
    <td class="tg-0pky">CN</td>
    <td class="tg-0pky"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-7zrl">GoGPT</td>
    <td class="tg-7zrl">Chinese Academy of Sciences</td>
    <td class="tg-7zrl">7B</td>
    <td class="tg-0lax">LLaMA2</td>
    <td class="tg-0lax">CN</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-0lax">TigerBot-Base</td>
    <td class="tg-0lax">TigerResearch</td>
    <td class="tg-0lax">7B</td>
    <td class="tg-0lax">BLOOM</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-0lax">TigerBot-SFT</td>
    <td class="tg-0lax">TigerResearch</td>
    <td class="tg-hx86">7B</td>
    <td class="tg-0lax">TigerBot-Base</td>
    <td class="tg-0lax">EN</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-za14">ChatGPT</td>
    <td class="tg-za14">OpenAI</td>
    <td class="tg-za14">N/A</td>
    <td class="tg-0lax"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">√</td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">API</td>
  </tr>
  <tr>
    <td class="tg-za14">GPT-4</td>
    <td class="tg-za14">OpenAI</td>
    <td class="tg-za14">N/A</td>
    <td class="tg-0lax"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">√</td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">API</td>
  </tr>
  <tr>
    <td class="tg-baqh" colspan="8"><span style="font-weight:400;font-style:normal"><b>Pretrained with Chinese as Majority Language</b></span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">XVERSE-13B</td>
    <td class="tg-7zrl">Shenzhen Yuanxiang Technology</td>
    <td class="tg-7zrl">13B</td>
    <td class="tg-7zrl">XVERSE-13B</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-7zrl">InternLM-7B</td>
    <td class="tg-7zrl">Shanghai AI Lab &amp; SenseTime</td>
    <td class="tg-7zrl">7B</td>
    <td class="tg-7zrl">InternLM-7B</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-7zrl">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-7zrl">InternLM-Chat-7B</td>
    <td class="tg-7zrl">Shanghai AI Lab &amp; SenseTime</td>
    <td class="tg-7zrl">7B</td>
    <td class="tg-7zrl">InternLM-7B</td>
    <td class="tg-0lax">CN</td>
    <td class="tg-0lax"></td>
    <td class="tg-7zrl">4/8K</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-7zrl">Baichuan-13B-Chat</td>
    <td class="tg-7zrl">Baichuan Intelligent Technology</td>
    <td class="tg-7zrl">13B</td>
    <td class="tg-7zrl">Baichuan-13B</td>
    <td class="tg-0lax">CN</td>
    <td class="tg-0lax"></td>
    <td class="tg-7zrl">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-7zrl">Baichuan</td>
    <td class="tg-7zrl">Baichuan Intelligent Technology</td>
    <td class="tg-7zrl">7/13B</td>
    <td class="tg-7zrl">Baichuan</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-7zrl">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-7zrl">ChatGLM2-6B</td>
    <td class="tg-7zrl">Tsinghua University</td>
    <td class="tg-7zrl">6B</td>
    <td class="tg-7zrl">ChatGLM</td>
    <td class="tg-0lax">CN</td>
    <td class="tg-0lax">√</td>
    <td class="tg-7zrl">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-7zrl">Qwen-7B</td>
    <td class="tg-7zrl">Alibaba</td>
    <td class="tg-7zrl">7B</td>
    <td class="tg-7zrl">Qwen-7B</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-7zrl">Qwen-7B-Chat</td>
    <td class="tg-7zrl">Alibaba</td>
    <td class="tg-7zrl">7B</td>
    <td class="tg-7zrl">Qwen-7B</td>
    <td class="tg-0lax">CN</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-7zrl">MOSS-Moon</td>
    <td class="tg-7zrl">Fudan university</td>
    <td class="tg-7zrl">16B</td>
    <td class="tg-7zrl">MOSS-Moon</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
  <tr>
    <td class="tg-7zrl">MOSS-Moon-SFT</td>
    <td class="tg-7zrl">Fudan university</td>
    <td class="tg-7zrl">16B</td>
    <td class="tg-7zrl">MOSS-Moon</td>
    <td class="tg-0lax">CN</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">2k</td>
    <td class="tg-0lax">Weights</td>
  </tr>
</tbody>
</table>

## Model Performance
We test the  model performance under 2 scenarios: (1) zero-shot, where only instructions are provided in the prompt, and (2) one-shot, where instructions and one-shot examples are concatenated in the prompt.

### Zero-shot Performance
We show the performances of top-5 models with the highest average scores.

**Note: gpt-3.5-turbo is version 2023.6.13, and all gpt-3.5-turbo results below are for this version**

| Task ID   |   GPT4 |   GPT-3.5-turbo-0613 |   freewilly2_70b-hf |   qwen-7b-chat-hf |   internlm-chat-7b-8k-hf |
|:----------|-------:|---------------------:|--------------------:|------------------:|-------------------------:|
| AVG       |  50.17 |                40.97 |               37.65 |             37.57 |                    35.04 |
| 1-1       |  15.38 |                15.86 |               14.58 |             18.54 |                    15.45 |
| 1-2       |  55.2  |                36    |               34.6  |             34    |                    40.4  |
| 2-1       |  12.53 |                 9.1  |                7.7  |             22.56 |                    22.64 |
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
| Task ID   |   GPT4 |   GPT-3.5-turbo-0613 |   qwen-7b-chat-hf |   freewilly2_70b-hf |   internlm-chat-7b-8k-hf |
|:----------|-------:|---------------------:|------------------:|--------------------:|-------------------------:|
| AVG       |  51.95 |                43.49 |             39.33 |               37.39 |                    36.75 |
| 1-1       |  17.21 |                16.15 |             17.73 |               15.03 |                    15.16 |
| 1-2       |  54.8  |                37.2  |             28.6  |               36    |                    40.6  |
| 2-1       |  18.31 |                13.5  |             25.16 |                8.93 |                    21.64 |
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

For example, the zero-shot predictions from the 46 tested models are saved in [predictions/zero_shot](https://github.com/open-compass/LawBench/tree/main/predictions/zero_shot).
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

## Future Plan
- The corresponding paper will be released soon.
- ROUGE-L is not a good metric to evaluate long-form generation results. We will explore using large language model-based evaluation metrics dedicated to law tasks.
- We will keep updating the task list included in LawBench. We welcome external contributors to collaborate with. 

**If you have law datasets that you would like to include or evaluate your own models. Feel free to contact us**.
