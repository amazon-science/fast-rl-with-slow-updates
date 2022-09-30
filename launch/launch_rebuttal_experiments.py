import os
import sys
import multiprocessing
import time





EC2_MACHINE_LIST = [
    "ec2-3-101-18-48.us-west-1.compute.amazonaws.com",
    "ec2-54-67-43-217.us-west-1.compute.amazonaws.com",
    "ec2-54-193-155-137.us-west-1.compute.amazonaws.com",
    "ec2-54-193-18-108.us-west-1.compute.amazonaws.com",
    "ec2-54-219-225-142.us-west-1.compute.amazonaws.com",
    "ec2-13-52-81-34.us-west-1.compute.amazonaws.com",
    "ec2-18-144-166-25.us-west-1.compute.amazonaws.com",
    "ec2-54-193-114-57.us-west-1.compute.amazonaws.com",
    "ec2-54-153-69-50.us-west-1.compute.amazonaws.com",
    "ec2-184-169-241-110.us-west-1.compute.amazonaws.com",
    "ec2-54-219-112-72.us-west-1.compute.amazonaws.com",
    "ec2-52-53-213-147.us-west-1.compute.amazonaws.com",
    "ec2-54-176-92-159.us-west-1.compute.amazonaws.com",
    "ec2-54-153-23-137.us-west-1.compute.amazonaws.com",
    "ec2-13-57-25-163.us-west-1.compute.amazonaws.com",
    "ec2-13-57-18-208.us-west-1.compute.amazonaws.com",
    "ec2-54-67-124-62.us-west-1.compute.amazonaws.com",
    "ec2-54-241-137-21.us-west-1.compute.amazonaws.com",
    "ec2-54-67-101-207.us-west-1.compute.amazonaws.com",
    "ec2-13-52-239-86.us-west-1.compute.amazonaws.com",
    "ec2-54-215-189-21.us-west-1.compute.amazonaws.com",
    "ec2-54-183-211-71.us-west-1.compute.amazonaws.com",
    "ec2-13-52-239-198.us-west-1.compute.amazonaws.com",
    "ec2-54-193-40-152.us-west-1.compute.amazonaws.com",
    "ec2-54-183-160-65.us-west-1.compute.amazonaws.com",
    "ec2-54-183-53-51.us-west-1.compute.amazonaws.com",
    "ec2-50-18-242-151.us-west-1.compute.amazonaws.com",
    "ec2-52-53-168-26.us-west-1.compute.amazonaws.com",
    "ec2-54-67-88-98.us-west-1.compute.amazonaws.com",
    "ec2-13-57-33-222.us-west-1.compute.amazonaws.com",
    "ec2-54-151-68-144.us-west-1.compute.amazonaws.com",
    "ec2-54-151-58-180.us-west-1.compute.amazonaws.com",
    "ec2-54-193-203-9.us-west-1.compute.amazonaws.com",
    "ec2-54-215-135-24.us-west-1.compute.amazonaws.com",
    "ec2-3-101-15-101.us-west-1.compute.amazonaws.com",
    "ec2-54-176-118-101.us-west-1.compute.amazonaws.com",
    "ec2-54-177-114-116.us-west-1.compute.amazonaws.com",
    "ec2-184-169-190-90.us-west-1.compute.amazonaws.com",
    "ec2-52-53-239-88.us-west-1.compute.amazonaws.com",
    "ec2-18-144-170-102.us-west-1.compute.amazonaws.com"
]

