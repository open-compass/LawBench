# Code to evaluate the model predictions

# How to Run
1. Put all your prediction results under a folder F
2. Name your prediction for each task according to the schema [here](https://github.com/open-compass/LawBench/new/main/evaluation/main.py#L29)
3. Run "python main.py -i F -o <metric_result>"

The result is a csv file with four columns: task, model_name, score and abstention_rate. 
It will be saved in <metric_result>.

For example, you can run "python main.py -i ../predictions/zero_shot -o ../predictions/zero_shot/results.csv" to get the evaluation results for all zero_shot inferences.
