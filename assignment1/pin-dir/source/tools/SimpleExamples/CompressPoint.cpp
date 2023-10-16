/*BEGIN_LEGAL 
Intel Open Source License 

Copyright (c) 2002-2015 Intel Corporation. All rights reserved.
 
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.  Redistributions
in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution.  Neither the name of
the Intel Corporation nor the names of its contributors may be used to
endorse or promote products derived from this software without
specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE INTEL OR
ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
END_LEGAL */
//
// @ORIGINAL_AUTHOR: Artur Klauser
// @EXTENDED: Rodric Rabbah (rodric@gmail.com) 
//

/*! @file
 *  This file contains an ISA-portable cache simulator
 *  data cache hierarchies
 */


#include "pin.H"

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <unistd.h>

std::ofstream outFile;
using namespace std;
/* ===================================================================== */
/* Global Variables */
/* ===================================================================== */

UINT64 realinst=1;

/* ===================================================================== */
/* Commandline Switches */
/* ===================================================================== */

KNOB<string> KnobOutputFile(KNOB_MODE_WRITEONCE,    "pintool",
    "o", "dcache.out", "specify dcache file name");
KNOB<BOOL> KnobCompress(KNOB_MODE_WRITEONCE,    "pintool",
    "c", "0", "compress all pages in main mem");
KNOB<string> KnobTmpFile(KNOB_MODE_WRITEONCE,    "pintool",
    "temp", "/tmp/list.txt", "specify tmp file name");
KNOB<int> KnobForward(KNOB_MODE_WRITEONCE,    "pintool",
    "forward", "1", "specify forward in terms of 5 bill ins");


/* ===================================================================== */
/* Print Help Message                                                    */
/* ===================================================================== */

INT32 Usage()
{
    cerr <<
        "This tool represents a CompressVector Generator.\n"
        "\n";

    cerr << KNOB_BASE::StringKnobSummary() << endl; 
    return -1;
}




/* ===================================================================== */

VOID CountPhase(uint64_t IP)
{
	realinst++;
	if(realinst% (1000000000)==0) {
		cout << realinst<<endl;
	}
	if(realinst% (KnobForward.Value()*5000000000)==0) {
		cout << realinst << " " << hex <<  IP << dec << endl;
		outFile << "inst: " << realinst << " IP : " << hex << IP << dec<< endl;
		/*if(KnobCompress) {
			//int ret = std::system("~/Documents/Research/SPECcpu2006_install/benchspec/CPU2006/433.milc/run/run_base_ref_ubuntu64-1004-gcc443.0000/sleep.sh");
			FILE *f = fopen(KnobTmpFile.Value().c_str(),"w");
			fclose(f);
			while(access( KnobTmpFile.Value().c_str(), F_OK ) != -1){sleep(1);}
			cout << "Running " << endl;
		}*/
	}
}

/* ===================================================================== */

VOID Instruction(INS ins, void * v)
{
	INS_InsertCall(ins,IPOINT_BEFORE,(AFUNPTR)CountPhase, IARG_INST_PTR, IARG_END);

}

/* ===================================================================== */

VOID Fini(int code, VOID * v)
{
    outFile.close();
}
void DetachFini(void *v) {Fini(0,v);}
/* ===================================================================== */
/* Main                                                                  */
/* ===================================================================== */

int main(int argc, char *argv[])
{
    PIN_InitSymbols();

    if( PIN_Init(argc,argv) )
    {
        return Usage();
    }

    INS_AddInstrumentFunction(Instruction, 0);
    PIN_AddFiniFunction(Fini, 0);
    PIN_AddDetachFunction(DetachFini, 0);

    // Never returns

    PIN_StartProgram();
    
    return 0;
}

/* ===================================================================== */
/* eof */
/* ===================================================================== */