NUM_GPUS = 1 # number of gpus for each instance
KEY_PEM = '~/Desktop/AWS_keys/mirror_cali.pem'
C_LIST = [0.05, 0] # c values rainbow
C_LIST = [0.5, 0.2] # c values DQN
D_LIST = [0.005, 0] 
D_LIST = [0] 
#D_LIST = [0.05]
# get seeds to run
seed_list = [0,1]
N_LIST = [3]
MODEL_LIST = ['Rainbow'] # models
FULL_ENV_LIST = ['Asterix', 'Qbert', 'Breakout', 'Seaquest', 'Amidar',
                 'Kangaroo', 'BeamRider', 'Gopher', 'Phoenix', 'Zaxxon',
                 'Frostbite', 'StarGunner', 'TimePilot', 'Venture', 'WizardOfWor',
                 'AirRaid', 'Alien', 'Assault', 'Atlantis', 'BankHeist',
                 'BattleZone', 'Berzerk', 'Carnival', 'ChopperCommand', 'CrazyClimber',
                 'DemonAttack', 'YarsRevenge', 'VideoPinball', 'Tutankham', 'SpaceInvaders',
                 'Robotank', 'Riverraid', 'Pooyan', 'NameThisGame', 'MsPacman',
                 'KungFuMaster', 'Krull', 'Jamesbond',  'Gravitar', 'Enduro',
                 'FishingDerby', 'Freeway', 'Hero', 'JourneyEscape', 'MontezumaRevenge',
                 'Boxing', 'Pitfall', 'Pong', 'RoadRunner', 'UpNDown',
                 'Asteroids', 'Bowling', 'IceHockey', 'PrivateEye', 'Solaris'] # games

FULL_ENV_LIST = ['Phoenix', 'SpaceInvaders', 'Asterix', 'WizardOfWor', 'Gopher',
                 'Gravitar', 'Amidar', 'PrivateEye', 'Hero', 'Frostbite']

#FULL_ENV_LIST = ['Asterix']

def create_train_command():
    cmd_list = list()

    # exp counter
    cnt = 0

    # for each env
    for env in FULL_ENV_LIST:
        # for each model
        for model in MODEL_LIST:
            # get config file
            gin_file = "./dopamine/agents/{}/configs/{}_our_first_paper.gin".format(model.lower(), model.lower())

            # for each c
            for c in C_LIST:

                for d in D_LIST:

                    # for each n
                    for n in N_LIST:

                        # for each seed
                        for seed in seed_list:
                            tmp_list = []
                            # get gpu id
                            gpu_id = cnt % NUM_GPUS

                            base_dir = "./exp_{}_{}_c{}_d{}_n{}_trial{}".format(env, model.lower(), c, d, n, seed)
                            tmp_cmd  = "CUDA_VISIBLE_DEVICES={} python -um dopamine.discrete_domains.train".format(gpu_id)
                            tmp_cmd += " --base_dir {}".format(base_dir)
                            tmp_cmd += " --gin_files {}".format(gin_file)
                            tmp_cmd += " --gin_bindings {}Agent.mu={}".format(model, c)
                            tmp_cmd += " --gin_bindings {}Agent.nu={}".format(model, d)
                            tmp_cmd += " --gin_bindings {}Agent.update_horizon={}".format(model, n)
                            tmp_cmd += " --gin_bindings atari_lib.create_atari_environment.game_name='\"{}\"'".format(env)

                            tmp_list.append(tmp_cmd)
                            cmd_list.append(tmp_list)
                            cnt += 1

    for cmd in cmd_list:
        print(cmd)
    print("*********************")
    print("in total i have {} experiments".format(len(cmd_list)))
    print("*********************")
    if input("Are you sure?") == 'yes':
        pass
    else:
        assert False
    return cmd_list


# create scripts
def create_bash_script(ec2_instance, cnt, train_cmd_list, save_folder='./tmp'):
    # bash header
    header = '#!/usr/bin/env bash'

    # ec2 instance
    ec2_instance = ec2_instance.split('.')[0]

    # name
    file_name = ec2_instance + "_ProxIter_{}.sh".format(cnt)
    file_path = os.path.join(save_folder, file_name)

    # write script
    with open(file_path, 'w') as f:
        f.write(header + '\n')
        f.write('unzip -qq ./dopamine.zip \n')
        f.write('cd ./dopamine \n')
        f.write('source ~/anaconda3/etc/profile.d/conda.sh \n')
        f.write('conda activate tensorflow2_p38 \n')
        f.write("kill -9 $(nvidia-smi|grep python|awk {'print$5'}) \n")
        for train_cmd in train_cmd_list:
            f.write(train_cmd + '\n')
        f.close()
    return file_name, file_path

