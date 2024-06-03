import torch

def process_batch(images, num_frames):
    image_list = []
    for i in images:
        if i != 0:
            image_list.append(images[i-1], images[i], num_frames[i])
    return torch.cat(image_list)