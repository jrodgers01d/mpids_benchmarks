#!/bin/bash
#SBATCH -N 8
#SBATCH --job-name=s_8p
#SBATCH -o s_8p.%j.stdout
#SBATCH -e s_8p.%j.error
#SBATCH -x crill-001,crill-10[1-5]
#SBATCH --exclusive
#SBATCH -t 2:00:00
#SBATCH -p crill

module load mpi4py/3.0.0-python3.4

#See if results directory exists, if not create it
if [ ! -d "$(pwd)/Results" ];then
  mkdir $(pwd)/Results
fi

HEADER_SCALING="\"Type\",\"Num_Proc\",\"Obs\",\"Feats\",\"Clusters\",\"Time\"";
DATE=$(date +%Y%m%d_%H_%M_%S);

echo $HEADER_SCALING > ./Results/results_strong_8_${2}_${DATE}.csv
date;
mpiexec -n 8 --map-by node python3 ./mpi_scipy_kmeans.py $1 $2 >> ./Results/results_strong_8_${2}_${DATE}.csv
date;
