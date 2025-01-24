import platform
import os
import sys
import json

root_dir = 'E:\\GitHub\\RandomTelecomPayments' if platform.system() == 'Windows' else '/home/ubuntu/RandomTelecomPayments'
sys.path.append(root_dir)
# set directories
creds_data = os.path.join(root_dir, '.creds')
ec2_ref_data_dir = os.path.join(root_dir, "aws", "ref")
session_token_fpath = os.path.join(creds_data, "sessionToken.json")
launch_template_config_fpath = os.path.join(ec2_ref_data_dir, "launch_template_config.json")
create_fleet_config_fpath = os.path.join(ec2_ref_data_dir, "create_fleet_config.json")
run_instances_config_fpath = os.path.join(ec2_ref_data_dir, "run_instances_config.json")

# load aws ec2 references
with open(launch_template_config_fpath) as json_file: 
    launch_template_config = json.load(json_file)
with open(create_fleet_config_fpath) as json_file: 
    create_fleet_config = json.load(json_file)
with open(run_instances_config_fpath) as json_file: 
    run_instances_config = json.load(json_file)
