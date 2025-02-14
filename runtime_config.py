from dataclasses import dataclass

@dataclass
class Config:
    device: str = 'cpu'
    distributed: bool = True
    runtime: str = 'gloo'
