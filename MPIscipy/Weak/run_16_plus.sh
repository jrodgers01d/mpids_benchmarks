#!/bin/bash
#SBATCH -N 15
#SBATCH --job-name=kmeans_weak
#SBATCH -o kmeans_weak.%j.stdout
#SBATCH -e kmeans_weak.%j.error
#SBATCH -x crill-001
#SBATCH -w crill-00[2-9],crill-01[0-6]
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

echo $HEADER_SCALING > ./Results/results_weak_16p_%j_${DATE}.csv
date;
for procs in 16 32 64 128 256 512;do
  mpiexec -n $procs --map-by node python3 ./mpi_scipy_kmeans.py $1 $2 >> ./Results/results_weak_16p_%j_${DATE}.csv
done
date;
