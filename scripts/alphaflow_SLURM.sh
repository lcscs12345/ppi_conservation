#!/bin/bash

#SBATCH --job-name=alphaflow
#SBATCH --time=24:00:00

#log files:
#SBATCH -e /home/limch05p/lim_group/ppi_conservation/logs/alphaflow_%A_%a_err.txt
#SBATCH -o /home/limch05p/lim_group/ppi_conservation/logs/alphaflow_%A_%a_out.txt

#SBATCH -p aoraki_gpu_A100
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4000


WORK_DIR=/home/limch05p/lim_group/ppi_conservation/data
SRC_DIR=/home/limch05p/lim_group/ppi_conservation/src
GPUs=`apptainer exec --nv ${SRC_DIR}/alphaflow.sif python -c "import torch; print(torch.cuda.device_count())"`

if [ $GPUs != 0 ]
  then
    echo "${GPUs} GPUs found..."
    
    mkdir -p ${WORK_DIR}/tmp/
    awk "NR==($SLURM_ARRAY_TASK_ID)+1" ${WORK_DIR}/selected.csv \
    | sed '1i name,seqres' > ${WORK_DIR}/tmp/${SLURM_ARRAY_TASK_ID}.csv

    apptainer exec \
    --nv ${SRC_DIR}/alphaflow_20240515.sif \
    python ${SRC_DIR}/alphaflow/predict.py \
    --mode esmfold \
    --input_csv ${WORK_DIR}/tmp/${SLURM_ARRAY_TASK_ID}.csv \
    --weights ${SRC_DIR}/alphaflow/weights/esmflow_md_base_202402.pt \
    --outpdb ${WORK_DIR} \
    --samples 250
  else
    echo " No GPUs found!"
fi

