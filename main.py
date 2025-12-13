from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Button, Color
from pybricks.robotics import DriveBase 
from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE) #define o motor de movimento da esquerda
right_motor = Motor(Port.E) #define o motor de movimento da direita
color_sensor = ColorSensor(Port.D)

#define os motores de anexos
att_right_motor = Motor(Port.F) # cabo descascado
att_left_motor = Motor (Port.B)


#print (right_motor.angle())

#print (left_motor.angle())

#print (att_right_motor.angle())

#print (att_left_motor.angle())

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter =56, axle_track=113)

# Optionally, uncomment the line below to use the gyro for improved accuracy.
drive_base.use_gyro(True)

hub = PrimeHub()



def curva (angulo, kp, ki):
    integral = 0
    while abs(hub.imu.heading())<=abs(angulo):
        erro = angulo-hub.imu.heading()
        integral = erro+integral
        movimento = (kp*erro)+(ki*integral)
        left_motor.dc(movimento)
        right_motor.dc(movimento*-1)
    left_motor.stop()
    right_motor.stop()

distancia_percorrida = drive_base.distance()


while True:
    print(color_sensor.color())
   # START 2
    if hub.buttons.pressed()==({Button.RIGHT} or {Button.LEFT})and color_sensor.color() == Color.RED:
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     drive_base.settings(450,800)
     drive_base.straight(640)
     curva(-38.6,0.9,0.0007)
     att_right_motor.run_angle(-500,330)
     att_left_motor.run_angle(500,187)
     drive_base.settings(450,300)
     drive_base.straight(100)
     att_right_motor.run_angle(500,215)
    # drive_base.straight(-7)
     att_left_motor.run_angle(-300,460)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     drive_base.straight(-125)
     curva(49,0.9,0.0004)
    # drive_base.straight(-7)
     att_right_motor.run_angle(500,270)
     drive_base.straight(-60)
     curva(65,0.9,0.004)
     drive_base.settings(800,9000)
     drive_base.straight(-590)
     drive_base.use_gyro(False)

#START 1
    if hub.buttons.pressed()==({Button.RIGHT} or {Button.LEFT})and color_sensor.color() == Color.YELLOW:
      #att_left_motor.run_angle(900,600)
     ''' drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     drive_base.settings(500,400)
     drive_base.straight(590)
     curva(180,0.4,0.0002)
     drive_base.straight(-260)
     wait(500)
     drive_base.straight(100)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(-85.6,0.4,0.0002)
     wait(500)
     drive_base.settings(400,100)
     drive_base.straight(175)
     att_right_motor.run_angle(800,400,wait=False)
     att_left_motor.run_angle(800,-110)
     drive_base.straight(-190)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(95,0.9,0.002)
     drive_base.settings(800,9000)
     drive_base.straight(680)
     drive_base.use_gyro(False)'''
     #att_left_motor.run_angle(900,600)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     drive_base.settings(500,400)
     drive_base.straight(630)
     curva(-85,0.5,0.0002)
     drive_base.settings(500,400)
     drive_base.straight(-311)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(83,0.3,0.0002)
     drive_base.straight(-3)
     att_right_motor.run_angle(-500,350)
     att_left_motor.run_angle(400,280)
     wait(300)
     drive_base.straight(136)
     wait(300)
     #att_left_motor.run_angle(-400,475)
     att_left_motor.run_time(-400,1700)
    # att_left_motor.run_angle(400,380)
    # att_left_motor.run_angle(400,380)
     drive_base.straight(-110)

     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(90,0.5,0.0002)
     drive_base.settings(600,5000)
     drive_base.straight(-300)
     curva(180,0.5,0.0002)
     drive_base.settings(800,8000)
     drive_base.settings(800,9000)
     drive_base.straight(599)
     drive_base.use_gyro(False)


