#!/bin/bash

# Set your local MySQL connection details here
export MYSQL_HOST="your-mysql-host"
export MYSQL_USER="your-mysql-user"
export MYSQL_PASSWORD="your-mysql-password"
export MYSQL_DATABASE="your-database"
export MYSQL_PORT="3306"

# Deploy using serverless
npx serverless deploy 