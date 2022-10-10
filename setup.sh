TERRAFORM_DIR="/home/ryan/Documents/repos/github/image-optimization/terraform"
ANSIBLE_DIR="/home/ryan/Documents/repos/github/image-optimization/ansible"
HOSTS="$ANSIBLE_DIR/hosts"

cd $TERRAFORM_DIR

terraform apply -var "do_token=${DO_TOKEN}" -var "do_pvt=${DO_PVT}"

terraform state show digitalocean_droplet.image-optimizer \
    | grep ipv4 \
    | grep -Eo "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" \
    | {
        read ip;
        echo "[image_optimizer]" > $HOSTS;
        echo "$ip" >> $HOSTS;
    }

cd $ANSIBLE_DIR
ansible-playbook -i $HOSTS deploy.yml