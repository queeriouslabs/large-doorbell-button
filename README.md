# large-doorbell-button

Sourcecode to run the large doorbell button.

# Installing as a service

run install_service.sh:

sudo cp doorbell.service /etc/systemd/system/
sudo chmod 644 /etc/systemd/system/doorbell.service
sudo systemctl start doorbell
sudo systemctl status doorbell