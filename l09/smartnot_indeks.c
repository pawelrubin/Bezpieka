#include <unistd.h>
#include <stdio.h>
#include <string.h>

char shellcode[] =  "\xeb\x19\x31\xc0\x31\xdb\x31\xd2\x31\xc9\xb0\x04\xb3\x01"\
                    "\x59\xb2\x06\xcd\x80\x31\xc0\xb0\x01\x31\xdb\xcd\x80"\
                    "\xe8\xe2\xff\xff\xff"\
/*numer indeksu = */"\x31\x32\x33\x34\x35\x36"; /* 123456 */

int main(int argc, char *argv[]) {
  int *ret;
  ret = (int *)&ret + 2;
  (*ret) = (int) shellcode;
}