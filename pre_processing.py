import cPickle
import sys
import json
import pandas as pd
import numpy as np

def load_json(file):
    with open(file) as json_file:
        data = json.load(json_file)
        return data

def getDatasetDict():

    json_data= load_json("/home/kesci/work/Broad/meta.json")
    database=json_data['database']
    train_dict={}
    val_dict={}
    test_dict={}
    for video_name in database.keys():
        video_info=database[video_name]
        video_new_info={}
        video_subset=video_info["subset"]
        video_new_info['annotations']=video_info['annotations']
        if video_subset=="training":
            train_dict[video_name]=video_new_info
        elif video_subset=="validation":
            val_dict[video_name]=video_new_info
        elif video_subset=="testing":
            test_dict[video_name]=video_new_info
    return train_dict,val_dict,test_dict
    
    json_data= load_json("/home/kesci/work/Broad/INFO/meta.json")
    database=json_data['database']

    len_image_list=[]
    video_list=[]
    subset_list=[]
    for video in database.keys():
        dataSet=database[video]["subset"]
        try:
            with open("/mnt/BROAD-datasets/video/"+dataSet+"/"+str(video)+".pkl",'rb') as f:
                img_fea=cPickle.load(f)
        except:
            continue
        len_image=len(img_fea)
        len_image_list.append(len_image)
        video_list.append(video)
        subset_list.append(dataSet)
        print np.shape(img_fea)
        
