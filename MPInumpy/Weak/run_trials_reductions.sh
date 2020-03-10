#!/bin/bash
#SBATCH -N 15
#SBATCH --job-name=reductions
#SBATCH -o reductions.%j.stdout
#SBATCH -e reductions.%j.error
#SBATCH -x crill-001
#SBATCH -w crill-00[2-9],crill-01[0-6]
#SBATCH --exclusive
#SBATCH -t 1:20:00
#SBATCH -p crill

module load mpi4py/3.0.0-python3.4

#See if results directory exists, if not create it
if [ ! -d "$(pwd)/Results" ];then
  mkdir $(pwd)/Results
fi

HEADER_SCALING="\"Type\",\"Op\",\"Num_Proc\",\"Size\",\"Time\"";
DATE=$(date +%Y%m%d_%H_%M_%S);

echo $HEADER_SCALING > ./Results/results_reductions_${DATE}.csv
date;
for run in {1..50};do
  for procs in 1 2 4 8 16 32 64 128 256 512;do
    mpiexec -n $procs --map-by node python3 ./reductions_mpi_np.py >> ./Results/results_reductions_${DATE}.csv
  done
done
date;
