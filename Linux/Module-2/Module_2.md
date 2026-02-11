# Module 2 Assignment

#### Output of the following commands can be found here:

Drive link : [Output](https://drive.google.com/drive/folders/1iKSC0BHvJyZ9Z9eEBMAjtgX5azbfvhzd?usp=sharing)

---

### 1) Use the appropriate command to list all files larger than 1 MB in the current directory and save the output to a file.

```bash
# find files larger than 1M recursively and save to file
find . -size +1M > large_files.txt

# verify if large_files stored details
wc -l large_files
head large_files
```

---

### 2) Replace all occurrences of "localhost" with "127.0.0.1" in a configuration file named config.txt, and save the updated file as updated_config.txt.

```bash
# command to replace localhost with 127.0.0.1 and save in a new file
sed 's/localhost/127.0.0.1/g' config.txt > updated_config.txt

# verify updated_config
cat updated_config.txt
```

---

### 3) Use the appropriate command to search for lines containing the word "ERROR" in a log file but exclude lines containing "DEBUG". Save the results to a file named filtered_log.txt.

```bash
# include "ERROR" but remove "DEBUG"
grep "ERROR" log.txt | grep -v "DEBUG" > filtered_log.txt

# verify contents of filtered_log
cat filtered_log.txt
```

---

### 4) Write a code to identify the process with the highest memory usage and then terminate it.

```bash
# display the USER, PID, %MEM and COMMAND that uses the most memory
ps aux --sort=-%mem | head -2 | awk ' {print $1"\t"$2"\t"$4"\t"$11} '

# delete the process with PID using kill command
ps aux --sort=-%mem | tail -n +2 | head -1 | awk ' { print $2 } ' | xargs kill

# verify if a new process is using the most memory
ps aux --sort=-%mem | head -2 | awk ' {print $1"\t"$2"\t"$4"\t"$11} '
```

---

### 5) Use the networking tool command and print all the gateway available in a sorted manner

```bash
ip route
```

---
