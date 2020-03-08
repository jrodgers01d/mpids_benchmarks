#!/bin/bash

sbatch run_trials_accessing.sh
sbatch run_trials_arithmetic.sh
sbatch run_trials_creation.sh
sbatch run_trials_global_accessing.sh
sbatch run_trials_local_accessing.sh
sbatch run_trials_reductions.sh
sbatch run_trials_reshape.sh
sleep 10
sbatch run_trials_reshape.sh
sleep 10
sbatch run_trials_reshape.sh
sleep 10
sbatch run_trials_reshape.sh
sleep 10
sbatch run_trials_reshape.sh
