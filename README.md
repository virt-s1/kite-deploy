# kite-deploy

kite-deploy is one of sub-projects of kite, which is to run Linux application or kernel test on public and private cloud platform, such as AWS EC2, VMWare ESXi, OpenStck, Azure, etc.

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

### deploy OpenStack instance

    ansible-playbook -v -i inventory -e cloud_platform=openstack deploy.yaml

## remove instance/VM on cloud

### remove AWS EC2 instance

    ansible-playbook -v -i inventory -e cloud_platform=aws remove.yaml

### remove VMWare ESXi VM

    ansible-playbook -v -i inventory -e cloud_platform=esxi remove.yaml

### remove OpenStack instance

    ansible-playbook -v -i inventory -e cloud_platform=openstack remove.yaml

## kite-deploy Image

kite-deploy will build/update images for different cloud platforms weekly.

**Images kite-deploy build and maintain**

| Cloud Platform / Linux Distro | Image Info |
| ---- | ---- |
| VMWare ESXi 7.0 / RHEL 8.3.1 | vSphere template `template-rhel-8-3-bios` and `template-rhel-8-3-efi` |
| VMWare ESXi 7.0 / RHEL 8.4.0 | vSphere template `template-rhel-8-4-bios` and `template-rhel-8-4-efi` |
| AWS EC2 AMI / RHEL 8.3.1 | Region `US East (N. Virginia)` AMI ID is stored in Amazon Simple Systems Manager parameter with parameter name `kite_imagebuild_rhel-8-3` |
| AWS EC2 AMI / RHEL 8.4.0 | Region `US East (N. Virginia)` AMI ID is stored in Amazon Simple Systems Manager parameter with parameter name `kite_imagebuild_rhel-8-4` |
| Openstack / RHEL 8.3.1 | OpenStack qcow2 image ` kite-openstack-rhel-8-3 ` |
| Openstack / RHEL 8.4.0 | OpenStack qcow2 image ` kite-openstack-rhel-8-4 ` |

Image building [kickstart files](https://github.com/henrywang/lctp/tree/master/roles/image/templates) are for [LTP](https://github.com/linux-test-project/ltp) test running. If you need more packages according to your test, feel free to send PR to [kickstart files](https://github.com/henrywang/lctp/tree/master/roles/image/templates).

### Image Building

Build ESXi image with:

    ansible-playbook -v -i inventory -e esxi_firmware=<bios or efi> -e cloud_platform=esxi build.yaml

Build AWS EC2 AMI image with:

    ansible-playbook -v -i inventory -e cloud_platform=aws build.yaml

Build Openstack qcow2 image with:

    ansible-playbook -v -i inventory -e cloud_platform=openstack build.yaml

## kite-deploy configuration

You can set these environment variables to configure to run kite-deploy

    TEST_OS           The OS to run the tests in.  Currently supported values:
                          "rhel-8-3"
                          "rhel-8-4"

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

    AWS_INSTANCE_TPYE     AWS instance type. Suggested instance types:
                              "t2.medium": Xen based instance with xen_netfront NIC
                              "t3.medium": KVM based instance with Elastic Network Adapter (ena)
                              "t3a.medium": KVM based instance with AMD CPU
                              "m4.large": Xen based instance with the Intel 82599 VF interface (SRIOV)
