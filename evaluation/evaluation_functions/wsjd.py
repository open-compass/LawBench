from utils.function_utils import compute_gleu

"""
Task: legal document grammar correction
Metric: GLEU score
"""
def compute_wsjd(data_dict):
    references, predictions = [], []
    for example in data_dict:
        question, prediction, answer = example["origin_prompt"], example["prediction"], example["refr"]
        predictions.append(prediction)
        references.append(answer)

    gleu_score = compute_gleu(predictions, references)
    return gleu_score