#START 5
    if hub.buttons.pressed()=={Button.LEFT}and color_sensor.color() == Color.NONE:
    
      att_left_motor.run_angle(700,150,wait=False)
      drive_base.settings(800,700)
      drive_base.straight(200)
      curva(39,0.9,0.002)
      drive_base.straight(260)
      drive_base.settings(500,400)
      drive_base.straight(-150)
      #drive_base.settings(500,200)
      #drive_base.straight(200)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(48,0.5,0.0002)
      drive_base.straight(440)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      att_left_motor.run_angle(-700,160)
      curva(-109,0.4,0.0002)
     # curva(180,0.9,0.0004)
      drive_base.straight(120)
      att_left_motor.run_angle(1300,146)
      drive_base.settings(400,200)
      drive_base.straight(-123)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(105,0.3,0.002)
      drive_base.settings(800,9000)
      drive_base.straight(470)
      #curva(199.1,0.3,0.0002)
      #drive_base.straight(150)
      #att_right_motor.run_time(800,1120)
      #att_right_motor.run_time(-800,1120)
      #drive_base.settings(800,9000)
      #drive_base.straight(160)
      #drive_base.use_gyro(False)
      #hub.imu.reset_heading(0)
      #drive_base.use_gyro(True)
      #curva(11,0.7,0.004)
      #drive_base.settings(800,9000)
     # att_left_motor.run_angle(1200,150)
      #drive_base.straight(360)
      #att_right_motor.run_angle(-600,1695)
      #drive_base.straight(-100)
      drive_base.use_gyro(False)
      '''hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(11,0.9,0.004)
      att_left_motor.run_angle(1200,89)
      drive_base.settings(350,180)
      drive_base.straight(-230)
      wait(400)
      drive_base.settings(800,9000)
      drive_base.straight(60)
      drive_base.arc(-300,80)
      drive_base.straight(500)
      
      
      #drive_base.straight()
     # drive_base.straight(150)
      #drive_base.use_gyro(False)
      ##hub.imu.reset_heading(0)
      #drive_base.use_gyro(True)
      #curva(-77,0.7,0.0004)
      #drive_base.straight(650)
      drive_base.use_gyro(False)
      #drive_base.arc(100,90)'''

#START 3
    if hub.buttons.pressed()==({Button.RIGHT} or {Button.LEFT})and color_sensor.color() == Color.BLUE:
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     drive_base.settings(500,300)
     drive_base.straight(447)
     drive_base.settings(600,900)
     
     att_right_motor.run_time(400,800)
     drive_base.straight(-40)
     drive_base.straight(50)
     att_left_motor.run_time(-700,2150)
     att_right_motor.run_time(-900,1000)
     drive_base.straight(-200)
     drive_base.settings(600,9000)
     drive_base.straight(-400)

     drive_base.use_gyro(False)

# START 6
    if hub.buttons.pressed()=={Button.RIGHT} and color_sensor.color() == Color.WHITE:
      drive_base.settings(600,500)
      drive_base.straight(320)
      curva(-25,0.9,0.0004)
      drive_base.straight(306)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(62.5,1.0,0.0003)
      wait(700)
      drive_base.straight(110.5)
      wait(1000)
      #att_right_motor.run_angle(800,620)
      drive_base.straight(31)
      wait(1000)
      att_right_motor.run_angle(800,-756,wait=False)
      att_left_motor.run_angle(900,-120)
      drive_base.straight(25)
      wait(900)
      drive_base.straight(-100)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      wait(500)
      curva(-33,0.9,0.002)
      wait(500)
     # drive_base.straight(40)
      #curva(-30,0.9,0.003)
      drive_base.straight(-80)
      curva(-47,0.9,0.003)
      drive_base.settings(800,8000)
      drive_base.straight(-560)
      drive_base.use_gyro(False)

