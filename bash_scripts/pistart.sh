#crontab -e
@reboot  /Test_Stand_Control/Bash_Scripts/PiStart.sh

#!/bin/bash

clear

echo "PI startup!"

echo "If you're running the test for real, you shouldn't be reading this"

curr_date =`date "+%Y-%m-%d-%H:%M:%S"`

echo "datecheck:"
echo $curr_date

python3 runtest.py
