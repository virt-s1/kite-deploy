# kite-deploy

kite-deploy is one of sub-projects of kite, which is to run Linux application or kernel test on all kinds of public and private cloud platform.

kite-deploy will provide an easy way to setup Linux guest/instance/VM, build and maintain Linux image on public and private cloud platform.

## kite-deploy Roles

kite-deploy includes two roles to have different jobs done. You can group them together into ansible playbook to finish your work.

    guest     Create guest/instance/VM in different cloud platform
    image     Build image for different cloud platform

## deploy instance/VM on cloud

### deploy AWS EC2 instance

    ansible-playbook -v -i inventory -e cloud_platform=aws deploy.yaml

### deploy VMWare ESXi VM

    ansible-playbook -v -i inventory -e esxi_firmware=<bios or efi> -e cloud_platform=esxi deploy.yaml

## remove instance/VM on cloud

### remove AWS EC2 instance

    ansible-playbook -v -i inventory -e cloud_platform=aws remove.yaml

### remove VMWare ESXi VM

    ansible-playbook -v -i inventory -e cloud_platform=esxi remove.yaml

## kite-deploy Image

kite-deploy will build/update images for different cloud platforms weekly.

**Images kite-deploy build and maintain**

| Cloud Platform / Linux Distro | Image Info |
| ---- | ---- |
| VMWare ESXi 7.0 / RHEL 8.3 | vSphere template `template-rhel-8-3-bios` and `template-rhel-8-3-efi` |
| AWS EC2 AMI / RHEL 8.3 | Region `US East (N. Virginia)` AMI ID is stored in Amazon Simple Systems Manager parameter with parameter name `kite_imagebuild_rhel-8-3` |

Image building [kickstart files](https://github.com/henrywang/lctp/tree/master/roles/image/templates) are for [LTP](https://github.com/linux-test-project/ltp) test running. If you need more packages according to your test, feel free to send PR to [kickstart files](https://github.com/henrywang/lctp/tree/master/roles/image/templates).

### Image Building

Build ESXi image with:

    ansible-playbook -v -i inventory -e esxi_firmware=<bios or efi> -e cloud_platform=esxi build.yml

Build AWS EC2 AMI image with:

    ansible-playbook -v -i inventory -e cloud_platform=aws build.yml

## kite-deploy configuration

You can set these environment variables to configure to run kite-deploy

    TEST_OS           The OS to run the tests in.  Currently supported values:
                          "rhel-8-3"

    GITHUB_SHA        The commit SHA that triggered the workflow
                      Used by VM name or instance tag

    VSPHERE_SERVER    The vSphere server hostname or IP address

    VSPHERE_USERNAME  Username to login vSphere server

    VSPHERE_PASSWORD  Password to login vSphere server

    ESXI_HOST         ESXi host name or IP address

    ESXI_DATACENTER   Datacenter name

    ESXI_DATASTORE    Datastore name

    VAULT_PASSWORD    Password to decrypt openstack configuration file

    AWS_ACCESS_KEY    AWS access key for AWS API authentication

    AWS_SECRET_KEY    AWS secret key for AWS API authentication

    AWS_REGION        AWS region

    AWS_INSTANCE_TPYE     AWS instance type. We suggested type:
                              "t2.medium" Xen based instance with xen_netfront NIC
                              "t3.medium" KVM based instance with Elastic Network Adapter (ena)
                              "t3a.medium": KVM based instance with AMD CPU
                              "m4.large": Xen based instance with the Intel 82599 VF interface (SRIOV)
