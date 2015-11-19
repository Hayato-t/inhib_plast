#!/bin/bash -x
#
#PJM --rsc-list "rscgrp=small"
#PJM --rsc-list "node=120"
#PJM --rsc-list "elapse=02:00:00"
#PJM --mpi "proc=960"
#PJM --stg-transfiles all
#PJM --mpi "use-rankdir"

#PJM --stgin "rank=* ./* %r:./"
#PJM --stgin "rank=* ./data/* %r:./data/"
#PJM --stgin "rank=* ./weights/* %r:./weights/"
#PJM --stgin "rank=* ./result/* %r:./result/"
#PJM --stgin "rank=* ./change/* %r:./change/"

#PJM --stgin "rank=* /home/hp120263/k01792/neuron_kplus/specials/sparc64/special %r:./"
#PJM --stgin "rank=* /home/hp120263/k01792/neuron_kplus/stgin/* %r:./"

#PJM --stgout "rank=* %r:./result/* /data/hp120263/fukuda/inhib_plast/move/result/%j/"
#PJM --stgout "rank=* %r:./change/* /data/hp120263/fukuda/inhib_plast/move/change/%j/"

#PJM -s
#PJM -m "e"
#PJM --mail-list "fukuda@g.brain.imi.i.u-tokyo.ac.jp"
#

. /work/system/Env_base

#NRNIV="../../../neuron_kplus/specials/sparc64/special -mpi"
NRNIV="./special -mpi"
HOC_NAME="./network.hoc"

NRNOPT=\
" -c INPUT_E=0.028"\
" -c INPUT_I=0.04"\
" -c OUT1_E=0.001"\
" -c OUT1_I=0.01"\
" -c OUT2_E=0.002"\
" -c OUT2_I=0.01"\
" -c IO_E=0.002"\
" -c IO_I2E=0.001"\
" -c IO_I2I=0.001"\
" -c OUT1_SPON_E_K=0"\
" -c OUT1_SPON_E_T=0"\
" -c OUT2_SPON_E_K=0.13"\
" -c OUT2_SPON_E_T=0.32"\
" -c IN_SPON_K=0.12"\
" -c IN_SPON_T=0.3"\
" -c DOPAMINE=0.01"\
" -c LEARNING_RATE=0.00025"\
" -c LR4INPUT=0.00015"\
" -c OUT1_SPON_I_K=0.15"\
" -c OUT1_SPON_I_T=0.3"\
" -c LTD=0.7"\
" -c LTD4INPUT=1.3"\
" -c LEARNING_RATE_I=0.0001"\
" -c LR4INPUT_I=0.001"


LPG="lpgparm -t 4MB -s 4MB -d 4MB -p 4MB"
MPIEXEC="mpiexec -mca mpi_print_stats 1"
PROF=""
echo "${PROF} ${MPIEXEC} ${LPG} ${NRNIV} ${HOC_NAME}"
time ${PROG} ${MPIEXEC} ${LPG} ${NRNIV} ${NRNOPT} ${HOC_NAME}

sync