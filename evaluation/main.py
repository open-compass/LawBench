import json
import os
import pandas as pd
from evaluation_functions import jec_ac, jec_kd, cjft, ydlj, ftcs, jdzy, jetq, ljp_accusation, ljp_article, ljp_imprison, wbfl, xxcq, flzx, wsjd, yqzy, lblj
import sys
import argparse

def read_json(input_file):
    # load the json file
    with open(input_file, "r", encoding="utf-8") as f:
        data_dict = json.load(f)

    dict_size = len(data_dict)
    new_data_dict = []
    for i in range(dict_size):
        example = data_dict[str(i)]
        new_data_dict.append(example)

    return new_data_dict


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_folder", dest="input_folder",
                  help="input folder: it should be a folder containing the prediction results", metavar="FILE")
    parser.add_argument("-o", "--outfile", dest="outfile",
                  help="output file saving the evaluation results", metavar="FILE")
    args = parser.parse_args(argv)
    funct_dict = {"lawbench_JEC-AC": jec_ac.compute_jec_ac,
                  "lawbench_JEC-KD": jec_kd.compute_jec_kd,
                  "lawbench_CJFT": cjft.compute_cjft,
                  "lawbench_FLZX": flzx.compute_flzx,
                  "lawbench_FTCS": ftcs.compute_ftcs,
                  "lawbench_JDZY": jdzy.compute_jdzy,
                  "lawbench_JETQ": jetq.compute_jetq,
                  "lawbench_LJP-Accusation": ljp_accusation.compute_ljp_accusation,
                  "lawbench_LJP-Article": ljp_article.compute_ljp_article,
                  "lawbench_LJP-Imprison": ljp_imprison.compute_ljp_imprison,
                  "lawbench_LJP-Imprison-fatiao": ljp_imprison.compute_ljp_imprison,
                  "lawbench_WBFL": wbfl.compute_wbfl,
                  "lawbench_XXCQ": xxcq.compute_xxcq,
                  "lawbench_WSJD": wsjd.compute_wsjd,
                  "lawbench_YQZY": yqzy.compute_yqzy,
                  "lawbench_LBLJ": lblj.compute_lblj,
                  "lawbench_YDLJ": ydlj.compute_ydlj}


    input_dir = args.input_folder

    output_file = args.outfile
    results = {"task": [], "model_name": [], "score": [], "abstention_rate": []}
    # list all folders in input_dir
    system_folders = os.listdir(input_dir)
    for system_folder in system_folders:
        if system_folder.startswith("."):
            continue
        system_folder_dir = os.path.join(input_dir, system_folder)
        if not os.path.isdir(system_folder_dir):
            continue
        # list all files in system_folder_path
        dataset_files = os.listdir(system_folder_dir)
        print(f"*** Evaluating System: {system_folder} ***")
        for dataset_file in dataset_files:
            datafile_name = dataset_file.split(".")[0]
            input_file = os.path.join(system_folder_dir, dataset_file)
            data_dict = read_json(input_file)
            if datafile_name not in funct_dict:
                print(f"*** Warning: {datafile_name} is not in funct_dict ***")
                continue
            print(f"Processing {datafile_name}:")
            score_function = funct_dict[datafile_name]
            score = score_function(data_dict)
            print(f"Score of {datafile_name}: {score}")
            results["task"].append(datafile_name)
            results["model_name"].append(system_folder)
            results["score"].append(score["score"])
            abstention_rate = score["abstention_rate"] if "abstention_rate" in score else 0
            results["abstention_rate"].append(abstention_rate)

        print(f"*** Evaluating System: {system_folder} Done! ***")
        print()
        print()

    results = pd.DataFrame(results)
    results.to_csv(output_file, index = False)

if __name__ == '__main__':
    main(sys.argv[1:])
