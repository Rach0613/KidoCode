void setup()
{
  pinMode(9, INPUT); //Echo
  pinMode(8, OUTPUT); //Trig
  Serial.begin(9600);
}

void loop()
{
  //Sensor
  //transmit to shoot
  digitalWrite(8, HIGH);
  delay(500);
  digitalWrite(8, LOW);

  int duration = pulseIn(9, HIGH);
  int distance = (duration/2)/29.1;

  Serial.print(distance);
  Serial.println("cm");

  //how fast or slow to print in Serial Monitor
  delay(500);

}