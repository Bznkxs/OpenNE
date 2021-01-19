python3 -m openne --model ss_nodemodel --dataset cora --enc none --dec inner --sampler node-neighbor-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc none --dec inner --sampler node-neighbor-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc none --dec inner --sampler node-rand_walk-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc none --dec bilinear --sampler node-neighbor-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc none --dec bilinear --sampler node-neighbor-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc none --dec bilinear --sampler node-rand_walk-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc none --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc none --dec mlp --sampler node-neighbor-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc none --dec mlp --sampler node-neighbor-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc none --dec mlp --sampler node-rand_walk-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc none --dec mlp --sampler node-rand_walk-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gcn --dec inner --sampler node-neighbor-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gcn --dec inner --sampler node-neighbor-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gcn --dec inner --sampler node-rand_walk-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gcn --dec inner --sampler node-rand_walk-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gcn --dec bilinear --sampler node-rand_walk-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gcn --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gcn --dec mlp --sampler node-neighbor-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gcn --dec mlp --sampler node-rand_walk-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gcn --dec mlp --sampler node-rand_walk-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gat --dec inner --sampler node-neighbor-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gat --dec inner --sampler node-rand_walk-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gat --dec inner --sampler node-rand_walk-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gat --dec bilinear --sampler node-neighbor-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gat --dec bilinear --sampler node-rand_walk-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gat --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gat --dec mlp --sampler node-neighbor-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gat --dec mlp --sampler node-rand_walk-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gat --dec mlp --sampler node-rand_walk-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-rand_walk-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-rand_walk-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-rand_walk-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc none --dec inner --sampler node-neighbor-random --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
python3 -m openne --model ss_nodemodel --dataset cora --enc none --dec inner --sampler node-neighbor-except_neighbor --epochs 1 --lr 0.001 --early-stopping 20 --dim 16 --readout mean --est jsd --devices 7
