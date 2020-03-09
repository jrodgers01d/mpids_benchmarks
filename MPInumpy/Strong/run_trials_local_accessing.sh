#!/bin/bash
#SBATCH -N 15
#SBATCH --job-name=local_acc
#SBATCH -o local_acc.%j.stdout
#SBATCH -e local_acc.%j.error
#SBATCH -x crill-001
#SBATCH -w crill-00[2-9],crill-01[0-6]
#SBATCH --exclusive
#SBATCH -t 5:59:00
#SBATCH -p crill

module load mpi4py/3.0.0-python3.4

#See if results directory exists, if not create it
if [ ! -d "$(pwd)/Results" ];then
  mkdir $(pwd)/Results
fi

HEADER_SCALING="\"Type\",\"Op\",\"Num_Proc\",\"Size\",\"Time\"";
DATE=$(date +%Y%m%d_%H_%M_%S);

echo $HEADER_SCALING > ./Results/results_local_accessing_${DATE}.csv
date;
for run in {1..5};do
  for procs in 1 2 4 8 16 32 64 128 256 512;do
    mpiexec -n $procs --map-by node python3 ./local_accessing_mpi_np.py >> ./Results/results_local_accessing_${DATE}.csv
  done
done
date;
