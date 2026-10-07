import time

#Most of this is just to track the actual time passing
def timer_start(): 
    start_time = time.perf_counter()
    print(f"Starting timer")
    return start_time

def timer_end():
    end_time = time.perf_counter()
    print(f"Stopping timer")
    return end_time

def timer(start, stop):
    elapsed_time = stop - start
    return elapsed_time

def seconds_to_minutes(total_seconds):
    minutes = int(total_seconds // 60)
    seconds = total_seconds % 60
    return minutes, seconds

#This function increments the current dictionary times according to their rollover values
def roll_over(small_time, big_time):
    if small_time["current"] == small_time["rollover"]:
        small_time["current"] = 0
        big_time["current"] += 1


#This exists to compare the speeds of using the print function for every iteration
def efficient_main():
    times = {
            #This was a mistake
            #"milliseconds" : {
            #    "current" : 0,
            #    "rollover" : 1000
            #},
            "seconds" : {
                "current" : 0,
                "rollover" : 60
            },
            "minutes" : {
                "current" : 0,
                "rollover" : 60
            },
            "hours" : {
                "current" : 0,
                "rollover" : 24
            },
            "days" : {
                "current" : 0,
                "rollover" : 365
            },
            "years" : {
                "current" : 0
            }       
        }
    
    #this helps the for in range loop iterate through the dictionary
    time_list = list(times)
    
    go = timer_start()
    
    print()
    print(f"Begin")
    print()
    
    
    #loop continues until 1 computer year passes
    while times["years"]["current"] < 1:
    
        #again, this was originally seconds, I made a mistake changing it
        #it really was a mistake, reverted
        times["seconds"]["current"] += 1
    
        #iterates through the dictionary via the list, runs rollover each time to switch dictionary items if rollover value is reached
        for i in range(len(time_list) - 1) :
            time_first = time_list[i]
            time_next = time_list[(i + 1)]
    
            roll_over(times[time_first], times[time_next])
    
        #Removed the printing of each passing... millisecond UGH
        #was a mistake, reverted
    
    
    #a bunch of math to provide satisfying final numbers
    stop = timer_end()
    
    efficient_elapsed = timer(go, stop)
        
    efficient_mins, efficient_secs = seconds_to_minutes(efficient_elapsed)
    
    efficient_comp_sec = efficient_elapsed / 31536000
    
    efficient_simulation_speed = 31536000 / efficient_elapsed
    
    print(f"31,536,000 efficient computer seconds passed in {efficient_elapsed:,.2f} real seconds.")
    print()
    print(f"One efficient computer year is equal to {efficient_mins} minutes and {efficient_secs:.2f} seconds.")
    print()
    print(f"One efficient computer second is equal to {efficient_comp_sec:.8f} real seconds.")
    print()
    print(f"Therefore, {efficient_simulation_speed:,.2f} efficient computer seconds pass every real second.")
    print()

    return efficient_elapsed, efficient_mins, efficient_secs, efficient_comp_sec, efficient_simulation_speed

#I originally wrote this with just seconds, milliseconds makes it take oh so much longer
#Huge mistake, reverted
def main():
    times = {
        #"milliseconds" : {
        #    "current" : 0,
        #    "rollover" : 1000
        #},
        "seconds" : {
            "current" : 0,
            "rollover" : 60
        },
        "minutes" : {
            "current" : 0,
            "rollover" : 60
        },
        "hours" : {
            "current" : 0,
            "rollover" : 24
        },
        "days" : {
            "current" : 0,
            "rollover" : 365
        },
        "years" : {
            "current" : 0
        }       
    }

    #this helps the for in range loop iterate through the dictionary
    time_list = list(times)

    go = timer_start()

    print()
    print(f"Begin")
    print()


    #loop continues until 1 computer year passes
    while times["years"]["current"] < 1:

        #again, this was originally seconds, I made a mistake changing it
        #Huge mistake, reverted
        times["seconds"]["current"] += 1

        #iterates through the dictionary via the list, runs rollover each time to switch dictionary items if rollover value is reached
        for i in range(len(time_list) - 1) :
            time_first = time_list[i]
            time_next = time_list[(i + 1)]

            roll_over(times[time_first], times[time_next])

        #Prints each passing... millisecond UGH... in a decent format for user interpretation
        #now in seconds
        print(f"{times['years']['current']} years, {times['days']['current']} days. {times['hours']['current']}:{times['minutes']['current']}:{times['seconds']['current']}")
        print()


    #a bunch of math to provide satisfying final numbers
    stop = timer_end()

    elapsed = timer(go, stop)
    
    mins, secs = seconds_to_minutes(elapsed)

    comp_sec = elapsed / 31536000

    simulation_speed = 31536000 / elapsed

    print(f"31,536,000 computer seconds passed in {elapsed:,.2f} real seconds.")
    print()
    print(f"One computer year is equal to {mins} minutes and {secs:.2f} seconds.")
    print()
    print(f"One computer second is equal to {comp_sec:.8f} real seconds.")
    print()
    print(f"Therefore, {simulation_speed:,.2f} computer seconds pass every real second.")
    print()

    print(f"at least, while generating all this text...")
    print(f"AGAIN!")
    print()
    print()

    efficient_elapsed, efficient_mins, efficient_secs, efficient_comp_sec, efficient_simulation_speed = efficient_main()

    print(f"Comparisons")
    print(f"{'Times':>45} {'Original':>15} {'Efficient':>15}")
    print(f"{'31,536,000 computer seconds to real seconds':>45} {elapsed:>15,.2f} {efficient_elapsed:>15,.2f}")
    print(f"{'Computer year is equal to mins and seconds':>45} {mins:>11}:{secs:>4.2f} {efficient_mins:>11}:{efficient_secs:>4.2f}")
    print(f"{'Computer second is equal to real seconds':>45} {comp_sec:>15.8f} {efficient_comp_sec:>15.8f}")
    print(f"{'Real second is equal to computer seconds':>45} {simulation_speed:>15,.2f} {efficient_simulation_speed:>15,.2f}")

if __name__ == "__main__":
    main()