#define JOY_X A4
#define JOY_Y A5
#define JOY_Z 4

int tps = 20;

const int count = 3;
String labels[count] = {
  "joy_y",
  "joy_x",
  "joy_b"
};

int values[count] {
  0,
  0,
  0
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
}

void loop () {
  values[0] = analogRead(JOY_X);
  values[1] = analogRead(JOY_Y);
  values[2] = !digitalRead(JOY_Z);
  
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
