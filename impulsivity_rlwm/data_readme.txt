Descriptions of data tables and columns:

RLWM_train_data.csv: RLWM training phase data. Each row represents a trial from a block of a participant. 
* id: de-identfied subject ID
* block: block number (0 for practice block, excluded from analyses)
* trial: trial number in block
* stimulus: stimulus presented for this trial (1:x, x = set size)
* rt: response time in milliseconds
* key_press: action for the trial (0 = J, 1 = K, 2 = L)
* key_answer: correct action for the trial (0 = J, 1 = K, 2 = L)
* correct: whether response was corect
* set_size: set size of this block
* set: image folder used for this block
* img_num: image file used for this trial's stimulus
* iteration: how many times this stimulus has been seen so far
* delay: how many trials since last presentation of this stimulus
* reward_history: how many correct responses for this stimulus since block start

RLWM_test_data.csv: RLWM test phase data. Each row represents a trial in test phase. Test phase consists of 3 independently shuffled sequences of all stimuli seen in training phase. 
* id: de-identfied subject ID
* block: block where stimulus was presented
* trial: testing trial number
* stimulus: stimulus number
* rt: response time in milliseconds
* key_press: action for the trial (0 = J, 1 = K, 2 = L)
* key_answer: correct action for the trial (0 = J, 1 = K, 2 = L)
* correct: whether response was corect
* set_size: set size of this block
* set: image folder used for this block
* img_num: image file used for this trial's stimulus

The following columns aren't really used for test phase behavior analysis: 
* iteration: how many times this stimulus has been seen so far
* delay: how many trials since last presentation of this stimulus
* reward_history: how many correct responses for this stimulus since start of test phase

RLWM_meta_data.csv: simple meta data for subjects who completed RLWM. Every row is a subject. 
* id: de-identfied subject ID
* cond: which stimuli sequence was used to generate their task
* instruction_reps: how many times they repeated instructions
* train_cor_overall: overall performance in train phase
* missed_trial_trials: number of no-response trials from training phase 
* train_time: minutes spent completing training phase
* test_cor_overall: overall performance in test phase
* missed_test_trials: number of no-response trials from testing phase
* test_time: minutes spent completing testing phase