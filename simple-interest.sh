#!/bin/bash

echo "Simple Interest Calculator"
echo "========================="

read -p "Enter principal amount: " principal
read -p "Enter rate of interest: " rate
read -p "Enter time period (years): " time

interest=$(echo "scale=2; $principal * $rate * $time / 100" | bc)
total=$(echo "scale=2; $principal + $interest" | bc)

echo "========================="
echo "Simple Interest: $interest"
echo "Total Amount: $total"
