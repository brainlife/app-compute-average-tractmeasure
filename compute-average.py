#!/usr/bin/env python3

import os,sys
import pandas as pd
import numpy as np
import json

def compute_average(data):

    out_data = data.groupby(['structureID']).mean().reset_index()
    out_data = out_data.drop(columns={'nodeID'})

    return out_data

def main():
    
    # load config.json
    with open('config.json','r') as config_f:
        config = json.load(config_f)
        
    # set input variables
    tractmeasures = pd.read_csv(config['input'])

    # compute average
    tractmeasures_average = compute_average(tractmeasures)
    
    # make output directory
    if not os.path.exists('output'):
        os.mkdir('output')
        
    # save cut nodes csv
    tractmeasures_average.to_csv('./output/tractmeasures.csv',index=False)
    
if __name__ == '__main__':
    main()
