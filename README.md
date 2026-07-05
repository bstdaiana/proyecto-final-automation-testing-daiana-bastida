\# Proyecto Final - Automation Testing



\*\*Alumna:\*\* Daiana Bastida

\*\*Curso:\*\* Talento Lab - Módulo de Automation

\*\*Sitio de prueba (UI):\*\* \[saucedemo.com](https://www.saucedemo.com/)

\*\*API de prueba:\*\* \[JSONPlaceholder](https://jsonplaceholder.typicode.com/)



Framework de automatización de pruebas en Python que combina testing de UI (Selenium WebDriver) y de API (Requests), estructurado con el patrón \*\*Page Object Model (POM)\*\*, generación de reportes HTML, logging y captura automática de screenshots en fallos.



\## Tecnologías



\- Python 3.13

\- Pytest

\- Selenium WebDriver

\- Requests

\- pytest-html

\- Git / GitHub



\## Estructura del proyecto
proyecto-final-automation-testing-daiana-bastida/

├── pages/                  # Page Objects (POM)

│   ├── login\_page.py

│   └── inventory\_page.py

├── tests/

│   ├── conftest.py         # Fixture del driver + hook de screenshots en fallos

│   ├── ui/                 # Casos de prueba de UI

│   │   ├── test\_01\_login.py

│   │   ├── test\_02\_checkout.py

│   │   ├── test\_03\_remove\_from\_cart.py

│   │   └── test\_04\_sort\_products.py

│   └── api/                # Casos de prueba de API

│       └── test\_reqres\_api.py

├── data/

│   └── users.json          # Datos parametrizados de login

├── screenshots/             # Capturas automáticas de tests fallidos

├── logs/                    # Logs de ejecución

├── reports/                  # Reportes HTML generados por pytest-html

├── pytest.ini

└── requirements.txt





\## Instalación



```bash

git clone https://github.com/bstdaiana/proyecto-final-automation-testing-daiana-bastida.git

cd proyecto-final-automation-testing-daiana-bastida

python -m venv .venv

.venv\\Scripts\\Activate.ps1

pip install -r requirements.txt

```



Requiere tener \*\*Google Chrome\*\* instalado (Selenium 4 gestiona el ChromeDriver automáticamente).



\## Ejecución de las pruebas



```bash

\# Correr toda la suite (UI + API)

pytest -v



\# Solo pruebas de UI

pytest tests/ui -v



\# Solo pruebas de API

pytest tests/api -v

```



El reporte HTML se genera automáticamente en `reports/report.html`. Los logs de ejecución quedan en `logs/execution.log`. Ante cualquier fallo en un test de UI se guarda un screenshot en `screenshots/` con el nombre del test y timestamp.



\## Casos de prueba implementados



\### UI (Selenium)

| Archivo | Descripción |

|---|---|

| test\_01\_login.py | Login parametrizado (válido e inválido) vía `data/users.json` |

| test\_02\_checkout.py | Flujo de agregar producto y completar checkout |

| test\_03\_remove\_from\_cart.py | Agregar y eliminar producto del carrito |

| test\_04\_sort\_products.py | Ordenamiento de productos por precio |



\### API (Requests) — JSONPlaceholder

| Caso | Método |

|---|---|

| Obtener post existente, validar estructura | GET |

| Post inexistente devuelve 404 | GET (negativo) |

| Crear post nuevo | POST |

| Eliminar post | DELETE |

| Encadenamiento: crear post y luego listar | POST + GET |



\## Próximos pasos / mejoras propuestas



\- Integrar GitHub Actions para correr los tests en cada push.

\- Sumar más escenarios negativos de API (400, 422).

\- Ampliar cobertura de UI a búsqueda y navegación entre productos.

