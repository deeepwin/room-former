import os
import cv2
import numpy as np

from data_preprocess.stru3d.stru3d_utils import generate_density
from data_preprocess.common_utils import read_scene_pc


ply_path= "/mnt/data/github/room-former/data/dons_house_1.ply"

scene_id = "dons"
out_folder = "/mnt/data/github/room-former/data/stru3d/test/"


def generate_density_image():
    
    # load pre-generated point cloud 
    points = read_scene_pc(ply_path)
    xyz = points[:, :3]

    # project point cloud to density map
    density_map, normalization_dict = generate_density(xyz, width=256, height=256)

    # store density image
    density_path = os.path.join(out_folder, scene_id+'.png')
    density_uint8 = (density_map * 255).astype(np.uint8)
    cv2.imwrite(density_path, density_uint8)