# START 7
    if hub.buttons.pressed()=={Button.LEFT}and color_sensor.color() == Color.WHITE:
       att_right_motor.run_time(1200,800)
       drive_base.settings(600,500)
       drive_base.straight(690)
       curva(35,0.6,0.0003)
       drive_base.straight(234)
       att_right_motor.run_angle(-1200,400)
       drive_base.straight(200)
       drive_base.straight(-300)
    
    if hub.buttons.pressed()=={Button.RIGHT} and color_sensor.color() == Color.GREEN:
         #att_left_motor.run_angle(500,200)
         drive_base.use_gyro(False)
         hub.imu.reset_heading(0)
         drive_base.use_gyro(True)
         drive_base.settings(500,400)
         drive_base.straight(320)
         att_right_motor.run_angle(1200,200)
         att_right_motor.run_angle(-1200,200)
         wait(300)
         att_right_motor.run_angle(1200,200)
         att_right_motor.run_angle(-1200,200)
         wait(300)
         att_right_motor.run_angle(1200,200)
         att_right_motor.run_angle(-1200,200)
         wait(300)
         #att_right_motor.run_angle(1200,200)
         #att_right_motor.run_angle(-1200,200)
         #wait(300)
         curva(-41,0.7,0.0004)
         att_left_motor.run_angle(-800,200,wait=False)
         drive_base.settings(400,200)
         drive_base.straight(588)
         att_left_motor.run_angle(800,200)
         drive_base.settings(800,8000)
         drive_base.straight(-500)
         drive_base.use_gyro(False)
         hub.imu.reset_heading(0)
         drive_base.use_gyro(True)
         curva(28,0.7,0.0004)
         drive_base.settings(800,9000)
         drive_base.straight(-390)
         drive_base.use_gyro(False)


    if hub.buttons.pressed()=={Button.LEFT}and color_sensor.color() == Color.YELLOW:
       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)
       drive_base.settings(500,400)
       att_left_motor.run_angle(400,150,wait=False)
       drive_base.straight(415)
       #att_left_motor.run_angle(-800,500)
       #drive_base.straight(100)
       #curva(-41,0.9,0.0004)
       #drive_base.straight(407)
       
       att_left_motor.run_angle(-800,435)
       wait(500)
       att_right_motor.run_angle(-900,410)
       wait(500)
       #drive_base.straight(25)
       att_left_motor.run_angle(800,385)
       wait(500)
       drive_base.settings(800,1000)
       drive_base.straight(-35)
       drive_base.straight(35)
       drive_base.straight(-145)
       drive_base.straight(40)
       att_right_motor.run_angle(400,400)
       drive_base.settings(800,9000)
       drive_base.straight(-185)
       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)
       curva(-10,0.9,0.004)
       drive_base.straight(-190)
       drive_base.use_gyro(False)

 
    if hub.buttons.pressed()=={Button.LEFT} and color_sensor.color() == Color.BLUE:
       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)
       drive_base.settings(500,400)
       drive_base.straight(350)
       curva(26.6,0.7,0.0004)
       drive_base.settings(400,200)
       drive_base.straight(630)
       drive_base.settings(800,9000)
       drive_base.straight(-260)
       drive_base.use_gyro(False)      
      # curva(86,0.4,0.0002)
      # drive_base.straight(875)
      # curva(-164,0.5,0.0004)
      # drive_base.straight(120)

      # att_left_motor.run_angle(800,200)
       #drive_base.use_gyro(False)
       #hub.imu.reset_heading(0)
       #drive_base.use_gyro(True)
       #curva(15,0.5,0.004)
       #drive_base.straight(-150)

    



# Lista de funções para alternar
#starts = [start0,start2]
#starts = [start0,start1,start2,start3,start4,start5,start6,start7, start8]
#indice_funcao = 0  # Começa na primeira função

# Loop principal
#while True:
    # Executa a função atual
 #   starts[indice_funcao]()
    
    # Espera pelo pressionamento do botão esquerdo
  #  while not (Button.LEFT in hub.buttons.pressed() or Button.RIGHT in hub.buttons.pressed()):
   #     wait(10)
    
    # Aguarda até o botão ser liberado para evitar múltiplos acionamentos
    #while (Button.LEFT in hub.buttons.pressed()or Button.RIGHT in hub.buttons.pressed()):
     #   wait(10)
      #  hub.imu.reset_heading(0)
       # drive_base.use_gyro(True) # ativa o uso do sensor giroscópio na correção de movimento antes de executar um novo start

    
    # Passa para a próxima função, ou seja, vai para o próximo start
    #indice_funcao = (indice_funcao + 1) % len(starts)  # Volta ao início ao alcançar o final
