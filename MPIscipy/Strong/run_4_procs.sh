#!/bin/bash
#SBATCH -N 4
#SBATCH --job-name=s_4p
#SBATCH -o s_4p.%j.stdout
#SBATCH -e s_4p.%j.error
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

echo $HEADER_SCALING > ./Results/results_strong_4_${2}_${DATE}.csv
date;
mpiexec -n 4 --map-by node python3 ./mpi_scipy_kmeans.py $1 $2 >> ./Results/results_strong_4_${2}_${DATE}.csv
date;
