#setup demo

print("creating demo text file: topsecret.txt ", '\n')

ts1 = "Top Secret text - Do not modify this text file!!"
lb1 = "your text is gone - Logic bom has worked!!"

f = open("topsecret.txt", "w")
f.write(ts1)
f.close()

print("open new text file and print the content of the text file:", '\n')

f = open("topsecret.txt", "r")
print(f.read())
print('\n')

#logic bom

# import the time module
import time
  
# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print("\033[31m", 'Logic BOM!!!', "\033[0m", '\n')
    f = open("topsecret.txt", "w")
    f.write(lb1)
    f.close()
  
# input time in seconds
t = 5
  
# function call
countdown(int(t))


print("open text file after the logic bom and print the new content of the text file: topsecret.txt", '\n')

f = open("topsecret.txt", "r")
print(f.read())
print('\n', "end of logic bom demo")