import requests
import json
import time

BASE_URL = "http://localhost:8080"


def print_separator(title):
    print("=" * 50)
    print(f"🧪 {title}")
    print("=" * 50)


def test_404_error():
    """Prueba error 404 - Tarea no encontrada"""
    print("\n1️⃣ GENERANDO ERROR 404 - Recurso No Encontrado")
    response = requests.put(f"{BASE_URL}/api/tasks/999/complete")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    return response.status_code == 404


def test_400_error():
    """Prueba error 400 - JSON malformado"""
    print("\n2️⃣ GENERANDO ERROR 400 - Solicitud Malformada")

    # JSON vacío
    response = requests.post(f"{BASE_URL}/api/tasks", json={})
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    return response.status_code == 400


def test_500_error():
    """Prueba error 500 - Error interno del servidor"""
    print("\n3️⃣ GENERANDO ERROR 500 - Error Interno del Servidor")
    response = requests.post(f"{BASE_URL}/api/tasks/simulate-error")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    return response.status_code == 500


def check_error_stats():
    """Ver estadísticas de errores"""
    print("\n📊 ESTADÍSTICAS DE ERRORES:")
    response = requests.get(f"{BASE_URL}/errors/stats")
    if response.status_code == 200:
        stats = response.json()
        print(f"   Total errores: {stats['total_errors']}")
        print(f"   Tipos de errores: {stats['error_types']}")
        print("\n   Errores recientes:")
        for error in stats['recent_errors'][-3:]:
            print(f"     • {error['timestamp']}: {error['type']}")
            print(f"       {error['message']} ({error['endpoint']})")
    return stats


def main():
    print_separator("DEMOSTRACIÓN DE DETECCIÓN DE ERRORES")

    # Ejecutar todas las pruebas
    errors_generated = []

    if test_404_error():
        errors_generated.append("404")

    if test_400_error():
        errors_generated.append("400")

    if test_500_error():
        errors_generated.append("500")

    time.sleep(1)  # Esperar a que se registren los errores

    # Mostrar estadísticas finales
    print_separator("RESULTADOS")
    stats = check_error_stats()

    print(f"\n✅ ERRORES GENERADOS: {', '.join(errors_generated)}")
    print(f"🎯 TOTAL DETECTADOS: {stats['total_errors']}")

    print_separator("DASHBOARD")
    print(f"🌐 Dashboard: {BASE_URL}/errors/dashboard")
    print(f"📊 API JSON: {BASE_URL}/errors/stats")


if __name__ == "__main__":
    main()