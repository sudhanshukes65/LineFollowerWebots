
from controller import Robot

def run_robot(robot):
   
    time_step = 32   
    max_speed = 10
    




   
    # created motor instances
    left_motor = robot.getDevice('front_left_motor')
    right_motor = robot.getDevice('front_right_motor')
    
    back_left_motor = robot.getDevice('back_left_motor')
    back_right_motor = robot.getDevice('back_right_motor')
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    back_right_motor.setPosition(float('inf'))
    back_right_motor.setVelocity(0.0)
    
    back_left_motor.setPosition(float('inf'))
    back_right_motor.setVelocity(0.0)
    
    
    
    
    left_ir = robot.getDevice('left_ir')
    left_ir.enable(time_step)
    
    middle_ir = robot.getDevice('middle_ir')
    middle_ir.enable(time_step)
    
    right_ir = robot.getDevice('right_ir')
    right_ir.enable(time_step)
    
    stop_ir = robot.getDevice('stop_sensor')
    stop_ir.enable(time_step)
    
    
    
    
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(time_step) != -1:
    
         #wb_led_set(right_led, 1)
         #Reading IR Sensor values
         
         
         left_ir_value =left_ir.getValue()
         middle_ir_value = middle_ir.getValue()
         right_ir_value = right_ir.getValue()
         stop_ir_value = stop_ir.getValue()
         
         #Storing speed in variables
         
         left_speed = max_speed
         right_speed = max_speed
         back_left_speed = max_speed
         back_right_speed = max_speed
         
         
         # Printing sensors values for Debugging 
          
         print("Right: {} Middle: {} left: {} stop: {}".format(right_ir_value ,middle_ir_value,left_ir_value,stop_ir_value))
          
         #<600 means white and >600 means black 
         #For right turn : turn right only if no straight path avaiable    
         if( left_ir_value <600 ) and (  right_ir_value >600 ) and ( 900>middle_ir_value >600  ) :
              left_speed = max_speed
              right_speed = -max_speed
              
              back_left_speed = max_speed
              back_right_speed = -max_speed
              print("Turn Right")
               
         #Turn left if ,left  and straight both path avaiable    
         elif( left_ir_value >800 ) and  ( 850>middle_ir_value>600  ) :
              left_speed = -max_speed
              right_speed = max_speed
              
              back_left_speed = -max_speed
              back_right_speed = max_speed
              print("Turn Left")
                           
         #if all four sensor reads black then stop
         elif( left_ir_value >999 ) and (  right_ir_value>999 ) and (  middle_ir_value >999 )and ( stop_ir_value>999 ) :

              left_speed = max_speed*0
              right_speed = max_speed*0
              
              back_left_speed = max_speed*0
              back_right_speed = max_speed*0
              print("Stop")
              
   
         #Passing values to motors 
         left_motor.setVelocity(left_speed)
         right_motor.setVelocity(right_speed)  
         
         back_left_motor.setVelocity(back_left_speed) 
         back_right_motor.setVelocity(back_right_speed) 

            
    # Enter here exit cleanup code.
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)
    
    
    #Jai hind Dosto