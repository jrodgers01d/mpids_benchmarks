#!/bin/bash
#SBATCH -N 15
#SBATCH --job-name=mpinumpy-strong
#SBATCH -o mpinumpy-strong.%j.stdout
#SBATCH -e mpinumpy-strong.%j.error
#SBATCH -x crill-001
#SBATCH --exclusive
#SBATCH -t 10:00:00
#SBATCH -p crill

module load mpi4py/3.0.0-python3.4

HEADER_SCALING="\"Type\",\"Op\",\"Num_Proc\",\"Size\",\"Time\"";
DATE=$(date +%Y%m%d_%H_%M_%S);

echo $HEADER_SCALING > mpi_np_strong_${DATE}.csv
for run in {1..50};do
  for procs in 1 2 4 8 16 32 64 128 256 512;do
    mpiexec -n $procs --map-by node python3 ./bench_strong.py >> mpi_np_strong_${DATE}.csv
  done
done
