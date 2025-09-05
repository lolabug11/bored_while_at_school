import time as t
def count():
    amount = int(input('How high do you want to count?\n'))
    sec_wait = float(input('How many seconds do you want to wait for each number?\n'))
    time_waiting = amount * sec_wait
    print(f'You will wait {time_waiting} seconds.')
    for i in range(amount):
        print(i+1)
        t.sleep(sec_wait)