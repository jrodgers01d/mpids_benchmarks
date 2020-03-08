#!/bin/bash
#SBATCH -N 1
#SBATCH --job-name=creation
#SBATCH --ntasks-per-node 1
#SBATCH -o creation.%j.stdout
#SBATCH -e creation.%j.error
#SBATCH -x crill-001
#SBATCH -w crill-00[1-9],crill-01[0-6]
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

echo $HEADER_NPVMPINP > ./Results/results_creation_${DATE}.csv
for run in {1..50};do
  python3 ./creation_numpy.py >> ./Results/results_creation_${DATE}.csv
  mpiexec -n 1 python3 ./creation_mpi_np.py >> ./Results/results_creation_${DATE}.csv
done
