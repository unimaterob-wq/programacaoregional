from pybricks.pupdevices import Motor, ColorSensor, ForceSensor
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

sensor_toque = ForceSensor(Port.C)
hub = PrimeHub()


def moverPI (referência,velocidade, distância, kp, ki ):
    left_motor.reset_angle(0)
    integral=0
    velocidade=0
    conversor=365*distância/19.4   # TRANSFORMA OS GRAUS EM CENTÍMETROS
    while abs(left_motor.angle())<conversor:   # LOOP 
       erro =referência-hub.imu.heading()  #CÁLCULO DO ERRO
       integral = erro+integral #CÁLCULO DA INTEGRAL
       correção = (kp*erro)+(ki*integral) #CÁLCULO DA CORREÇÃO 
       left_motor.dc(correção+velocidade)  #VELOCIDADE DO MOTOR ESQUERDO
       right_motor.dc(correção+velocidade)  #VELOCIDADE DO MOTOR DIREITO
       if velocidade <= 200:  # LOOP DA VELOCIDADE
          velocidade = 200
    left_motor.stop() #MOTOR ESQUERDO PARAR
    right_motor.stop() #MOTOR DIREITO PARAR

def moverP (referência,velocidade, distância, kp):
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
    integral = 0  # DEFINE INTEGRAL PARA ZERO
    while abs(hub.imu.heading())<=abs(angulo):  #LOOP QUE LIMITA O MOVIMENTO DA CURVA
        erro = angulo-hub.imu.heading()  # CÁLCULO DO ERRO DA CURVA
        integral = erro+integral # CÁÇCULO DA INTEGRAL
        movimento = (kp*erro)+(ki*integral) #CÁLCULO DA CORREÇÃO DO MOVIMENTO
        left_motor.dc(movimento) #DIREÇÃO DO MOTOR ESQUERDO
        right_motor.dc(movimento*-1) #DIREÇÃO DO MOTOR DIREITO
    left_motor.stop()   # PARA MOTOR ESQUERDO
    right_motor.stop()  #PARA MOTOR DIREITO

distancia_percorrida = drive_base.distance()


while True:
    #print(color_sensor.color())
    #print (sensor_toque.force())
    
 
   # START 2
    if hub.buttons.pressed()==({Button.RIGHT} or {Button.LEFT})and color_sensor.color() == Color.RED and sensor_toque.force()>5:
     print('to aq 1')
    # moverPI(hub.imu.heading(),200,20,0.5,0.0004)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     drive_base.settings(700,700)
     drive_base.straight(640)
     drive_base.settings(450,800)
     drive_base.straight(-20)
     #drive_base.straight(20)
     curva(-40,0.9,0.0007)
     drive_base.straight(50)
     att_right_motor.run_angle(-500,330)
     att_left_motor.run_angle(500,187)
     drive_base.settings(450,400)
     drive_base.straight(60)
    # drive_base.turn(5)
     att_right_motor.run_angle(950,250)
    # drive_base.straight(-7)
     att_left_motor.run_angle(-300,460)

     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     drive_base.turn(-3)
     drive_base.straight(-140)

     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(48,0.9,0.0004)
    # drive_base.straight(-7)
   #  drive_base.straight(10)
     att_right_motor.run_angle(900,200)
     drive_base.straight(30)
     #wait(700)
     drive_base.straight(-50)
     curva(52,0.9,0.004)
     drive_base.settings(900,9000)
     drive_base.straight(-560)
     drive_base.use_gyro(False)

#START 1
    if hub.buttons.pressed()==({Button.RIGHT} or {Button.LEFT})and color_sensor.color() == Color.YELLOW and sensor_toque.force()>5:
     print('to aq 2')
  
      #att_left_motor.run_angle(900,600)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     drive_base.settings(700,900)
     drive_base.straight(620)
     curva(180,0.4,0.0002)
     drive_base.straight(-231)
     wait(500)
     drive_base.straight(27)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(-84.6,0.4,0.0002)
     wait(500)
     drive_base.settings(400,100)
     drive_base.straight(115)
     #att_left_motor.run_angle(800,48)
     drive_base.straight(31)

     att_left_motor.run_angle(800,120)

     att_right_motor.run_time(-900,800)
     wait(500)
     att_right_motor.run_time(900,700)

     drive_base.straight(-170)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(87,0.9,0.0004)
     drive_base.settings(900,9000)
     drive_base.straight(770)
     drive_base.use_gyro(False)
