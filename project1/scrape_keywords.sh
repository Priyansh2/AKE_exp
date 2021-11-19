#!/bin/bash
#SBATCH -A research
#SBATCH -n 5
#SBATCH --qos=medium
#SBATCH -p long
#SBATCH --gres=gpu:0
#SBATCH --mem-per-cpu=3G
#SBATCH --time=4-00:00:00

ruby /home/$USER/project1/scrap_blogs.rb
