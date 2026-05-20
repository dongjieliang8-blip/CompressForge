"""CompressForge 入口"""
from .optimizer import QuantizationConfig

config = QuantizationConfig(method="gptq", bits=4)
print(f"CompressForge 配置: {config.method}, {config.bits}bit")
print("模块测试通过")
