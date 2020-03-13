#!/bin/bash

#Run single process jobs
for power in {10..15};do
  sbatch ./run_single_process.sh 50 $power
done


#Run multi-process jobs
for power in {10..15};do
  sbatch ./run_2_procs.sh 50 $power
done

for power in {10..15};do
  sbatch ./run_4_procs.sh 50 $power
done

for power in {10..15};do
  sbatch ./run_8_procs.sh 50 $power
done

for job in {1..5};do
  for power in {10..15};do
    sbatch ./run_16_plus.sh 10 $power $job
  done
done
