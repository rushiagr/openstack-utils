import ifconfig
import boto.ec2

wlan0_ip = ifconfig.get_interface_dict()['wlan0']

region = boto.ec2.regioninfo.RegionInfo(name="nova", endpoint=wlan0_ip)


conn = boto.connect_ec2(aws_access_key_id="8be8eb94e2ae4b688c9d46c058346ebe",
                                aws_secret_access_key="8ae29a0c02d046068880d81fc9e52d82",
                                is_secure=False,
                                region=region,
                                port=8773,
                                path="/services/Cloud")

