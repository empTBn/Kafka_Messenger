from app_service import AppService


def main():
    # Configuración
    db_name = "my_db"
    collection_name = "messages"
    kafka_bootstrap_servers = "localhost:9092"
    topic = "my_topic"

    # Inicialización del servicio de la aplicación
    app_service = AppService(db_name, collection_name, kafka_bootstrap_servers)

    while True:
        # Menú de opciones
        print("1. Enviar mensaje")
        print("2. Leer mensajes")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mensaje = input("Ingrese el mensaje a enviar: ")
            app_service.send_message(mensaje, topic)
            print("Mensaje enviado correctamente.")
        elif opcion == "2":
            print("Mensajes almacenados en MongoDB:")
            mensajes = app_service.read_messages()
            for mensaje in mensajes:
                print(mensaje)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
