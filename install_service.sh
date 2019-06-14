sudo cp doorbell.service /etc/systemd/system/
sudo chmod 644 /etc/systemd/system/doorbell.service
sudo systemctl daemon-reload
sudo systemctl start doorbell
sudo systemctl status doorbell