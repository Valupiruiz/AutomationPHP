# Automation SomosAgro
Este repositorio contiene (o contendrá, je) la automatización mobile y web de la app y backend de Somos Agro.

## Requisitos
#### Para web:
- Python 3.7 o +
- Descargarse el [chromedriver](https://chromedriver.chromium.org/downloads) *(según la versión que tengas instalada de Chrome en tu PC)*.
#### Para mobile:
- Python 3.7 o +
- Appium 1.15 o +
- Android Studio (o en su defecto el Android SDK)
- Node.js
- Veremos que más

## Esquema Appium
```mermaid
graph LR
A[Dispositivo] --> B[AppiumApp]
B --> C[Appium Server]
C --> D[Código Python]
C --> B
B --> A
D --> C
```