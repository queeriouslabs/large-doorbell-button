# large-doorbell-button

Sourcecode to run the large doorbell button.

# Installing as a service

sudo cp doorbell.service /etc/systemd/system/
sudo chmod 644 /etc/systemd/system/doorbell.service
sudo systemctl start myservice
sudo systemctl status myservice