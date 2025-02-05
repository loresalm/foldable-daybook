#!/bin/bash

# Execute the Python script
echo "Running calendar generator script ..."
python3 calendar_generator.py

# Check if the Python script completed successfully
if [ $? -eq 0 ]; then
    echo "foldable_daybook.pdf completed successfully."
else
    echo "foldable_daybook.pdf. encountered an error" >&2
fi

exit 0