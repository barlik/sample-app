# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.network :private_network, ip: "192.168.100.2"

  # Use ansible local provisioner
  # Ansible will be installed inside the guest machine
  config.vm.provision "ansible_local" do |ansible|
    ansible.compatibility_mode = "2.0"
    ansible.playbook = "playbook.yml"
    ansible.become = true
    # ansible.verbose = true
  end
end
