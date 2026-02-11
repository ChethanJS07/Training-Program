# Module 4 Assignment

#### Output of the following commands can be found here:

Drive link : [Output](https://drive.google.com/drive/folders/1iKSC0BHvJyZ9Z9eEBMAjtgX5azbfvhzd?usp=sharing)

---

### For the attached file, write a bash script which should take the file as input and have to go through it line by line and need to generate an output file (say output.txt) with listings of following parameters fetched from the input file.

Attached File: [Link](https://embedur-my.sharepoint.com/:t:/p/sharath_s/ERgQgXKs78JLoq79V9hBV44B0f2Cmh7o0qEsHY4yQ6SHSg?e=Eqa4dp)

Requirements:

1. Params expected to be fetched from input.txt file : "frame.time", "wlan.fc.type", "wlan.fc.subtype"

2. Sample output expected in output.txt:

   "frame.time": "Nov 14, 2024 11:44:48.219200000 India Standard Time",
   "wlan.fc.type": "1",
   "wlan.fc.subtype": "9"
   "frame.time": "Nov 14, 2024 11:44:48.219208000 India Standard Time",
   "wlan.fc.type": "0",
   "wlan.fc.subtype": "1",
   and so on.

```bash
#!/usr/bin/env bash

if [ $# -ne 1 ]; then
  echo "Input file not found!"
  echo "Usage: $0 <input_file>"
  exit 1
fi

INPUT_FILE=$1
OUTPUT_FILE="output.txt"

if [ ! -f $INPUT_FILE ]; then
  echo "File not found!"
  exit 1
fi

paste -d '\n' <(grep -w "frame.time" "$INPUT_FILE") <(grep -w "wlan.fc.type" "$INPUT_FILE") <(grep -w "wlan.fc.subtype" "$INPUT_FILE") > "$OUTPUT_FILE"
```

```bash
# verify output
cat output.txt
```

---
