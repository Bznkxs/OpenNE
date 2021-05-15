python3 -m openne --clf-ratio 0.2 --dataset cora --dec bilinear --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler dgi --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler node-neighbor-random --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --lr 0.001 --model ss_nodemodel --patience 3 --readout sum --sampler mvgrl --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est nce --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler gca --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec bilinear --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler dgi --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler node-neighbor-random --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --lr 0.001 --model ss_nodemodel --patience 3 --readout sum --sampler mvgrl --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est nce --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler gca --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec bilinear --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --lr 0.01 --model ss_nodemodel --patience 3 --readout mean --sampler dgi --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --lr 0.01 --model ss_nodemodel --patience 3 --readout mean --sampler node-neighbor-random --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --lr 0.01 --model ss_nodemodel --patience 3 --readout sum --sampler mvgrl --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est nce --lr 0.01 --model ss_nodemodel --patience 3 --readout mean --sampler gca --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec bilinear --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 128 128 --lr 0.01 --model ss_nodemodel --patience 3 --readout mean --sampler dgi --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 128 128 --lr 0.01 --model ss_nodemodel --patience 3 --readout mean --sampler node-neighbor-random --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 128 128 --lr 0.01 --model ss_nodemodel --patience 3 --readout sum --sampler mvgrl --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est nce --hiddens 128 128 128 --lr 0.01 --model ss_nodemodel --patience 3 --readout mean --sampler gca --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec bilinear --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 --lr 0.01 --model ss_nodemodel --patience 3 --readout mean --sampler dgi --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 --lr 0.01 --model ss_nodemodel --patience 3 --readout mean --sampler node-neighbor-random --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 --lr 0.01 --model ss_nodemodel --patience 3 --readout sum --sampler mvgrl --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est nce --hiddens 64 --lr 0.01 --model ss_nodemodel --patience 3 --readout mean --sampler gca --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec bilinear --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler dgi --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler node-neighbor-random --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 --lr 0.001 --model ss_nodemodel --patience 3 --readout sum --sampler mvgrl --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est nce --hiddens 64 --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler gca --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec bilinear --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 64 64 --lr 0.01 --model ss_nodemodel --patience 3 --readout mean --sampler dgi --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 64 64 --lr 0.01 --model ss_nodemodel --patience 3 --readout mean --sampler node-neighbor-random --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 64 64 --lr 0.01 --model ss_nodemodel --patience 3 --readout sum --sampler mvgrl --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est nce --hiddens 64 64 64 --lr 0.01 --model ss_nodemodel --patience 3 --readout mean --sampler gca --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec bilinear --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 128 128 --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler dgi --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 128 128 --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler node-neighbor-random --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 128 128 --lr 0.001 --model ss_nodemodel --patience 3 --readout sum --sampler mvgrl --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est nce --hiddens 128 128 128 --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler gca --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec bilinear --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 64 64 --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler dgi --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 64 64 --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler node-neighbor-random --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 64 64 --lr 0.001 --model ss_nodemodel --patience 3 --readout sum --sampler mvgrl --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est nce --hiddens 64 64 64 --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler gca --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec bilinear --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 --lr 0.01 --model ss_nodemodel --patience 3 --readout mean --sampler dgi --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 --lr 0.01 --model ss_nodemodel --patience 3 --readout mean --sampler node-neighbor-random --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 --lr 0.01 --model ss_nodemodel --patience 3 --readout sum --sampler mvgrl --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est nce --hiddens 128 --lr 0.01 --model ss_nodemodel --patience 3 --readout mean --sampler gca --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec bilinear --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 128 --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler dgi --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 128 --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler node-neighbor-random --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 128 --lr 0.001 --model ss_nodemodel --patience 3 --readout sum --sampler mvgrl --task unsupervisednodeclassification
python3 -m openne --clf-ratio 0.2 --dataset cora --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est nce --hiddens 128 128 --lr 0.001 --model ss_nodemodel --patience 3 --readout mean --sampler gca --task unsupervisednodeclassification
