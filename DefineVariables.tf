variable "cidr" {
  type = string
}

variable "rg_name" {
  type = string
}

variable "location" {
  type = string
}

data "azurerm_client_config" "current" {
}

data "external" "me" {
  program = ["az", "account", "show", "--query", "user"]
}

locals {
  prefix = "abd-pl"
  tags = {
    Environment = "Demo"
    Owner       = lookup(data.external.me.result, "name")
  }
}
