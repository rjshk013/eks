#!/bin/bash

# Configuration variables
GIT_REPO="https://your-git-repo-url.git"  # Replace with your repository URL
LOCAL_DIR="/path/to/airflow/dags"        # Path to the local directory where DAGs are stored
BRANCH="master"                          # Branch to sync

# Check if the local directory exists, if not, clone the repo
if [ ! -d "$LOCAL_DIR" ]; then
    echo "Cloning repository..."
    git clone -b $BRANCH $GIT_REPO $LOCAL_DIR
else
    echo "Updating repository..."
    cd $LOCAL_DIR
    git fetch origin
    git reset --hard origin/$BRANCH
    git clean -fd
fi

echo "Sync completed."
