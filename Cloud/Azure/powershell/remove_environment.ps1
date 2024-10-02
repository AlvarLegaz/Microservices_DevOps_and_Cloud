# Forzar la eliminación de un grupo de recursos en Azure usando PowerShell y un archivo JSON

# Leer el archivo JSON
$config = Get-Content -Path "config.json" | ConvertFrom-Json
$resourceGroupName = $config.ResourceGroupName

Remove-AzResourceGroup -Name $resourceGroupName -Force