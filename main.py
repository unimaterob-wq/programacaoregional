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


def moverPI (referência,velocidade, distância, kp, ki ):
    left_motor.reset_angle(0)
    integral=0
    velocidade=0
    conversor=365*distância/19.4
    while abs(left_motor.angle())<conversor:
       erro =referência-hub.imu.heading()
       integral = erro+integral
       correção = (kp*erro)+(ki*integral)
       left_motor.dc(correção+velocidade)
       right_motor.dc(correção+velocidade)
       if velocidade <= 200:
          velocidade = 200
    left_motor.stop()
    right_motor.stop()

def moverPI (referência,velocidade, distância, kp):
    left_motor.reset_angle(0)
    velocidade=0
    conversor=365*distância/19.4
    while abs(left_motor.angle())<conversor:
       erro =referência-hub.imu.heading()
       correção = (kp*erro)
       left_motor.dc(correção+velocidade)
       right_motor.dc(correção+velocidade)
       if velocidade <= 200:
          velocidade = 200
    left_motor.stop()
    right_motor.stop()


def curva (angulo, kp , ki):
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
     print('to aq 1')
    # moverPI(hub.imu.heading(),200,20,0.5,0.0004)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     drive_base.settings(450,800)
     drive_base.straight(640)
     curva(-36,0.9,0.0007)
     att_right_motor.run_angle(-500,330)
     att_left_motor.run_angle(500,187)
     drive_base.settings(450,300)
     drive_base.straight(105)
    # drive_base.turn(5)
     att_right_motor.run_angle(400,180)
    # drive_base.straight(-7)
     att_left_motor.run_angle(-300,460)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     drive_base.straight(-135)
     curva(48,0.9,0.0004)
    # drive_base.straight(-7)
   #  drive_base.straight(10)
     att_right_motor.run_angle(900,200)
     #wait(700)
     drive_base.straight(-10)
     curva(50,0.9,0.004)
     drive_base.settings(800,9000)
     drive_base.straight(-590)
     drive_base.use_gyro(False)

#START 1
    if hub.buttons.pressed()==({Button.RIGHT} or {Button.LEFT})and color_sensor.color() == Color.YELLOW:
     print('to aq 2')
  
      #att_left_motor.run_angle(900,600)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     drive_base.settings(500,400)
     drive_base.straight(600)
     curva(180,0.4,0.0002)
     drive_base.straight(-251)
     wait(500)
     drive_base.straight(100)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(-85.6,0.4,0.0002)
     wait(500)
     drive_base.settings(400,100)
     drive_base.straight(125)
     #att_left_motor.run_angle(800,48)
     drive_base.straight(40)
     att_right_motor.run_angle(800,400,wait=False)
     att_left_motor.run_angle(800,-120)
     drive_base.straight(-180)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(90,0.9,0.0004)
     drive_base.settings(800,9000)
     drive_base.straight(680)
     drive_base.use_gyro(False)
     '''#att_left_motor.run_angle(900,600)
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
     drive_base.use_gyro(False)'''


#START 5
    if hub.buttons.pressed()=={Button.LEFT} and color_sensor.color() == Color.NONE:
      print('to aq 3')

      #att_left_motor.run_angle(700,150,wait=False)
      drive_base.settings(800,700)
      drive_base.straight(-200)
      curva(42,0.9,0.0004)
      drive_base.straight(260)
      drive_base.settings(500,400)
      drive_base.straight(-150)
      #drive_base.settings(500,200)
      #drive_base.straight(200)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(43,0.9,0.0004)
      drive_base.straight(370)


      drive_base.settings(800,9000)
      drive_base.straight(1000)
     
      drive_base.use_gyro(False)
    ''' drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      att_left_motor.run_angle(-400,210)
      curva(-44,0.4,0.0002)
      #drive_base.straight(-60)
      att_left_motor.run_angle(400,160)
      drive_base.straight(10)
      drive_base.straight(-30)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)'''
     # curva(,0.9,0.004)
  
    
   

#START 3
    if hub.buttons.pressed()==({Button.RIGHT} or {Button.LEFT})and color_sensor.color() == Color.BLUE:
     print('to aq 4')
     
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     drive_base.settings(500,500)
     drive_base.straight(520)
     drive_base.settings(600,900)
     
     att_right_motor.run_time(-4000,1300)
     drive_base.straight(-40)

     drive_base.straight(50)
     att_left_motor.run_time(400,2850)
     drive_base.straight(-40)
     att_right_motor.run_time(10000,1300)
     
     drive_base.straight(-200)
     drive_base.settings(600,9000)
     drive_base.straight(-400)

     drive_base.use_gyro(False)

