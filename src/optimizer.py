"""模型优化核心模块"""
from dataclasses import dataclass


@dataclass
class QuantizationConfig:
    method: str = "gptq"
    bits: int = 4
    group_size: int = 128


@dataclass
class DistillationConfig:
    teacher_model: str = "deepseek-7b"
    student_model: str = "deepseek-1.3b"
    temperature: float = 2.0
