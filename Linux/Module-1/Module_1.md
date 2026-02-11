# Module 1 Assignment

#### Output of the following commands can be found here:

Drive link : [Output](https://drive.google.com/drive/folders/1iKSC0BHvJyZ9Z9eEBMAjtgX5azbfvhzd?usp=sharing)

---

### 1) Create a file and add executable permission to all users (user, group and others)

```bash
# create a new file
touch new_file1.txt

# view default permissions
ls -l

# add executable permission for all users (user, group and other)
chmod +x new_file1.txt

# verify new permissions
ls -l
```

---

### 2) create a file and remove write permission for group user alone.

```bash
# create a new file
touch new_file2.txt

# view default permissions
ls -l

# give full permissions to all users
chmod 777 new_file2.txt

# remove write permissions to group users
chmod g-w new_file2.txt

# verify new permissions
ls -l
```

---

### 3) Create a file and add a softlink to the file in different directory (Eg : Create a file in dir1/dir2/file and create a softlink for file inside dir1)

```bash
# create new file in dir1/dir2/
mkdir dir1/dir2/
touch dir1/dir2/new_file3.txt

# verify file creation
ls -l

# create a softlink for the file new_file.txt in dir1/
cd dir1/
ln -s dir2/new_file3.txt link_file.txt

# verify softlink
ls -l
```

---

### 4) Use ps command with options to display all active process running on the system

```bash
# display all running processes with options
ps aux
```

---

### 5) Create 3 files in a dir1 and re-direct the output of list command with sorted by timestamp of the files to a file

```bash
# create a new directory dir1 and create 3 new files inside dir1
mkdir dir1/
touch file1
touch file2
touch file3

# verify files creation and their timestamps
ls -l

# redirect the output of list command with sorted timestamps of the files to a file
ls -lt > output.txt # for newest first
ls -ltr > output.txt # for oldest first

# verify the contents of the output.txt
cat output.txt
```

---
