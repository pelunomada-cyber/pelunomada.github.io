# beer_bot.py
import datetime

def tomar_pedido():
    print("--- Cervecería El Champaquí | Sistema de Pedidos ---")
    cervezas = {
        "1": "IPA Montañesa",
        "2": "Stout del Valle",
        "3": "Golden Traslasierra"
    }
    
    print("\nMenú disponible:")
    for id, nombre in cervezas.items():
        print(f"{id}. {nombre}")
    
    seleccion = input("\nSeleccione el número de la cerveza: ")
    cantidad = input("¿Cuántas pintas?: ")
    nombre_cliente = input("Nombre para el pedido: ")
    
    if seleccion in cervezas:
        pedido = f"{datetime.datetime.now()} | Cliente: {nombre_cliente} | Producto: {cervezas[seleccion]} | Cantidad: {cantidad}\n"
        
        # Simulación de guardado en base de datos local (archivo .txt)
        with open("log_pedidos.txt", "a") as f:
            f.write(pedido)
            
        print("\n[ÉXITO] Pedido registrado y enviado a barra.")
    else:
        print("\n[ERROR] Selección no válida.")

if __name__ == "__main__":
    tomar_pedido()
