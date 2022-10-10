terraform {
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean",
      version = "~> 2.0"
    }
  }
}

variable "do_token" {
  type        = string
  description = "Digital Ocean personal access token."
}

variable "do_pvt" {
  type        = string
  description = "Private key location of the droplet."
}

provider "digitalocean" {
  token = var.do_token
}

data "digitalocean_ssh_key" "terraform" {
  name = "Battlestation_Manjaro"
}

resource "digitalocean_droplet" "image-optimizer" {
  image  = "ubuntu-22-04-x64"
  name   = "image-optimizer"
  region = "sfo3"
  size   = "s-1vcpu-2gb"
  ssh_keys = [
    data.digitalocean_ssh_key.terraform.id
  ]

  connection {
    host        = self.ipv4_address
    user        = "root"
    type        = "ssh"
    private_key = file(var.do_pvt)
    timeout     = "2m"
  }
}


