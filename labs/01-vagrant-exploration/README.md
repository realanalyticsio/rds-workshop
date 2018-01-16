Exploring Vagrant workflow and environment for reproducible data project

1.	Open up a Command Prompt (CMD) and change to the rds-workshop directory. Ensure that there is a file named Vagrantfile.

2.	Run the following command to start a Linux VM automatically: vagrant up

3.	Wait until you get the command prompt back and run the following command to log into the VM: vagrant ssh

4. You are now in a Linux environment running the Bash shell. If you are familiar with Linux and Bash commands, you should be able to list files and access different directories.

5a. You should be able to also launch Python by running the following command: python

5b. To exit the Python prompt, type the following and press Enter: exit()

6. Navigate to the following directory with the cd command: cd \vagrant

7. To exit the Linux VM environment, type the following in a Bash shell and press Enter: exit

8. To log back again in the Linux VM, run the following command again: vagrant ssh

9. To destroy the Linux VM if no longer in use, exit the Linux VM and run the following command: vagrant destroy

10. The whole workflow is reproducible, you should be able to re-run the steps 1 to 9 by just following the commands again.
