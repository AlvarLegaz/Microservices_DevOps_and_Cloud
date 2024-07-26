# Terraform

**Terraform** is an Infrastructure as Code (IaC) tool that allows you to build, change, and version infrastructure safely and efficiently. It can handle low-level components such as compute instances, storage, and networks, as well as high-level components such as DNS entries and SaaS features.

## Installation on Ubuntu

To install Terraform on Ubuntu, first update the system and install the necessary packages. Then, add the HashiCorp GPG key and install the official HashiCorp repository for Linux. Finally, install the Terraform command line interface.

## Installation on Linux PowerShell

To install Terraform on Linux PowerShell, follow the same steps as for Ubuntu. Make sure the Terraform binary is available in your PATH.

## Terraform Commands

- `terraform init`: This command initializes a working directory containing Terraform configuration files. It is the first command that should be run after writing a new Terraform configuration or cloning an existing one.
- `terraform plan`: Creates an execution plan that allows you to preview the changes that Terraform plans to make to your infrastructure.
- `terraform apply`: Executes the actions proposed in a Terraform plan. Creates, updates, or destroys resources to match the state described in your configuration file.
- `terraform destroy`: This command destroys all remote objects managed by a Terraform configuration. It is useful for cleaning up all temporary infrastructure once you have finished your work.
