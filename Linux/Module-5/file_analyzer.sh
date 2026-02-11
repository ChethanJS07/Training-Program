#!/usr/bin/env bash

ERROR_LOG="errors.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

print_help() {
    cat << EOF
Usage: $0 [OPTIONS]

A script that demonstrates command-line argument parsing with getopts.

Options:
  -d, --directory DIR   Print files containing a keyword in the directory and its sub directories
  -k, --keyword KEY     Keyword to be searched (REQUIRED with -d or -f)
  -f, --file FILE       Check if the keyword is present in the file
  -h, --help            Show this help message and exit

Examples:
  $0 -d /home/user -k "search term"   # Search directory
  $0 -f data.txt -k "search term"     # Search single file
  $0 --help

EOF
    exit 0
}

log_error() {
    local error_msg="$1"
    echo "[$TIMESTAMP] ERROR: $error_msg" | tee -a "$ERROR_LOG" >&2
}

log_warning() {
    local warning_msg="$1"
    echo "[$TIMESTAMP] WARNING: $warning_msg" | tee -a "$ERROR_LOG" >&2
}

log_info() {
    local info_msg="$1"
    echo "[$TIMESTAMP] INFO: $info_msg" >> "$ERROR_LOG"
}

recursive_search() {
    local DIR="$1"
    local KEYWORD="$2"
    
    if [[ ! -d "$DIR" ]]; then
        log_error "Directory '$DIR' does not exist or is not accessible."
        return 1
    fi
    
    if [[ ! -r "$DIR" ]]; then
        log_error "No read permission for directory '$DIR'."
        return 1
    fi
    
    if [[ -z "$KEYWORD" ]]; then
        log_error "Keyword is empty for directory search."
        return 1
    fi
    
    echo "Files in $DIR with the keyword '$KEYWORD': "
    
    log_info "Starting search in '$DIR' for keyword '$KEYWORD'"
    
    find "$DIR" -type f -exec grep -il "$KEYWORD" {} \; 2>> "$ERROR_LOG"
    
    local find_exit_code=$?
    if [[ $find_exit_code -ne 0 ]]; then
        log_warning "find command exited with code $find_exit_code"
    fi
    
    log_info "Search completed in '$DIR'"
}

single_file_search() {
    local FILE="$1"
    local KEYWORD="$2"
    
    if [[ ! -f "$FILE" ]]; then
        log_error "File '$FILE' does not exist."
        return 1
    fi
    
    if [[ ! -r "$FILE" ]]; then
        log_error "No read permission for file '$FILE'."
        return 1
    fi
    
    if [[ -z "$KEYWORD" ]]; then
        log_error "Keyword is empty for file search."
        return 1
    fi
    
    log_info "Searching file '$FILE' for keyword '$KEYWORD'"
    
    echo "Searching file '$FILE' for keyword '$KEYWORD': "
    
    if grep -iq "$KEYWORD" "$FILE" 2>> "$ERROR_LOG"; then
        echo "✓ Keyword found in '$FILE'"
        log_info "Keyword found in '$FILE'"
        grep -in "$KEYWORD" "$FILE" 2>> "$ERROR_LOG"
    else
        echo "✗ Keyword not found in '$FILE'"
        log_info "Keyword not found in '$FILE'"
    fi
}

main() {
    log_info "Script started with arguments: $*"
    
    DIRECTORY=""
    FILE_NAME=""
    KEYWORD=""
    
    for arg in "$@"; do
        case "$arg" in
            --help|-h)
                print_help
                ;;
        esac
    done
    
    while getopts "d:k:f:h" opt; do
        case $opt in
            d)
                DIRECTORY="$OPTARG"
                log_info "Directory set to: $DIRECTORY"
                ;;
            k)
                KEYWORD="$OPTARG"
                log_info "Keyword set to: $KEYWORD"
                ;;
            f)
                FILE_NAME="$OPTARG"
                log_info "File set to: $FILE_NAME"
                ;;
            h)
                print_help
                ;;
            :)
                log_error "Option -$OPTARG requires an argument."
                echo "Error: Option -$OPTARG requires an argument." >&2
                print_help
                ;;
            \?)
                log_error "Invalid option: -$OPTARG"
                echo "Error: Invalid option: -$OPTARG" >&2
                print_help
                ;;
        esac
    done
    
    if [[ -n "$DIRECTORY" ]] && [[ -n "$FILE_NAME" ]]; then
        log_error "Cannot use both -d and -f options simultaneously."
        echo "Error: Cannot use both -d and -f options simultaneously." >&2
        print_help
    fi
    
    if [[ -z "$KEYWORD" ]]; then
        log_error "Keyword (-k) is required."
        echo "Error: Keyword (-k) is required." >&2
        print_help
    fi
    
    if [[ -n "$DIRECTORY" ]]; then
        recursive_search "$DIRECTORY" "$KEYWORD"
    elif [[ -n "$FILE_NAME" ]]; then
        single_file_search "$FILE_NAME" "$KEYWORD"
    else
        log_error "Either -d (directory) or -f (file) must be specified."
        echo "Error: Either -d (directory) or -f (file) must be specified." >&2
        print_help
    fi
    
    if [[ -s "$ERROR_LOG" ]]; then
        echo -e "\n--- Errors/Warnings were logged to '$ERROR_LOG' ---"
        echo "Last few lines of error log:"
        tail -5 "$ERROR_LOG" | sed 's/^/  /'
    else
        log_info "Script completed successfully"
        echo -e "\n✓ Script completed successfully (no errors)"
    fi
}

main "$@"
