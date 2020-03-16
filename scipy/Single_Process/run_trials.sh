#!/bin/bash
#SBATCH -N 1
#SBATCH --job-name=kmeans_single
#SBATCH -o kmeans_single.%j.stdout
#SBATCH -e kmeans_single.%j.error
#SBATCH -x crill-001
#SBATCH --exclusive
#SBATCH -t 2:00:00
#SBATCH -p crill

module load mpi4py/3.0.0-python3.4

#See if results directory exists, if not create it
if [ ! -d "$(pwd)/Results" ];then
  mkdir $(pwd)/Results
fi

DATE=$(date +%Y%m%d_%H_%M_%S);

date;
python3 ./scipy_kmeans.py >> ./Results/results_scipy_single_${DATE}.csv
date;
