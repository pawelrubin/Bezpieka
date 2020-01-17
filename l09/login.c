#include <stdio.h>
#include <string.h>

int auth(char *code) {
  return !strcmp(code, "haslo");
}

void login(char *code) {
  int secret = 9;
  int authenticated = auth(code);
  char pass[10];
  strcpy(pass, code);
  if (authenticated) {
    printf("The secret is: %d\n", secret);
  } else {
    printf("Unauthorized\n");
  }
}

int main(int argc, char *argv[]) {
  char code[10];
  strcpy(code, argv[1]);
  login(code);
  return 0;
}