# START 6
    if hub.buttons.pressed()=={Button.RIGHT} and color_sensor.color() == Color.WHITE:
      print('to aq 5')
      
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      drive_base.settings(600,500)
      drive_base.straight(280)
      curva(-25,0.9,0.0004)
      drive_base.straight(326)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(62.7,0.6,0.0003)
      att_right_motor.run_angle(800,-270)
      wait(700)
      drive_base.settings(900,800)

      drive_base.straight(196.5)
      wait(500)
      #att_right_motor.run_angle(800,620)
    
      att_right_motor.run_angle(800,270)
      #att_left_motor.run_angle(900,-130)
      #att_left_motor.run_angle(900,130)
      #att_left_motor.run_angle(900,-130)
      drive_base.settings(600,400)
      #drive_base.straight(25)
      wait(800)
      drive_base.straight(-120)
      wait(500)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(-30.5,0.1,0.0005)
      wait(500)
     # drive_base.straight(40)
      #curva(-30,0.9,0.003)
      drive_base.straight(-82)
      curva(-58,0.1,0.001)
      drive_base.settings(800,8000)
      drive_base.straight(-605)
      drive_base.use_gyro(False)
     
      #drive_base.curve()

# START 7
    if hub.buttons.pressed()=={Button.LEFT}and color_sensor.color() == Color.WHITE:
       print('to aq 6')
       
       att_right_motor.run_time(1200,800)
       drive_base.settings(600,500)
       drive_base.straight(690)
       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)
       curva(35,0.6,0.0003)
       drive_base.straight(234)
       att_right_motor.run_angle(-1200,400)
       drive_base.straight(200)
       drive_base.straight(-300)
    
    if hub.buttons.pressed()=={Button.RIGHT} and color_sensor.color() == Color.GREEN:
         print('to aq 7')

         #att_left_motor.run_angle(500,200)
         drive_base.use_gyro(False)
         hub.imu.reset_heading(0)
         drive_base.use_gyro(True)
         drive_base.settings(500,400)
         drive_base.straight(350)
         att_right_motor.run_angle(-1200,250)
         att_right_motor.run_angle(1200,250)
         wait(300)
         att_right_motor.run_angle(-1200,250)
         att_right_motor.run_angle(1200,250)
         wait(300)
         att_right_motor.run_angle(-1200,250)
         att_right_motor.run_angle(1200,250)
         wait(300)
         #att_right_motor.run_angle(1200,200)
         #att_right_motor.run_angle(-1200,200)
         #wait(300)
         drive_base.use_gyro(False)
         hub.imu.reset_heading(0)
         drive_base.use_gyro(True)
         curva(-40,0.7,0.0004)
         att_left_motor.run_angle(-800,200,wait=False)
         drive_base.settings(400,200)
         drive_base.straight(560)
         att_left_motor.run_angle(800,200)
         drive_base.settings(900,9000)
         drive_base.straight(-485)
         drive_base.use_gyro(False)
         hub.imu.reset_heading(0)
         drive_base.use_gyro(True)
         curva(28,0.7,0.0004)
         drive_base.settings(800,9000)
         drive_base.straight(-390)
         drive_base.use_gyro(False)


    if hub.buttons.pressed()=={Button.LEFT}and color_sensor.color() == Color.YELLOW:
       print('to aq 8')

       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)
       drive_base.settings(500,395)
       drive_base.straight(420)
      # att_left_motor.run_angle(400,100)
      # drive_base.straight(200)
       #drive_base.straight(415)
       #att_left_motor.run_angle(-800,500)
       #drive_base.straight(100)
       #curva(-41,0.9,0.0004)
       #drive_base.straight(407)
       
       att_left_motor.run_angle(-800,230)
       wait(500)
       att_right_motor.run_angle(-900,410)
       wait(500)
       #drive_base.straight(25)
       att_left_motor.run_angle(800,710)
       wait(500)
       drive_base.settings(800,1000)
       drive_base.straight(-35)
       drive_base.straight(45)
       drive_base.straight(-145)
       drive_base.straight(40)
       att_right_motor.run_angle(400,400)
       wait(500)
       drive_base.settings(400,300)
       drive_base.straight(26)
      # att_right_motor.run_angle(-900,410)
       #drive_base.straight(50)
       wait(600)

       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)

       curva(-30,0.9,0.004)
       wait(600)

      # drive_base.straight(-70)
       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       curva(27,0.9,0.004)
       drive_base.settings(800,9000)
       #drive_base.straight(-185)
       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)
       #curva(-10,0.9,0.004)
       drive_base.straight(-300)
       
       drive_base.use_gyro(False)

 
    if hub.buttons.pressed()=={Button.LEFT} and color_sensor.color() == Color.BLUE:
       print('to aq 9')

       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)
       drive_base.settings(500,400)
       drive_base.straight(630)
       wait (700)
       curva(33.6,0.7,0.0004)
       drive_base.settings(209,200)
       drive_base.straight(390)
       #curva(-30,0.9,0.0004)
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
