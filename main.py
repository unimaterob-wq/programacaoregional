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
att_right_motor = Motor(Port.F) 
att_left_motor = Motor (Port.B)

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
     drive_base.settings(600,500)
     drive_base.straight(590)   
    # drive_base.settings(500,200)
    # drive_base.straight(-110)
    # drive_base.settings(600,500)
    # drive_base.straight(150)
     att_right_motor.run_angle(-300,260)
     drive_base.straight(30)
     #drive_base.straight(13)
     wait(300)
     curva(-41,0.8,0.0004)
     wait(300)
     drive_base.settings(600,500)
     drive_base.straight(100)
     att_right_motor.run_angle(900,260)
     drive_base.straight(152)
     att_right_motor.run_angle(-900,260)
     drive_base.settings(600,400)
     drive_base.straight(-140)
     curva(-90,0.9,0.0004)
     drive_base.straight(190)
     att_left_motor.run_angle(-300,200)
     drive_base.straight(-110)
     curva(-152,0.9,0.0004)
     drive_base.settings(800,8000)
     drive_base.straight(520)
     drive_base.use_gyro(False)
    # hub.imu.reset_heading(0)
    # drive_base.use_gyro(True)

#START 1
    if hub.buttons.pressed()==({Button.RIGHT} or {Button.LEFT})and color_sensor.color() == Color.YELLOW:
     #att_left_motor.run_angle(900,600)
     drive_base.settings(400.200)
     drive_base.straight(630)
     curva(-85,0.5,0.0002)
     drive_base.settings(400,200)
     drive_base.straight(-326)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(86,0.3,0.0002)
     drive_base.straight(-3)
     att_right_motor.run_angle(-500,250)
     wait(300)
     drive_base.straight(136)
     wait(300)
     att_left_motor.run_angle(-400,400)
     wait(300)
     att_left_motor.run_angle(400,330)
     drive_base.straight(-110)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(90,0.5,0.0002)
     drive_base.settings(800,8000)
     drive_base.straight(-300)
     curva(180,0.5,0.0002)
     drive_base.settings(800,8000)
     drive_base.straight(599)
     drive_base.use_gyro(False)

#START 4
    if hub.buttons.pressed()==({Button.RIGHT} or {Button.LEFT})and color_sensor.color() == Color.NONE:
     drive_base.settings(800,700)
     drive_base.straight(370)
     drive_base.straight(-380)
     drive_base.use_gyro(False)

#START 5
    if hub.buttons.pressed()=={Button.LEFT}and color_sensor.color() == Color.NONE:
    #  att_left_motor.run_angle(700,150)
      drive_base.settings(500,400)
      drive_base.straight(190)
      curva(89,0.5,0.0002)
      drive_base.straight(595)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
     # att_left_motor.run_angle(-700,150)
      curva(-108,0.4,0.0002)
     # curva(180,0.9,0.0004)
      drive_base.straight(170)
      att_left_motor.run_angle(1300,150)
      drive_base.settings(400,300)
      drive_base.straight(-140)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(110,0.3,0.0002)
      drive_base.straight(125)
      curva(193,0.3,0.0002)
      drive_base.straight(150)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(-2.9,0.9,0.004)
     # att_left_motor.run_angle(1200,150)
     # drive_base.straight(-100)
      att_right_motor.run_angle(-800,1400)
      drive_base.straight(-100)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(14,0.9,0.0004)
      drive_base.straight(-236)
      wait(300)
      drive_base.settings(800,8000)
      drive_base.arc(-325,100)
      drive_base.straight(120)

      
      #drive_base.straight()
      drive_base.straight(150)
      #drive_base.use_gyro(False)
      ##hub.imu.reset_heading(0)
      #drive_base.use_gyro(True)
      #curva(-77,0.7,0.0004)
      #drive_base.straight(650)
      drive_base.use_gyro(False)
      #drive_base.arc(100,90)

#START 3
    if hub.buttons.pressed()==({Button.RIGHT} or {Button.LEFT})and color_sensor.color() == Color.BLUE:
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     drive_base.settings(600,500)
     drive_base.straight(355)
     drive_base.settings(400,300)
     drive_base.straight(-190)
     drive_base.settings(600,500)
     drive_base.straight(290)
     drive_base.straight(-420)
     drive_base.use_gyro(False)


# START 6
    if hub.buttons.pressed()=={Button.RIGHT} and color_sensor.color() == Color.WHITE:
      drive_base.settings(500,400)
      drive_base.straight(539)
      curva(73,0.7,0.0002)
      att_left_motor.run_angle(-900,200)
      drive_base.settings(300,100)
      drive_base.straight(200)
      
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
     # curva(-1.5,1,0.004)
      drive_base.straight(10)
      
      att_left_motor.run_angle(300,200)
      wait(300)
      drive_base.straight(-110)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(-9,0.9,0.004)
      drive_base.settings(600,500)
      drive_base.straight(9.5)
      curva(-23,0.5,0.004)
      drive_base.straight(-150)
      curva(-71,0.7,0.0003)
      drive_base.settings(800,8000)
      drive_base.straight(-490)
      drive_base.use_gyro(False)

# START 7
    if hub.buttons.pressed()=={Button.LEFT}and color_sensor.color() == Color.WHITE:
       att_right_motor.run_time(1200,800)
       drive_base.settings(600,500)
       drive_base.straight(660)
       curva(35,0.6,0.0003)
       drive_base.straight(234)
       att_right_motor.run_angle(-1200,400)
       drive_base.straight(200)
       drive_base.straight(-300)
    
    if hub.buttons.pressed()=={Button.RIGHT} and color_sensor.color() == Color.GREEN:
         #att_left_motor.run_angle(500,200)
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
         att_right_motor.run_angle(1200,200)
         att_right_motor.run_angle(-1200,200)
         wait(300)
         curva(-39,0.7,0.0004)
         att_left_motor.run_angle(-800,200,wait=False)
         drive_base.settings(400,200)
         drive_base.straight(560)
         att_left_motor.run_angle(800,200)
         drive_base.settings(800,8000)
         drive_base.straight(-500)
         drive_base.use_gyro(False)
         hub.imu.reset_heading(0)
         drive_base.use_gyro(True)
         curva(28,0.7,0.0004)
         drive_base.straight(-330)
         drive_base.use_gyro(False)


    if hub.buttons.pressed()=={Button.LEFT}and color_sensor.color() == Color.YELLOW:
       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)
       drive_base.settings(500,400)
       drive_base.straight(60)
       #att_left_motor.run_angle(-800,500)
       #drive_base.straight(100)
       curva(-41,0.9,0.0004)
       drive_base.straight(420)
       att_right_motor.run_angle(800,460,wait=False)
       att_left_motor.run_angle(-800,200)
       wait(300)
       #att_left_motor.run_angle(-180,240)
       drive_base.straight(-105)
       drive_base.straight(30)
       att_left_motor.run_angle(400,220)
       drive_base.settings(800,8000)
       drive_base.straight(-420)
       drive_base.use_gyro(False)

 
    if hub.buttons.pressed()=={Button.LEFT} and color_sensor.color() == Color.BLUE:
       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)
       drive_base.settings(400,350)
       drive_base.straight(630)
       
       curva(-86,0.4,0.0002)
       drive_base.straight(875)
       curva(-164,0.5,0.0004)
       drive_base.straight(120)

       att_left_motor.run_angle(800,200)
       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)
       curva(15,0.5,0.004)
       drive_base.straight(-150)

    



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
