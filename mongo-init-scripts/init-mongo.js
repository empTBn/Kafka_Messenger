// script para inicializar la base de datos con algiu
// Conectarse a la base de datos
var db = db.getSiblingDB("MensajesDB");

// Crear la colección "topics" si no existe
db.topics.createIndex({ topic: '' }, { unique: true });

/* Insertar la encuesta en la colección "topics"

--NOTA: esto es un ejemplo de como se veria la estructura de la base de datos
  si se pudiera elegir un canal ya existente, que por el problema de que khafka-python
  de no recibir el topic desde un atributo de la clase controller no podemos hacerlo, o sea, 
  no deja guardar un 'current topic' para que todos los mensaje se escriban y lean sobre ese topic 
  seleccionado.



db.topics.insertMany([
  {
    topic: "Canal 1",
    mensajes: [
      {
        timestamp: "",
        autor: "Crisac",
        texto:" texto de ejemplo",
      },
      {
        timestamp: "",
        autor: "Samuel",
        texto:" texto de ejemplo",
      },
    ],
  },
  {
    topic: "canal 2",
    mensajes: [
      {
        timestamp: "",
        autor: "Crisac",
        texto:" texto de ejemplo",
      },
      {
        timestamp: "",
        autor: "Erick",
        texto:" texto de ejemplo",
      },
    ],
  },
]);

  */