def run(KEY_PEM, ec2_machine, cnt, NUM_GPUS, train_cmd_list):

    delete_cmd =   'ssh -i {} -o StrictHostKeyChecking=no -T ubuntu@{} "rm -rf ./ec2* &"'.format(KEY_PEM, ec2_machine)
    if os.system(delete_cmd) != 0:
        print("FAILED --> ", delete_cmd)
    else:
        print(" erased existing bash file")

    # create script
    script_name, script_path = create_bash_script(ec2_machine, cnt % NUM_GPUS, train_cmd_list)
    send_cmd = 'scp -i {} -o StrictHostKeyChecking=no {} ubuntu@{}:~/'.format(KEY_PEM, script_path, ec2_machine)
    if os.system(send_cmd) != 0:
        print("FAILED --> ", send_cmd)
    else:
        print('{} copied: '.format(cnt), script_name)


    delete_cmd =   'ssh -i {} -o StrictHostKeyChecking=no -T ubuntu@{} "rm -rf ./dopamine/* &"'.format(KEY_PEM, ec2_machine)
    if os.system(delete_cmd) != 0:
        print("FAILED --> ", delete_cmd)
    else:
        print(" erased existing dopamine stuff")


    send_code_cmd = 'scp -i {} -o StrictHostKeyChecking=no {} ubuntu@{}:~/'.format(KEY_PEM, './tmp/dopamine.zip', ec2_machine)
    if os.system(send_code_cmd) != 0:
        print("FAILED --> ", send_code_cmd)
    else:
        print('{} copied code: '.format(cnt), script_name)


    # run cmd
    run_cmd = 'ssh -i {} -o StrictHostKeyChecking=no -T ubuntu@{} "nohup bash ~/{}  &> ./mylog.log & "'.format(KEY_PEM, ec2_machine, script_name)
    if os.system(run_cmd) != 0:
        print("FAILED --> ", run_cmd)
    else:
        print('{} run: '.format(cnt), script_name)


if __name__ == "__main__":
    num_machines = len(EC2_MACHINE_LIST)
    print("*********************")
    print("in total i have {} machines".format(num_machines))
    print("*********************")
    '''
    if len(EC2_MACHINE_LIST) < 1:
        print("at least one machine")
        exit()
    else:
        for ec2_machine in EC2_MACHINE_LIST:
            os.system('ssh-keyscan {} >> $HOME/.ssh/known_hosts'.format(ec2_machine))
    '''

    # create cmd list
    full_train_cmd_list = create_train_command()
    if input("did you commit code? ") == 'yes':
        pass
    else:
        assert False

    # get dopamine code
    os.system("rm -rf ./tmp/dopamine")
    os.system("mkdir ./tmp/dopamine")
    os.system("git clone https://gitlab.aws.dev/kavasadi/dopamine.git  ./tmp/dopamine")
    os.system("rm -rf ./tmp/dopamine/.git")
    os.system("cd ./tmp && zip -qq -r dopamine dopamine && cd ..")
    os.system("rm -rf ./tmp/dopamine")
    #assert False



    # # for each command
    process_list = []
    for cnt, train_cmd_list in enumerate(full_train_cmd_list):
        ec2_machine = EC2_MACHINE_LIST[cnt // NUM_GPUS]
        #run(KEY_PEM, ec2_machine, cnt, NUM_GPUS, train_cmd_list)
        p =  multiprocessing.Process(target= run, 
                                     args = (KEY_PEM, ec2_machine, cnt, NUM_GPUS, train_cmd_list))
        p.start()
        time.sleep(.1)
        process_list.append(p)
    for process in process_list:
        process.join()

