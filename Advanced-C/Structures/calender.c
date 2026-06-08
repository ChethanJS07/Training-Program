#include <stdio.h>
#include <string.h>

#define MAX_TASKS 3
#define MAX_TASK_LEN 64
#define DAYS_IN_WEEK 7

struct day {
  char dayName[12];
  char tasks[MAX_TASKS][MAX_TASK_LEN];
};

int is_task_empty(const char *task) { return task[0] == '\0'; }

int add_task_to_day(struct day *d, const char *task) {
  for (int i = 0; i < MAX_TASKS; i++) {
    if (is_task_empty(d->tasks[i])) {
      strncpy(d->tasks[i], task, MAX_TASK_LEN - 1);
      d->tasks[i][MAX_TASK_LEN - 1] = '\0'; // ensure null termination
      return 0;
    }
  }
  return -1;
}

void display_all_days(struct day week[], int num_days) {
  printf("\n===== TASKS GROUPED BY DAY =====\n");
  for (int i = 0; i < num_days; i++) {
    printf("\n%s:\n", week[i].dayName);
    int has_tasks = 0;
    for (int j = 0; j < MAX_TASKS; j++) {
      if (!is_task_empty(week[i].tasks[j])) {
        printf("  - %s\n", week[i].tasks[j]);
        has_tasks = 1;
      }
    }
    if (!has_tasks) {
      printf("  (no tasks)\n");
    }
  }
  printf("===============================\n");
}

int main() {
  const char *day_names[DAYS_IN_WEEK] = {"Monday",   "Tuesday", "Wednesday",
                                         "Thursday", "Friday",  "Saturday",
                                         "Sunday"};

  struct day week[DAYS_IN_WEEK];
  for (int i = 0; i < DAYS_IN_WEEK; i++) {
    strncpy(week[i].dayName, day_names[i], sizeof(week[i].dayName) - 1);
    week[i].dayName[sizeof(week[i].dayName) - 1] = '\0';
    for (int j = 0; j < MAX_TASKS; j++) {
      week[i].tasks[j][0] = '\0';
    }
  }

  int choice;
  do {
    printf("\n--- DAILY TASK MANAGER ---\n");
    printf("1. Add task to a day\n");
    printf("2. Display all tasks (grouped by day)\n");
    printf("3. Exit\n");
    printf("Your choice: ");
    scanf("%d", &choice);
    getchar();
    switch (choice) {
    case 1: {
      printf("\nSelect a day:\n");
      for (int i = 0; i < DAYS_IN_WEEK; i++) {
        printf("%d. %s\n", i + 1, week[i].dayName);
      }
      int day_choice;
      printf("Enter day number (1-%d): ", DAYS_IN_WEEK);
      scanf("%d", &day_choice);
      getchar();
      if (day_choice < 1 || day_choice > DAYS_IN_WEEK) {
        printf("Invalid day number!\n");
        break;
      }
      struct day *selected_day = &week[day_choice - 1];

      char task_input[MAX_TASK_LEN];
      printf("Enter task (max %d characters): ", MAX_TASK_LEN - 1);
      fgets(task_input, sizeof(task_input), stdin);
      task_input[strcspn(task_input, "\n")] = '\0';

      if (strlen(task_input) == 0) {
        printf("Task cannot be empty!\n");
        break;
      }

      int result = add_task_to_day(selected_day, task_input);
      if (result == 0) {
        printf("Task added to %s.\n", selected_day->dayName);
      } else {
        printf("Cannot add task: %s already has %d tasks.\n",
               selected_day->dayName, MAX_TASKS);
      }
      break;
    }
    case 2:
      display_all_days(week, DAYS_IN_WEEK);
      break;
    case 3:
      printf("Goodbye!\n");
      break;
    default:
      printf("Invalid choice. Please enter 1, 2 or 3.\n");
    }
  } while (choice != 3);

  return 0;
}
