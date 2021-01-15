python -m openne --model ss_nodemodel --dataset cora --enc none --dec inner --sampler node-neighbor-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc none --dec inner --sampler node-neighbor-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc none --dec inner --sampler node-rand_walk-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc none --dec inner --sampler node-rand_walk-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc none --dec bilinear --sampler node-neighbor-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc none --dec bilinear --sampler node-neighbor-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc none --dec bilinear --sampler node-rand_walk-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc none --dec bilinear --sampler node-rand_walk-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc none --dec mlp --sampler node-neighbor-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc none --dec mlp --sampler node-neighbor-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc none --dec mlp --sampler node-rand_walk-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc none --dec mlp --sampler node-rand_walk-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gcn --dec inner --sampler node-neighbor-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gcn --dec inner --sampler node-neighbor-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gcn --dec inner --sampler node-rand_walk-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gcn --dec inner --sampler node-rand_walk-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gcn --dec bilinear --sampler node-neighbor-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gcn --dec bilinear --sampler node-neighbor-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gcn --dec bilinear --sampler node-rand_walk-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gcn --dec bilinear --sampler node-rand_walk-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gcn --dec mlp --sampler node-neighbor-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gcn --dec mlp --sampler node-neighbor-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gcn --dec mlp --sampler node-rand_walk-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gcn --dec mlp --sampler node-rand_walk-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gat --dec inner --sampler node-neighbor-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gat --dec inner --sampler node-neighbor-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gat --dec inner --sampler node-rand_walk-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gat --dec inner --sampler node-rand_walk-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gat --dec bilinear --sampler node-neighbor-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gat --dec bilinear --sampler node-neighbor-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gat --dec bilinear --sampler node-rand_walk-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gat --dec bilinear --sampler node-rand_walk-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gat --dec mlp --sampler node-neighbor-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gat --dec mlp --sampler node-neighbor-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gat --dec mlp --sampler node-rand_walk-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gat --dec mlp --sampler node-rand_walk-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-neighbor-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-rand_walk-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gin --dec inner --sampler node-rand_walk-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-neighbor-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gin --dec bilinear --sampler node-rand_walk-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-neighbor-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-rand_walk-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc gin --dec mlp --sampler node-rand_walk-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc linear --dec inner --sampler node-neighbor-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc linear --dec inner --sampler node-neighbor-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc linear --dec inner --sampler node-rand_walk-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc linear --dec inner --sampler node-rand_walk-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc linear --dec bilinear --sampler node-neighbor-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc linear --dec bilinear --sampler node-neighbor-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc linear --dec bilinear --sampler node-rand_walk-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc linear --dec bilinear --sampler node-rand_walk-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc linear --dec mlp --sampler node-neighbor-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc linear --dec mlp --sampler node-neighbor-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc linear --dec mlp --sampler node-rand_walk-random --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
python -m openne --model ss_nodemodel --dataset cora --enc linear --dec mlp --sampler node-rand_walk-except_neighbor --readout mean --est jsd --epochs 1 --early-stopping 20 --dim 16 --lr 0.001 %1 %2 %3 %4 %5 %6 %7 %8 %9
