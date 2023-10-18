#!/bin/bash

if [ "$#" -lt 8 ] || [ "$#" -gt 9 ]; then
    echo "Illegal number of parameters"
    echo "Usage: ./run_champsim.sh [BINARY] [N_WARM] [N_SIM] [N_CEV] [N_STRAT] [TRACE0] [TRACE1] [TRACE2] [TRACE3]"
    exit 1
fi

TRACE_DIR=$PWD/../spec2006
BINARY=${1}
N_WARM=${2}
N_SIM=${3}
N_CEV=${4}
N_STRAT=${5}
TRACE0=${6}
TRACE1=${7}
TRACE2=${8}
TRACE3=${9}

# Sanity check
if [ -z $TRACE_DIR ] || [ ! -d "$TRACE_DIR" ] ; then
    echo "[ERROR] Cannot find a trace directory: $TRACE_DIR"
    exit 1
fi

if [ ! -f "../bin/$BINARY" ] ; then
    echo "[ERROR] Cannot find a ChampSim binary: bin/$BINARY"
    exit 1
fi

re='^[0-9]+$'
if ! [[ $N_WARM =~ $re ]] || [ -z $N_WARM ] ; then
    echo "[ERROR]: Number of warmup instructions is NOT a number" >&2;
    exit 1
fi

re='^[0-9]+$'
if ! [[ $N_SIM =~ $re ]] || [ -z $N_SIM ] ; then
    echo "[ERROR]: Number of simulation instructions is NOT a number" >&2;
    exit 1
fi

re='^[0-9]+$'
if ! [[ $N_CEV =~ $re ]] || [ -z $N_CEV ] ; then
    echo "[ERROR]: CEVICHE is NOT a number" >&2;
    exit 1
fi

re='^[0-9]+$'
if ! [[ $N_STRAT =~ $re ]] || [ -z $N_STRAT ] ; then
    echo "[ERROR]: Strategy is NOT a number" >&2;
    exit 1
fi


if [ ! -f "$TRACE_DIR/$TRACE0" ] ; then
    echo "[ERROR] Cannot find a trace0 file: $TRACE_DIR/$TRACE0"
    exit 1
fi

if [ ! -f "$TRACE_DIR/$TRACE1" ] ; then
    echo "[ERROR] Cannot find a trace1 file: $TRACE_DIR/$TRACE1"
    exit 1
fi

if [ ! -f "$TRACE_DIR/$TRACE2" ] ; then
    echo "[ERROR] Cannot find a trace2 file: $TRACE_DIR/$TRACE2"
    exit 1
fi

if [ ! -f "$TRACE_DIR/$TRACE3" ] ; then
    echo "[ERROR] Cannot find a trace3 file: $TRACE_DIR/$TRACE3"
    exit 1
fi

../bin/${BINARY} -warmup_instructions ${N_WARM}000000 -simulation_instructions ${N_SIM}000000 -ceviche $N_CEV -strategy $N_STRAT -traces ${TRACE_DIR}/${TRACE0} ${TRACE_DIR}/${TRACE1} ${TRACE_DIR}/${TRACE2} ${TRACE_DIR}/${TRACE3}
