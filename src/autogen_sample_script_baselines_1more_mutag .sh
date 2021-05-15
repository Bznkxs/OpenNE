python3 -m openne --clf-ratio 0.8 --dataset mutag --dec bilinear --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 64 --lr 0.001 --model ss_graphmodel --patience 3 --readout mean --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 64 --lr 0.001 --model ss_graphmodel --patience 3 --readout sum --sampler mvgrl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 64 --early-stopping 20 --enc gin --epochs 500 --est jsd --hiddens 64 64 --lr 0.001 --model ss_graphmodel --patience 3 --readout sum --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 64 --early-stopping 20 --enc gin --epochs 500 --est nce --hiddens 64 64 --lr 0.001 --model ss_graphmodel --patience 3 --readout sum --sampler graphcl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec bilinear --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --lr 0.001 --model ss_graphmodel --patience 3 --readout mean --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --lr 0.001 --model ss_graphmodel --patience 3 --readout sum --sampler mvgrl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gin --epochs 500 --est jsd --lr 0.001 --model ss_graphmodel --patience 3 --readout sum --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gin --epochs 500 --est nce --lr 0.001 --model ss_graphmodel --patience 3 --readout sum --sampler graphcl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec bilinear --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 128 --lr 0.01 --model ss_graphmodel --patience 3 --readout mean --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 128 --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler mvgrl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gin --epochs 500 --est jsd --hiddens 128 128 --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gin --epochs 500 --est nce --hiddens 128 128 --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler graphcl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec bilinear --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --lr 0.01 --model ss_graphmodel --patience 3 --readout mean --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler mvgrl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gin --epochs 500 --est jsd --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gin --epochs 500 --est nce --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler graphcl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec bilinear --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --lr 0.01 --model ss_graphmodel --patience 3 --readout mean --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler mvgrl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 64 --early-stopping 20 --enc gin --epochs 500 --est jsd --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 64 --early-stopping 20 --enc gin --epochs 500 --est nce --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler graphcl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec bilinear --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 64 64 --lr 0.001 --model ss_graphmodel --patience 3 --readout mean --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 64 64 --lr 0.001 --model ss_graphmodel --patience 3 --readout sum --sampler mvgrl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 64 --early-stopping 20 --enc gin --epochs 500 --est jsd --hiddens 64 64 64 --lr 0.001 --model ss_graphmodel --patience 3 --readout sum --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 64 --early-stopping 20 --enc gin --epochs 500 --est nce --hiddens 64 64 64 --lr 0.001 --model ss_graphmodel --patience 3 --readout sum --sampler graphcl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec bilinear --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 64 64 --lr 0.01 --model ss_graphmodel --patience 3 --readout mean --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 64 64 --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler mvgrl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 64 --early-stopping 20 --enc gin --epochs 500 --est jsd --hiddens 64 64 64 --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 64 --early-stopping 20 --enc gin --epochs 500 --est nce --hiddens 64 64 64 --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler graphcl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec bilinear --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 128 --lr 0.001 --model ss_graphmodel --patience 3 --readout mean --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 128 --lr 0.001 --model ss_graphmodel --patience 3 --readout sum --sampler mvgrl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gin --epochs 500 --est jsd --hiddens 128 128 --lr 0.001 --model ss_graphmodel --patience 3 --readout sum --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gin --epochs 500 --est nce --hiddens 128 128 --lr 0.001 --model ss_graphmodel --patience 3 --readout sum --sampler graphcl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec bilinear --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 --lr 0.01 --model ss_graphmodel --patience 3 --readout mean --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler mvgrl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gin --epochs 500 --est jsd --hiddens 128 --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gin --epochs 500 --est nce --hiddens 128 --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler graphcl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec bilinear --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 --lr 0.001 --model ss_graphmodel --patience 3 --readout mean --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 128 --lr 0.001 --model ss_graphmodel --patience 3 --readout sum --sampler mvgrl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gin --epochs 500 --est jsd --hiddens 128 --lr 0.001 --model ss_graphmodel --patience 3 --readout sum --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 128 --early-stopping 20 --enc gin --epochs 500 --est nce --hiddens 128 --lr 0.001 --model ss_graphmodel --patience 3 --readout sum --sampler graphcl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec bilinear --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 --lr 0.01 --model ss_graphmodel --patience 3 --readout mean --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 64 --early-stopping 20 --enc gcn --epochs 500 --est jsd --hiddens 64 --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler mvgrl --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 64 --early-stopping 20 --enc gin --epochs 500 --est jsd --hiddens 64 --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler dgi --task graphclassification
python3 -m openne --clf-ratio 0.8 --dataset mutag --dec inner --dim 64 --early-stopping 20 --enc gin --epochs 500 --est nce --hiddens 64 --lr 0.01 --model ss_graphmodel --patience 3 --readout sum --sampler graphcl --task graphclassification
