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

LOG_FILE="pip_install.log"
PYTHON_PATH="/usr/bin/python3"
PATH_PY_URL="https://github.com/jaraco/path.git"
VENE_DIR="local_lib"
SMALL_PROGRAM="my_program.py"

# print 42_HEADER
echo "$BANNER"

# setup venv
$PYTHON_PATH -m venv $VENE_DIR
source $VENE_DIR/bin/activate

# pip version
python -m pip --version

# pip install
python -m pip install --log $LOG_FILE --force-reinstall git+$PATH_PY_URL

# execute the small program
echo "=============execute-output============="
python $SMALL_PROGRAM
