import os
import sys
import multiprocessing
import time





EC2_MACHINE_LIST = [
    "ec2-18-144-20-170.us-west-1.compute.amazonaws.com",
    "ec2-54-177-160-227.us-west-1.compute.amazonaws.com",
    "ec2-13-56-160-186.us-west-1.compute.amazonaws.com",
    "ec2-18-144-31-248.us-west-1.compute.amazonaws.com",
    "ec2-54-215-254-231.us-west-1.compute.amazonaws.com",
    "ec2-13-57-235-221.us-west-1.compute.amazonaws.com",
    "ec2-54-215-56-167.us-west-1.compute.amazonaws.com",
    "ec2-50-18-16-163.us-west-1.compute.amazonaws.com",
    "ec2-3-101-108-138.us-west-1.compute.amazonaws.com",
    "ec2-18-144-65-242.us-west-1.compute.amazonaws.com",
    "ec2-54-193-85-222.us-west-1.compute.amazonaws.com",
    "ec2-54-151-36-50.us-west-1.compute.amazonaws.com",
    "ec2-54-219-244-0.us-west-1.compute.amazonaws.com",
    "ec2-54-219-198-174.us-west-1.compute.amazonaws.com",
    "ec2-52-53-178-153.us-west-1.compute.amazonaws.com",
    "ec2-54-153-104-29.us-west-1.compute.amazonaws.com",
    "ec2-54-153-31-79.us-west-1.compute.amazonaws.com",
    "ec2-54-176-3-224.us-west-1.compute.amazonaws.com",
    "ec2-13-56-13-80.us-west-1.compute.amazonaws.com",
    "ec2-54-219-94-191.us-west-1.compute.amazonaws.com",
    "ec2-13-56-19-212.us-west-1.compute.amazonaws.com",
    "ec2-18-144-54-64.us-west-1.compute.amazonaws.com",
    "ec2-3-101-64-114.us-west-1.compute.amazonaws.com",
    "ec2-54-215-223-113.us-west-1.compute.amazonaws.com",
    "ec2-54-176-9-149.us-west-1.compute.amazonaws.com",
    "ec2-52-53-255-65.us-west-1.compute.amazonaws.com",
    "ec2-54-193-31-115.us-west-1.compute.amazonaws.com",
    "ec2-13-56-59-105.us-west-1.compute.amazonaws.com",
    "ec2-204-236-162-192.us-west-1.compute.amazonaws.com",
    "ec2-54-176-124-181.us-west-1.compute.amazonaws.com",
    "ec2-13-57-49-210.us-west-1.compute.amazonaws.com",
    "ec2-54-183-180-46.us-west-1.compute.amazonaws.com",
    "ec2-54-219-0-196.us-west-1.compute.amazonaws.com",
    "ec2-18-144-40-234.us-west-1.compute.amazonaws.com",
    "ec2-54-219-234-216.us-west-1.compute.amazonaws.com",
    "ec2-3-101-68-98.us-west-1.compute.amazonaws.com",
    "ec2-54-219-209-67.us-west-1.compute.amazonaws.com",
    "ec2-13-56-251-233.us-west-1.compute.amazonaws.com",
    "ec2-52-8-240-194.us-west-1.compute.amazonaws.com",
    "ec2-13-57-236-175.us-west-1.compute.amazonaws.com",
    "ec2-54-67-122-101.us-west-1.compute.amazonaws.com",
    "ec2-54-176-97-124.us-west-1.compute.amazonaws.com",
    "ec2-3-101-191-151.us-west-1.compute.amazonaws.com",
    "ec2-54-176-191-27.us-west-1.compute.amazonaws.com",
    "ec2-184-72-7-194.us-west-1.compute.amazonaws.com",
    "ec2-18-144-70-105.us-west-1.compute.amazonaws.com",
    "ec2-13-57-234-45.us-west-1.compute.amazonaws.com",
    "ec2-54-151-8-209.us-west-1.compute.amazonaws.com",
    "ec2-54-176-227-162.us-west-1.compute.amazonaws.com",
    "ec2-54-67-69-203.us-west-1.compute.amazonaws.com",
    "ec2-13-56-252-81.us-west-1.compute.amazonaws.com",
    "ec2-54-176-144-115.us-west-1.compute.amazonaws.com",
    "ec2-54-177-134-239.us-west-1.compute.amazonaws.com",
    "ec2-54-193-220-3.us-west-1.compute.amazonaws.com",
    "ec2-13-57-230-82.us-west-1.compute.amazonaws.com",
    "ec2-52-53-237-197.us-west-1.compute.amazonaws.com",
    "ec2-13-56-191-24.us-west-1.compute.amazonaws.com",
    "ec2-54-193-203-151.us-west-1.compute.amazonaws.com",
    "ec2-54-177-17-9.us-west-1.compute.amazonaws.com",
    "ec2-54-219-177-161.us-west-1.compute.amazonaws.com",
    "ec2-3-101-61-208.us-west-1.compute.amazonaws.com",
    "ec2-50-18-7-152.us-west-1.compute.amazonaws.com",
    "ec2-54-241-106-230.us-west-1.compute.amazonaws.com",
    "ec2-54-176-15-161.us-west-1.compute.amazonaws.com",
    "ec2-54-215-84-132.us-west-1.compute.amazonaws.com",
    "ec2-54-215-44-170.us-west-1.compute.amazonaws.com",
    "ec2-54-219-161-78.us-west-1.compute.amazonaws.com",
    "ec2-54-176-192-206.us-west-1.compute.amazonaws.com",
    "ec2-204-236-162-102.us-west-1.compute.amazonaws.com",
    "ec2-54-215-132-172.us-west-1.compute.amazonaws.com",
    "ec2-52-53-130-142.us-west-1.compute.amazonaws.com",
    "ec2-13-56-164-133.us-west-1.compute.amazonaws.com",
    "ec2-54-183-173-181.us-west-1.compute.amazonaws.com",
    "ec2-54-176-102-66.us-west-1.compute.amazonaws.com",
    "ec2-3-101-104-87.us-west-1.compute.amazonaws.com",
    "ec2-13-57-27-70.us-west-1.compute.amazonaws.com",
    "ec2-54-193-66-193.us-west-1.compute.amazonaws.com",
    "ec2-54-193-220-253.us-west-1.compute.amazonaws.com",
    "ec2-54-67-88-146.us-west-1.compute.amazonaws.com",
    "ec2-50-18-6-8.us-west-1.compute.amazonaws.com",
    "ec2-13-57-20-29.us-west-1.compute.amazonaws.com",
    "ec2-54-177-74-14.us-west-1.compute.amazonaws.com",
    "ec2-54-193-138-94.us-west-1.compute.amazonaws.com",
    "ec2-54-151-59-156.us-west-1.compute.amazonaws.com",
    "ec2-13-56-195-254.us-west-1.compute.amazonaws.com",
    "ec2-50-18-136-40.us-west-1.compute.amazonaws.com",
    "ec2-54-219-121-121.us-west-1.compute.amazonaws.com",
    "ec2-50-18-102-20.us-west-1.compute.amazonaws.com",
    "ec2-54-215-252-46.us-west-1.compute.amazonaws.com",
    "ec2-54-183-63-78.us-west-1.compute.amazonaws.com",
    "ec2-18-144-19-185.us-west-1.compute.amazonaws.com",
    "ec2-54-219-94-253.us-west-1.compute.amazonaws.com",
    "ec2-13-56-226-235.us-west-1.compute.amazonaws.com",
    "ec2-54-183-241-193.us-west-1.compute.amazonaws.com",
    "ec2-54-183-166-242.us-west-1.compute.amazonaws.com",
    "ec2-13-57-58-209.us-west-1.compute.amazonaws.com",
    "ec2-54-215-252-64.us-west-1.compute.amazonaws.com",
    "ec2-13-57-243-26.us-west-1.compute.amazonaws.com",
    "ec2-52-53-237-162.us-west-1.compute.amazonaws.com",
    "ec2-54-183-73-252.us-west-1.compute.amazonaws.com",
    "ec2-54-215-60-118.us-west-1.compute.amazonaws.com",
    "ec2-13-56-149-249.us-west-1.compute.amazonaws.com",
    "ec2-18-144-45-214.us-west-1.compute.amazonaws.com",
    "ec2-54-215-205-232.us-west-1.compute.amazonaws.com",
    "ec2-54-177-7-123.us-west-1.compute.amazonaws.com",
    "ec2-54-177-244-85.us-west-1.compute.amazonaws.com",
    "ec2-54-176-88-246.us-west-1.compute.amazonaws.com",
    "ec2-54-219-68-255.us-west-1.compute.amazonaws.com",
    "ec2-54-177-23-224.us-west-1.compute.amazonaws.com",
    "ec2-13-57-220-171.us-west-1.compute.amazonaws.com",
    "ec2-54-176-79-20.us-west-1.compute.amazonaws.com",
    "ec2-204-236-150-142.us-west-1.compute.amazonaws.com",
    "ec2-18-144-16-230.us-west-1.compute.amazonaws.com",
    "ec2-13-57-188-196.us-west-1.compute.amazonaws.com",
    "ec2-54-193-34-222.us-west-1.compute.amazonaws.com",
    "ec2-13-56-180-98.us-west-1.compute.amazonaws.com",
    "ec2-54-215-255-42.us-west-1.compute.amazonaws.com",
    "ec2-54-176-142-6.us-west-1.compute.amazonaws.com",
    "ec2-3-101-102-32.us-west-1.compute.amazonaws.com",
    "ec2-13-57-220-203.us-west-1.compute.amazonaws.com",
    "ec2-54-215-254-188.us-west-1.compute.amazonaws.com",
    "ec2-54-219-143-226.us-west-1.compute.amazonaws.com",
    "ec2-18-144-50-110.us-west-1.compute.amazonaws.com",
    "ec2-54-193-134-146.us-west-1.compute.amazonaws.com",
    "ec2-13-56-252-122.us-west-1.compute.amazonaws.com",
    "ec2-54-215-71-193.us-west-1.compute.amazonaws.com",
    "ec2-3-101-60-16.us-west-1.compute.amazonaws.com",
    "ec2-54-219-225-219.us-west-1.compute.amazonaws.com",
    "ec2-54-183-206-39.us-west-1.compute.amazonaws.com",
    "ec2-54-193-83-82.us-west-1.compute.amazonaws.com",
    "ec2-13-57-51-80.us-west-1.compute.amazonaws.com",
    "ec2-52-53-240-54.us-west-1.compute.amazonaws.com",
    "ec2-54-193-227-248.us-west-1.compute.amazonaws.com",
    "ec2-54-215-27-183.us-west-1.compute.amazonaws.com",
    "ec2-54-176-104-54.us-west-1.compute.amazonaws.com",
    "ec2-54-193-212-138.us-west-1.compute.amazonaws.com",
    "ec2-50-18-141-228.us-west-1.compute.amazonaws.com",
    "ec2-13-56-249-56.us-west-1.compute.amazonaws.com",
    "ec2-18-144-34-153.us-west-1.compute.amazonaws.com",
    "ec2-18-144-11-1.us-west-1.compute.amazonaws.com",
    "ec2-13-57-191-240.us-west-1.compute.amazonaws.com",
    "ec2-54-215-124-145.us-west-1.compute.amazonaws.com",
    "ec2-18-144-21-162.us-west-1.compute.amazonaws.com",
    "ec2-18-144-50-21.us-west-1.compute.amazonaws.com",
    "ec2-54-183-35-230.us-west-1.compute.amazonaws.com",
    "ec2-54-241-233-87.us-west-1.compute.amazonaws.com",
    "ec2-13-57-242-153.us-west-1.compute.amazonaws.com",
    "ec2-54-183-183-242.us-west-1.compute.amazonaws.com",
    "ec2-54-67-14-67.us-west-1.compute.amazonaws.com",
    "ec2-54-193-129-103.us-west-1.compute.amazonaws.com",
    "ec2-54-215-230-92.us-west-1.compute.amazonaws.com",
    "ec2-13-56-81-5.us-west-1.compute.amazonaws.com",
    "ec2-54-215-215-203.us-west-1.compute.amazonaws.com",
    "ec2-54-176-240-105.us-west-1.compute.amazonaws.com",
    "ec2-13-56-184-234.us-west-1.compute.amazonaws.com",
    "ec2-54-177-237-124.us-west-1.compute.amazonaws.com",
    "ec2-184-169-253-235.us-west-1.compute.amazonaws.com",
    "ec2-54-176-254-139.us-west-1.compute.amazonaws.com",
    "ec2-54-177-243-64.us-west-1.compute.amazonaws.com",
    "ec2-54-215-108-149.us-west-1.compute.amazonaws.com",
    "ec2-18-144-60-215.us-west-1.compute.amazonaws.com",
    "ec2-54-183-226-118.us-west-1.compute.amazonaws.com",
    "ec2-54-177-71-126.us-west-1.compute.amazonaws.com",
    "ec2-3-101-30-251.us-west-1.compute.amazonaws.com",
    "ec2-54-193-47-251.us-west-1.compute.amazonaws.com",
    "ec2-13-56-232-188.us-west-1.compute.amazonaws.com",
    "ec2-54-176-210-16.us-west-1.compute.amazonaws.com",
    "ec2-54-241-109-32.us-west-1.compute.amazonaws.com",
    "ec2-13-56-248-248.us-west-1.compute.amazonaws.com",
    "ec2-50-18-41-52.us-west-1.compute.amazonaws.com",
    "ec2-18-144-41-58.us-west-1.compute.amazonaws.com",
    "ec2-54-241-214-153.us-west-1.compute.amazonaws.com",
    "ec2-13-56-13-1.us-west-1.compute.amazonaws.com",
    "ec2-13-56-180-142.us-west-1.compute.amazonaws.com",
    "ec2-13-57-6-231.us-west-1.compute.amazonaws.com",
    "ec2-54-219-55-41.us-west-1.compute.amazonaws.com",
    "ec2-54-176-50-60.us-west-1.compute.amazonaws.com",
    "ec2-52-53-125-29.us-west-1.compute.amazonaws.com",
    "ec2-54-176-164-236.us-west-1.compute.amazonaws.com",
    "ec2-54-241-59-97.us-west-1.compute.amazonaws.com",
    "ec2-54-177-112-140.us-west-1.compute.amazonaws.com",
    "ec2-54-219-148-137.us-west-1.compute.amazonaws.com",
    "ec2-54-67-52-215.us-west-1.compute.amazonaws.com",
    "ec2-13-57-188-45.us-west-1.compute.amazonaws.com",
    "ec2-13-57-230-45.us-west-1.compute.amazonaws.com",
    "ec2-18-144-47-107.us-west-1.compute.amazonaws.com",
    "ec2-54-219-40-171.us-west-1.compute.amazonaws.com",
    "ec2-18-144-36-222.us-west-1.compute.amazonaws.com",
    "ec2-54-219-36-94.us-west-1.compute.amazonaws.com",
    "ec2-13-56-159-144.us-west-1.compute.amazonaws.com",
    "ec2-18-144-19-130.us-west-1.compute.amazonaws.com",
    "ec2-54-215-214-72.us-west-1.compute.amazonaws.com",
    "ec2-54-183-175-108.us-west-1.compute.amazonaws.com",
    "ec2-54-177-119-4.us-west-1.compute.amazonaws.com",
    "ec2-54-219-46-37.us-west-1.compute.amazonaws.com",
    "ec2-13-56-236-84.us-west-1.compute.amazonaws.com",
    "ec2-18-144-38-212.us-west-1.compute.amazonaws.com",
    "ec2-54-193-63-38.us-west-1.compute.amazonaws.com",
    "ec2-13-56-161-252.us-west-1.compute.amazonaws.com",
    "ec2-54-241-111-144.us-west-1.compute.amazonaws.com",
    "ec2-54-176-214-94.us-west-1.compute.amazonaws.com",
    "ec2-54-183-22-233.us-west-1.compute.amazonaws.com",
    "ec2-54-176-151-164.us-west-1.compute.amazonaws.com",
    "ec2-54-215-219-239.us-west-1.compute.amazonaws.com",
    "ec2-52-53-231-237.us-west-1.compute.amazonaws.com",
    "ec2-54-176-218-10.us-west-1.compute.amazonaws.com",
    "ec2-54-215-203-209.us-west-1.compute.amazonaws.com",
    "ec2-54-153-92-249.us-west-1.compute.amazonaws.com",
    "ec2-54-176-7-0.us-west-1.compute.amazonaws.com",
    "ec2-54-183-113-5.us-west-1.compute.amazonaws.com",
    "ec2-52-53-226-225.us-west-1.compute.amazonaws.com",
    "ec2-54-219-173-176.us-west-1.compute.amazonaws.com",
    "ec2-52-53-230-38.us-west-1.compute.amazonaws.com",
    "ec2-54-177-184-17.us-west-1.compute.amazonaws.com",
    "ec2-54-183-71-45.us-west-1.compute.amazonaws.com",
    "ec2-13-57-6-180.us-west-1.compute.amazonaws.com",
    "ec2-54-193-178-105.us-west-1.compute.amazonaws.com",
    "ec2-54-193-43-246.us-west-1.compute.amazonaws.com",
    "ec2-54-219-183-57.us-west-1.compute.amazonaws.com",
    "ec2-54-176-219-240.us-west-1.compute.amazonaws.com",
    "ec2-18-144-35-125.us-west-1.compute.amazonaws.com",
    "ec2-54-177-118-208.us-west-1.compute.amazonaws.com",
    "ec2-3-101-127-248.us-west-1.compute.amazonaws.com",
    "ec2-13-56-210-196.us-west-1.compute.amazonaws.com",
    "ec2-50-18-142-253.us-west-1.compute.amazonaws.com",
    "ec2-54-219-183-152.us-west-1.compute.amazonaws.com",
    "ec2-54-219-11-175.us-west-1.compute.amazonaws.com",
    "ec2-50-18-78-205.us-west-1.compute.amazonaws.com",
    "ec2-54-219-253-154.us-west-1.compute.amazonaws.com",
    "ec2-54-176-153-38.us-west-1.compute.amazonaws.com",
    "ec2-18-144-69-56.us-west-1.compute.amazonaws.com",
    "ec2-54-219-247-71.us-west-1.compute.amazonaws.com",
    "ec2-54-219-208-105.us-west-1.compute.amazonaws.com",
    "ec2-54-193-114-255.us-west-1.compute.amazonaws.com",
    "ec2-13-57-240-241.us-west-1.compute.amazonaws.com",
    "ec2-54-193-80-188.us-west-1.compute.amazonaws.com",
    "ec2-50-18-81-242.us-west-1.compute.amazonaws.com",
    "ec2-18-144-68-255.us-west-1.compute.amazonaws.com",
    "ec2-13-56-181-27.us-west-1.compute.amazonaws.com",
    "ec2-54-241-67-147.us-west-1.compute.amazonaws.com",
    "ec2-54-153-44-153.us-west-1.compute.amazonaws.com",
    "ec2-54-215-254-120.us-west-1.compute.amazonaws.com",
    "ec2-184-72-20-223.us-west-1.compute.amazonaws.com",
    "ec2-54-153-61-253.us-west-1.compute.amazonaws.com",
    "ec2-13-56-160-112.us-west-1.compute.amazonaws.com",
    "ec2-54-219-83-213.us-west-1.compute.amazonaws.com",
    "ec2-54-193-113-105.us-west-1.compute.amazonaws.com",
    "ec2-54-215-251-250.us-west-1.compute.amazonaws.com",
    "ec2-54-219-169-134.us-west-1.compute.amazonaws.com",
    "ec2-3-101-107-223.us-west-1.compute.amazonaws.com",
    "ec2-54-215-103-21.us-west-1.compute.amazonaws.com",
    "ec2-50-18-42-73.us-west-1.compute.amazonaws.com",
    "ec2-13-57-236-78.us-west-1.compute.amazonaws.com",
    "ec2-54-176-24-204.us-west-1.compute.amazonaws.com",
    "ec2-204-236-185-170.us-west-1.compute.amazonaws.com",
    "ec2-54-193-119-196.us-west-1.compute.amazonaws.com",
    "ec2-54-193-112-113.us-west-1.compute.amazonaws.com",
    "ec2-54-219-1-163.us-west-1.compute.amazonaws.com",
    "ec2-54-183-73-29.us-west-1.compute.amazonaws.com",
    "ec2-54-219-187-192.us-west-1.compute.amazonaws.com",
    "ec2-13-52-238-68.us-west-1.compute.amazonaws.com",
    "ec2-13-57-244-92.us-west-1.compute.amazonaws.com",
    "ec2-54-215-106-217.us-west-1.compute.amazonaws.com",
    "ec2-54-176-250-239.us-west-1.compute.amazonaws.com",
    "ec2-54-176-50-237.us-west-1.compute.amazonaws.com",
    "ec2-54-153-110-89.us-west-1.compute.amazonaws.com",
    "ec2-13-57-3-14.us-west-1.compute.amazonaws.com",
    "ec2-54-176-98-21.us-west-1.compute.amazonaws.com",
    "ec2-3-101-155-49.us-west-1.compute.amazonaws.com",
    "ec2-50-18-231-177.us-west-1.compute.amazonaws.com",
    "ec2-13-52-248-149.us-west-1.compute.amazonaws.com",
    "ec2-3-101-40-22.us-west-1.compute.amazonaws.com",
    "ec2-54-215-140-64.us-west-1.compute.amazonaws.com",
    "ec2-54-67-118-152.us-west-1.compute.amazonaws.com",
    "ec2-184-72-10-67.us-west-1.compute.amazonaws.com",
    "ec2-54-219-134-45.us-west-1.compute.amazonaws.com",
    "ec2-50-18-39-175.us-west-1.compute.amazonaws.com",
    "ec2-54-151-30-34.us-west-1.compute.amazonaws.com",
    "ec2-13-52-98-215.us-west-1.compute.amazonaws.com",
    "ec2-54-193-136-239.us-west-1.compute.amazonaws.com",
    "ec2-13-57-228-194.us-west-1.compute.amazonaws.com",
    "ec2-13-52-163-156.us-west-1.compute.amazonaws.com",
    "ec2-18-144-6-72.us-west-1.compute.amazonaws.com",
    "ec2-54-176-201-84.us-west-1.compute.amazonaws.com",
    "ec2-54-176-70-95.us-west-1.compute.amazonaws.com",
    "ec2-3-101-36-27.us-west-1.compute.amazonaws.com",
    "ec2-54-177-17-90.us-west-1.compute.amazonaws.com",
    "ec2-18-144-168-103.us-west-1.compute.amazonaws.com",
    "ec2-13-52-231-188.us-west-1.compute.amazonaws.com",
    "ec2-3-101-43-27.us-west-1.compute.amazonaws.com",
    "ec2-13-52-248-4.us-west-1.compute.amazonaws.com",
    "ec2-54-219-199-166.us-west-1.compute.amazonaws.com",
    "ec2-54-153-107-184.us-west-1.compute.amazonaws.com",
    "ec2-54-153-2-110.us-west-1.compute.amazonaws.com",
    "ec2-50-18-241-71.us-west-1.compute.amazonaws.com",
    "ec2-52-53-210-235.us-west-1.compute.amazonaws.com",
    "ec2-13-52-179-7.us-west-1.compute.amazonaws.com",
    "ec2-54-215-31-233.us-west-1.compute.amazonaws.com",
    "ec2-54-176-179-228.us-west-1.compute.amazonaws.com",
    "ec2-54-176-35-147.us-west-1.compute.amazonaws.com"
]
NUM_GPUS = 1 # number of gpus for each instance
KEY_PEM = '~/Desktop/AWS_keys/mirror_cali.pem'
C_LIST = [0.05, 0] # c values rainbow
C_LIST = [0] # c values DQN
D_LIST = [0.005,0.0025] 
D_LIST = [0] 
#D_LIST = [0.05]
# get seeds to run
seed_list = [0,1,2,]
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

FULL_ENV_LIST = ['Asterix', 'Qbert', 'Breakout', 'Seaquest', 'Amidar',
                 'Kangaroo', 'BeamRider', 'Gopher', 'Phoenix', 'Zaxxon']

FULL_ENV_LIST = FULL_ENV_LIST + ['Frostbite', 'StarGunner', 'TimePilot', 'Venture', 'WizardOfWor',
                                 'AirRaid', 'Alien', 'Assault', 'Atlantis', 'BankHeist',]

def create_train_command():
    cmd_list = list()

    # exp counter
    cnt = 0

    # for each env
    for env in FULL_ENV_LIST:
        # for each model
        for model in MODEL_LIST:
            # get config file
            #gin_file = "./dopamine/agents/{}/configs/{}_dqnpro.gin".format(model.lower(), model.lower())
            gin_file = "./dopamine/agents/rainbow/configs/rainbow_our_second_paper.gin".format(model.lower(), model.lower())

            for c,d in zip( [0.0,0.0,0.0,0.0,0.0] , [0.025, 0.01,0.0075, 0.0025,0.001] ):
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
        time.sleep(5)
        process_list.append(p)
    for process in process_list:
        process.join()
    

