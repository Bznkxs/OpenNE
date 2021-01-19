# Logs

| name | dataset | enc | dec | sampler | epochs | lr | early_stopping | dim | hiddens | readout | est | time | micro | weighted | samples | macro | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-17 23:53:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-17 17:41:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 17:49:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 23:37:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 16:31:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-17 21:05:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 18:20:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-17 18:08:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 16:33:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-17 17:44:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 20:59:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-17 17:26:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-17 21:57:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-17 20:15:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-17 16:13:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-16 04:27:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 20:27:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-17 19:48:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 20:38:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 19:28:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-17 19:10:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 17:17:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-17 22:35:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 16:52:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-17 23:13:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 12:02:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-17 22:16:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 01:48:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-17 17:35:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 16:19:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-17 23:42:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.03 | 20 | 512 | [512] | mean | jsd | 21-01-17 17:55:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-17 17:25:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-17 18:04:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-17 17:13:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 01:28:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 03:57:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-17 17:07:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-17 17:05:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-14 23:24:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-17 17:16:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-17 22:23:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-17 16:11:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 23:11:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-17 21:14:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 23:00:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-15 09:39:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-17 22:09:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-17 22:02:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-17 18:57:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-17 22:00:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512] | mean | jsd | 21-01-17 21:26:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-17 17:11:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-randwalk-except_neighbor | - | - | - | 512 | [512, 512, 512] | mean | jsd | 21-01-17 00:05:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-17 17:20:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 16:58:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 20:57:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 22:45:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-17 16:46:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 300 | 0.01 | 100 | 128 | - | mean | jsd | 21-01-15 09:58:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-17 23:44:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-17 19:20:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-17 19:15:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-17 16:27:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-17 20:05:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-18 00:36:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-17 17:29:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-15 09:37:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 300 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 12:11:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-17 16:24:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-17 16:38:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-17 17:27:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 18:27:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 11:45:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 17:08:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-17 22:12:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-17 16:17:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 18:41:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-17 16:22:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-17 16:08:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-17 16:02:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | - | - | - | 128 | - | mean | jsd | 21-01-16 05:22:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-17 16:15:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-17 18:14:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 17:31:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-17 18:34:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-17 22:32:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 300 | 1e-05 | 100 | 128 | - | mean | jsd | 21-01-15 09:48:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-17 17:51:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-17 16:04:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 22:05:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-17 17:03:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.001 | 50 | 128 | - | mean | jsd | 21-01-15 11:50:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.001 | 50 | 128 | - | mean | jsd | 21-01-15 11:54:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 20:46:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-17 23:41:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-18 02:19:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 19:39:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-17 16:45:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 22:50:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 18:02:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 18:50:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 17:48:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 16:54:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:43:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-17 17:33:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:44:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-17 17:37:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-16 04:34:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-17 22:21:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-17 19:57:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 18:00:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-17 17:42:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-17 16:49:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 12:10:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 300 | 1e-05 | 100 | 128 | - | mean | jsd | 21-01-15 09:45:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-17 23:29:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-16 23:52:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-14 23:23:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 10:52:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-16 23:12:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 20:56:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-16 22:36:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 22:49:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-16 19:31:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:38:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-17 14:48:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 19:22:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 20:43:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-16 20:28:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-17 14:47:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-17 14:54:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-17 14:48:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-17 14:43:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-17 01:22:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 20:07:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-17 15:04:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 20:57:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 14:44:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 19:38:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-16 22:44:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 23:51:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-17 14:40:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-16 20:24:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 22:39:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 14:42:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 19:14:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-17 14:39:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 21:03:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-17 14:55:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 19:17:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-17 14:40:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.02 | 100 | 128 | - | mean | jsd | 21-01-15 10:52:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-16 21:06:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-17 14:57:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 19:16:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 22:44:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | - | - | - | 128 | - | mean | jsd | 21-01-15 12:45:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-17 04:22:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 15:00:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-17 14:48:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-17 15:12:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-16 19:12:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 15:56:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-16 19:22:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-16 20:19:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 14:51:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 23:35:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-16 19:26:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | - | - | - | 128 | - | mean | jsd | 21-01-15 12:31:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-16 22:42:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:38:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-16 20:04:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 15:49:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-17 15:30:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 15:42:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-16 19:50:23 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-17 09:24:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 10:34:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-17 00:05:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-17 09:32:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 300 | - | - | 128 | - | mean | jsd | 21-01-14 23:30:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-17 00:23:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 22:41:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 22:39:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-17 14:44:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.02 | 100 | 128 | - | mean | jsd | 21-01-15 10:48:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 19:13:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-17 15:26:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-17 15:42:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.01 | 20 | 512 | [512] | mean | jsd | 21-01-16 19:42:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 14:46:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-16 19:53:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-17 15:02:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 20:16:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 14:58:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-17 14:53:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-16 20:37:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-16 19:29:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-17 14:40:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-17 13:00:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-17 08:56:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | - | - | - | 128 | - | mean | jsd | 21-01-15 12:41:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 20:15:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:32:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 19:23:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-17 14:39:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 20 | - | - | 128 | - | mean | jsd | 21-01-15 12:45:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-16 19:30:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-17 15:19:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 21:26:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 14:54:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-16 19:39:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.001 | 50 | 128 | - | mean | jsd | 21-01-15 11:03:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 19:18:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 19:12:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 22:56:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-16 22:38:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-17 15:32:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-17 15:07:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | [256] | mean | jsd | 21-01-17 09:48:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 23:04:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256] | mean | jsd | 21-01-17 14:41:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 21:01:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-17 14:50:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-17 14:12:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-16 21:00:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-16 20:58:50 | 0 | 0 | 0 | 0 | 
| line | cora | gcn | inner | node-rand_walk-random | - | - | - | 128 | - | mean | jsd | 21-01-15 10:13:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 10:54:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-17 14:41:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 19:19:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 19:24:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-16 19:27:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 11:22:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | - | - | - | 128 | - | mean | jsd | 21-01-15 12:47:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:37:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-16 23:47:52 | 0 | 0 | 0 | 0 | 
| gcn | cora | gcn | inner | node-rand_walk-random | - | - | - | 128 | - | mean | jsd | 21-01-15 19:59:06 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-16 19:14:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 19:32:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-16 19:36:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512] | mean | jsd | 21-01-16 21:29:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 21:19:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-16 19:31:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 23:51:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 21:12:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 19:49:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-17 15:15:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 21:04:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:42:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 12:12:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:48:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-16 19:13:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:43:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 20:11:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-17 00:10:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 21:46:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-16 19:33:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 19:49:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 22:40:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 22:11:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-17 15:11:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 00:36:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 09:31:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-16 19:21:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 15:41:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-17 14:41:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-16 19:34:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-17 05:43:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 20:33:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 15:22:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-16 23:44:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 19:27:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-16 19:12:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 20:49:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-16 19:17:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-16 19:30:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:40:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.001 | 50 | 128 | - | mean | jsd | 21-01-15 10:56:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 0 | - | - | 128 | - | mean | jsd | 21-01-15 12:46:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 19:45:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-16 22:47:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-17 14:49:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-16 19:20:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-17 15:36:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:39:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 19:15:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-16 20:00:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-17 14:55:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-17 14:52:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-17 15:35:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 19:57:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:39:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 20 | - | - | 128 | - | mean | jsd | 21-01-15 12:42:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-17 14:45:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:48:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-16 20:59:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-16 23:49:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gin | inner | node-neighbor-random | 500 | 0.001 | 50 | 128 | - | mean | jsd | 21-01-15 11:05:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gin | inner | node-neighbor-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 11:37:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gin | inner | node-neighbor-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 11:39:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gin | inner | node-neighbor-random | 500 | 0.03 | - | 128 | - | mean | jsd | 21-01-15 12:55:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gin | inner | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-16 04:34:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gin | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-14 23:24:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gin | inner | node-neighbor-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 11:06:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | gin | inner | node-neighbor-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 11:17:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-18 19:13:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 08:57:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-18 22:15:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 00:21:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-18 11:49:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 512 | [512] | mean | jsd | 21-01-19 00:50:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-18 11:14:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 08:43:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 11:33:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 21:01:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 08:52:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-18 23:48:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 10:33:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 11:50:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:12:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 01:05:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-19 01:22:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | [512] | mean | jsd | 21-01-18 23:59:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 21:31:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-18 23:12:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-18 09:23:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 22:18:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-19 01:27:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-19 01:02:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-19 00:30:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-18 21:25:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-18 22:46:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-18 14:35:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 00:59:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 11:52:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-18 19:54:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 12:40:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-18 18:29:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-18 08:59:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-19 05:00:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-19 00:57:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-18 09:44:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-18 17:28:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-18 21:33:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 17:19:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-18 09:57:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 23:19:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-18 18:28:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-18 19:14:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-19 00:31:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 18:11:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 11:56:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512] | mean | jsd | 21-01-18 23:56:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 09:25:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-18 19:25:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 01:03:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-18 08:54:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-18 08:44:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-neighbor-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-18 10:00:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-19 01:32:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-19 01:18:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-18 21:53:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-18 08:57:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 08:42:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 01:26:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 11:54:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-18 20:30:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 10:55:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-18 21:24:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-18 19:12:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-18 21:58:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-18 18:31:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-18 21:00:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 17:45:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-18 19:56:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-18 19:52:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 00:56:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 17:38:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:11:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-18 08:50:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 22:21:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 22:24:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 10:20:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 19:33:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-18 10:37:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-18 19:24:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 19:26:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-19 00:33:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-19 00:55:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-19 03:55:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 19:32:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-19 00:26:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-18 23:10:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 10:22:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 22:27:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 00:40:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-19 02:18:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 13:41:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-18 11:27:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-19 00:53:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-random | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-18 18:37:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-18 22:01:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-19 00:23:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-18 21:43:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 10:26:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 21:39:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-18 19:21:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 512 | [512] | mean | jsd | 21-01-18 15:41:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-19 04:38:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 18:04:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 20:10:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-19 02:55:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 08:44:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-18 17:26:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 23:45:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-19 05:20:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-18 11:46:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 20:56:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 01:54:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 00:13:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 00:26:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 11:34:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 00:37:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 17:29:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 00:43:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 21:39:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 11:28:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-18 08:45:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 21:30:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-19 02:34:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 03:10:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-19 01:12:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-18 11:45:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 16:58:23 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-18 09:40:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-18 21:32:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 19:28:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 00:27:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-18 22:12:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 11:59:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256] | mean | jsd | 21-01-19 00:51:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-18 21:51:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 00:38:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 00:09:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 10:20:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-19 01:48:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-18 09:46:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 01:28:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-19 00:47:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-18 10:20:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 21:05:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 20:14:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 11:01:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 13:00:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-18 22:47:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 22:31:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 00:52:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-18 23:09:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-18 11:18:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 04:18:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 01:33:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 22:58:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 21:38:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-18 17:27:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-18 11:04:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 18:30:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 19:27:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 23:20:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 17:29:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 19:18:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-18 23:11:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 08:47:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:11:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-18 21:49:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-18 11:25:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 18:39:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-18 18:33:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-18 20:34:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 23:24:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 11:00:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 21:46:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-19 01:30:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-18 08:55:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 19:29:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-18 08:56:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 11:31:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 01:27:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-18 22:40:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-19 00:25:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 17:50:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 21:53:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 00:04:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-18 17:45:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 03:25:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-18 19:36:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-18 17:27:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 21:28:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 21:30:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 20:46:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 00:28:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 02:14:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:12:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 09:08:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-18 21:43:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-18 10:35:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-18 15:58:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 12:19:23 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 19:16:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 10:32:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-18 17:30:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-18 19:22:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 20:42:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 10:30:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-18 11:51:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-18 10:54:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-18 08:51:23 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-18 21:24:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-19 00:24:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-19 00:33:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 20:45:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-18 20:22:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-19 01:57:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-18 18:22:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 10:11:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:12:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 16:39:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-18 08:49:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-18 10:36:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-18 22:08:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 21:29:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 04:37:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 21:28:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-18 08:44:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-18 19:14:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 20:06:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 00:50:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-random | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-18 11:01:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 10:23:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-19 00:48:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 20:53:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-18 19:13:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 21:45:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-18 19:40:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-18 23:18:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 19:20:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | [512] | mean | jsd | 21-01-18 16:18:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 00:18:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-18 08:53:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 03:45:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 23:35:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:11:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 23:00:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 14:22:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-18 17:31:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 22:55:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-18 23:33:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 22:54:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-18 19:48:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 19:18:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-18 20:38:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-19 06:04:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 11:56:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 11:10:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 01:00:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-18 09:16:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 512 | [512] | mean | jsd | 21-01-19 00:54:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 09:13:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 19:19:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-18 23:44:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-18 10:46:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-19 00:45:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 03:15:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 20:04:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-18 08:45:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-19 04:16:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-19 01:24:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 10:09:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 11:36:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-19 01:16:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 01:29:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 21:46:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-18 11:02:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 00:29:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 21:37:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-19 00:24:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-18 19:55:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 23:28:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-18 10:59:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 00:05:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 04:59:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 20:00:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-18 19:12:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 08:43:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-18 23:39:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-18 23:52:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-18 23:01:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 19:15:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 23:32:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 19:17:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-18 23:28:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-18 09:27:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-18 11:15:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-18 14:59:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 08:50:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-18 22:17:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 22:56:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-18 22:05:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-19 00:16:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-18 18:20:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-18 22:47:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-18 11:03:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-18 21:36:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-19 00:46:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-18 20:26:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 01:25:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:11:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-18 17:33:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-19 01:25:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-18 23:14:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 08:48:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-18 09:30:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-18 21:35:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 23:33:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-random | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 17:33:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-18 21:58:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-18 21:33:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-18 21:25:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:12:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-18 08:56:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 01:06:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 21:52:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-19 05:20:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-19 02:34:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-18 23:37:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-18 08:46:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-random | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-18 08:57:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 21:45:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-18 10:30:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-18 19:23:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 19:31:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-18 09:38:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 00:12:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 09:48:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:11:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 11:12:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-18 21:27:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-18 23:58:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256] | mean | jsd | 21-01-18 23:14:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-18 11:06:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 10:58:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-18 11:20:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-19 00:54:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-19 01:07:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 19:16:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-18 17:28:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-18 11:43:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-18 21:27:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-18 11:09:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-18 21:41:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-19 00:53:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 00:41:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 23:37:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-18 11:39:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-18 21:32:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-18 23:41:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-19 00:36:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 08:56:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 22:30:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 00:39:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-18 10:37:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-18 23:48:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-18 09:41:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 100 | - | - | 128 | - | mean | jsd | 21-01-14 23:41:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 00:40:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-18 15:21:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-19 00:32:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 03:34:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 05:42:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 19:04:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 21:37:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 20:50:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-18 17:32:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 21:47:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 08:44:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 10:56:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 19:30:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 00:58:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-18 21:41:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 22:25:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-18 11:22:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 22:22:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 22:50:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 00:28:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-18 21:26:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-18 21:54:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-18 21:48:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 08:54:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-random | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-18 08:58:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 20:10:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-random | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-18 17:31:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-18 21:26:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 21:40:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-18 20:20:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 21:31:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-18 19:44:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 09:10:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-18 21:35:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 01:04:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-18 20:18:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-19 00:35:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-random | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 08:58:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 10:25:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 01:02:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 512 | [512] | mean | jsd | 21-01-18 21:50:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-18 19:20:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-random | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 08:58:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-18 08:48:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-18 23:11:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 10:11:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:12:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-18 08:53:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 21:47:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | bilinear | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 23:43:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-18 23:05:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 00:49:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-18 17:26:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-18 09:02:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-18 21:40:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-19 00:23:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-18 08:45:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 21:36:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-18 11:08:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-18 22:35:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-18 08:41:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 09:05:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-18 08:42:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-19 00:48:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-19 05:40:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | [256] | mean | jsd | 21-01-18 09:20:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 14:01:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | mlp | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-18 10:04:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-18 22:42:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 13:19:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-18 11:05:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-18 23:18:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 18:35:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 23:22:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 11:53:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 01:09:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-18 08:42:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-18 21:44:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-18 21:42:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-18 18:48:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 10:28:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:12:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 08:42:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-19 01:36:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 11:58:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-18 21:50:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 01:21:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 22:28:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-19 02:53:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 17:57:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-18 22:38:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-18 11:47:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 03:59:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | bilinear | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:11:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-19 00:34:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 09:33:23 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 23:25:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 00:42:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 10:24:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-18 19:30:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | linear | mlp | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-18 21:34:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 08:43:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 21:47:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 01:15:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 19:12:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-15 17:03:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 02:00:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-15 17:05:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-15 17:07:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-16 17:34:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-15 22:36:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:19:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-19 07:02:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 10:01:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 06:34:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-15 21:54:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 07:26:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-18 09:27:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 11:21:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 11:09:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 06:08:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 06:29:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 06:25:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-15 21:42:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 02:30:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-19 06:09:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-15 21:49:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-16 18:45:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 22:05:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 21:46:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 06:19:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 07:23:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 2000 | 128 | - | mean | jsd | 21-01-15 10:30:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 07:16:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-19 07:32:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 07:41:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 06:20:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 07:53:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 06:26:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 00:50:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:08:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256] | mean | jsd | 21-01-16 01:04:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-19 06:12:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 06:57:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-15 16:38:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:47:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | [512] | mean | jsd | 21-01-19 06:02:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 06:14:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-19 06:28:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 07:11:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-18 11:32:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 16:49:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-18 11:16:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-15 17:23:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 07:06:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:46:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-19 06:27:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 15:43:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-19 08:03:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-19 06:52:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 22:03:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-16 17:52:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 21:45:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-19 06:06:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 17:29:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 18:28:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 17:33:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-19 06:24:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 21:40:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-15 17:50:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 07:27:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:44:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 17:42:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-19 07:10:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-16 17:34:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 06:28:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | - | 128 | - | mean | jsd | 21-01-15 12:52:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-19 06:32:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 22:28:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-18 11:43:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-16 18:57:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 01:08:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 07:54:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-18 11:42:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 06:12:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:08:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 06:13:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-19 06:43:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 06:59:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-19 07:51:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-15 12:50:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 07:43:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 23:24:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-19 07:35:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 06:19:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:19:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-19 07:09:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 15:00:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-15 18:12:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 22:54:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:18:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:22:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-19 07:19:23 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 10:14:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 06:38:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 07:06:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 06:36:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-15 22:31:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 09:46:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 17:59:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-15 16:58:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 09:37:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-16 18:17:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-15 22:40:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 01:28:23 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-19 06:35:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 19:05:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 06:26:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 07:46:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 09:46:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 21:45:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-18 09:26:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-19 06:45:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-15 22:02:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 07:54:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512] | mean | jsd | 21-01-15 17:15:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-15 23:11:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:08:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-15 23:51:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 22:03:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-18 11:41:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:46:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-18 12:33:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-15 21:48:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-18 11:06:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-18 11:13:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-18 11:11:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 07:33:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-18 12:13:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 11:51:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 06:03:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-15 16:44:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-15 21:42:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:44:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:44:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 06:26:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 11:12:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 08:00:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 06:08:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 11:25:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-19 07:48:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:19:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-18 11:09:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-18 11:18:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 17:32:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:08:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-19 06:19:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 2000 | 128 | - | mean | jsd | 21-01-15 10:31:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-15 21:46:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 07:40:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-18 11:13:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 11:11:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 12:08:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 06:41:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 06:25:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 17:47:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:43:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-15 17:18:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-19 07:52:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 00:17:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 11:12:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 21:52:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-18 11:15:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 07:55:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-19 07:47:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-15 23:18:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 17:31:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-15 17:13:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 18:05:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-14 23:38:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-18 11:38:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-15 23:45:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-19 06:16:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 09:52:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 07:49:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-15 22:05:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-19 06:45:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-16 17:53:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-19 06:27:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 23:22:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-19 06:34:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 18:33:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-16 03:08:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-15 16:43:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 06:03:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-19 06:07:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:47:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:44:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 17:45:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:19:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-15 21:39:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 09:38:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-18 12:09:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-18 11:44:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-19 08:01:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 512 | [512] | mean | jsd | 21-01-16 18:01:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-19 07:21:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-15 23:11:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-15 21:47:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 06:05:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 06:58:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-19 06:51:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-14 23:25:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 06:48:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 11:48:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-18 09:26:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 09:49:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 22:59:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 17:45:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 11:19:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-19 06:38:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 06:29:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-15 21:58:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:19:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-16 18:40:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-16 00:43:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-15 18:17:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-19 07:03:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-16 17:36:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-19 06:28:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 300 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-15 10:41:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:43:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-19 07:11:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-15 21:43:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-15 21:40:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 23:20:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 11:45:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-19 07:01:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 17:46:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 08:00:23 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-19 08:01:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-15 19:57:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-16 17:39:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-16 00:37:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-16 04:17:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-15 23:12:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 23:13:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 06:21:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-19 07:51:23 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-19 07:13:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-19 06:27:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 09:47:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 06:04:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 1000 | 128 | - | mean | jsd | 21-01-15 10:43:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 06:36:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-18 10:01:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 07:45:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 18:45:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:44:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 06:15:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-18 09:26:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 11:34:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 07:06:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 23:05:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 11:23:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-15 21:52:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 11:45:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256] | mean | jsd | 21-01-18 11:27:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 09:26:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-19 07:58:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-15 20:09:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-19 06:24:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-19 06:54:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 19:03:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-16 02:27:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 06:14:23 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 06:36:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-16 06:21:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 11:26:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-14 23:36:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-19 06:34:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-15 17:22:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-18 09:26:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 07:29:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-19 06:11:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 07:50:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-16 17:37:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-19 06:47:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 09:54:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 07:59:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-18 13:19:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 06:16:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-16 11:37:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 10:46:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:18:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 06:40:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-16 00:57:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-16 00:41:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 17:33:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-19 07:04:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:21:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-16 00:45:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256] | mean | jsd | 21-01-19 07:22:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-19 07:53:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 21:59:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-15 21:44:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-16 00:39:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-16 08:15:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-16 18:21:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 06:57:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 15:23:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:21:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 17:48:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:46:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 06:37:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-18 09:33:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-19 06:56:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:43:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-19 06:04:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 07:44:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 06:06:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-16 00:40:23 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-19 06:10:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 17:54:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:08:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 07:13:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 07:14:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-15 23:38:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:08:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 11:47:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-19 06:18:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 18:15:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-19 06:06:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-19 07:57:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-18 14:22:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-19 07:02:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 09:51:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 17:44:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-18 09:45:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-19 06:08:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 06:59:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-19 07:00:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-18 11:31:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-18 09:26:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 512 | [512] | mean | jsd | 21-01-15 20:30:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 09:55:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:46:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-19 06:56:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-15 19:43:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-15 17:59:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 07:18:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 12:03:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:08:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-19 06:06:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-18 11:50:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-18 10:55:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 23:12:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 07:40:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 07:05:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 17:27:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 12:05:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 14:54:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 17:50:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-15 20:20:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-15 22:24:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-15 23:17:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-18 11:18:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-16 09:40:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 11:54:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 18:53:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 18:12:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-15 21:51:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 06:48:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 06:22:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-15 21:41:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-15 17:35:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-18 09:56:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 17:50:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-16 17:32:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-19 06:23:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-19 07:37:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-19 06:10:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-19 06:11:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-19 07:30:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 300 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-15 10:27:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-16 03:21:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-19 07:04:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-19 06:04:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-15 20:19:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 06:36:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 10:38:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-15 22:00:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-19 06:29:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 20:20:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 00:55:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 300 | 0.01 | 2000 | 128 | - | mean | jsd | 21-01-15 10:29:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-15 17:54:23 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-15 16:42:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:19:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 06:17:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 11:20:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 06:42:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 17:51:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-19 06:38:23 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:42:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-19 07:23:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-18 12:01:16 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-15 23:32:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 10:20:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-15 19:21:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-18 10:02:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 06:15:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-16 17:57:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 06:50:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 22:18:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 06:07:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 16:40:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-15 21:40:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | - | 128 | - | mean | jsd | 21-01-15 12:50:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-19 07:58:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-19 07:33:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-19 06:53:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-19 07:20:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 11:35:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-19 06:34:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-19 07:46:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-18 11:10:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 19:02:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-18 10:12:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-19 06:17:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 06:58:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-19 06:39:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-15 21:44:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 11:37:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 11:23:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-19 06:05:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 06:13:31 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-15 21:50:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 07:00:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-18 11:28:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 07:15:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 17:33:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-18 12:58:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-19 06:35:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 16:39:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-18 11:16:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-19 07:27:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-19 06:34:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 06:25:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-19 07:56:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-16 05:26:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 06:28:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-18 11:10:23 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 12:07:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 12:10:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-16 17:40:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-19 07:14:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 07:51:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 256 | [256] | mean | jsd | 21-01-15 22:07:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-19 07:34:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-15 21:42:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:44:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 09:37:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-15 22:49:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-15 21:53:45 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 00:52:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-15 21:56:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 07:38:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 09:50:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-18 11:27:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-15 21:43:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-19 06:05:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-19 06:53:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-15 22:13:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:47:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-19 07:52:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 06:07:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | [256] | mean | jsd | 21-01-19 07:08:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-15 20:19:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 15:13:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-18 09:44:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-16 17:49:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-18 11:41:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-19 06:25:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-16 01:35:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-15 18:31:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 06:35:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 07:50:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-19 06:05:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-18 10:37:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:44:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 06:21:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:08:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-19 07:52:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 10:11:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 12:07:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-19 06:35:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 300 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-15 10:10:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-15 22:10:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-19 07:00:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-15 22:44:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-19 07:36:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 07:36:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-15 19:32:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-19 06:55:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-19 06:24:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:19:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-18 09:34:10 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-15 22:09:23 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:08:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-18 11:42:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-19 08:03:42 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-19 07:48:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 07:49:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 22:04:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-19 06:44:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 06:12:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-19 07:31:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-16 18:31:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-19 07:02:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 08:57:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-19 07:12:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 10:02:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512] | mean | jsd | 21-01-15 21:59:03 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 06:40:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-19 06:11:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 17:33:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 07:42:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-19 06:26:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-16 02:37:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-16 00:48:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 16:54:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 07:28:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-19 06:46:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 18:54:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 15:46:28 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-16 17:36:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-18 11:40:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-19 07:55:38 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-15 17:25:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-15 17:10:29 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-16 17:38:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 18:08:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 16:52:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-16 17:48:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-15 16:41:15 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-19 07:56:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 07:08:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-19 06:23:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:08:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:43:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-16 17:55:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-15 16:47:17 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-19 06:39:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 18:49:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-15 23:14:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-19 06:46:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-18 12:10:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-19 06:09:49 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 09:29:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-19 06:40:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 21:40:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 06:07:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:47:01 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 06:41:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 17:41:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 09:52:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-19 06:52:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-19 07:53:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:21:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 07:42:05 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 06:37:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:09:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-19 06:10:36 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 10:12:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-18 09:33:23 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 17:33:27 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-15 17:00:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 06:29:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 11:36:46 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-16 17:52:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-19 07:47:18 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-19 06:54:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 11:33:53 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 07:08:55 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:19:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 03:08:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 09:58:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-15 20:19:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 22:16:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 10:30:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 07:49:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 12:11:44 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-15 21:57:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-19 07:49:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 07:50:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-15 22:21:34 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 16:39:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-19 06:18:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 09:29:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 02:34:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 16:56:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 22:04:20 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:22:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 07:30:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 06:25:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-19 07:47:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-18 11:18:12 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 07:48:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256] | mean | jsd | 21-01-19 06:09:39 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-18 09:36:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 07:07:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-19 06:49:58 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-15 22:01:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-18 12:09:07 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 17:35:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-19 06:09:02 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 06:42:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 18:39:19 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:46:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 06:43:26 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 07:54:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-19 08:02:21 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-18 13:59:57 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 02:51:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:42:00 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 01:23:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:47:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:24 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 16:50:30 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 17:38:40 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-19 06:47:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-19 07:17:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:46:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 07:17:43 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-15 22:02:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-19 07:39:14 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-18 14:36:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-19 06:41:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-15 23:25:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:54 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-19 06:14:04 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-19 08:04:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-19 07:20:51 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-19 07:54:47 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-19 07:24:59 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-19 06:24:06 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 18:24:37 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-15 21:55:32 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-15 23:15:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-16 17:49:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-15 21:41:11 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 18:35:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-15 17:38:22 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-19 06:24:13 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-15 17:41:41 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-16 17:43:09 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:44:33 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-18 08:19:25 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-19 06:38:52 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 22:06:50 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256] | mean | jsd | 21-01-18 11:29:35 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-18 09:57:56 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | citeseer | none | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-19 06:55:48 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | pubmed | none | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-18 13:39:08 | 0 | 0 | 0 | 0 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-18 09:25:48 | 0 | 0 | 0 | 0 | 

