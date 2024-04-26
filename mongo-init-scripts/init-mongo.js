// script para inicializar la base de datos con algunos topics
// Conectarse a la base de datos
var db = db.getSiblingDB("MensajesDB");

// Crear la colección "topics" si no existe
db.topics.createIndex({ topic: '' }, { unique: true });

db.topics.insertMany([
  {
    topic: "General",
    mensajes: [],
  },,
  {
    topic: "Canal",
    mensajes: [],
  },
  {
    topic: "Canal2",
    mensajes: [],
  },
]);