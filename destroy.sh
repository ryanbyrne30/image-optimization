TERRAFORM_DIR="/home/ryan/Documents/repos/github/image-optimization/terraform"
ANSIBLE_DIR="/home/ryan/Documents/repos/github/image-optimization/ansible"
HOSTS="$ANSIBLE_DIR/hosts"

cd $TERRAFORM_DIR

terraform destroy -var "do_token=${DO_TOKEN}" -var "do_pvt=${DO_PVT}"