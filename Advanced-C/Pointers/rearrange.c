#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void rearrange(int *arr, int size) {
  bool swapped = true;

  while (swapped) {
    swapped = false;
    for (int i = 0; i < size - 1; i++) {
      if (arr[i] % 2 != 0 && arr[i + 1] % 2 == 0) {
        arr[i] = arr[i] + arr[i + 1];
        arr[i + 1] = arr[i] - arr[i + 1];
        arr[i] = arr[i] - arr[i + 1];
        swapped = true;
      }
    }
  }
}

int main() {
  char *line = NULL;
  size_t len = 0;
  size_t nread = 0;

  printf("Enter array elements (space separated): ");
  if ((nread = getline(&line, &len, stdin)) == -1) {
    printf("Error reading input...\n");
    return 1;
  }

  if (nread > 0 && line[nread - 1] == '\n') {
    line[nread - 1] = '\0';
  }

  int *arr = NULL;
  int count = 0;
  int capacity = 0;
  char *token = strtok(line, " ");

  while (token != NULL) {
    if (count >= capacity) {
      capacity = (capacity == 0) ? 4 : capacity * 2;
      int *temp = realloc(arr, capacity * sizeof(int));
      if (temp == NULL) {
        free(arr);
        free(line);
        return 1;
      }
      arr = temp;
    }
    arr[count++] = atoi(token);
    token = strtok(NULL, " ");
  }

  printf("Original Array: ");
  for (int i = 0; i < count; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");

  rearrange(arr, count);

  printf("Rearranged Array: ");
  for (int i = 0; i < count; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");

  free(arr);
  free(line);
  return 0;
}
