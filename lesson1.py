# name = "Jay Patel"

# def main(_name):
#     print("Hello ", _name)
#     print("How Are you? is there anything I can do for you?")

# #Check function exists and properly loaded or not!
# if __name__ == "__main__":
#     main(name)


# def myFunc():
#     print("Test me");
    
# myFunc()

def loops():
    #While loop
    # counter = 0
    # while(counter < 5):
    #     print(counter)
    #     counter = counter + 1
    for counter in range(5,10):
        print(counter)
    days = ["day0","day1","day2","day3","day4","day5","day6","day7","day8"]
    for index, day in enumerate(days):
        print(index," ",day)   
    
    
loops()
