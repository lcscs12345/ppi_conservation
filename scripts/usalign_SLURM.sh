#!/bin/bash

#SBATCH --job-name=usalign
#SBATCH --time=08:00:00

#log files:
#SBATCH -e /home/limch05p/lim_group/ppi_conservation/logs/usalign_%A_err.txt
#SBATCH -o /home/limch05p/lim_group/ppi_conservation/logs/usalign_%A_out.txt

#Adjust this depending on the node
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=8000

source /home/limch05p/anaconda3/etc/profile.d/conda.sh
conda activate utils

WORK_DIR=/home/limch05p/lim_group/ppi_conservation/data
SCRIPTS_DIR=/home/limch05p/lim_group/ppi_conservation/src
FILE_PATH=$( ls -1 $WORK_DIR/*.pdb )
TASK=$( echo "$FILE_PATH" | awk "NR==$SLURM_ARRAY_TASK_ID" )

python ${SCRIPTS_DIR}/usalign_multimodels.py -i $TASK -s 250 -r $WORK_DIR/6ahy.pdb -c A,B
