#!/bin/bash

#Run single process jobs
for job in {1..5};do
  for power in {15..20};do
    sbatch ./run_single_process.sh 10 $power $job
  done
done

#Run multi-process jobs
for job in {1..5};do
  for power in {15..20};do
    sbatch ./run_2_procs.sh 10 $power $job
  done
done

for power in {15..20};do
  sbatch ./run_4_procs.sh 50 $power
done

for power in {15..20};do
  sbatch ./run_8_procs.sh 50 $power
done

for power in {15..20};do
  sbatch ./run_16_plus.sh 50 $power
done
