import scipy.stats
import pandas as pd
import numpy as np

def load_clean_data():
    df = pd.read_csv('impulsivity_rlwm/RLWM_train_data.csv')
    subj = df['id'].to_numpy()
    block = df['block'].to_numpy()
    trial = df['trial'].to_numpy()
    rt = df['rt'].to_numpy()
    key_answer = df['key_answer'].to_numpy()
    key_press = df['key_press'].to_numpy()
    correct = df ['correct'].to_numpy()
    set_size = df['set_size'].to_numpy()
    iteration = df['iteration'].to_numpy()
    delay = df['delay'].to_numpy()
    reward_history = df['reward_history'].to_numpy()
    stimulus = df['stimulus'].to_numpy()

    bad_trials = np.where(block==0)[0]
    more_bad = np.where(np.nan_to_num(rt)<=200)[0]
    bad_subj = np.where(subj==1)[0]
    bad_idx = np.append(bad_trials, more_bad)
    print(f'{(bad_idx.shape[0]/subj.shape[0])*100:.2f} percent trials removed')

    clean_setsize = np.array([i for j, i in enumerate(set_size) if j not in bad_idx])
    clean_correct = np.array([i for j, i in enumerate(correct) if j not in bad_idx])
    clean_iterations = np.array([i for j, i in enumerate(iteration) if j not in bad_idx])
    clean_subj = np.array([i for j, i in enumerate(subj) if j not in bad_idx])
    clean_reward = np.array([i for j, i in enumerate(reward_history) if j not in bad_idx])
    clean_delay = np.array([i for j, i in enumerate(delay) if j not in bad_idx])
    clean_action = np.array([i for j, i in enumerate(key_press) if j not in bad_idx])
    clean_block = np.array([i for j, i in enumerate(block) if j not in bad_idx])
    clean_stimulus = np.array([i for j, i in enumerate(stimulus) if j not in bad_idx])

    data_dict = dict()
    data_dict['set_size'] = clean_setsize
    data_dict['iterations'] = clean_iterations
    data_dict['correct'] = clean_correct
    data_dict['subj'] = clean_subj
    data_dict['reward'] = clean_reward
    data_dict['delay'] = clean_delay
    data_dict['action'] = clean_action
    data_dict['block'] = clean_block
    data_dict['stimulus'] = clean_stimulus
    return data_dict
