// init-mongo.js

// Conectarse a la base de datos
var db = db.getSiblingDB("MensajesDB");

// Crear la colección "topics" si no existe
db.topics.createIndex({ id_topic: 1 }, { unique: true });

// Insertar la encuesta en la colección "topics"
db.topics.insertMany([
  {
    id_topic: "1",
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
    id_topic: "2",
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