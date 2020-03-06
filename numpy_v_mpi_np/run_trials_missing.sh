#!/bin/bash
#SBATCH -N 1
#SBATCH --job-name=np_v_mpi_np
#SBATCH --ntasks-per-node 1
#SBATCH -o np_v_mpi_np.%j.stdout
#SBATCH -e np_v_mpi_np.%j.error
#SBATCH -x crill-001
#SBATCH -w crill-002
#SBATCH --exclusive
#SBATCH -t 05:59:00
#SBATCH -p crill

module load mpi4py/3.0.0-python3.4

HEADER_NPVMPINP="\"Type\",\"Op\",\"Size\",\"Time\"";
DATE=$(date +%Y%m%d_%H_%M_%S);

echo $HEADER_NPVMPINP > np_v_mpi_np_missing_${DATE}.csv
for run in {1..50};do
  python3 ./bench_numpy_missing.py >> np_v_mpi_np_missing_${DATE}.csv
  mpiexec -n 1 python3 ./bench_MPInumpy_missing.py >> np_v_mpi_np_missing_${DATE}.csv
done
