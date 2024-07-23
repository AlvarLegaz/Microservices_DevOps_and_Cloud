# Terraform

**Terraform** es una herramienta de Infraestructura como Código (IaC) que permite construir, cambiar y versionar la infraestructura de manera segura y eficiente[^1^][1]. Puede manejar componentes de bajo nivel como instancias de computación, almacenamiento y redes, así como componentes de alto nivel como entradas DNS y características de SaaS[^1^][1].

## Instalación en Ubuntu

Para instalar Terraform en Ubuntu, primero actualiza el sistema e instala los paquetes necesarios[^2^][14]. Luego, añade la clave GPG de HashiCorp e instala el repositorio oficial de HashiCorp para Linux[^2^][14]. Finalmente, instala la interfaz de línea de comandos de Terraform[^2^][14].

## Instalación en PowerShell de Linux

Para instalar Terraform en PowerShell de Linux, sigue los mismos pasos que para Ubuntu. Asegúrate de que el binario de Terraform esté disponible en tu PATH[^3^][21].

## Comandos de Terraform

- `terraform init`: Este comando inicializa un directorio de trabajo que contiene archivos de configuración de Terraform[^4^][5]. Es el primer comando que se debe ejecutar después de escribir una nueva configuración de Terraform o clonar una existente[^4^][5].
- `terraform plan`: Crea un plan de ejecución que te permite previsualizar los cambios que Terraform planea hacer en tu infraestructura[^5^][28].
- `terraform apply`: Ejecuta las acciones propuestas en un plan de Terraform[^6^][32]. Crea, actualiza o destruye recursos para que coincidan con el estado descrito en tu archivo de configuración[^6^][32].
- `terraform destroy`: Este comando destruye todos los objetos remotos administrados por una configuración de Terraform[^7^][22]. Es útil para limpiar toda la infraestructura temporal una vez que hayas terminado con tu trabajo[^7^][22].
