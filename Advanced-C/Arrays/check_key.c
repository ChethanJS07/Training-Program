#include <stdio.h>
#include <stdlib.h>

int checkKey(int size, int mat[size][size], int key) {
  int row = 0, col = size - 1;
  while (row < size && col >= 0) {
    if (mat[row][col] == key) {
      return 1;
    } else if (mat[row][col] < key) {
      row++;
    } else {
      col--;
    }
  }

  return 0;
}

int main() {

  FILE *file = fopen("input.txt", "r");
  if (file == NULL) {
    fprintf(stderr, "Error: Could not open input.txt\n");
    return 1;
  }

  int *data = NULL;
  int capacity = 0;
  int count = 0;
  int num;

  while (fscanf(file, "%d", &num) == 1) {
    if (count >= capacity) {
      capacity = (capacity == 0) ? 16 : capacity * 2;
      int *temp = realloc(data, capacity * sizeof(int));
      if (temp == NULL) {
        fprintf(stderr, "Error: Memory Allocation failed!\n");
        free(data);
        fclose(file);
        return 1;
      }
      data = temp;
    }
    data[count++] = num;
  }
  fclose(file);

  if (count == 0) {
    fprintf(stderr, "File is empty\n");
    free(data);
    return 1;
  }

  int size = 0;
  while (size * size < count)
    size++;
  if (size * size != count) {
    fprintf(
        stderr,
        "The number of integers (%d) does not form a perfect square matrix\n",
        count);
    free(data);
    return 1;
  }

  int mat[size][size];
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      mat[i][j] = data[i * size + j];
    }
  }
  free(data);

  int key;
  printf("Enter key to check: ");
  if (scanf("%d", &key) != 1) {
    fprintf(stderr, "Invalid input for key!\n");
    return 1;
  }

  if (checkKey(size, mat, key)) {
    printf("Key found!\n");
  } else {
    printf("Key not found?!\n");
  }
  return 0;
}
