# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:23:01 2020

@author: jbris
"""

import turtle
import random

screen = turtle.Screen()
screen.setup(1000,1000)
screen.title("Particle animation")
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0,0)

# Constants

FPS = 120 # constant: refresh about 30 times per second
TIMER_VALUE = 1000//FPS # the timer value in milliseconds for timer events
N = 100 # Number of particles

# Variables
particles = [] # list of particle turtles
current_xpos = [] # list of current x coordinate
current_ypos = [] # list of current y coordinate

def initialze_particles():
    for i in range(N):
        particles.append(turtle.Turtle()) # Add a turtle to the particle turtle list
        current_xpos.append(random.uniform(-500,500)) # Let them go anywhere on screen
        current_ypos.append(random.uniform(-500,500))

    for particle in particles: # initialize these turtles
        particle.hideturtle()
        particle.up()

#look into adding collisions

def update_position():
    global current_xpos,current_ypos#,target_xpos,target_ypos
    for i in range(N):
        current_xpos[i] += random.randint(-3,3)#*math.cos(angle_to_target)
        current_ypos[i] += random.randint(-3,3)#*math.sin(angle_to_target)
        
def update_states():
    global should_draw
    update_position()
    should_draw = True
    screen.ontimer(update_states,TIMER_VALUE)

def draw():
    global particles,should_draw,current_xpos,current_ypos
    if should_draw == False: # There is no change. Don't draw and return immediately
        return
    for i in range(N):
        particles[i].clear() # clear the current drawing
        particles[i].goto(current_xpos[i],current_ypos[i])
        particles[i].dot(10)
    should_draw = False # just finished drawing, set should_draw to False

screen.bgcolor('white')
initialze_particles()                
update_states()
while True:
    draw() # draw forever
    screen.update()