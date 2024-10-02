# Crear un grupo de recursos y una máquina virtual Ubuntu usando PowerShell y un archivo JSON

Write-Output "Deploy test environment"

# Conectar a tu cuenta de Azure
#Connect-AzAccount

# Leer el archivo JSON
$config = Get-Content -Path ".\\config.json" | ConvertFrom-Json

# Obtener los valores desde el archivo JSON
$resourceGroupName = $config.ResourceGroupName
$location = $config.Location
$vmName = $config.VMName
$adminUsername = $config.AdminUsername
$sshKeyPath = $config.SSHKeyPath

# Crear el grupo de recursos
Write-Output "Creating resource group ..."
New-AzResourceGroup -Name $resourceGroupName -Location $location

# Crear la configuración de la máquina virtual
Write-Output "Creating virtual machine ..."
$vmConfig = New-AzVMConfig -VMName $vmName -VMSize "Standard_B1s" | # Tamaño de VM disponible en suscripción de prueba
    Set-AzVMOperatingSystem -Linux -ComputerName $vmName -Credential (New-Object System.Management.Automation.PSCredential ($adminUsername, (ConvertTo-SecureString "dummyPassword" -AsPlainText -Force))) -DisablePasswordAuthentication |
    Set-AzVMSourceImage -PublisherName "Canonical" -Offer "UbuntuServer" -Skus "18.04-LTS" -Version "latest" |
    Add-AzVMNetworkInterface -Id (New-AzNetworkInterface -ResourceGroupName $resourceGroupName -Name "$vmName-NIC" -Location $location -SubnetId (New-AzVirtualNetworkSubnetConfig -Name "default" -AddressPrefix "10.0.0.0/24").Id).Id |
    Add-AzVMSSHKey -KeyData (Get-Content -Path $sshKeyPath -Raw) -Path "/home/$adminUsername/.ssh/authorized_keys"

# Crear la máquina virtual
New-AzVM -ResourceGroupName $resourceGroupName -Location $location -VM $vmConfig

Write-Output "Grupo de recursos '$resourceGroupName' y máquina virtual '$vmName' creados en la ubicación '$location'."
