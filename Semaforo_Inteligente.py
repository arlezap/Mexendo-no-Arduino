// Definindo os pinos
const int pinLuzVerde = 8;    // Pino para o LED verde
const int pinLuzAmarela = 9; // Pino para o LED amarelo
const int pinLuzVermelha = 10; // Pino para o LED vermelho
const int pinBuzzer = 7;      // Pino para o buzzer


#define emissorTrig 6
#define recepEcho 5

long duracao;
int distancia;

// Definindo os tempos para cada fase
const int tempoVerde = 3000;   // Tempo da luz verde em milissegundos
const int tempoAmarelo = 1000; // Tempo da luz amarela em milissegundos
const int tempoVermelho = 3000; // Tempo da luz vermelha em milissegundos
const int tempoBuzzer = 100;   // Tempo do buzzer em milissegundos

void setup() {
  // Configurando os pinos como saída
  pinMode(pinLuzVerde, OUTPUT);
  pinMode(pinLuzAmarela, OUTPUT);
  pinMode(pinLuzVermelha, OUTPUT);
  pinMode(pinBuzzer, OUTPUT);
  pinMode(emissorTrig, OUTPUT);
  pinMode(recepEcho, INPUT);
  
  // Inicialmente, todos os LEDs e o buzzer estão desligados
  digitalWrite(pinLuzVerde, LOW);
  digitalWrite(pinLuzAmarela, LOW);
  digitalWrite(pinLuzVermelha, LOW);
  digitalWrite(pinBuzzer, LOW);

  Serial.begin(9600);
}


void loop() {
  dist();
  // Verifica se há movimento detectado pelo sensor
  if (digitalRead(distancia) == HIGH) {
    // Luz verde acende
    digitalWrite(pinLuzVerde, HIGH);
    
    // Aciona o buzzer em sequência
    for (int i = 0; i < 3; i++) {
      digitalWrite(pinBuzzer, HIGH);
      delay(tempoBuzzer);
      digitalWrite(pinBuzzer, LOW);
      delay(tempoBuzzer);
    }
    
    // Espera com a luz verde acesa e o buzzer em sequência
    delay(tempoVerde);
    
    // Desliga a luz verde
    digitalWrite(pinLuzVerde, LOW);
  }

  // Fase Amarela
  digitalWrite(pinLuzAmarela, HIGH);
  delay(tempoAmarelo);
  digitalWrite(pinLuzAmarela, LOW);

  // Fase Vermelha
  digitalWrite(pinLuzVermelha, HIGH);
  delay(tempoVermelho);
  digitalWrite(pinLuzVermelha, LOW);
}
void dist() {
  digitalWrite(emissorTrig, LOW);
  delayMicroseconds(2);
  digitalWrite(emissorTrig, HIGH);
  delayMicroseconds(10);
  digitalWrite(emissorTrig, LOW);
  duracao = pulseIn(recepEcho, HIGH);
  distancia = duracao * 0.034 / 2;
  Serial.println(distancia);
}