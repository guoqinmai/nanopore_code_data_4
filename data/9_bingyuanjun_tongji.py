#!/usr/bin/env python
# coding: utf-8

# In[1]:


#####good_保持这个
import pandas as pd
import numpy as np



with open(r"/ifs1/User/maiguoqin/pathogen/国家病原库基因组/bacteria_virus_funge_para_arm/test2_hebing/code/blastn_list.txt") as dff:
    d=dff.readlines()
    for name in d:
        fpath = (r"/ifs1/User/maiguoqin/pathogen/国家病原库基因组/bacteria_virus_funge_para_arm/test2_hebing/8_amr_blastn/%s.fastq.gz.txt"%(name.split(".")[0]))
        
         #####读入文件
        f = pd.read_table(fpath,header=None)

        f[12]=np.rint(f[2]*f[3]*0.01)  # ∑Xi*Yi

        df = pd.DataFrame([f.groupby(1)[0].nunique(), 
                           f.groupby(1)[12].sum() / f.groupby(1)[0].count(), 
                           f.groupby(1)[12].sum(), 
                           f.groupby(1)[0].nunique() / f[0].nunique(),
                           (f.groupby(1)[0].nunique())* (f.groupby(1)[12].sum() / f.groupby(1)[0].count())*(f.groupby(1)[12].sum())*(f.groupby(1)[0].nunique() / f[0].nunique()),
                          (f.groupby(1)[0].nunique())* (f.groupby(1)[12].sum() / f.groupby(1)[0].count())*(f.groupby(1)[12].sum())*(f.groupby(1)[0].nunique() / f[0].nunique()) / ((f.groupby(1)[0].nunique())* (f.groupby(1)[12].sum() / f.groupby(1)[0].count())*(f.groupby(1)[12].sum())*(f.groupby(1)[0].nunique() / f[0].nunique())).sum()]).T

        df.columns = ['number_of_matches', 'average', 'sum', 'reads_ratio','all_sum','all_ratio']
        df.sort_values('all_ratio', ascending=False, inplace=True) # 按all_ratio从高到低排序
        
        #df.to_excel('P9.3.out.xlsx') 
        ####保存到文件夹
       
        
        df.to_csv(r"/ifs1/User/maiguoqin/pathogen/国家病原库基因组/bacteria_virus_funge_para_arm/test2_hebing/9_amr_tongji/%s.csv"%(name.split(".")[0]))


