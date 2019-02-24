# 字典
config = {
    "ip": "192.168.50.2",
    "port": 5432,
    "uid": "postgres",
    "pwd": "123456",
    "options": {
        "timeout": 30,
        "encode": "utf-8"
    },
    "drivers": ["pgsql", "Npgsql", "jdbpgsql"]
}
print(config)
print(config["ip"])
print(config["port"])
print(config["options"]["timeout"])
# 增加一个属性
config["aa"] = "AA"
print(config)
# 修改值
config["aa"] = "BB"
print(config)
# 删除一个属性
del config["aa"]
print(config)
# 遍历所有属性
for key, val in config.items():
    print(key, "=", val)
# 遍历所有key
for key in config.keys():
    print(key, "=", config[key])
# 遍历所有的值
for val in config.values():
    print(val)

options = config["options"]
for key, val in options.items():
    print(key, "=", val)

for i, val in enumerate(config["drivers"]):
    print(i, "=", val)
for val in config["drivers"]:
    print(val)

