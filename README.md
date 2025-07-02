# Lawyer System

Sistema de gestión para abogados basado en FastAPI con Clean Architecture y soporte multi-tenant.

## Requisitos

- Python 3.11+
- Docker y Docker Compose
- PostgreSQL (si no usas Docker)

## Instalación en Local

### Opción 1: Usando Docker

1. **Clonar el repositorio** (si aplica) o crear la estructura de carpetas con los archivos proporcionados.

2. **Crear archivo `.env`**:
   Copia el contenido de `.env` proporcionado y actualiza `SECRET_KEY` con una clave segura.

3. **Construir y ejecutar**:
   ```bash
   docker-compose up --build