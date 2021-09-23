import argparse
import yaml
import os

###########################################
# Example 01
###########################################
def get_parser():
    parser = argparse.ArgumentParser(description='Point Cloud Segmentation')
    parser.add_argument('--config', type=str, default='config/pointgroup_default_scannet.yaml', help='path to config file')

    ### pretrain
    parser.add_argument('--pretrain', type=str, default='', help='path to pretrain model')

    args_cfg = parser.parse_args()
    assert args_cfg.config is not None
    with open(args_cfg.config, 'r') as f:
        config = yaml.load(f)
    for key in config:
        for k, v in config[key].items():
            setattr(args_cfg, k, v)

    return args_cfg


cfg = get_parser()

###########################################
# Example 02
###########################################
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_root', help='path to the input dataset files', default='../dataset/scannetv2')
    parser.add_argument('--result_root', help='path to the predicted results', default='exp/scannetv2/pointgroup/pointgroup_run1_scannet/result/epoch384_nmst0.3_scoret0.09_npointt100')
    parser.add_argument('--room_name', help='room_name', default='scene0000_00')
    parser.add_argument('--room_split', help='train / val / test', default='train')
    parser.add_argument('--task', help='input / semantic_gt / semantic_pred / instance_gt / instance_pred', default='input')
    opt = parser.parse_args()

    print(opt.room_name)
