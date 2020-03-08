#!/bin/bash
#SBATCH -N 1
#SBATCH --job-name=local_acc
#SBATCH --ntasks-per-node 1
#SBATCH -o local_acc.%j.stdout
#SBATCH -e local_acc.%j.error
#SBATCH -x crill-001
#SBATCH --exclusive
#SBATCH -t 5:59:00
#SBATCH -p crill

module load mpi4py/3.0.0-python3.4

#See if results directory exists, if not create it
if [ ! -d "$(pwd)/Results" ];then
  mkdir $(pwd)/Results
fi

HEADER_NPVMPINP="\"Type\",\"Op\",\"Size\",\"Time\"";
DATE=$(date +%Y%m%d_%H_%M_%S);

echo $HEADER_NPVMPINP > ./Results/results_local_accessing_${DATE}.csv
for run in {1..50};do
  mpiexec -n 1 python3 ./local_accessing_mpi_np.py >> ./Results/results_local_accessing_${DATE}.csv
done
