# LawBench
大语言模型（LLMs）在各个方面都展现出了其强大的能力。然而，当将它们应用于高度专业化、安全关键的法律领域时，它们究竟掌握了多少法律知识以及它们是否能可靠地执行法律相关任务我们却不得而知。为了填补这一空白，我们提出了一个综合评估基准**LawBench**。
**LawBench中的任务基于中国的法律体系。基于美国法律体系的类似基准可参见[链接](https://github.com/HazyResearch/legalbench)。**

## 介绍
LawBench经过精心设计，可对大语言模型的法律能力进行精确评估。
在设计测试任务时，我们模拟了司法认知的三个维度，并选择了 18 个任务来评估大模型的能力。与一些仅有多项选择题的现有基准相比，我们包含了更多与现实世界应用密切相关的任务类型，如法律实体识别、阅读理解、犯罪金额计算和咨询等。
我们认识到当前大模型的安全性策略可能会拒绝回应某些法律询问，或在理解指令方面遇到困难，从而导致缺乏回应。因此，我们开发了一个单独的评估指标 "弃权率"，以衡量模型拒绝提供答案或未能正确理解指令的频率。
我们汇报了 46 种大语言模型在 LawBench 上的表现，包括多种多语言/中文特有、通用/法律特有、开源/闭源的大语言模型。

## 数据集
我们的数据集包括 18 个不同的任务，涵盖 3 个认知水平： 
- **法律知识记忆**：大语言模型能否记忆其参数中必要的法律知识。
- **法律知识理解**：大语言模型能否理解法律文本中的实体、事件和关系，从而理解法律文本的内容。
- **法律知识应用**：大语言模型能否正确利用其法律知识解决下游应用中的现实法律任务。

任务列表

以下是包含的任务列表。每项任务都有 500 个示例。

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">认知水平</th>
    <th class="tg-0pky">ID</th>
    <th class="tg-0pky">任务</th>
    <th class="tg-0pky">数据源</th>
    <th class="tg-0pky">指标</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-lboi" rowspan="2"><b>法律知识记忆</b></td>
    <td class="tg-qdov">1-1</td>
    <td class="tg-qdov">法条背诵</td>
    <td class="tg-qdov">FLK</td>
    <td class="tg-qdov">ROUGE-L</td>
  </tr>
  <tr>
    <td class="tg-0pky">1-2</td>
    <td class="tg-qdov">知识问答</td>
    <td class="tg-0pky">JEC_QA</td>
    <td class="tg-0pky">Accuracy</td>
  </tr>
  <tr>
    <td class="tg-lboi" rowspan="8"><b>法律知识理解</b></td>
    <td class="tg-0pky">2-1</td>
    <td class="tg-0pky">文件校对</td>
    <td class="tg-0pky">CAIL</td>
    <td class="tg-0pky">F0.5</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-2</td>
    <td class="tg-0pky">纠纷焦点识别</td>
    <td class="tg-0pky">LAIC</td>
    <td class="tg-0pky">F1</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-3</td>
    <td class="tg-0pky">婚姻纠纷鉴定</td>
    <td class="tg-0pky">AIStudio</td>
    <td class="tg-0pky">F1</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-4</td>
    <td class="tg-0pky">问题主题识别</td>
    <td class="tg-0pky"><a href="https://github.com/liuhuanyong/CrimeKgAssitant">CrimeKgAssitant</a></td>
    <td class="tg-0pky">Accuracy</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-5</td>
    <td class="tg-0pky">阅读理解</td>
    <td class="tg-0pky">CAIL</td>
    <td class="tg-0pky">F1</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-6</td>
    <td class="tg-0pky">名称实体识别</td>
    <td class="tg-0pky">CAIL</td>
    <td class="tg-0pky">F1</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-7</td>
    <td class="tg-0pky">意见总结</td>
    <td class="tg-0pky">CAIL</td>
    <td class="tg-0pky">ROUGE-L</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-8</td>
    <td class="tg-qdov">论点挖掘</td>
    <td class="tg-0pky">CAIL</td>
    <td class="tg-0pky">Accuracy</td>
  </tr>
  <tr>
    <td class="tg-lboi" rowspan="8"><b>法律知识应用</b></td>
    <td class="tg-0pky">3-1</td>
    <td class="tg-0pky">基于事实的法条预测</td>
    <td class="tg-0pky">CAIL-2018</td>
    <td class="tg-0pky">F1</td>
  </tr>
  <tr>
    <td class="tg-0pky">3-2</td>
    <td class="tg-0pky">基于场景的法条预测</td>
    <td class="tg-0pky"><a href="https://github.com/LiuHC0428/LAW-GPT">LawGPT_zh Project</a></td>
    <td class="tg-0pky">ROUGE-L</td>
  </tr>
  <tr>
    <td class="tg-0pky">3-3</td>
    <td class="tg-0pky">指控预测</td>
    <td class="tg-0pky">CAIL-2018</td>
    <td class="tg-0pky">F1</td>
  </tr>
  <tr>
    <td class="tg-0pky">3-4</td>
    <td class="tg-0pky">不基于法条的刑期预测</td>
    <td class="tg-0pky">CAIL-2018</td>
    <td class="tg-0pky">Normalized log-distance</td>
  </tr>
  <tr>
    <td class="tg-0pky">3-5</td>
    <td class="tg-0pky">基于法条的刑期预测</td>
    <td class="tg-0pky">CAIL-2018</td>
    <td class="tg-0pky">Normalized log-distance</td>
  </tr>
  <tr>
    <td class="tg-0lax">3-6</td>
    <td class="tg-0lax">案例分析</td>
    <td class="tg-0lax">JEC_QA</td>
    <td class="tg-0lax">Accuracy</td>
  </tr>
  <tr>
    <td class="tg-0lax">3-7</td>
    <td class="tg-0lax">犯罪金额计算</td>
    <td class="tg-0lax">LAIC</td>
    <td class="tg-0lax">Accuracy</td>
  </tr>
  <tr>
    <td class="tg-0lax">3-8</td>
    <td class="tg-0lax">咨询</td>
    <td class="tg-0lax"><a href="https://www.66law.cn/">hualv.com</a></td>
    <td class="tg-0lax">ROUGE-L</td>
  </tr>
</tbody>
</table>

### 数据格式
数据存储在 [data](https://github.com/open-compass/LawBench/tree/main/data)  文件夹下。每个任务都存储在 <task_id>.json 文件中。
可以通过 json.load 将 json 文件作为字典列表加载。
数据格式如下（以任务 3-2 为例）：

```json
[
  {
    "instruction": "请根据具体场景与问题给出法律依据，只需要给出具体法条内容，每个场景仅涉及一个法条。",
    "question": "场景:某个地区的三个以上专业农民合作社想要出资设立农民专业合作社联合社，以提高其在市场中的竞争力和规模效应。根据哪条法律，三个以上的农民专业合作社可以出资设立农民专业合作社联合社？",
    "answer": "根据《农民专业合作社法》第五十六条，三个以上的农民专业合作社在自愿的基础上，可以出资设立农民专业合作社联合社。该联合社应当有自己的名称、组织机构和住所，由联合社全体成员制定并承认的章程，以及符合章程规定的成员出资。"
  },
]
```

### 模型输出格式
模型输出存储在 [predictions/zero_shot](https://github.com/open-compass/LawBench/tree/main/predictions/zero_shot) 和 [predictions/one_shot](https://github.com/open-compass/LawBench/tree/main/predictions/one_shot)  文件夹下。每个系统都有自己的子文件夹。在每个子文件夹中，任务预测都存储在 <task_id>.json 文件中。
可以通过 json.load 将 json 文件作为字典加载。
数据格式如下（以 GPT-4 零样本预测中的任务 3-2 为例）：

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

## 模型列表
我们测试了 46 种热门的大语言模型。我们对它们进行了分组，如下表所示：
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">模型</th>
    <th class="tg-0pky">开发者</th>
    <th class="tg-0pky">参数</th>
    <th class="tg-0lax">基模型</th>
    <th class="tg-0pky">SFT</th>
    <th class="tg-0pky">RLHF</th>
    <th class="tg-0lax">最大长度</th>
    <th class="tg-0lax">权限</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-9wq8" colspan="8"><b>以英语为主语言预训练</b></td>
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
    <td class="tg-0lax">512</td>
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
    <td class="tg-baqh" colspan="8"><span style="font-weight:400;font-style:normal"><b>以中文为主语言预训练</b></span></td>
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


## 模型性能
我们测试了模型在两种情况下的性能： (1)zero-shot，即在提示中只提供指令；(2)one-shot，即在提示中将指令和one-shot示例连接起来。

### Zero-shot 性能
我们展示了平均得分最高的前 5 个模型的性能。

**注：gpt-3.5-turbo 为 2023.6.13 版本，以下所有 gpt-3.5-turbo 结果均为该版本的结果**

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

### One-Shot 性能
我们展示了平均得分最高的前 5 个模型的性能。
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


## 如何评估模型
我们设计了不同的基于规则的解析来从模型预测中提取答案。每个任务的评估脚本都在 [evaluation/evaluation_functions](https://github.com/open-compass/LawBench/tree/main/evaluation/evaluation_functions)。
### 步骤
评估模型预测的步骤如下：
1. 将所有系统的预测结果放在 F 文件夹中，每个系统有一个子文件夹。
2. 在每个系统的子文件夹下，每个任务都有一个预测文件。每个任务的名称就是任务 ID。
3. 进入评估文件夹并运行 "python main.py -i F -o <metric_result>" 

数据格式如下：
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


输出结果将保存在 <metric_result> 中。

例如，46 个测试模型的zero-shot预测结果保存在 [predictions/zero_shot](https://github.com/open-compass/LawBench/tree/main/predictions/zero_shot)

您可以运行
   ```
   cd evaluation
   python main.py -i ../predictions/zero_shot -o ../predictions/zero_shot/results.csv
   ```
来获取它们的评估结果，存储为 [../predictions/zero_shot/results.csv](https://github.com/open-compass/LawBench/tree/main/predictions/zero_shot/results.csv)

### 结果格式

结果文件是一个 csv 文件，共有四列：任务、模型名称、得分和舍弃率：

| 列   |   描述 |
|---------|-------       |
| task       |  任务名称。设置为预测文件的名称 |
| model_name       |  模型名称。设置为存储预测文件的文件夹名称 |
| score       |  相应任务的模型得分  |
| abstention_rate       |  相应任务的舍弃率。该比率表示无法从模型预测中提取答案的频率 |
### 要求

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

## 未来计划
- 相关论文即将发布。
- ROUGE-L 并不是评估长表生成结果的好指标。我们将探索使用基于大语言模型的法律任务专用评价指标。
- 我们将不断更新 LawBench 中的任务列表。欢迎外部贡献者与我们合作。

**如果您希望进一步完善这个法律数据集或评估自己的模型，请随时联系我们。**