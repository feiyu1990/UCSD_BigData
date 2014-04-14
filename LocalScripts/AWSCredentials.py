### AWS credentials: ####
# Change entries here to match your own #
# Get values for the first two entries from the "Security crediential" Tab
# Under in the menu under your name.
aws_access_key_id='AKIAJ6ZYUM4BOJ7DKYOA'
aws_secret_access_key='gMICRTXsMpTLjVE1zKMIpSOxOzb9befKJEEIfUt+'
# Get the Keypair in the EC2 Dashboard page.
keyPairFile="</Users/wangyufei/.ssh/yufei.pem>" # name of file keeping local key
key_name="yufei" # name of keypair (not name of file where key is stored)
# Set the security group On the EC2 page (You will need to add IP addresses if
# you want to connect from a place previously unauthorized.
security_groups=['default']
### End of AWS credentials ####
