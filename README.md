# Edge-Direct Visual Odometry
If you find this useful, please cite the related [paper](https://arxiv.org/pdf/1906.04838.pdf):
```
@article{DBLP:journals/corr/abs-1906-04838,
  author    = {Kevin Christensen and
               Martial Hebert},
  title     = {Edge-Direct Visual Odometry},
  journal   = {CoRR},
  volume    = {abs/1906.04838},
  year      = {2019},
  url       = {http://arxiv.org/abs/1906.04838},
  archivePrefix = {arXiv},
  eprint    = {1906.04838},
}
```
## Setup
This repository assumes the following directory structure, and is setup for the [TUM-RGBD Dataset](https://vision.in.tum.de/data/datasets/rgbd-dataset):
```
EdgeDirectVO
|-- tum_rgbd_dataset/
    |-- depth/
    |-- rgb/
    |-- assoc.txt
|-- tum_rgbd_dataset_ground_truth.txt
```

### Boost
On Mac-OS M1,
```console
arch -arm64 brew install boost
```

### Eigen3
> If you just want to use Eigen, you can use the header files right away. There is no binary library to link to, and no configured header file. Eigen is a pure template library defined in the headers.
- Download `eigen-3.3.9` in the project directory and simply unzip it.

### OpenCV 4.5
```
arch -arm64 brew install opencv
```

## Build and Run
Use a **Non-Rosetta Terminal**/Default terminal on M1.
```
cd EdgeDirectVO
mkdir build && cd build
cmake ..
make -j
```

---

### Dataset
The repo build assuming the user has downloaded `rgbd_dataset_freiburg1_xyz` dataset. This is pre-defined in the [Settings.h](include/Settings.h). For example, if I were to use `fr1/desk2` instead, I simply change  `const int DATASET_NUMBER = 0;` in the same file and proceed as indicated below:
- Download [fr1/desk2](https://vision.in.tum.de/data/datasets/rgbd-dataset/download#) in the 'Handheld SLAM' category. Untar using `tar -xf rgbd_dataset_freiburg1_desk2.tgz `.
Be sure to run [assoc.py](https://vision.in.tum.de/data/datasets/rgbd-dataset) to associate timestamps with corresponding frames.
- Run `python2 associate.py rgbd_dataset_freiburg1_desk2/rgb.txt rgbd_dataset_freiburg1_desk2/depth.txt > rgbd_dataset_freiburg1_desk2/assoc.txt`

#### Ground-truth trajectories
(quoted from [official site](https://vision.in.tum.de/data/datasets/rgbd-dataset/file_formats))
Each line in the text file contains a single pose.
The format of each line is 'timestamp tx ty tz qx qy qz qw'
* timestamp (float) gives the number of seconds since the Unix epoch.
* tx ty tz (3 floats) give the position of the optical center of the color camera with respect to the world origin as defined by the motion capture system.
* qx qy qz qw (4 floats) give the orientation of the optical center of the color camera in form of a unit quaternion with respect to the world origin as defined by the motion capture system.
The file may contain comments that have to start with "#".


## Run
```
cd build
./EdgeDirectVO
```

## Evaluation
After evaluating on a dataset, the corresponding evaluation commands will be printed to terminal.  Simpy copy and run them in terminal in project root directory.  Examples are shown below:

### For [relative pose error](https://vision.in.tum.de/data/datasets/rgbd-dataset/tools):
```
python2 evaluate_rpe.py groundtruth_fr1desk2.txt rgbd_dataset_freiburg1_desk2_results.txt --fixed_delta --delta 1 --verbose
```
### For [absolute trajectory error](https://vision.in.tum.de/data/datasets/rgbd-dataset/tools):
```
python2 evaluate_ate.py groundtruth_fr1desk2.txt rgbd_dataset_freiburg1_desk2_results.txt --verbose
```
