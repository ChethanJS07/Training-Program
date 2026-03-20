# Networking Training Program

## Module 1 and 2 assessment questions.

---

1. Consider a case, a folder has multiple files and how would you copy it to destination machine path (Try using SCP, cp options in Linux)

```bash
# if we have to copy a folder with multiple files in the same machine
cp -r /path/to/source/folder /path/to/destination/folder

# if the destination is a remote machine
scp -p 2222 -r /path/to/source/folder username@ipaddress:path/to/destination/folder
```

---

2. Host a FTP and SFTP server and try PUT and GET operations

```bash
sftp -P 2222 root@localhost
(root@localhost) Password:
Connected to localhost.
sftp> ls /mnt/shared
/mnt/shared/develop
sftp> get /mnt/shared/develop/kernel/hello-1/hello-1.c
Fetching /mnt/shared/develop/kernel/hello-1/hello-1.c to hello-1.c
sftp> put qemu-lab/shared/develop/user/hello-1/hello-1.c
Uploading qemu-lab/shared/develop/user/hello-1/hello-1.c to /root/hello-1.c
sftp> ls
hello-1.c
```

---

3. Explore with Wireshark/TCP-dump/Cisco packet tracer tools and learn about packets filters

```bash

```

---
