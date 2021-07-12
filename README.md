dconf
=========
or DotConf

## Make Config Great Again.

Easy dot representation configuration module to make config life better.

How to use
----------

Example:

### config.toml

```toml
title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00

[database]
enabled = true
ports = [ 8000, 8001, 8002 ]
data = [ ["delta", "phi"], [3.14] ]
temp_targets = { cpu = 79.5, case = 72.0 }

[servers]

[servers.alpha]
ip = "10.0.0.1"
role = "frontend"

[servers.beta]
ip = "10.0.0.2"
role = "backend"

[[products]]
name = "Hammer"
sku = 738594937

[[products]]
name = "Nail"
sku = 284758393
```

```python
>>> import tomli
... from dotconfig import DotConfig
... CONFIG = DotConfig()
... CONFIG.load(tomli.load, "config.toml")
>>> CONFIG
{'title': 'TOML Example', 'owner': {'name': 'Tom Preston-Werner', 'dob': datetime.datetime(1979, 5, 27, 7, 32, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=57600)))}, 'database': {'enabled': True, 'ports': [8000, 8001, 8002], 'data': [['delta', 'phi'], [3.14]], 'temp_targets': {'cpu': 79.5, 'case': 72.0}}, 'servers': {'alpha': {'ip': '10.0.0.1', 'role': 'frontend'}, 'beta': {'ip': '10.0.0.2', 'role': 'backend'}}, 'products': [{'name': 'Hammer', 'sku': 738594937}, {'name': 'Nail', 'sku': 284758393}]}
>>> CONFIG.title
'TOML Example'
>>> CONFIG.database.ports
[8000, 8001, 8002]
>>> CONFIG.database.temp_targets.cpu
79.5
>>> CONFIG.servers
{'alpha': {'ip': '10.0.0.1', 'role': 'frontend'}, 'beta': {'ip': '10.0.0.2', 'role': 'backend'}}
>>> CONFIG.servers.alpha.role
'frontend'
>>> CONFIG.products
[{'name': 'Hammer', 'sku': 738594937}, {'name': 'Nail', 'sku': 284758393}]
>>> CONFIG.products[0].sku
738594937
```
### Another way to load the configuration

```python
>>> config = {'alpha': {'ip': '10.0.0.1', 'role': 'frontend'}, 'beta': {'ip': '10.0.0.2', 'role': 'backend'}}
... CONFIG = DotConfig(config)
>>> CONFIG.beta.ip
'10.0.0.2'
```


Contribute
----------

Feel free to fork and pr.