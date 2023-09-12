import json
import os
import pandas as pd
from evaluation_functions import jec_ac, jec_kd, cjft, ydlj, ftcs, jdzy, jetq, ljp_accusation, ljp_article, ljp_imprison, wbfl, xxcq, flzx, wsjd, yqzy, lblj, zxfl
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
    funct_dict = {"3-6": jec_ac.compute_jec_ac,
                  "1-2": jec_kd.compute_jec_kd,
                  "3-2": cjft.compute_cjft,
                  "3-8": flzx.compute_flzx,
                  "1-1": ftcs.compute_ftcs,
                  "2-2": jdzy.compute_jdzy,
                  "3-7": jetq.compute_jetq,
                  "3-3": ljp_accusation.compute_ljp_accusation,
                  "3-1": ljp_article.compute_ljp_article,
                  "3-4": ljp_imprison.compute_ljp_imprison,
                  "3-5": ljp_imprison.compute_ljp_imprison,
                  "2-3": wbfl.compute_wbfl,
                  "2-6": xxcq.compute_xxcq,
                  "2-1": wsjd.compute_wsjd,
                  "2-4": zxfl.compute_zxfl,
                  "2-7": yqzy.compute_yqzy,
                  "2-8": lblj.compute_lblj,
                  "2-5": ydlj.compute_ydlj}
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
