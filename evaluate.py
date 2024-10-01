import torch
from your_dataset_class import BrainMRIDataset
from torch.utils.data import DataLoader
from nested_unet import NestedUNet
from attention_unet import AttentionUNet

def calculate_dice_score(pred, target):
    # Implement dice score calculation
    pass

def evaluate_model(model, test_loader):
    # Implement evaluation logic
    pass

if __name__ == '__main__':
    test_dataset = BrainMRIDataset('data/test')
    test_loader = DataLoader(test_dataset, batch_size=1)
    
    nested_unet = NestedUNet(num_classes=1)
    nested_unet.load_state_dict(torch.load('nested_unet.pth'))
    nested_unet_score = evaluate_model(nested_unet, test_loader)
    
    attention_unet = AttentionUNet(num_classes=1)
    attention_unet.load_state_dict(torch.load('attention_unet.pth'))
    attention_unet_score = evaluate_model(attention_unet, test_loader)
    
    print(f"Nested U-Net Dice Score: {nested_unet_score}")
    print(f"Attention U-Net Dice Score: {attention_unet_score}")