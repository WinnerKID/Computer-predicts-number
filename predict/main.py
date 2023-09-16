from tqdm import tqdm
import time

user_number = int(input('Choose a number between 1 and 100: '))
loading_messages = ['Loading...', 'Calculating possibilities...', 'Scanning brainwaves...', 'Completed']

# Initialize the tqdm progress bar with the initial message
pbar = tqdm(total=300, desc='Loading...', ascii=False, ncols=75, dynamic_ncols=False)

for i in range(300):
    message_index = (i // 100) % len(loading_messages)
    pbar.set_description(loading_messages[message_index])
    time.sleep(0.05)
    pbar.update(1)

pbar.close()  # Close the progress bar

print('Computer: Your number is ' + str(user_number))
