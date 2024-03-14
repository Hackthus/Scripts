# Vérifiez si le module RemoteDesktop est installé
if (!(Get-WindowsFeature -Name 'Remote-Desktop-Services' -ErrorAction SilentlyContinue)) {
    # Installez le module RemoteDesktop si ce n'est pas déjà fait
    Install-WindowsFeature -Name 'Remote-Desktop-Services' -IncludeManagementTools
}

# Activez le service RDP
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name 'fDenyTSConnections' -Value 0

# Autorisez l'accès au bureau à distance via le pare-feu
Enable-NetFirewallRule -DisplayGroup 'Remote Desktop'

# Démarrez le service Bureau à distance
Start-Service -Name 'TermService' -ErrorAction SilentlyContinue
