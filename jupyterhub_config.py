c.KubeSpawner.start_timeout = 180
c.KubeSpawner.http_timeout = 120

import os
os.environ['http_proxy'] = "http://user:passwd@host:port" 
os.environ['https_proxy'] = "https://user:passwd@host:port" 
