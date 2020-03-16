int red=6;
int green=5;
int blue=3;
void setup() {
  pinMode(red,OUTPUT);
  pinMode(green,OUTPUT);
  pinMode(blue,OUTPUT);

}

void rgb(int x,int y,int z){
  analogWrite(red,x);
  analogWrite(green,y);
  analogWrite(blue,z);
}

void loop() {

  while(digitalRead(2)==HIGH){
    rgb(0,0,255);
  }
  while(digitalRead(2)==LOW){
    //null statement
  }
  while(digitalRead(2)==HIGH){
    rgb(0,255,0);
  }
  while(digitalRead(2)==LOW){
    //null statement
  }
  while(digitalRead(2)==HIGH){
    rgb(255,0,0);
  }
  while(digitalRead(2)==LOW){
    //null statement
  }
}
