import matplotlib.pyplot as plt
import numpy as ni


def mnist():
    # exchange with the corrupted mnist dataset
    train = torch.randn(50000, 784)
    test = torch.randn(10000, 784) 
    return train, test
