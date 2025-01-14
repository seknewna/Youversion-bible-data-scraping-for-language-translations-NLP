from training import *
from training_arg import*
import transformers
from transformers import M2M100Tokenizer, M2M100ForConditionalGeneration
from transformers import T5ForConditionalGeneration, AutoTokenizer
import torch
torch.cuda.empty_cache()

args_dict = {
    "output_dir": "m2m100_small_fr_sba",
    "model_name_or_path": "facebook/m2m100_418M",
    "train_file": "/home/jupyter/Projects/Ngambay-French-Neural-Machine-Translation-sba_fr_v1-/Dataset/sba_fr_train_sy.json",
    "validation_file": "/home/jupyter/Projects/Ngambay-French-Neural-Machine-Translation-sba_fr_v1-/Dataset/sba_fr_JSON/sba_fr_val.json",
    "test_file": "/home/jupyter/Projects/Ngambay-French-Neural-Machine-Translation-sba_fr_v1-/Dataset/sba_fr_JSON/sba_fr_test.json",
    "source_lang": "fr",
    "target_lang": "sw",
    

    "max_source_length": "200",
    "max_target_length": "200",
    "num_train_epochs": "60",
    "per_device_train_batch_size": "5",
    "per_device_eval_batch_size": "5",
    "num_beams": "10",
    "save_steps": "10000",
    "seed": "65",
    

    "do_train": "True",
    "do_eval": "True",
    "do_predict":"True",
    "predict_with_generate": "True",
    "overwrite_output_dir": "True",
   

    # optional
    # for mt5
    # "source_prefix": "translate Frecnh to Wolof: ",
    # for m2m100
    "forced_bos_token": "sw",
    # for mBART50
    #"forced_bos_token": "en_XX", # language code has _[country code]

}

model_args, data_args, training_args = get_args(args_dict)

start_training(model_args, data_args, training_args)

#Prediction function

model = M2M100ForConditionalGeneration.from_pretrained("/home/jupyter/Projects/Ngambay-French-Neural-Machine-Translation-sba_fr_v1-/Baseline/m2m100_small_fr_sba")
tokenizer = M2M100Tokenizer.from_pretrained("/home/jupyter/Projects/Ngambay-French-Neural-Machine-Translation-sba_fr_v1-/Baseline/m2m100_small_fr_sba")