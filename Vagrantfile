Vagrant.configure("2") do |o|
    o.vm.box = "trusty-server-cloudimg-amd64-vagrant-disk1"
    o.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

    o.vm.synced_folder "~/.subversion", "/home/vagrant/.subversion", create:true

    o.vm.network :private_network, ip: "192.168.55.57"

    o.vm.provision :shell, :path => "system/vagrant_setup.sh"

    o.vm.provider "virtualbox" do |vb|
        vb.customize ["modifyvm", :id, "--memory", "1024"]
    end
end