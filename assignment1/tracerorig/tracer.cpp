#include "pin.H"
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <string>

using namespace std;

/* =========================== NOTE ================================= */
// The processor operates at 1GHZ
// The cycle values and latency are in picoseconds --> 1000ps = 1ns
/* ================================================================== */

INT64 instrCount = 0;
INT64 change = 0;

/* ============= TRACK MEMORY + NONMEMORY INST ====================== */
INT64 meminstCount = 0;
INT64 nonmeminstCount = 0;

/* ============= TRACK BRANCH INST ====================== */
INT64 branchCount = 0;

/* ============================ BASELINE ============================ */
INT64 CYCLEVALS = 0;
INT64 CYCLEVALP = 0;
INT64 MEMDELAY = 2000; // 2ns
INT64 NONMEMDELAY = 1000; // 1ns

/* ============================= OPT ================================ */
INT64 OPTCYCLEVALS = 0;
INT64 OPTCYCLEVALP = 0;
INT64 OPTMEMDELAY = 2000; // 2ns
INT64 OPTNONMEMDELAY = 1000; // 1ns
/* ================================================================== */
/* ================================================================== */



/* ================================================================== */
// Global variables 
/* ================================================================== */

FILE* out;
bool output_file_closed = false;

/* ================================================================== */
// Add your variables below this
/* ================================================================== */









/* ================================================================== */
// Add your variables above this
/* ================================================================== */


/* ===================================================================== */
// Command line switch
/* ===================================================================== */

KNOB<INT64> KnobMemChange(KNOB_MODE_WRITEONCE, "pintool", "m", "0", "Percentage Change in Non-Memory Latency: From -90 to +90");


/* ===================================================================== */
// Utilities
/* ===================================================================== */

/*!
 *  Print out help message.
 */
INT32 Usage()
{
	cerr << "This tool creates helps instrument instructions" << endl << "Percentage Change in Non-Memory Latency: From -90 to +90 with -o" << endl;
	cerr << KNOB_BASE::StringKnobSummary() << endl;
	return -1;
}


/* ===================================================================== */
// Analysis routines
/* ===================================================================== */

void BeginInstruction(VOID *ip, UINT32 op_code, VOID *opstring){
	instrCount++;

	if(instrCount%1000000 == 0){
		std::cout << "." << std::flush;
		if(instrCount%10000000 == 0){
			std::cout << " -- " << instrCount/1000000 << " Million Instructions" << std::endl << std::flush;
		}
	}
}

/* ++++++++++++++++ ADD YOUR FUNCTION (IF ANY) BELOW ++++++++++++++++++++ */

void MemInstructionCount(VOID *ip) {
    meminstCount++; 
}

void NonMemInstructionCount(VOID *ip) {
    nonmeminstCount++;
}

void BranchInstructionCount(VOID *ip) {
    branchCount++;
}

void MemInstructionDelay(VOID *ip) {
	CYCLEVALS += MEMDELAY;
}

void NonMemInstructionDelay(VOID *ip) {
	CYCLEVALS += NONMEMDELAY;
}

void NonMemInstructionDelayOnly(VOID *ip) {
	CYCLEVALP += NONMEMDELAY;
}

void OptMemInstructionDelay(VOID *ip) {
	OPTCYCLEVALS += OPTMEMDELAY;
}

void OptNonMemInstructionDelay(VOID *ip) {
	OPTCYCLEVALS += OPTNONMEMDELAY;
}

void OptNonMemInstructionDelayOnly(VOID *ip) {
	OPTCYCLEVALP += OPTNONMEMDELAY;
}


/* ++++++++++++++++ ADD YOUR FUNCTION (IF ANY) ABOVE ++++++++++++++++++++ */


void EndInstruction()
{

}

/* ===================================================================== */
// Instrumentation callbacks
/* ===================================================================== */

