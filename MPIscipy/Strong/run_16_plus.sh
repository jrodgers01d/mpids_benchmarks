#!/bin/bash
#SBATCH -N 15
#SBATCH --job-name=kmeans_strong
#SBATCH -o kmeans_strong.%j.stdout
#SBATCH -e kmeans_strong.%j.error
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

echo $HEADER_SCALING > ./Results/results_strong_16p_${2}_${DATE}.csv
date;
for procs in 16 32 64 128 256 512;do
  mpiexec -n $procs --map-by node python3 ./mpi_scipy_kmeans.py $1 $2 >> ./Results/results_strong_16p_${2}_${DATE}.csv
done
date;
