
void shortest_and_longest(char **p, int n, int *shortest, int *longest);
// REQUIRES: n > 0. p[0] ... p[n-1] all point to beginnings of strings.
// shortest and longest point to appropriate variables.
// PROMISES:
// *shortest contains the length of the shortest string found with
// p[0] ... p[n-1].
// *longest contains the length of the longest string found with
// p[0] ... p[n-1]

void shortest_and_longest(char **p, int n, int *shortest, int *longest);
// REQUIRES: n > 0. p[0] ... p[n-1] all point to beginnings of strings.
// shortest and longest point to appropriate variables.
// PROMISES:
// *shortest contains the length of the shortest string found with
// p[0] ... p[n-1].
// *longest contains the length of the longest string found with
// p[0] ... p[n-1]
// Language: c
// Path: code.c


void shortest_and_longest(char **p, int n, int *shortest, int *longest)
{
  int i;
  int len;
  int min;
  int max;

  min = strlen(p[0]);
  max = strlen(p[0]);
  for (i = 1; i < n; i++) {
    len = strlen(p[i]);
    if (len < min) {
      min = len;
    }
    if (len > max) {
      max = len;
    }
  }
  *shortest = min;
  *longest = max;
}









