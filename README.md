# Connecting the Dots: Floorplan Reconstruction Using Two-Level Queries

Testing RoomFormer on a sample point cloud. Original repository can be found here: [[Project Webpage](https://ywyue.github.io/RoomFormer/)]



## Level 1

Input          |  Output | Floorplan
:-------------------------:|:-------------------------: |:-------------------------:
![level_1](./data/03251_1.png) | ![level_2](./checkpoints/eval_stru3d/3251_pred_room_map.png) | ![level_2](./checkpoints/eval_stru3d/3251_pred_floorplan.png)
## Level 2

Input          |  Room Map | Floorplan
:-------------------------:|:-------------------------:|:-------------------------:
![level_2](./data/03250_1.png) | ![level_2](./checkpoints/eval_stru3d/3250_pred_room_map.png) | ![level_2](./checkpoints/eval_stru3d/3250_pred_floorplan.png) 

 
 
## Citation
If you find RoomFormer useful in your research, please cite our paper:
```
@inproceedings{yue2023connecting,
  title     = {{Connecting the Dots: Floorplan Reconstruction Using Two-Level Queries}},
  author    = {Yue, Yuanwen and Kontogianni, Theodora and Schindler, Konrad and Engelmann, Francis},
  booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2023}
}
```
