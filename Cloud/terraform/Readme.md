# Terraform

**Terraform** es una herramienta de Infraestructura como Código (IaC) que permite construir, cambiar y versionar la infraestructura de manera segura y eficiente. Puede manejar componentes de bajo nivel como instancias de computación, almacenamiento y redes, así como componentes de alto nivel como entradas DNS y características de SaaS.

## Instalación en Ubuntu

Para instalar Terraform en Ubuntu, primero actualiza el sistema e instala los paquetes necesarios. Luego, añade la clave GPG de HashiCorp e instala el repositorio oficial de HashiCorp para Linux. Finalmente, instala la interfaz de línea de comandos de Terraform.

## Instalación en PowerShell de Linux

Para instalar Terraform en PowerShell de Linux, sigue los mismos pasos que para Ubuntu. Asegúrate de que el binario de Terraform esté disponible en tu PATH.

## Comandos de Terraform

- `terraform init`: Este comando inicializa un directorio de trabajo que contiene archivos de configuración de Terraform. Es el primer comando que se debe ejecutar después de escribir una nueva configuración de Terraform o clonar una existente.
- `terraform plan`: Crea un plan de ejecución que te permite previsualizar los cambios que Terraform planea hacer en tu infraestructura.
- `terraform apply`: Ejecuta las acciones propuestas en un plan de Terraform. Crea, actualiza o destruye recursos para que coincidan con el estado descrito en tu archivo de configuración.
- `terraform destroy`: Este comando destruye todos los objetos remotos administrados por una configuración de Terraform. Es útil para limpiar toda la infraestructura temporal una vez que hayas terminado con tu trabajo.
