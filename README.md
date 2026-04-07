# Actuación en clase - GitHub Actions y Docker (DEMO)

## Objetivo

Diagnosticar y corregir los problemas en un pipeline de CI/CD existente que utiliza GitHub Actions y Docker para conseguir un flujo de integración y despliegue funcional.

## Contexto

Se te ha entregado un repositorio con una aplicación web simple y un pipeline de CI/CD implementado con GitHub Actions y Docker. Sin embargo, el pipeline tiene varios problemas que debes identificar y corregir para que funcione correctamente.

## Problemas a resolver

El pipeline actual tiene los siguientes componentes, pero ninguno funciona correctamente:

### 1. Integración Continua
- [  ] El workflow no se activa correctamente con push y pull requests sobre la rama main
- [  ] Faltan los permisos para poder ejecutar el build y publish a  GitHub Container Registry (*)
- [  ] Python se encuentra actualizado
- [  ] Revisar la configuración de pytest

### 2. Docker
- [  ] Imagen de Python con vulnerabilidades
- [  ] Revisar copia de requirements.txt
- [  ] Corregir error al ejecutar la aplicación

### 3. APP
- [  ] Confirmar puerto por defecto de Flask
- [  ] Los mensajes deben ser en inglés

### 4. TEST
- [  ] Solucionar comportamiento del test

## Estructura del repositorio

```
├── app/                    # Código fuente de la aplicación
│   ├── main.py             # Aplicación simple en Python
│   └── test_main.py        # Pruebas unitarias
├── .github/
│   └── workflows/          # Contiene el workflow ci-cd.yml (tiene errores)
├── Dockerfile              # Dockerfile 
├── README.md               # Este archivo
└── requirements.txt        # Dependencias de la aplicación
```

## Evaluación

Tu solución se evaluará automáticamente según los siguientes criterios:
1. El pipeline se ejecuta correctamente sin errores
2. Todos los problemas identificados han sido corregidos
3. La imagen Docker se construye y publica correctamente
4. Las pruebas automáticas se ejecutan y pasan
5. El flujo implementa las prácticas de seguridad requeridas

Recibirás puntos por cada problema que identifiques y corrijas correctamente.

## Entrega

Para completar el ejercicio:
1. Acepta la asignación a través del enlace proporcionado
2. Clona el repositorio generado
3. Identifica y corrige todos los problemas en:
   - El archivo de workflow (.github/workflows/ci-cd.yml)
4. Haz commit y push de tus cambios
5. Verifica que el pipeline funcione correctamente en la pestaña "Actions"

¡Buena suerte!