// Is called for every instruction
VOID Instruction(INS ins, VOID *v)
{
	// begin each instruction with this function
	UINT32 opcode = INS_Opcode(ins);
	INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)BeginInstruction, IARG_INST_PTR, IARG_UINT32, opcode, IARG_END);
	
	//+++++++++++++++++ ADD YOUR CODE BELOW THIS POINT ++++++++++++++++++++++++++//

	// memory and nonmemory instruction count
	if (INS_IsMemoryRead(ins) || INS_IsMemoryWrite(ins)) {
		INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)MemInstructionCount, IARG_INST_PTR, IARG_END);
	} else {
		INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)NonMemInstructionCount, IARG_INST_PTR, IARG_END);
	}

	// branch instruction count
	if (INS_IsBranch(ins)) {
		INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)BranchInstructionCount, IARG_INST_PTR, IARG_END);
	}

	// delay for nonmemory and memory instructions
	if (INS_IsMemoryRead(ins) || INS_IsMemoryWrite(ins)) {
		INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)MemInstructionDelay, IARG_INST_PTR, IARG_END);
	} else {
		INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)NonMemInstructionDelay, IARG_INST_PTR, IARG_END);
	}

	// delay for nonmemory instructions only
	if (!(INS_IsMemoryRead(ins) || INS_IsMemoryWrite(ins))) {
		INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)NonMemInstructionDelayOnly, IARG_INST_PTR, IARG_END);
	}

	// optimized delay for nonmemory and memory instructions
	if (INS_IsMemoryRead(ins) || INS_IsMemoryWrite(ins)) {
		INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)OptMemInstructionDelay, IARG_INST_PTR, IARG_END);
	} else {
		INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)OptNonMemInstructionDelay, IARG_INST_PTR, IARG_END);
	}

	// optimized delay for nonmemory instructions only
	if (!(INS_IsMemoryRead(ins) || INS_IsMemoryWrite(ins))) {
		INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)OptNonMemInstructionDelayOnly, IARG_INST_PTR, IARG_END);
	}




	//+++++++++++++++++ ADD YOUR CODE ABOVE THIS POINT ++++++++++++++++++++++++++//
	// finalize each instruction with this function
	INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)EndInstruction, IARG_END);
}

VOID Fini(INT32 code, VOID *v)
{
	if(nonmeminstCount != 0){
		assert(instrCount == (nonmeminstCount+meminstCount));
	}

	fprintf(out, "instrCount,%ld\n", instrCount);
	fprintf(out, "nonmeminstCount,%ld\n", nonmeminstCount);
	fprintf(out, "meminstCount,%ld\n", meminstCount);
	fprintf(out, "branchCount,%ld\n", branchCount);

	fprintf(out, "MEMDELAY,%ld\n", MEMDELAY);
	fprintf(out, "NONMEMDELAT,%ld\n", NONMEMDELAY);
	fprintf(out, "CYCLEVAL-SERIAL,%ld\n", CYCLEVALS);
	fprintf(out, "CYCLEVAL-HIDEMEM,%ld\n", CYCLEVALP);

	fprintf(out, "CHANGE,%ld\n", change);
	fprintf(out, "OPT-MEMDELAY,%ld\n", OPTMEMDELAY);
	fprintf(out, "OPT-NONMEMDELAT,%ld\n", OPTNONMEMDELAY);
	fprintf(out, "OPT-CYCLEVAL-SERIAL,%ld\n", OPTCYCLEVALS);
	fprintf(out, "OPT-CYCLEVAL-HIDEMEM,%ld\n", OPTCYCLEVALP);

	fprintf(out, "SPEEDUP,%f\n", ((double)CYCLEVALS)/OPTCYCLEVALS);
	fprintf(out, "SPEEDUP-HIDEMEM,%f\n", ((double)CYCLEVALP)/OPTCYCLEVALP);
	
	// close the file if it hasn't already been closed
	if(!output_file_closed) 
	{
		fclose(out);
		output_file_closed = true;
	}
}

int main(int argc, char *argv[]){
	// Initialize PIN library. Print help message if -h(elp) is specified
	// in the command line or the command line is invalid 
	if( PIN_Init(argc,argv) )
		return Usage();

	const char* fileName = "../output/tracerorig.out";

	out = fopen(fileName, "w+");

	if (out == NULL){
		cout << "Couldn't open output file. Exiting." << endl;
		exit(1);
	}

	change = KnobMemChange.Value();

	if(change > 90){
		cout << "Incorrect Change of Memory Latency Option. Exiting." << endl;
		exit(1);
	}
	if(change < -90){
		cout << "Incorrect Change of Memory Latency Option. Exiting." << endl;
		exit(1);
	}

	OPTMEMDELAY = OPTMEMDELAY - ((change*OPTMEMDELAY)/100);
	OPTNONMEMDELAY = OPTNONMEMDELAY + ((change*OPTNONMEMDELAY)/100);

	assert(OPTMEMDELAY > 0);
	assert(OPTNONMEMDELAY > 0);

	// Register function to be called to instrument instructions
	INS_AddInstrumentFunction(Instruction, 0);

	// Register function to be called when the application exits
	PIN_AddFiniFunction(Fini, 0);

	// Start the program, never returns
	PIN_StartProgram();

	return 0;
}
