python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-rand_walk-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-rand_walk-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-rand_walk-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-rand_walk-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-rand_walk-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 128 --hiddens 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 128 --hiddens 128 128 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 256 --hiddens 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.001 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.01 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.02 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --epochs 500 --lr 0.03 --early-stopping 20 --dim 256 --hiddens 256 256 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.03 --early-stopping 20 --dim 64 --hiddens 64 --readout mean --est jsd $*
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-except_neighbor --epochs 500 --lr 0.01 --early-stopping 20 --dim 64 --hiddens 64 64 --readout mean --est jsd $*
