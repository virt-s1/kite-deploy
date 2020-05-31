# Linux Cloud Test Project (LCTP)

Linux cloud test project (lctp) is to run Linux application or kernel test on all kinds of public and private cloud platform.

LCTP will provide you an easy way to setup Linux guest/instance/VM and build and maintain Linux image for you. All you need to care about is your test. Let LCTP finish the rest of things.

## LCTP Image

LCTP will build/update images for different cloud platforms weekly.

*** Images LCTP build and maintain ***

| Cloud Platform / Linux Distro | Image Info |
| ---- | ---- |
| VMWare ESXi 6.7 / RHEL 8.3 | vSphere template `template-rhel-8-3-bios` and `template-rhel-8-3-efi` |
| AWS EC2 AMI / RHEL 8.3 | Region `US East (N. Virginia)` AMI ID is stored in Amazon Simple Systems Manager parameter with parameter name `lctp_imagebuild_rhel-8-3` |


