# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import leaderboard as lb

#-----game configuration----
trtlshape = "turtle"
turtlesize = 5
trtlcolor = "red"

score = 0
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False


# scoreboard variables
leaderboard_file_name = "a122.leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name.")




#-----initialize turtle-----
miles = trtl.Turtle(shape = trtlshape)
miles.color(trtlcolor)
miles.shapesize(turtlesize)
miles.speed(0)



scorewriter = trtl.Turtle()
scorewriter.ht()
scorewriter.penup()
scorewriter.goto(-350,300)

font_setup = ("Arial", 30, "bold" )
scorewriter.write(score, font = font_setup)

counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(275,300)







#-----game functions--------
def miles_clicked (x,y):
    print("miles got clicked")
    change_position()
    update_score()


def change_position():
    miles.penup()
    miles.ht()
    if not timer_up:
      milesx = random.randint(-400,400)
      milesy = random.randint(-300,300)
      miles.goto(milesx,milesy)
      miles.st()

def update_score():
    global score
    score += 1
    print(score)
    scorewriter.clear()
    scorewriter.write(score, font = font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("GAME OVER", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global miles

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, miles, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, miles, score)






#-----events----------------





wn = trtl.Screen()
wn.bgcolor("pink")
miles.onclick(miles_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()