#!/bin/bash
#SBATCH -N 15
#SBATCH --job-name=mpinumpy-weak
#SBATCH -o mpinumpy-weak.%j.stdout
#SBATCH -e mpinumpy-weak.%j.error
#SBATCH -x crill-001
#SBATCH -w crill-00[2-9],crill-01[0-6]
#SBATCH --exclusive
#SBATCH -t 02:00:00
#SBATCH -p crill

module load mpi4py/3.0.0-python3.4

HEADER_SCALING="\"Type\",\"Op\",\"Num_Proc\",\"Size\",\"Time\"";
DATE=$(date +%Y%m%d_%H_%M_%S);

echo $HEADER_SCALING > mpi_np_weak_missing_${DATE}.csv
for run in {1..50};do
  for procs in 1 2 4 8 16 32 64 128 256 512;do
    mpiexec -n $procs --map-by node python3 ./bench_weak_missing.py >> mpi_np_weak_missing_${DATE}.csv
  done
done
