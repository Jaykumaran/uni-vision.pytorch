from torch.utils.data import DataLoader
from torch.utils.data.dataset import Dataset
from custom_dataclass import CustomDatasetClass
 





def get_loader(custom_dataclass : Dataset, batch_size: int, shuffle = False, num_workers: int = 2) -> DataLoader:
    
    loader = DataLoader(custom_dataclass, 
                        batch_size = batch_size, 
                        shuffle=shuffle,
                        num_workers= num_workers
                        )
    
    
    return loader