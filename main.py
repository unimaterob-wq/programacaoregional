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
# START 1
    if hub.buttons.pressed()==({Button.RIGHT} or {Button.LEFT})and color_sensor.color() == Color.RED:

     drive_base.settings(800,800)
     drive_base.straight(580)   
     drive_base.settings(800,800)
     drive_base.straight(-200)
     drive_base.settings(700,700)
     drive_base.straight(220)
     wait(1000)
     curva(-36,0.7,0.0004)
     wait(1000)
     drive_base.settings(400,300)
     drive_base.straight(250)
     att_right_motor.run_angle(-300,260)
     drive_base.straight(-250)
     curva(-81,0.7,0.0004)
     drive_base.straight(190)
     att_left_motor.run_angle(-300,200)
     drive_base.straight(-150)
     curva(-150,0.7,0.0004)
     drive_base.straight(400)
     drive_base.use_gyro(False)
    # hub.imu.reset_heading(0)
    # drive_base.use_gyro(True)

# START 2
    if hub.buttons.pressed()==({Button.RIGHT} or {Button.LEFT})and color_sensor.color() == Color.YELLOW:
     drive_base.settings(500,500)
     drive_base.straight(-775)
     drive_base.straight(47)
     wait(1000)
     curva(-73.5,0.5,0.0004)
     wait(1000)
     drive_base.settings(100,50)
     drive_base.straight(150)
     att_left_motor.run_angle(200,130, wait=False)
     att_right_motor.run_angle(-200,200)
     drive_base.settings(600,600)
     drive_base.straight(-160)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(85,0.7,0.0004)
     drive_base.settings(800,800)
     drive_base.straight(740)
     drive_base.use_gyro(False)
# START 3

    if hub.buttons.pressed()==({Button.RIGHT} or {Button.LEFT})and color_sensor.color() == Color.BLUE:
     drive_base.settings(600,500)
     drive_base.straight(435)
     drive_base.settings(800,800)
     drive_base.straight(-150)
     att_left_motor.run_angle(-300,252)
     drive_base.straight(140)
     drive_base.settings(700,600)
     drive_base.straight(-110)
     curva(-42,0.7,0.0004)
     drive_base.straight(270)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(36,0.7,0.0004)
     att_right_motor.run_angle(300,150)
     att_right_motor.run_angle(-300,150)
     att_left_motor.run_angle(300,240)
     drive_base.straight(535)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(-55,0.9,0.0003)
     drive_base.straight(15)
     att_left_motor.run_angle(-300,270)
     drive_base.straight(-110)
     att_left_motor.run_angle(300,240)
     drive_base.use_gyro(False)
     hub.imu.reset_heading(0)
     drive_base.use_gyro(True)
     curva(-44,0.7,0.004)
     drive_base.straight(190)
     drive_base.straight(-160)
     curva(-102,0.7,0.0004)
     drive_base.settings(800,800)
     drive_base.straight(-490)
     drive_base.use_gyro(False)

# START 4
    if hub.buttons.pressed()==({Button.RIGHT} or {Button.LEFT})and color_sensor.color() == Color.GREEN:
      drive_base.settings(500,400)
      drive_base.straight(610)
      #curva(5,0.9,0.003)
      #drive_base.straight(120)
      
      wait(700)
      curva(87,0.9,0.0002)
      drive_base.straight(40)
      att_right_motor.run_angle(-950,250)
      att_right_motor.run_angle(950,250)
      att_right_motor.run_angle(-950,250)
      att_right_motor.run_angle(950,250)
      att_right_motor.run_angle(-950,250)
      att_right_motor.run_angle(950,250)
      drive_base.straight(140)
      att_left_motor.run_angle(-200,460)
      drive_base.straight(80)
      att_left_motor.run_angle(200,460)
      drive_base.straight(-320)
      wait(700)
      drive_base.use_gyro(False)
      hub.imu.reset_heading(0)
      drive_base.use_gyro(True)
      curva(-85,0.9,0.0003)
      wait(1000)
      drive_base.settings(500,300)
      drive_base.straight(30)
      wait(1000)
      curva(-108,0.9,0.0003)
      drive_base.settings(-800,800)
      drive_base.straight(-500)
      

    
# START 5
    
    if hub.buttons.pressed()==({Button.RIGHT} or {Button.LEFT})and color_sensor.color() == Color.WHITE:
         att_left_motor.run_angle(500,200)
         drive_base.settings(500,400)
         drive_base.straight(-670)
         drive_base.use_gyro(False)
         hub.imu.reset_heading(0)
         drive_base.use_gyro(True)
         curva(85,0.6,0.0003)
         drive_base.straight(90)
         drive_base.use_gyro(False)
         hub.imu.reset_heading(0)
         drive_base.use_gyro(True)
         drive_base.straight(16)
         curva(-5.5,0.9,0.004)
         att_right_motor.run_angle(200,600)
         drive_base.straight(-730)
         drive_base.use_gyro(False)
         hub.imu.reset_heading(0)
         drive_base.use_gyro(True)
         drive_base.straight(70)
         drive_base.use_gyro(False)
         hub.imu.reset_heading(0)
         drive_base.use_gyro(True)
         curva(-49,0.9,0.002)
         drive_base.settings(800,600)
         drive_base.straight(380)
         drive_base.settings(500,400)
         drive_base.straight(-100)
         drive_base.use_gyro(False)
         hub.imu.reset_heading(0)
         drive_base.use_gyro(True)
         curva(42,0.9,0.0004)
         drive_base.straight(-110)
         att_left_motor.run_angle(-800,200)
         drive_base.use_gyro(False)
         hub.imu.reset_heading(0)
         drive_base.use_gyro(True)
         curva(-50,0.9,0.0004)
         drive_base.straight(400)
         drive_base.use_gyro(False)
         hub.imu.reset_heading(0)
         drive_base.use_gyro(True)
         curva(40,0.5,0.0003)
         drive_base.settings(800,800)
         drive_base.straight(500)
         drive_base.use_gyro(False)

#START 6
    if hub.buttons.pressed()=={Button.LEFT}and color_sensor.color() == Color.YELLOW:
       drive_base.settings(500,400)
       drive_base.straight(610)
       curva(-88,0.4,0.0001)
       drive_base.straight(470)
       att_right_motor.run_angle(-1000,2600)
       att_right_motor.run_angle(1000,2600)
       drive_base.straight(420)
       #att_left_motor.run_angle(500,300)

       curva(-147,0.9,0.0003)
       att_left_motor.run_angle(500,300)
       #att_left_motor.run_angle(-800,500)
       drive_base.straight(10)
       curva(-171,0.9,0.004)
       drive_base.straight(70)
       att_left_motor.run_angle(-800,270)
       wait(700)
       #att_left_motor.run_angle(-180,240)
       drive_base.straight(40)
       drive_base.straight(-30)
       att_right_motor.run_angle(-1000,2750)


 



    



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
