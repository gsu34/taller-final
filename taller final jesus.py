class Envio:
    def __init__(self, peso_kg: float, distancia_km: float):
        self.peso_kg = peso_kg
        self.distancia_km = distancia_km

    def calcular_costo(self, monto_base: float) -> float:
        """Método que será sobrescrito por las subclases (polimorfismo)."""
        raise NotImplementedError("Las subclases deben implementar calcular_costo")


class EnvioEstandar(Envio):
    def calcular_costo(self, monto_base: float) -> float:
        """Aplica un recargo del 5% sobre el monto base."""
        return monto_base * 1.05


class EnvioExpress(Envio):
    def calcular_costo(self, monto_base: float) -> float:
        """Aplica un recargo del 15% por servicio prioritario."""
        return monto_base * 1.15


# ---------- Prueba del Ejercicio 2 ----------
if __name__ == "__main__":
    print("\n=== EJERCICIO 2 ===")

    # Lista mixta de envíos (polimorfismo)
    envios = [
        EnvioEstandar(peso_kg=2.5, distancia_km=120),
        EnvioExpress(peso_kg=1.0, distancia_km=80),
        EnvioEstandar(peso_kg=5.0, distancia_km=300),
        EnvioExpress(peso_kg=3.2, distancia_km=450),
    ]

    monto_base = 20000  # ejemplo de monto base del paquete

    print(f"Monto base del paquete: ${monto_base:,.0f}\n")

    for i, envio in enumerate(envios, 1):
        costo = envio.calcular_costo(monto_base)
        tipo = type(envio).__name__
        print(f"Envío {i} ({tipo}):")
        print(f"  Peso: {envio.peso_kg} kg | Distancia: {envio.distancia_km} km")
        print(f"  Costo final: ${costo:,.2f}\n")
        
        