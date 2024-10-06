# NOTE:
# 1. make sure to add ip address to security groups inbound rules (https://whatismyipaddress.com/)
# 2. make sure to increase volume in /dev/nvme0n1 (/dev/xvda) e.g. 100gb

# linux file formatting
# sudo yum install -y dos2unix 
# dos2unix ~/linux_docker_setup.sh 
# bash ~/linux_docker_setup.sh 

#-- EC2 Spot Instance Checks --#

# check available memory and cpu capacity
free -h
df -h
lscpu
# calculate percentage of used memory
free -m | awk 'FNR == 2 {print $3/($3+$4)*100}'

#-- Configure Permissions and Overcommit Settings --#

# reset premission for the /opt /dev /run and /sys directories
ls -larth /.
sudo chmod -R 777 /opt /dev /run /sys/fs/cgroup
sudo chmod 775 /var/run/screen
ls -larth /.
# mask permissoin for home docker file
sudo chmod 700 ~/.creds
sudo chmod 600 ~/.creds/*
# update overcommit memory setting
cat /proc/sys/vm/overcommit_memory
echo 1 | sudo tee /proc/sys/vm/overcommit_memory

#-- Increase EBS Volume --#

# verify that the root partition mounted under "/" is full (100%)
df -h
# gather details about your attached block devices
lsblk
lsblk -f
# mount the temporary file system tmpfs to the /tmp mount point
sudo mount -o size=10M,rw,nodev,nosuid -t tmpfs tmpfs /tmp
# Run the growpart command to grow the size of the root partition or partition 1
sudo growpart /dev/nvme0n1 1 
# Run the lsblk command to verify that partition 1 is expanded
lsblk
# Expand the file system
sudo xfs_growfs -d /
# file system on partition 1 is expanded
sudo resize2fs /dev/nvme0n1p1
# use the df -h command to verify that the OS can see the additional space
df -h
# Run the unmount command to unmount the tmpfs file system.
sudo umount /tmp

#-- Download Required Programmes --#

# update os
sudo yum update -y
# install required base software
sudo yum install -y htop vim tmux dos2unix docker git
# remove unneed dependencies
sudo yum autoremove

#-- Pull and Run Docker Contianer --#

# clone git repo for persistant data and folder structure
git clone https://github.com/oislen/RandomTelecomPayments.git --branch randomtelecompayments_prod_1.0 /home/$USER/RandomTelecomPayments
# login to docker
sudo gpasswd -a $USER 
sudo systemctl start docker
sudo chmod 666 /var/run/docker.sock
cat ~/.creds/docker | docker login --username oislen --password-stdin
# set docker constants
export DOCKER_IMAGE=oislen/randomtelecompayments:latest
export DOCKER_CONTAINER_NAME=rtp
# pull docker container
docker pull $DOCKER_IMAGE
# run pulled docker container
docker run --name $DOCKER_CONTAINER_NAME --memory 10GB --volume /home/$USER/RandomTelecomPayments/data:/home/ubuntu/RandomTelecomPayments/data --rm $DOCKER_IMAGE  --n_users 13000 --use_random_seed 1 --n_itr 2