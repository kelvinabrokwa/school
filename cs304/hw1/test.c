#include <stdio.h>
#include <limits.h>

typedef unsigned packed_t;

int xbyte(packed_t word, int bytenum) {
    word = word << ((3 - bytenum) << 3);
    int m = (1 << 31) & word;
    word = word >> 24;
    return word - ((m << 31) >> 24);
}

int main() {
    packed_t w = 0xFF000000;
    int a = xbyte(w, 3);
    printf("%lu\n", sizeof(a));
}
