# Linux Cloud Test Project (LCTP)

Linux cloud test project (lctp) is to run Linux application or kernel test on all kinds of public and private cloud platform.

LCTP will provide you an easy way to setup Linux guest/instance/VM and build and maintain Linux image for you. All you need to care about is your test. Let LCTP finish the rest of things.

## LCTP Roles

LCTP includes some roles to have different jobs done. You can group them together into ansible playbook to finish your work.

    guest     Create guest/instance/VM in different cloud platform
    image     Build image for different cloud platform
    kernel    Download kernel, install kernel(rebooting included)
    test      Run your test here
    umb       Send UMB message

How to group rules into ansible playbook?

In [cki](https://github.com/henrywang/lctp/blob/master/cki.yml) case, I'd like to run LTP test on different kernels on different cloud platforms.

1. downloading kernel files: include kernel role with download action
2. create a guest/instance: include guest role with deploy action
3. update kernel on target guest/instance: include kernel role with install action
4. run LTP test: include test role with running LTP
5. report result: include umb role with action send
6. remove guest/instance after test: include guest role with remove action

Pretty easy!

## LCTP Image

LCTP will build/update images for different cloud platforms weekly.

**Images LCTP build and maintain**

| Cloud Platform / Linux Distro | Image Info |
| ---- | ---- |
| VMWare ESXi 6.7 / RHEL 8.3 | vSphere template `template-rhel-8-3-bios` and `template-rhel-8-3-efi` |
| AWS EC2 AMI / RHEL 8.3 | Region `US East (N. Virginia)` AMI ID is stored in Amazon Simple Systems Manager parameter with parameter name `lctp_imagebuild_rhel-8-3` |

Image building [kickstart files](https://github.com/henrywang/lctp/tree/master/roles/image/templates) are for [LTP](https://github.com/linux-test-project/ltp) test running. If you need more packages according to your test, feel free to send PR to [kickstart files](https://github.com/henrywang/lctp/tree/master/roles/image/templates).

### Image Building

Build ESXi image with:

    ansible-playbook -v -i inventory -e esxi_firmware=<bios or efi> -e cloud_platform=esxi build.yml

Build AWS EC2 AMI image with:

    ansible-playbook -v -i inventory -e cloud_platform=aws build.yml

## LCTP configuration

You can set these environment variables to configure to run LCTP

    TEST_OS         The OS to run the tests in.  Currently supported values:
                        "rhel-8-3"

    VSPHERE_SERVER  The vSphere server hostname or IP address


    VSPHERE_USERNAME  Username to login vSphere server

    VSPHERE_PASSWORD  Password to login vSphere server

    ESXI_HOST         ESXi host name or IP address

    ESXI_DATACENTER   Datacenter name

    ESXI_DATASTORE    Datastore name

    AWS_ACCESS_KEY    AWS access key for AWS API authentication

    AWS_SECRET_KEY    AWS secret key for AWS API authentication
