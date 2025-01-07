#!/bin/sh
for i in `cat nonore.list.txt`; do minimap2 -ax map-ont /ifs1/Database/human/GCF_000001405.39_GRCh38.p13_genomic.fna /ifs1/User/maiguoqin/pathogen/国家病原库基因组/bacteria_virus_funge_para_arm/test2/1_zhikong/$i -Y -N 20 -t 12 >/ifs1/User/maiguoqin/pathogen/国家病原库基因组/bacteria_virus_funge_para_arm/test2/2_qusuzhu/$i.sam;done
