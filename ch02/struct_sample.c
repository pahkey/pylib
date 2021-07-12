#include <stdio.h>
typedef struct {
    double v;
    int t;
    char c;
} save_type;

int main() {
    save_type s = {7.5f, 15, 'A'};
    FILE *f = fopen("output", "w");
    fwrite(&s, sizeof(save_type), 1, f);
    fclose(f);
    return 0;
}
