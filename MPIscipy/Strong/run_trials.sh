#!/bin/bash

#Run single process jobs
for job in {1..1};do
  for power in {15..20};do
    sbatch ./run_single_process.sh 1 $power
    sleep 5
  done
done

#Run multi-process jobs
for power in {15..20};do
  sbatch ./run_2_procs.sh 1 $power
done

for power in {15..20};do
  sbatch ./run_4_procs.sh 1 $power
done

for power in {15..20};do
  sbatch ./run_8_procs.sh 1 $power
done

for power in {15..20};do
  sbatch ./run_16_plus.sh 1 $power
done
