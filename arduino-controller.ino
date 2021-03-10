//#include <Wire.h>

//const int MPU_ADDRESS = 0x68;
//float elapsedTime, currentTime, previousTime;

#define JOY_X A6
#define JOY_Y A7
#define JOY_Z 4

int tps = 20;

const int count = 3;
String labels[count] = {
  "joy_y",
  "joy_x",
  "joy_b",
//  "acc_x",
//  "acc_y",
//  "acc_z",
//  "gyro_x",
//  "gyro_y",
//  "gyro_z"
};

float values[count] {
  0, 0, 0, //joystick
//  0, 0, 0, //acceleration
//  0, 0, 0 //gyroscope
};

/*
auto functions[count] = {
  [&]() { return analogRead(JOY_X); },
  [&]() { return analogRead(JOY_Y); },
  [&]() { return !digitalRead(JOY_Z); }
};
*/
 
void setup () {
  pinMode (JOY_X, INPUT);
  pinMode (JOY_Y, INPUT);  
  pinMode (JOY_Z, INPUT_PULLUP);

  Serial.begin (9600);

//  Wire.begin();
//  Wire.beginTransmission(MPU_ADDRESS);
//  Wire.write(0x6B);
//  Wire.write(0x00);
//  Wire.endTransmission(true);

  delay(20);
}

void loop () {
  values[0] = analogRead(JOY_X);
  values[1] = analogRead(JOY_Y);
  values[2] = !digitalRead(JOY_Z);

  // Get acceleration
//  Wire.beginTransmission(MPU_ADDRESS);
//  Wire.write(0x3B); //start with ACCEL_XOUT_H register
//  Wire.endTransmission(false);
//  Wire.requestFrom(MPU_ADDRESS, 6, true); //read 6 registers
//  values[3] = (Wire.read() << 8 | Wire.read()) / 16384.0;
//  values[4] = (Wire.read() << 8 | Wire.read()) / 16384.0;
//  values[5] = (Wire.read() << 8 | Wire.read()) / 16384.0;

  // Get gyroscope
//  previousTime = currentTime;
//  currentTime = millis();
//  elapsedTime = (currentTime - previousTime) / 1000;
//  Wire.beginTransmission(MPU_ADDRESS);
//  Wire.write(0x43); //start at gyroscope register
//  Wire.endTransmission(false);
//  Wire.requestFrom(MPU_ADDRESS, 6, true);
//  values[6] = (Wire.read() << 8 | Wire.read()) / 131.0;
//  values[7] = (Wire.read() << 8 | Wire.read()) / 131.0;
//  values[8] = (Wire.read() << 8 | Wire.read()) / 131.0;
  
  Serial.print("{");
  for (int i = 0; i < count; i++) {
    Serial.print("\"");
    Serial.print(labels[i]);
    Serial.print("\":");
    Serial.print(values[i]);

    if (i < count - 1) {
      Serial.print(",");
    }
  }
  Serial.print("}");
  Serial.println();

  delay(1/tps*1000);
}
