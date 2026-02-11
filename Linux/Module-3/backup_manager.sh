#!/usr/bin/env bash

if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <source_dir> <backup_dir> <file_extension>"
  exit 1
fi

SRC_DIR=$1
SRC_DIR="${SRC_DIR%/}"
SRC_DIR="${SRC_DIR/#\~/$HOME}"

if [ ! -d "$SRC_DIR" ]; then
  echo "Error: Source directory doesn't exist!"
  exit 1
fi

BACKUP_DIR=$2
BACKUP_DIR="${BACKUP_DIR%/}"
BACKUP_DIR="${BACKUP_DIR/#\~/$HOME}"

if [ ! -d "$BACKUP_DIR" ]; then 
  echo "Backup directory doesn't exist. Creating $BACKUP_DIR ..."
  if ! mkdir -p "$BACKUP_DIR"; then
    echo "Failed to create backup directory $BACKUP_DIR";
    exit 1;
  fi
fi

FILE_EXT=$3

shopt -s nullglob # this makes sure that it returns nothing if no files match
SRC_FILES=("$SRC_DIR"/*"$FILE_EXT")

if [ ${#SRC_FILES[@]} -eq 0 ]; then
  echo "No matching $FILE_EXT files in $SRC_DIR"
  exit 0
fi

export BACKUP_COUNT=0
export COPIED_SIZE=0
TOTAL_SIZE=0

echo "Files to be backed up: "
echo -e "File Name --> \tSize"
for file in "${SRC_FILES[@]}"; do
  size=$(stat -c %s "$file")
  hum_read_size=$(numfmt --to=iec --suffix=B "$size")
  TOTAL_SIZE=$((TOTAL_SIZE+size))
  echo -e "$(basename "$file") -->\t $hum_read_size"
done
echo "Total backup size : $TOTAL_SIZE bytes"

echo
echo "Starting backup..."

for file in "${SRC_FILES[@]}"; do
  filename=$(basename "$file")
  dest="$BACKUP_DIR/$filename"

  if [ -f "$dest" ]; then
    if [ "$file" -nt "$dest" ]; then
      cp -p "$file" "$dest"
      echo "Updated: $filename"
      size=$(stat -c %s "$file")
      COPIED_SIZE=$((COPIED_SIZE+size))
      BACKUP_COUNT=$((BACKUP_COUNT+1))
    else
      echo "Skipped (up-to-date): $filename"
    fi
  else
    cp -p "$file" "$dest"
    echo "Copied: $filename"
    size=$(stat -c %s "$file")
    COPIED_SIZE=$((COPIED_SIZE+size))
    BACKUP_COUNT=$((BACKUP_COUNT+1))
  fi
done
 
REPORT_FILE="$BACKUP_DIR/backup_report.log"

{
  echo "====================="
  echo "Backup Summary Report"
  echo "====================="
  echo "Source directory: $SRC_DIR"
  echo "Backed up files: $FILE_EXT"
  echo "Backup directory: $BACKUP_DIR"
  echo "Total number of files backed up: $BACKUP_COUNT"
  echo "Total size of backup: $(numfmt --to=iec --suffix=B "$COPIED_SIZE")"
  echo "Time: $(date)"
  echo
} >> "$REPORT_FILE"


echo "Backup complete. Report added to $REPORT_FILE"
