#!/bin/bash

sbatch run_trials_arithmetic.sh
sbatch run_trials_creation.sh
sbatch run_trials_global_accessing.sh
sbatch run_trials_local_accessing.sh
sbatch run_trials_reductions.sh
sbatch run_trials_reshape.sh
sbatch run_trials_reshape.sh
sbatch run_trials_collect_data.sh
#Way too expensive
# sbatch run_trials_global_iterating.sh
