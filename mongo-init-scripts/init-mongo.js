// init-mongo.js

// Conectarse a la base de datos
var db = db.getSiblingDB("MensajesDB");

// Crear la colección "topics" si no existe
db.topics.createIndex({ topic: 1 }, { unique: true });

// Insertar la encuesta en la colección "topics"
db.topics.insertMany([
  {
    topic: "Canal_Alterno",
    mensajes: [],
  },
  {
    topic: "Canal_BasesII",
    mensajes: [],
  },
  {
    topic: "General",
    mensajes: [],
  },
]);