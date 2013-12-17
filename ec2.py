import ifconfig
import boto.ec2

wlan0_ip = ifconfig.get_interface_dict()['wlan0']

region = boto.ec2.regioninfo.RegionInfo(name="nova", endpoint=wlan0_ip)


conn = boto.connect_ec2(aws_access_key_id="0d1ccb7b274f4c22849c2cbbfef7579e",
                                aws_secret_access_key="f3163ec60aeb4e7aada9d4ada5114846",
                                is_secure=False,
                                region=region,
                                port=8773,
                                path="/services/Cloud")

