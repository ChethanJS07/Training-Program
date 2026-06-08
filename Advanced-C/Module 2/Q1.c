#include <math.h>
#include <pthread.h>
#include <signal.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

volatile sig_atomic_t keep_running = 1;

void signal_handler(int sig) {
  if (sig == SIGINT) {
    printf("\nSIGINT received! Program continues...\n\n");
  }
}

void *primeSum(void *args) {
  int *n = (int *)args;
  long long *sum = calloc(1, sizeof(long long));

  if (*n == 0) {
    return sum;
  }

  int limit;
  if (*n < 6) {
    limit = 20;
  } else {
    limit = (*n) * (log(*n) + log(log(*n))) + 100;
  }

  bool *is_prime = calloc((limit + 1), sizeof(bool));
  for (int i = 2; i <= limit; i++) {
    is_prime[i] = true;
  }

  for (int i = 2; i * i <= limit; i++) {
    if (is_prime[i]) {
      for (int j = i * i; j <= limit; j += i) {
        is_prime[j] = false;
      }
    }
  }

  int count = 0;
  for (int i = 2; i <= limit && count < *n; i++) {
    if (is_prime[i]) {
      *sum += i;
      count++;
    }
  }

  free(is_prime);
  return (void *)sum;
}

void *printThread(void *args) {
  int *id = (int *)args;
  int interval = (*id == 1) ? 2 : 3;

  for (int elapsed = 0; elapsed < 100; elapsed += interval) {
    printf("Thread %d running at %d seconds\n", *id, elapsed);
    sleep(interval);
  }

  free(id);
  return NULL;
}

int main(int argc, char *argv[]) {
  signal(SIGINT, signal_handler);
  pthread_t th[3];
  int n;
  long long *sum = NULL;
  for (int i = 0; i < 3; i++) {
    if (i == 0) {
      printf("Enter the no primes: ");
      scanf("%d", &n);
      if (pthread_create(&th[i], NULL, &primeSum, &n) != 0) {
        fprintf(stderr, "Couldn't create thread %d\n", i);
        return 1;
      }
    } else {
      int *i_val = malloc(sizeof(int));
      *i_val = i;
      if (pthread_create(&th[i], NULL, &printThread, i_val) != 0) {
        fprintf(stderr, "Couldn't create thread %d\n", i);
        free(i_val);
        return 1;
      }
    }
  }

  for (int i = 0; i < 3; i++) {
    if (i == 0) {
      if (pthread_join(th[i], (void **)&sum) != 0) {
        fprintf(stderr, "Couldn't join thread %d\n", i);
      }
      printf("\nSum of first %d primes: %lld\n\n", n, *sum);

    } else {
      if (pthread_join(th[i], NULL) != 0) {
        fprintf(stderr, "Couldn't join thread %d\n", i);
      }
    }
  }

  free(sum);
  return 0;
}
