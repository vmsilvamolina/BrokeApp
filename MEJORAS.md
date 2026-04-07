# Mejoras pendientes

## Docker

- **`HEALTHCHECK`** en el Dockerfile — Docker verifica que el contenedor responda en `/ping`
  ```dockerfile
  HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:5000/ping || exit 1
  ```

## CI/CD (workflow)

- **Cache de pip** — agregar `cache: 'pip'` en el step `setup-python`, enseña optimización de pipelines
  ```yaml
  - name: Set up Python
    uses: actions/setup-python@v6
    with:
      python-version: '3.13'
      cache: 'pip'
  ```

- **Linting con `ruff` o `flake8`** — paso extra antes de los tests, introduce el concepto de quality gates
  ```yaml
  - name: Lint with ruff
    run: |
      pip install ruff
      ruff check app/
  ```

- **Escaneo de imagen con Trivy** — step que escanea vulnerabilidades de la imagen, introduce DevSecOps
  ```yaml
  - name: Scan image with Trivy
    uses: aquasecurity/trivy-action@master
    with:
      image-ref: ghcr.io/${{ github.repository }}:latest
      exit-code: '1'
      severity: 'CRITICAL,HIGH'
  ```

## App

- **Endpoint `/version`** — retorna versión leída de env var, útil para verificar qué versión está deployada
  ```python
  import os

  @app.route('/version')
  def version():
      return jsonify({
          "version": os.getenv("APP_VERSION", "dev"),
          "environment": os.getenv("ENVIRONMENT", "local")
      })
  ```

## Infraestructura local

- **`docker-compose.yml`** — para correr la app localmente con un comando
  ```yaml
  services:
    app:
      build: .
      ports:
        - "5000:5000"
      environment:
        - ENVIRONMENT=local
        - APP_VERSION=dev
  ```
