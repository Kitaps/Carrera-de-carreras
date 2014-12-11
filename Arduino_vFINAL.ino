#include <Stepper.h>

//CONFIGURACION
int steps_parado=500; //Steps desde tirado hasta parado
//CONFIGURACION


/*-----( Import needed libraries )-----*/
/*-----( Declare Constants and Pin Numbers )-----*/
#define FULLSTEP 4
#define HALFSTEP 8
// motor pins
#define motorPin1  4     // Blue   - 28BYJ48 pin 1
#define motorPin2  5     // Pink   - 28BYJ48 pin 2
#define motorPin3  6     // Yellow - 28BYJ48 pin 3
#define motorPin4  7     // Orange - 28BYJ48 pin 4
                        // Red    - 28BYJ48 pin 5 (VCC)
                        
#define motorPin5  8     // Blue   - 28BYJ48 pin 1
#define motorPin6  9     // Pink   - 28BYJ48 pin 2
#define motorPin7  10    // Yellow - 28BYJ48 pin 3
#define motorPin8  11    // Orange - 28BYJ48 pin 4
                        // Red    - 28BYJ48 pin 5 (VCC)
/*-----( Declare objects )-----*/
// NOTE: The sequence 1-3-2-4 is required for proper sequencing of 28BYJ48
Stepper stepper1(HALFSTEP, motorPin1, motorPin3, motorPin2, motorPin4);
Stepper stepper2(HALFSTEP, motorPin5, motorPin7, motorPin6, motorPin8);

/*-----( Declare Variables )-----*/
int step1=0;
int step2=0;
int estado=0;

void setup(){
  Serial.begin(9600); // set the baud rate
  //En el de la izquierda (1) - es subida, + es bajada
  //En el de la derecha (2) + es subida, - es bajada
  
  //stepper2.setSpeed(700); //sube el de la derecha + es subida
  //stepper2.step(-128);
  //stepper1.setSpeed(700); //sube el de la izquierda - es subida
  //stepper1.step(-256);  // 1 revolution
   
}//--(end setup )---


void loop(){
  if(Serial.available()){ 
    char msj = Serial.read();
    if (msj == 'c'){ //Si el valor despues de "c" es 0 entonces terminar comparación
      estado=Serial.parseInt();
      if (estado==0){
        Serial.print(estado);
        delay(8000);
        }
    }
    if (msj == 'a'){
      step1=Serial.parseInt();
      Serial.print(-step1);
      stepper1.setSpeed(600); 
      stepper1.step(-step1);
    }
    if (msj == 'b'){
      step2=Serial.parseInt();
      Serial.print(step2);
      stepper2.setSpeed(600); //sube el de la derecha + es subida
      stepper2.step(step2);
    }
    if (msj=='n'){
      Serial.println(" ");
    }
  }
}//--(end main loop )---


