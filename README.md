# SAEYogaApp

Aplicación móvil enfocada en introducir a principiantes al yoga con clases guiadas y recordatorios diarios. Este repositorio almacena el código y la documentación inicial del proyecto.

## Características previstas
- Rutinas guiadas en video y audio para distintos niveles.
- Recordatorios personalizables para mantener la constancia.
- Seguimiento básico del progreso del usuario.
- Biblioteca de poses con explicación de beneficios y contraindicaciones.
- Modo sin conexión para acceder a rutinas descargadas.
- Integración opcional con recordatorios del sistema.

## Stack sugerido
- **React Native + Expo** para desarrollo móvil multiplataforma.
- **TypeScript** para tipado estático.
- **React Navigation** para la estructura de pantallas.
- **AsyncStorage** o similar para persistencia local ligera.

## Cómo ejecutar (propuesta)
1. Instala dependencias globales si aún no las tienes:
   ```bash
   npm install -g expo-cli
   ```
2. Instala dependencias del proyecto:
   ```bash
   npm install
   ```
3. Inicia el servidor de desarrollo:
   ```bash
   npx expo start
   ```
4. Escanea el QR con la app Expo Go o usa un emulador de iOS/Android.

## Publicar el proyecto en GitHub
Si todavía no has subido el repositorio a GitHub, estos pasos te sirven de guía rápida:
1. Inicializa Git en la carpeta del proyecto y revisa el estado:
   ```bash
   git init
   git status
   ```
2. Crea un repositorio vacío en GitHub (sin README ni LICENSE) y copia la URL HTTPS o SSH.
3. Conecta el remoto y sube la rama principal:
   ```bash
   git remote add origin <url-del-repo>
   git branch -M main           # opcional: renombrar la rama a main
   git add .
   git commit -m "Initial commit: subir SAEYogaApp"
   git push -u origin main
   ```

## Configuración básica del repositorio
1. Clona el proyecto:
   ```bash
   git clone <url-del-repo>
   cd SAEYogaApp
   ```
2. Crea una rama para tu trabajo antes de empezar a modificar el código:
   ```bash
   git checkout -b nombre-de-tu-rama
   ```
3. Revisa el estado de los cambios y confirma tus commits con mensajes claros:
   ```bash
   git status
   git add .
   git commit -m "Descripción breve del cambio"
   ```

## Contribuir
- Sigue el flujo de trabajo por ramas y solicita revisiones mediante Pull Requests.
- Añade documentación para cualquier funcionalidad nueva.
- Usa mensajes de commit descriptivos y en español.
- Incluye pruebas o pasos de verificación cuando añadas funcionalidades.
- Respeta el formato y la estructura de componentes al enviar código React Native.

## Roadmap inicial
- [ ] Configurar proyecto base con Expo y TypeScript.
- [ ] Implementar navegación principal (Inicio, Rutinas, Biblioteca, Perfil).
- [ ] Crear pantalla de onboarding con selección de nivel y objetivos.
- [ ] Añadir primeras rutinas guiadas y biblioteca de poses.
- [ ] Configurar almacenamiento local para progreso y recordatorios.