# outra prog
     '''drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     drive_base.settings(700,600)
     drive_base.straight(600)
     curva(180,0.4,0.0002)
     drive_base.straight(-251)
     wait(500)
     drive_base.straight(90)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(-85.6,0.4,0.0002)
     wait(500)
     drive_base.settings(400,100)
     drive_base.straight(125)
     #att_left_motor.run_angle(800,48)
     drive_base.straight(40)

     att_left_motor.run_angle(800,-120)

     att_right_motor.run_angle(400,400)
     att_right_motor.run_angle(800,-400)

     drive_base.straight(-180)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(90,0.9,0.0004)
     drive_base.settings(900,9000)
     drive_base.straight(680)
     drive_base.use_gyro(False)'''

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


#START 4
    if hub.buttons.pressed()=={Button.LEFT} and color_sensor.color() == Color.NONE and sensor_toque.force()>5:
      print('to aq 3')

      #att_left_motor.run_angle(700,150,wait=False)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      drive_base.settings(800,700)
      drive_base.straight(200)
      curva(42,0.9,0.0004)
      drive_base.straight(260)
      drive_base.settings(500,400)
      drive_base.straight(-160)
      #drive_base.settings(500,200)
      #drive_base.straight(200)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(45,0.9,0.0004)



      drive_base.settings(800,9000)
      drive_base.straight(800)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(5,0.2,0.003)
      drive_base.straight(570)
     
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
    if hub.buttons.pressed()==({Button.RIGHT} or {Button.LEFT})and color_sensor.color() == Color.BLUE and sensor_toque.force()>5:
     print('to aq 4')
     
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     drive_base.settings(500,500)
     drive_base.straight(520)
     drive_base.settings(600,900)
     
     att_right_motor.run_time(-4000,1500)
     drive_base.straight(-40)

     drive_base.straight(50)
     att_left_motor.run_time(400,2850)
     drive_base.straight(-40)
     att_right_motor.run_time(10000,1550)
     
     #drive_base.straight(-200)
     drive_base.settings(900,9000)
     drive_base.straight(-600)

     drive_base.use_gyro(False)

# START 6
    if hub.buttons.pressed()=={Button.RIGHT} and color_sensor.color() == Color.WHITE and sensor_toque.force()>5:
      print('to aq 5')


      att_right_motor.run_angle(400,90, wait=False)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      drive_base.settings(500,500)
      drive_base.straight(650)
      att_right_motor.run_angle(900,-300)
      drive_base.settings(700,600)
      drive_base.straight(150)
      att_right_motor.run_angle(400,300)
      drive_base.settings(600,700)
      drive_base.straight(-45)
      curva(-25,0.3,0.003)
      drive_base.straight(-30)
      wait(500)
      curva(-78,0.7,0.0003)
      wait(500)
      drive_base.settings(900,900)
      drive_base.straight(-200)
     # drive_base.straight(110)
      wait(300)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(-9,0.5,0.005)
      #drive_base.straight(-100)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      
      drive_base.straight(260)
      curva(76,0.5,0.0003)
      drive_base.settings(900,9000)
      drive_base.straight(-600)
      drive_base.use_gyro(False)


      '''att_right_motor.run_angle(400,-140, wait=False)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      drive_base.settings(600,700)
      drive_base.straight(265)
      curva(-27,0.9,0.0004)
      drive_base.settings(600,750)
      drive_base.straight(339)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(64,0.7,0.0003)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      wait(700)
      drive_base.straight(20)
      att_left_motor.run_angle(800,-250)
      wait(700)
      drive_base.settings(600,300)

      drive_base.straight(75)
      drive_base.settings(900,9000)
      drive_base.straight(105)
      drive_base.settings(400,300)
      wait(500)
      drive_base.straight(-25)
      drive_base.straight(25)
     
      wait(500)
      
      att_left_motor.run_angle(400,270)
      
      drive_base.settings(600,400)
     
      wait(500)
      drive_base.straight(-120)
      
      wait(500)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(-30,0.1,0.0005)
      att_right_motor.run_angle(800,135)
      wait(500)
     
      drive_base.straight(-130)
      curva(-53,0.1,0.001)
      drive_base.settings(900,9000)
      drive_base.straight(-500)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
     
      wait(400)
     
      drive_base.use_gyro(False)'''
      

