import os
import yaml
import logging
from datetime import datetime

logger = logging.getLogger("agentkit")


def cargar_info_negocio() -> dict:
    try:
        with open("config/business.yaml", "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        logger.error("config/business.yaml no encontrado")
        return {}


def obtener_horario() -> dict:
    """Retorna el horario de atención y si está abierto ahora."""
    ahora = datetime.now()
    dia_semana = ahora.weekday()  # 0=lunes, 6=domingo
    hora = ahora.hour

    # Lunes a sábado (0-5), 8am a 9pm
    esta_abierto = (
        dia_semana <= 5 and  # no domingo
        8 <= hora < 21
    )

    return {
        "horario": "Lunes a sábado 8:00 AM a 9:00 PM (hora Colombia)",
        "esta_abierto": esta_abierto,
        "dia_actual": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"][dia_semana],
    }


def registrar_lead(telefono: str, nombre: str, interes: str, presupuesto: str = "") -> str:
    """Registra un lead interesado en los servicios de No-Set."""
    logger.info(f"Nuevo lead — Tel: {telefono} | Nombre: {nombre} | Interés: {interes} | Presupuesto: {presupuesto}")
    return f"Lead registrado: {nombre} interesado en {interes}"


def registrar_brief(telefono: str, servicio: str, descripcion: str, plataforma: str, fecha_entrega: str) -> str:
    """Registra el brief de un proyecto nuevo."""
    logger.info(
        f"Nuevo brief — Tel: {telefono} | Servicio: {servicio} | "
        f"Descripción: {descripcion} | Plataforma: {plataforma} | Entrega: {fecha_entrega}"
    )
    return f"Brief recibido para {servicio}. El equipo se pondrá en contacto para confirmar detalles."


def obtener_precios() -> dict:
    """Retorna el catálogo de precios de No-Set Creative Studio."""
    return {
        "video_comercial": {"min": 250000, "max": 450000, "entrega": "24-72h"},
        "ugc": {"min": 180000, "max": 350000, "entrega": "24-72h"},
        "vfx_motion": {"min": 350000, "max": 900000, "entrega": "24-72h"},
        "visualizacion_arq": {"min": 150000, "max": 400000, "entrega": "24h"},
        "foto_producto_ia": {"min": 200000, "max": 350000, "entrega": "24h"},
        "logo_identidad": {"min": 200000, "max": 500000, "entrega": "24-48h"},
        "paquetes": {
            "starter": {"precio": 500000, "videos": 4, "imagenes": 8},
            "pro": {"precio": 1200000, "videos": 8, "imagenes": 20, "vfx": 1},
            "studio": {"precio": 2200000, "videos": 15, "imagenes": 40, "vfx": 2},
        }
    }
