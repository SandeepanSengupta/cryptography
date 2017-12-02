void setup()
{
  Serial.begin(9600);
}

void loop()
{
  while (Serial.available() > NULL)
  {
    Serial.write(Serial.read());
    Serial.flush();
  }
}
