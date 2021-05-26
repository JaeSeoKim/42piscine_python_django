#!/bin/bash

BANNER="$(
  cat <<-EOF
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_script.sh                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaeskim <jaeskim@student.42seoul.kr>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    install path.py with pip!                         #+#    #+#              #
#                                                     ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
EOF
)"

LOG_FILE="my_script.log"
PYTHON_PATH="/usr/bin/python3"
PATH_PY_URL="https://github.com/jaraco/path.git"
VENE_DIR="local_lib"
SMALL_PROGRAM="my_program.py"

# print 42_HEADER
echo "$BANNER" | tee $LOG_FILE

# setup venv
$PYTHON_PATH -m venv $VENE_DIR | tee -a $LOG_FILE
source $VENE_DIR/bin/activate

# pip version
python -m pip --version | tee -a $LOG_FILE

# pip install
python -m pip install --force-reinstall git+$PATH_PY_URL | tee -a $LOG_FILE

# execute the small program
echo "=============execute-output=============" | tee -a $LOG_FILE
python $SMALL_PROGRAM | tee -a $LOG_FILE