# START 7
    if hub.buttons.pressed()=={Button.LEFT}and color_sensor.color() == Color.WHITE and sensor_toque.force()>5:
       print('to aq 6')
       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)
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
    
    if hub.buttons.pressed()=={Button.RIGHT} and color_sensor.color() == Color.GREEN and sensor_toque.force()>5:
         print('to aq 7')
        
         #att_left_motor.run_angle(500,200)
         drive_base.use_gyro(False)
         hub.imu.reset_heading(0)
         drive_base.use_gyro(True)
        # att_right_motor.run_angle(9000,190)
         drive_base.settings(500,400)
         drive_base.straight(320)
         att_right_motor.run_angle(10000,360)
         att_right_motor.run_angle(-10000,340)
         wait(400)
         att_right_motor.run_angle(10000,360)
         att_right_motor.run_angle(-10000,340)
         wait(400)
         att_right_motor.run_angle(10000,360)
         att_right_motor.run_angle(-10000,360)
         
         wait(400)
         #att_right_motor.run_angle(1200,200)
         #att_right_motor.run_angle(-1200,200)
         #wait(300)
         drive_base.use_gyro(False)
         hub.imu.reset_heading(0)
         drive_base.use_gyro(True)
         curva(-39,0.7,0.0004)
         att_left_motor.run_angle(800,200,wait=False)
         drive_base.settings(400,200)
         drive_base.straight(580)
         att_left_motor.run_angle(-800,300)
         drive_base.settings(900,9000)
         drive_base.straight(-485)
         drive_base.use_gyro(False)
         hub.imu.reset_heading(0)
         drive_base.use_gyro(True)
         curva(28,0.7,0.0004)
         drive_base.settings(800,9000)
         drive_base.straight(-390)
         drive_base.use_gyro(False)

  #start 5
    if hub.buttons.pressed()=={Button.LEFT}and color_sensor.color() == Color.YELLOW and sensor_toque.force()>5:
       print('to aq 8')

       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)
       drive_base.settings(500,395)
       drive_base.straight(420)
       #att_left_motor.run_angle(200,-250)
      # drive_base.straight(200)
       #drive_base.straight(415)
       #att_left_motor.run_angle(-800,500)
       #drive_base.straight(100)
       #curva(-41,0.9,0.0004)
       #drive_base.straight(407)
       wait(700)
       att_left_motor.run_time(9000,2150,wait=False)
       #wait(500)
       att_right_motor.run_angle(-900,410)
       wait(500)
       #drive_base.straight(25)
       att_left_motor.run_time(-1000,2950)
       wait(500)
       drive_base.settings(800,1000)
       drive_base.straight(-35)
       drive_base.straight(45)
       drive_base.straight(-145)
       drive_base.straight(40)
       att_right_motor.run_angle(900,400)
       wait(300)
       drive_base.settings(400,300)
       drive_base.straight(26)
      # att_right_motor.run_angle(-900,410)
       #drive_base.straight(50)
       wait(400)

       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)

       curva(-24,0.9,0.009)
       wait(400)
       drive_base.settings(-60)

      # drive_base.straight(-70)
       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       #curva(14.5,0.9,0.004)
       drive_base.settings(800,9000)
       #drive_base.straight(-185)
       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)
       curva(12,0.9,0.004)
       drive_base.settings(800,9000)
       drive_base.straight(-380)
       
       drive_base.use_gyro(False)

 
    if hub.buttons.pressed()=={Button.LEFT} and color_sensor.color() == Color.BLUE and sensor_toque.force()>5:
       print('to aq 9')

       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)
       drive_base.settings(500,400)
       drive_base.straight(680)
       wait (700)
       drive_base.use_gyro(False)
       hub.imu.reset_heading(0)
       drive_base.use_gyro(True)
       curva(33,0.7,0.0004)
       drive_base.settings(209,200)
       drive_base.straight(365)
       wait(500)
       #curva(-30,0.9,0.0004)
       drive_base.settings(800,900)
       drive_base.straight(-280)
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
    #indice_funcao = (indice_funcao + 1) % len(starts)  # Volta ao início ao alcançar o finalfrom pybricks.pupdevices import Motor, ColorSensor
