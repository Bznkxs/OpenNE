# Logs

| name | dataset | enc | dec | sampler | epochs | lr | early_stopping | dim | hiddens | readout | est | time | micro | macro | samples | weighted | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-17 19:10:52 | 0.779 | 0.7592 | 0.779 | 0.7765 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-17 17:44:59 | 0.7702 | 0.763 | 0.7702 | 0.7696 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 23:00:29 | 0.7647 | 0.7573 | 0.7647 | 0.7638 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-18 00:36:27 | 0.7642 | 0.7647 | 0.7642 | 0.7644 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 20:46:27 | 0.7619 | 0.7565 | 0.7619 | 0.7614 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-17 22:00:10 | 0.7503 | 0.7404 | 0.7503 | 0.7486 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-17 19:15:49 | 0.7494 | 0.7333 | 0.7494 | 0.7462 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-17 17:20:34 | 0.7467 | 0.7403 | 0.7467 | 0.7451 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-17 21:14:13 | 0.7462 | 0.738 | 0.7462 | 0.7447 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 19:28:53 | 0.743 | 0.7362 | 0.743 | 0.7428 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-17 23:29:11 | 0.742 | 0.7322 | 0.742 | 0.7409 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-17 18:57:28 | 0.7388 | 0.7318 | 0.7388 | 0.7391 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 18:20:19 | 0.737 | 0.732 | 0.737 | 0.7356 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-17 16:46:42 | 0.736 | 0.7052 | 0.736 | 0.733 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 20:27:46 | 0.731 | 0.7219 | 0.731 | 0.7291 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-17 22:23:33 | 0.7305 | 0.7212 | 0.7305 | 0.7294 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 22:05:04 | 0.7259 | 0.7147 | 0.7259 | 0.7253 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 18:41:46 | 0.7217 | 0.7154 | 0.7217 | 0.7211 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-18 01:28:06 | 0.7194 | 0.7097 | 0.7194 | 0.7193 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-17 21:57:07 | 0.7093 | 0.7057 | 0.7093 | 0.707 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-17 17:13:24 | 0.7065 | 0.7057 | 0.7065 | 0.7056 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-17 17:29:20 | 0.7005 | 0.6874 | 0.7005 | 0.6998 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-17 22:09:05 | 0.6996 | 0.69 | 0.6996 | 0.6992 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 16:58:36 | 0.6964 | 0.6552 | 0.6964 | 0.6873 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-17 17:51:31 | 0.6964 | 0.6899 | 0.6964 | 0.6963 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-17 16:27:31 | 0.6899 | 0.6837 | 0.6899 | 0.6883 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-17 20:05:00 | 0.6876 | 0.6695 | 0.6876 | 0.6845 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-17 22:32:35 | 0.6844 | 0.6727 | 0.6844 | 0.6822 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-17 17:03:06 | 0.682 | 0.6619 | 0.682 | 0.6803 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-17 23:53:17 | 0.6784 | 0.6579 | 0.6784 | 0.6779 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-17 16:22:53 | 0.676 | 0.6743 | 0.676 | 0.6748 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-17 16:11:47 | 0.6742 | 0.6669 | 0.6742 | 0.6733 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-17 16:45:31 | 0.6728 | 0.6688 | 0.6728 | 0.6721 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 16:54:11 | 0.6728 | 0.6399 | 0.6728 | 0.6656 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-17 16:04:33 | 0.6714 | 0.6473 | 0.6714 | 0.6679 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 23:37:25 | 0.6701 | 0.6033 | 0.6701 | 0.6312 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-17 17:26:04 | 0.6687 | 0.6439 | 0.6687 | 0.6626 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 12:02:38 | 0.6636 | 0.6462 | 0.6636 | 0.6565 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-17 17:37:14 | 0.6567 | 0.5773 | 0.6567 | 0.6331 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 18:02:36 | 0.6562 | 0.6357 | 0.6562 | 0.6504 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-17 16:49:29 | 0.6548 | 0.624 | 0.6548 | 0.6506 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-17 20:15:24 | 0.6507 | 0.6293 | 0.6507 | 0.6451 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-17 16:08:02 | 0.6497 | 0.6116 | 0.6497 | 0.6154 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 17:31:54 | 0.6493 | 0.6175 | 0.6493 | 0.6389 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:44:46 | 0.6437 | 0.6252 | 0.6437 | 0.639 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 300 | 0.01 | 100 | 128 | - | mean | jsd | 21-01-15 09:58:49 | 0.6433 | 0.626 | 0.6433 | 0.6393 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-17 18:04:21 | 0.6424 | 0.6326 | 0.6424 | 0.6398 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 11:45:53 | 0.641 | 0.6161 | 0.641 | 0.634 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-17 22:16:49 | 0.6364 | 0.5507 | 0.6364 | 0.6108 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | - | - | - | 128 | - | mean | jsd | 21-01-16 05:22:50 | 0.6294 | 0.6111 | 0.6294 | 0.6234 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-17 22:35:53 | 0.6225 | 0.5513 | 0.6225 | 0.5997 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:43:55 | 0.6156 | 0.5773 | 0.6156 | 0.6032 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-17 16:13:32 | 0.6082 | 0.5157 | 0.6082 | 0.5715 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 300 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 12:11:51 | 0.5944 | 0.5657 | 0.5944 | 0.5901 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 16:52:04 | 0.5916 | 0.4975 | 0.5916 | 0.5548 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 19:39:22 | 0.5842 | 0.5066 | 0.5842 | 0.5619 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 20:57:55 | 0.581 | 0.5366 | 0.581 | 0.5648 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-17 23:41:16 | 0.5759 | 0.5559 | 0.5759 | 0.5651 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-17 19:48:00 | 0.5727 | 0.5158 | 0.5727 | 0.5472 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-17 16:15:26 | 0.5695 | 0.5401 | 0.5695 | 0.5467 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-17 17:35:44 | 0.569 | 0.5235 | 0.569 | 0.5375 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-17 17:33:57 | 0.5602 | 0.5003 | 0.5602 | 0.5372 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-17 17:25:24 | 0.5542 | 0.5108 | 0.5542 | 0.5371 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 12:10:56 | 0.5496 | 0.4836 | 0.5496 | 0.5246 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-17 16:24:58 | 0.5307 | 0.4951 | 0.5307 | 0.5147 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-17 23:13:04 | 0.5279 | 0.4986 | 0.5279 | 0.5133 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-17 16:02:57 | 0.5104 | 0.4178 | 0.5104 | 0.4568 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-17 17:41:31 | 0.509 | 0.4516 | 0.509 | 0.4845 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-17 17:42:31 | 0.5035 | 0.3744 | 0.5035 | 0.457 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-17 21:05:57 | 0.4933 | 0.4446 | 0.4933 | 0.4725 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-18 02:19:37 | 0.4813 | 0.436 | 0.4813 | 0.4604 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.001 | 50 | 128 | - | mean | jsd | 21-01-15 11:54:43 | 0.4749 | 0.4337 | 0.4749 | 0.4558 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-17 18:34:50 | 0.4716 | 0.3648 | 0.4716 | 0.4207 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-17 23:42:57 | 0.4555 | 0.3408 | 0.4555 | 0.3922 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.001 | 50 | 128 | - | mean | jsd | 21-01-15 11:50:09 | 0.4504 | 0.3403 | 0.4504 | 0.4014 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 16:31:28 | 0.4347 | 0.3158 | 0.4347 | 0.3706 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-17 17:11:59 | 0.4209 | 0.3399 | 0.4209 | 0.3659 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 16:19:59 | 0.419 | 0.2607 | 0.419 | 0.3234 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512] | mean | jsd | 21-01-17 21:26:28 | 0.4061 | 0.2993 | 0.4061 | 0.3458 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-17 22:02:54 | 0.3946 | 0.2295 | 0.3946 | 0.3142 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-17 18:08:53 | 0.3927 | 0.2571 | 0.3927 | 0.3172 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-17 17:07:21 | 0.3918 | 0.2264 | 0.3918 | 0.2952 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-17 17:16:09 | 0.3756 | 0.2411 | 0.3756 | 0.2993 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-17 19:57:13 | 0.3715 | 0.2072 | 0.3715 | 0.2776 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-17 22:21:52 | 0.3641 | 0.2008 | 0.3641 | 0.263 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-17 23:44:32 | 0.3563 | 0.1637 | 0.3563 | 0.2502 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 20:38:56 | 0.353 | 0.1744 | 0.353 | 0.2423 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-17 17:27:21 | 0.3521 | 0.1777 | 0.3521 | 0.2589 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 17:48:31 | 0.3503 | 0.1492 | 0.3503 | 0.23 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-17 22:12:18 | 0.3498 | 0.182 | 0.3498 | 0.2468 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 23:11:09 | 0.3429 | 0.1706 | 0.3429 | 0.232 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-17 18:14:35 | 0.3369 | 0.1399 | 0.3369 | 0.2122 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-16 04:27:13 | 0.3318 | 0.1478 | 0.3318 | 0.2165 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-16 04:34:40 | 0.3318 | 0.1478 | 0.3318 | 0.2165 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 20:59:59 | 0.3295 | 0.1546 | 0.3295 | 0.213 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-18 01:48:09 | 0.3263 | 0.1282 | 0.3263 | 0.2033 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 22:50:16 | 0.3152 | 0.103 | 0.3152 | 0.177 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 17:49:08 | 0.3106 | 0.1064 | 0.3106 | 0.1782 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-17 17:05:46 | 0.3087 | 0.0888 | 0.3087 | 0.1611 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 22:45:51 | 0.3069 | 0.0956 | 0.3069 | 0.1676 | 
| ss_nodemodel | cora | gat | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-17 19:20:45 | 0.3055 | 0.1085 | 0.3055 | 0.1823 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-17 16:17:30 | 0.3032 | 0.0798 | 0.3032 | 0.151 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 18:50:38 | 0.3009 | 0.0811 | 0.3009 | 0.1528 | 
| ss_nodemodel | cora | gat | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-18 03:57:19 | 0.3004 | 0.0966 | 0.3004 | 0.1696 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 16:33:17 | 0.2953 | 0.0684 | 0.2953 | 0.138 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 17:17:01 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-14 23:24:09 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-15 09:39:17 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-15 09:37:22 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-17 16:38:20 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 18:27:52 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 17:08:29 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 300 | 1e-05 | 100 | 128 | - | mean | jsd | 21-01-15 09:48:35 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gat | inner | node-neighbor-random | 300 | 1e-05 | 100 | 128 | - | mean | jsd | 21-01-15 09:45:32 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.03 | 20 | 512 | [512] | mean | jsd | 21-01-17 17:55:03 | 0.2944 | 0.0733 | 0.2944 | 0.1415 | 
| ss_nodemodel | cora | gat | inner | node-rand_walk-random | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 18:00:17 | 0.2912 | 0.0668 | 0.2912 | 0.1351 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-17 04:22:57 | 0.8076 | 0.7986 | 0.8076 | 0.8067 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-16 23:12:06 | 0.803 | 0.792 | 0.803 | 0.8013 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-16 22:47:09 | 0.8016 | 0.7912 | 0.8016 | 0.8006 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-17 05:43:42 | 0.8006 | 0.7956 | 0.8006 | 0.7993 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-16 23:47:52 | 0.7997 | 0.7877 | 0.7997 | 0.7978 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-16 22:42:45 | 0.7988 | 0.7886 | 0.7988 | 0.7971 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | [256] | mean | jsd | 21-01-17 09:48:03 | 0.7905 | 0.788 | 0.7905 | 0.7899 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-17 09:32:24 | 0.7891 | 0.7747 | 0.7891 | 0.7881 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-17 01:22:33 | 0.7868 | 0.7724 | 0.7868 | 0.786 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-16 20:58:50 | 0.7845 | 0.7719 | 0.7845 | 0.7829 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:38:06 | 0.7808 | 0.7728 | 0.7808 | 0.7792 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:38:32 | 0.7808 | 0.7728 | 0.7808 | 0.7792 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:32:20 | 0.7808 | 0.7728 | 0.7808 | 0.7792 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:37:14 | 0.7808 | 0.7728 | 0.7808 | 0.7792 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:48:42 | 0.7808 | 0.7728 | 0.7808 | 0.7792 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:43:25 | 0.7808 | 0.7728 | 0.7808 | 0.7792 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:40:51 | 0.7808 | 0.7728 | 0.7808 | 0.7792 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:39:55 | 0.7808 | 0.7728 | 0.7808 | 0.7792 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:39:40 | 0.7808 | 0.7728 | 0.7808 | 0.7792 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-16 21:06:13 | 0.779 | 0.7688 | 0.779 | 0.7771 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-16 23:44:05 | 0.7766 | 0.7638 | 0.7766 | 0.7737 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-16 19:53:52 | 0.7753 | 0.7697 | 0.7753 | 0.7744 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-16 23:52:11 | 0.7748 | 0.7631 | 0.7748 | 0.7733 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-16 19:30:38 | 0.7725 | 0.7671 | 0.7725 | 0.7717 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-17 15:02:14 | 0.7702 | 0.757 | 0.7702 | 0.7685 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 20 | - | - | 128 | - | mean | jsd | 21-01-15 12:42:59 | 0.7693 | 0.7593 | 0.7693 | 0.7671 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-16 20:59:40 | 0.7693 | 0.7525 | 0.7693 | 0.7668 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-16 22:36:50 | 0.7679 | 0.7507 | 0.7679 | 0.7654 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-16 19:12:20 | 0.7679 | 0.7626 | 0.7679 | 0.7665 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-16 19:26:00 | 0.767 | 0.7618 | 0.767 | 0.7653 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | - | - | - | 128 | - | mean | jsd | 21-01-15 12:31:07 | 0.7642 | 0.7598 | 0.7642 | 0.7627 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | - | - | - | 128 | - | mean | jsd | 21-01-15 12:41:29 | 0.7642 | 0.7598 | 0.7642 | 0.7627 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-16 19:12:57 | 0.7637 | 0.759 | 0.7637 | 0.7625 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-17 09:24:33 | 0.7628 | 0.747 | 0.7628 | 0.7611 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-16 20:19:53 | 0.7619 | 0.7523 | 0.7619 | 0.7606 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-16 19:33:10 | 0.7619 | 0.7523 | 0.7619 | 0.7606 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:42:42 | 0.7587 | 0.7492 | 0.7587 | 0.7573 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-16 20:37:45 | 0.7582 | 0.7502 | 0.7582 | 0.7571 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 20 | - | - | 128 | - | mean | jsd | 21-01-15 12:45:39 | 0.7559 | 0.7497 | 0.7559 | 0.7542 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 19:45:42 | 0.755 | 0.7519 | 0.755 | 0.7539 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | - | - | - | 128 | - | mean | jsd | 21-01-15 12:45:58 | 0.7545 | 0.743 | 0.7545 | 0.7524 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-17 14:52:04 | 0.7545 | 0.7433 | 0.7545 | 0.7532 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | - | - | - | 128 | - | mean | jsd | 21-01-15 12:47:40 | 0.7457 | 0.7346 | 0.7457 | 0.7441 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.001 | 50 | 128 | - | mean | jsd | 21-01-15 11:03:37 | 0.7448 | 0.7383 | 0.7448 | 0.7451 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-17 15:42:54 | 0.7425 | 0.7375 | 0.7425 | 0.7409 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 19:27:58 | 0.7425 | 0.7455 | 0.7425 | 0.7436 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-17 14:43:02 | 0.7402 | 0.7338 | 0.7402 | 0.7388 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 19:15:14 | 0.7388 | 0.7411 | 0.7388 | 0.74 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-16 19:27:07 | 0.7383 | 0.7311 | 0.7383 | 0.7365 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256] | mean | jsd | 21-01-17 14:41:54 | 0.7351 | 0.733 | 0.7351 | 0.7352 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-16 19:31:53 | 0.7347 | 0.7263 | 0.7347 | 0.7344 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-16 20:24:21 | 0.7342 | 0.7243 | 0.7342 | 0.7325 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-16 19:39:41 | 0.7337 | 0.7202 | 0.7337 | 0.7321 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 20:33:03 | 0.7323 | 0.7306 | 0.7323 | 0.7323 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-16 19:29:24 | 0.7305 | 0.728 | 0.7305 | 0.7297 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-17 14:48:56 | 0.7296 | 0.7164 | 0.7296 | 0.7287 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-16 19:13:26 | 0.7296 | 0.7197 | 0.7296 | 0.7279 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-16 19:20:15 | 0.7296 | 0.7197 | 0.7296 | 0.7279 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 14:58:03 | 0.7231 | 0.7192 | 0.7231 | 0.7226 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-16 19:14:17 | 0.7217 | 0.7113 | 0.7217 | 0.7195 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-17 15:35:16 | 0.7217 | 0.7106 | 0.7217 | 0.7208 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 10 | - | - | 128 | - | mean | jsd | 21-01-15 12:48:22 | 0.7208 | 0.6849 | 0.7208 | 0.7136 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 14:51:02 | 0.7199 | 0.7156 | 0.7199 | 0.7178 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 20:49:44 | 0.7171 | 0.7086 | 0.7171 | 0.7159 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-17 14:55:16 | 0.7148 | 0.704 | 0.7148 | 0.7127 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-16 23:49:17 | 0.7144 | 0.6948 | 0.7144 | 0.709 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 20:11:45 | 0.7139 | 0.7134 | 0.7139 | 0.7148 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-16 19:50:23 | 0.7134 | 0.7082 | 0.7134 | 0.7105 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-16 19:30:02 | 0.7134 | 0.7082 | 0.7134 | 0.7105 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 14:42:19 | 0.7125 | 0.7101 | 0.7125 | 0.7104 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-16 21:00:41 | 0.7056 | 0.6747 | 0.7056 | 0.7013 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-17 15:32:24 | 0.6982 | 0.6833 | 0.6982 | 0.696 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-17 15:36:46 | 0.6982 | 0.69 | 0.6982 | 0.6976 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 19:24:40 | 0.6931 | 0.6884 | 0.6931 | 0.692 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-17 14:40:44 | 0.689 | 0.6721 | 0.689 | 0.6864 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 22:40:39 | 0.6848 | 0.6741 | 0.6848 | 0.6815 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-14 23:23:11 | 0.6839 | 0.675 | 0.6839 | 0.6808 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 300 | - | - | 128 | - | mean | jsd | 21-01-14 23:30:33 | 0.6839 | 0.675 | 0.6839 | 0.6808 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 14:46:08 | 0.6802 | 0.6704 | 0.6802 | 0.6744 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-17 14:45:16 | 0.6788 | 0.6668 | 0.6788 | 0.6743 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 21:01:44 | 0.6765 | 0.6711 | 0.6765 | 0.6763 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-17 15:26:17 | 0.6668 | 0.641 | 0.6668 | 0.6627 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-17 14:40:24 | 0.6641 | 0.6408 | 0.6641 | 0.6599 | 
| line | cora | gcn | inner | node-rand_walk-random | - | - | - | 128 | - | mean | jsd | 21-01-15 10:13:16 | 0.6636 | 0.6547 | 0.6636 | 0.6619 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.02 | 100 | 128 | - | mean | jsd | 21-01-15 10:52:04 | 0.6617 | 0.647 | 0.6617 | 0.6574 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-17 15:30:18 | 0.6585 | 0.6345 | 0.6585 | 0.6559 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 0 | - | - | 128 | - | mean | jsd | 21-01-15 12:46:40 | 0.6576 | 0.6394 | 0.6576 | 0.6533 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 19:19:10 | 0.6507 | 0.6367 | 0.6507 | 0.6451 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-17 14:47:08 | 0.6497 | 0.6247 | 0.6497 | 0.6454 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.02 | 100 | 128 | - | mean | jsd | 21-01-15 10:48:55 | 0.6327 | 0.6188 | 0.6327 | 0.6279 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-17 15:12:28 | 0.6267 | 0.6012 | 0.6267 | 0.6201 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-17 15:11:09 | 0.6257 | 0.6009 | 0.6257 | 0.6132 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 21:26:09 | 0.6105 | 0.5937 | 0.6105 | 0.5968 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-17 14:39:25 | 0.6064 | 0.5891 | 0.6064 | 0.6018 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-17 14:53:24 | 0.5893 | 0.5572 | 0.5893 | 0.5692 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-17 15:07:48 | 0.5888 | 0.5569 | 0.5888 | 0.5688 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 22:56:37 | 0.5884 | 0.5734 | 0.5884 | 0.5762 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 10:52:57 | 0.5838 | 0.5575 | 0.5838 | 0.5754 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.001 | 50 | 128 | - | mean | jsd | 21-01-15 10:56:43 | 0.5745 | 0.5489 | 0.5745 | 0.5667 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 10:54:30 | 0.5607 | 0.5343 | 0.5607 | 0.5491 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-17 14:41:19 | 0.5487 | 0.4993 | 0.5487 | 0.524 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 20:07:57 | 0.4961 | 0.3196 | 0.4961 | 0.4149 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 22:39:22 | 0.4495 | 0.307 | 0.4495 | 0.3617 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-17 14:40:04 | 0.4139 | 0.2843 | 0.4139 | 0.3222 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 22:41:41 | 0.407 | 0.2152 | 0.407 | 0.3044 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-17 15:19:21 | 0.3802 | 0.1743 | 0.3802 | 0.2558 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-17 14:48:45 | 0.3761 | 0.2142 | 0.3761 | 0.2648 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 15:49:30 | 0.3687 | 0.157 | 0.3687 | 0.2397 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 09:31:19 | 0.3613 | 0.1893 | 0.3613 | 0.2468 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-17 00:10:29 | 0.359 | 0.1497 | 0.359 | 0.2308 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-17 13:00:46 | 0.3498 | 0.193 | 0.3498 | 0.2205 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 23:35:15 | 0.347 | 0.201 | 0.347 | 0.2317 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 19:32:57 | 0.3336 | 0.1754 | 0.3336 | 0.2095 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 20:15:40 | 0.3332 | 0.1746 | 0.3332 | 0.209 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 21:04:16 | 0.3313 | 0.1219 | 0.3313 | 0.1986 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-17 14:39:47 | 0.3276 | 0.1541 | 0.3276 | 0.2283 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 19:16:24 | 0.3263 | 0.1216 | 0.3263 | 0.189 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 20:43:44 | 0.3207 | 0.1138 | 0.3207 | 0.1813 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-16 19:17:57 | 0.3207 | 0.1286 | 0.3207 | 0.2018 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 22:44:41 | 0.3193 | 0.1042 | 0.3193 | 0.1788 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 19:18:47 | 0.3193 | 0.1276 | 0.3193 | 0.1999 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-17 14:44:31 | 0.3161 | 0.0994 | 0.3161 | 0.1735 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 20:56:32 | 0.311 | 0.0972 | 0.311 | 0.1653 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 20:57:42 | 0.311 | 0.0972 | 0.311 | 0.1653 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 19:17:06 | 0.311 | 0.0972 | 0.311 | 0.1653 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 19:49:44 | 0.311 | 0.0972 | 0.311 | 0.1653 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 19:49:06 | 0.311 | 0.0972 | 0.311 | 0.1653 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 15:00:15 | 0.3096 | 0.0967 | 0.3096 | 0.1646 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 15:42:11 | 0.3096 | 0.0967 | 0.3096 | 0.1646 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512] | mean | jsd | 21-01-16 21:29:57 | 0.3083 | 0.0925 | 0.3083 | 0.1649 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-17 00:23:24 | 0.3018 | 0.0933 | 0.3018 | 0.15 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-16 19:31:25 | 0.3018 | 0.1143 | 0.3018 | 0.1842 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-17 14:55:53 | 0.3013 | 0.0805 | 0.3013 | 0.1515 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-16 22:44:19 | 0.2986 | 0.0718 | 0.2986 | 0.1419 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 22:39:07 | 0.2986 | 0.0793 | 0.2986 | 0.1495 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-17 15:04:10 | 0.2972 | 0.0694 | 0.2972 | 0.1392 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 22:49:18 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 19:22:49 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-16 20:28:39 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-17 14:54:06 | 0.2949 | 0.0651 | 0.2949 | 0.1344 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-17 14:48:04 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 14:44:04 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 19:38:01 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 23:51:55 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 19:14:49 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 21:03:55 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-17 14:57:00 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-17 15:56:09 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-16 19:22:00 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-16 20:04:17 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 10:34:02 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-17 00:05:13 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 19:13:59 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.01 | 20 | 512 | [512] | mean | jsd | 21-01-16 19:42:43 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 20:16:06 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-17 08:56:35 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 19:23:44 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 14:54:40 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 19:12:50 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-16 22:38:22 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 23:04:37 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-17 14:50:16 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-17 14:12:32 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-17 14:41:03 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 11:22:52 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-16 19:36:26 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 21:19:35 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 23:51:33 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 21:12:57 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-17 15:15:56 | 0.2949 | 0.0651 | 0.2949 | 0.1344 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-17 12:12:18 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 21:46:31 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 22:11:46 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 00:36:45 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-16 19:21:15 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-17 15:41:22 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-16 19:34:57 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-17 15:22:58 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-17 14:49:30 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-16 20:00:37 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | gcn | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 19:57:25 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| gcn | cora | gcn | inner | node-rand_walk-random | - | - | - | 128 | - | mean | jsd | 21-01-15 19:59:06 | 0.1674 | 0.8496 | 0.0057 | 
| ss_nodemodel | cora | gin | inner | node-neighbor-random | 500 | 0.03 | - | 128 | - | mean | jsd | 21-01-15 12:55:43 | 0.8283 | 0.8184 | 0.8283 | 0.8268 | 
| ss_nodemodel | cora | gin | inner | node-neighbor-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 11:39:16 | 0.8108 | 0.8038 | 0.8108 | 0.8092 | 
| ss_nodemodel | cora | gin | inner | node-neighbor-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 11:37:35 | 0.8076 | 0.796 | 0.8076 | 0.8068 | 
| ss_nodemodel | cora | gin | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-14 23:24:58 | 0.7287 | 0.7176 | 0.7287 | 0.7258 | 
| ss_nodemodel | cora | gin | inner | node-neighbor-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 11:06:33 | 0.7014 | 0.6924 | 0.7014 | 0.6988 | 
| ss_nodemodel | cora | gin | inner | node-neighbor-random | 500 | 0.01 | 50 | 128 | - | mean | jsd | 21-01-15 11:17:12 | 0.7 | 0.6902 | 0.7 | 0.6951 | 
| ss_nodemodel | cora | gin | inner | node-neighbor-random | 500 | 0.001 | 50 | 128 | - | mean | jsd | 21-01-15 11:05:15 | 0.6765 | 0.6665 | 0.6765 | 0.675 | 
| ss_nodemodel | cora | gin | inner | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-16 04:34:53 | 0.4855 | 0.4037 | 0.4855 | 0.4458 | 
| ss_nodemodel | cora | linear | inner | node-neighbor-random | 100 | - | - | 128 | - | mean | jsd | 21-01-14 23:41:44 | 0.5293 | 0.4951 | 0.5293 | 0.5226 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 19:12:38 | 0.7328 | 0.7289 | 0.7328 | 0.7326 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-15 17:23:49 | 0.7328 | 0.7289 | 0.7328 | 0.7326 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 17:29:26 | 0.7328 | 0.7289 | 0.7328 | 0.7326 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 17:33:13 | 0.7328 | 0.7289 | 0.7328 | 0.7326 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 18:54:34 | 0.7328 | 0.7289 | 0.7328 | 0.7326 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-15 17:25:49 | 0.7328 | 0.7289 | 0.7328 | 0.7326 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 22:05:18 | 0.7194 | 0.7157 | 0.7194 | 0.7187 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-15 22:02:49 | 0.7194 | 0.7157 | 0.7194 | 0.7187 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-15 22:05:53 | 0.7107 | 0.7 | 0.7107 | 0.7098 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-15 17:22:03 | 0.6927 | 0.6878 | 0.6927 | 0.6927 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 22:04:20 | 0.6922 | 0.6899 | 0.6922 | 0.6922 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-15 22:02:13 | 0.6922 | 0.6899 | 0.6922 | 0.6922 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-15 22:24:41 | 0.6742 | 0.6637 | 0.6742 | 0.6712 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 17:48:25 | 0.6608 | 0.6597 | 0.6608 | 0.6611 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-15 19:32:41 | 0.6608 | 0.6509 | 0.6608 | 0.6603 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-15 17:41:41 | 0.6608 | 0.6509 | 0.6608 | 0.6603 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-15 19:57:45 | 0.6544 | 0.6382 | 0.6544 | 0.65 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-15 17:54:23 | 0.6544 | 0.6382 | 0.6544 | 0.65 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-15 22:36:16 | 0.6447 | 0.6384 | 0.6447 | 0.6434 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-15 22:44:46 | 0.6447 | 0.6384 | 0.6447 | 0.6434 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-15 22:31:55 | 0.6008 | 0.592 | 0.6008 | 0.5974 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-15 22:40:37 | 0.6008 | 0.592 | 0.6008 | 0.5974 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 1000 | 128 | - | mean | jsd | 21-01-15 10:43:29 | 0.5635 | 0.5493 | 0.5635 | 0.5582 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 23:05:22 | 0.5635 | 0.5451 | 0.5635 | 0.5591 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-15 20:19:48 | 0.5362 | 0.5053 | 0.5362 | 0.5253 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 20:20:03 | 0.5362 | 0.5053 | 0.5362 | 0.5253 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-15 20:19:22 | 0.5362 | 0.5053 | 0.5362 | 0.5253 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 16:39:14 | 0.5362 | 0.5053 | 0.5362 | 0.5253 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 16:50:30 | 0.5362 | 0.5053 | 0.5362 | 0.5253 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 18:45:33 | 0.5335 | 0.5051 | 0.5335 | 0.5238 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 19:03:36 | 0.5335 | 0.5051 | 0.5335 | 0.5238 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 17:27:36 | 0.5335 | 0.5051 | 0.5335 | 0.5238 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64] | mean | jsd | 21-01-16 02:27:09 | 0.5279 | 0.4535 | 0.5279 | 0.5029 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-16 09:40:33 | 0.5279 | 0.4535 | 0.5279 | 0.5029 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 02:34:07 | 0.5279 | 0.4535 | 0.5279 | 0.5029 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 09:46:36 | 0.5159 | 0.444 | 0.5159 | 0.4744 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 21:47:38 | 0.4689 | 0.3928 | 0.4689 | 0.4402 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 2000 | 128 | - | mean | jsd | 21-01-15 10:31:00 | 0.4689 | 0.4332 | 0.4689 | 0.4594 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-15 21:40:15 | 0.4675 | 0.3987 | 0.4675 | 0.4455 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | - | 128 | - | mean | jsd | 21-01-15 12:52:03 | 0.4596 | 0.3795 | 0.4596 | 0.4206 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-15 21:42:01 | 0.4587 | 0.4138 | 0.4587 | 0.4458 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-15 21:49:18 | 0.4587 | 0.4138 | 0.4587 | 0.4458 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-15 21:42:20 | 0.4587 | 0.4138 | 0.4587 | 0.4458 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 21:52:03 | 0.4587 | 0.4138 | 0.4587 | 0.4458 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-15 21:43:13 | 0.4587 | 0.4138 | 0.4587 | 0.4458 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-15 21:51:06 | 0.4587 | 0.4138 | 0.4587 | 0.4458 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 10:30:04 | 0.4587 | 0.3478 | 0.4587 | 0.3875 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 02:51:33 | 0.4587 | 0.3478 | 0.4587 | 0.3875 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 10:14:15 | 0.4462 | 0.3354 | 0.4462 | 0.3776 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 03:08:00 | 0.4462 | 0.3354 | 0.4462 | 0.3776 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 22:03:51 | 0.4435 | 0.3142 | 0.4435 | 0.374 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 22:04:50 | 0.4435 | 0.3142 | 0.4435 | 0.374 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 22:28:17 | 0.443 | 0.3446 | 0.443 | 0.3857 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 22:06:50 | 0.443 | 0.3446 | 0.443 | 0.3857 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-15 17:50:55 | 0.4402 | 0.342 | 0.4402 | 0.3903 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-15 19:21:48 | 0.4402 | 0.342 | 0.4402 | 0.3903 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-15 17:38:22 | 0.4402 | 0.342 | 0.4402 | 0.3903 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 256 | [256] | mean | jsd | 21-01-16 05:26:27 | 0.4232 | 0.3016 | 0.4232 | 0.3614 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 23:13:20 | 0.4102 | 0.3153 | 0.4102 | 0.364 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-16 00:39:01 | 0.4102 | 0.3153 | 0.4102 | 0.364 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-16 04:17:04 | 0.4084 | 0.2796 | 0.4084 | 0.3347 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-15 17:59:43 | 0.4006 | 0.283 | 0.4006 | 0.3138 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-15 18:31:37 | 0.4006 | 0.283 | 0.4006 | 0.3138 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 15:46:28 | 0.3973 | 0.2872 | 0.3973 | 0.3536 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 22:59:54 | 0.3959 | 0.3155 | 0.3959 | 0.3564 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 22:18:53 | 0.3959 | 0.3155 | 0.3959 | 0.3564 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-15 22:49:00 | 0.3959 | 0.3155 | 0.3959 | 0.3564 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-15 22:13:36 | 0.3959 | 0.3155 | 0.3959 | 0.3564 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-15 23:11:00 | 0.3826 | 0.2643 | 0.3826 | 0.3178 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-16 11:37:00 | 0.3807 | 0.2175 | 0.3807 | 0.2802 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-15 19:43:35 | 0.3678 | 0.2043 | 0.3678 | 0.2594 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 16:49:01 | 0.3641 | 0.2239 | 0.3641 | 0.2767 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-15 23:12:11 | 0.3609 | 0.208 | 0.3609 | 0.2696 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-16 00:40:23 | 0.3609 | 0.208 | 0.3609 | 0.2696 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 23:12:46 | 0.3609 | 0.208 | 0.3609 | 0.2696 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 16:56:35 | 0.3539 | 0.1903 | 0.3539 | 0.2429 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 512 | - | mean | jsd | 21-01-16 06:21:11 | 0.3512 | 0.1582 | 0.3512 | 0.2412 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | [128] | mean | jsd | 21-01-16 00:48:08 | 0.3493 | 0.181 | 0.3493 | 0.2379 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 00:50:28 | 0.3466 | 0.1778 | 0.3466 | 0.2361 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 23:24:12 | 0.3466 | 0.1778 | 0.3466 | 0.2361 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-15 23:18:57 | 0.3466 | 0.1778 | 0.3466 | 0.2361 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-16 00:43:19 | 0.3466 | 0.1778 | 0.3466 | 0.2361 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 00:55:12 | 0.3466 | 0.1778 | 0.3466 | 0.2361 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-15 23:15:48 | 0.3466 | 0.1778 | 0.3466 | 0.2361 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 128 | - | mean | jsd | 21-01-15 21:41:37 | 0.3392 | 0.1865 | 0.3392 | 0.2611 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-15 21:42:46 | 0.3392 | 0.1865 | 0.3392 | 0.2611 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-15 21:52:55 | 0.3332 | 0.1295 | 0.3332 | 0.2062 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-15 21:44:05 | 0.3332 | 0.1295 | 0.3332 | 0.2062 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-15 21:56:22 | 0.3332 | 0.1295 | 0.3332 | 0.2062 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-15 21:57:11 | 0.3332 | 0.1295 | 0.3332 | 0.2062 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-16 08:15:07 | 0.3313 | 0.1233 | 0.3313 | 0.2003 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 08:57:27 | 0.3309 | 0.1414 | 0.3309 | 0.2206 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-15 23:32:07 | 0.3299 | 0.1241 | 0.3299 | 0.2008 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 00:17:51 | 0.329 | 0.1578 | 0.329 | 0.2209 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 23:22:42 | 0.329 | 0.1243 | 0.329 | 0.2009 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-16 00:41:17 | 0.329 | 0.1243 | 0.329 | 0.2009 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-15 23:17:25 | 0.329 | 0.1243 | 0.329 | 0.2009 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-15 23:14:11 | 0.329 | 0.1243 | 0.329 | 0.2009 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-15 20:19:35 | 0.3263 | 0.1611 | 0.3263 | 0.2174 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-15 16:47:17 | 0.3263 | 0.1611 | 0.3263 | 0.2174 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 01:23:06 | 0.3216 | 0.1177 | 0.3216 | 0.1933 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | - | mean | jsd | 21-01-15 17:00:52 | 0.3212 | 0.1217 | 0.3212 | 0.1964 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-15 23:51:41 | 0.317 | 0.1115 | 0.317 | 0.1864 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-15 17:07:55 | 0.3143 | 0.1137 | 0.3143 | 0.188 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-15 17:13:03 | 0.3143 | 0.1137 | 0.3143 | 0.188 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-15 16:43:35 | 0.3143 | 0.1137 | 0.3143 | 0.188 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-15 16:42:17 | 0.3143 | 0.1137 | 0.3143 | 0.188 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-15 18:17:43 | 0.3013 | 0.0877 | 0.3013 | 0.1593 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-15 20:09:31 | 0.3013 | 0.0877 | 0.3013 | 0.1593 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 512 | [512] | mean | jsd | 21-01-15 20:30:26 | 0.3013 | 0.0877 | 0.3013 | 0.1593 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 01:15:51 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-15 17:03:01 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 02:00:46 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-15 17:05:25 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-16 17:34:18 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-15 21:54:39 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 02:30:39 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-16 18:45:13 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256] | mean | jsd | 21-01-16 01:04:41 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-15 16:38:46 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:47:08 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:46:28 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 18:28:11 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256] | mean | jsd | 21-01-16 17:34:55 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-16 18:57:54 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 01:08:53 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-15 12:50:00 | 0.2949 | 0.0651 | 0.2949 | 0.1344 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-15 18:12:21 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 22:54:26 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 17:59:29 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-15 16:58:30 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-16 18:17:31 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 01:28:23 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 19:05:53 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 21:45:01 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512] | mean | jsd | 21-01-15 17:15:31 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:46:45 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-15 16:44:52 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 17:47:12 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-15 17:18:45 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 17:31:26 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 18:05:07 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-15 23:45:13 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-16 03:08:13 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:47:19 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 17:45:09 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 512 | [512] | mean | jsd | 21-01-16 18:01:38 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-15 23:11:25 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 17:45:05 | 0.2949 | 0.0667 | 0.2949 | 0.1362 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-16 18:40:19 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-16 17:36:55 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 17:46:10 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-16 00:37:46 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-16 17:37:47 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 10:46:12 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | - | mean | jsd | 21-01-16 00:57:19 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-16 18:21:17 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:46:33 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-15 23:38:51 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 18:15:30 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 17:44:13 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:46:39 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 14:54:13 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 17:50:17 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 18:53:02 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 18:12:06 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-15 17:35:04 | 0.2949 | 0.0667 | 0.2949 | 0.1362 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 17:50:56 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-16 03:21:25 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-15 22:00:47 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 17:51:34 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-16 17:57:28 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 16:40:27 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | - | 128 | - | mean | jsd | 21-01-15 12:50:55 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-16 19:02:05 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 17:33:08 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 16:39:52 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 256 | [256] | mean | jsd | 21-01-15 22:07:49 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-15 21:53:45 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 20 | 256 | [256, 256] | mean | jsd | 21-01-15 21:43:37 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:47:25 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.02 | 20 | 64 | - | mean | jsd | 21-01-16 17:49:04 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 512 | [512] | mean | jsd | 21-01-16 01:35:32 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 512 | - | mean | jsd | 21-01-15 22:10:55 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.01 | 20 | 256 | [256] | mean | jsd | 21-01-15 22:09:23 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 512 | [512] | mean | jsd | 21-01-15 21:59:03 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 16:54:44 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 512 | - | mean | jsd | 21-01-16 17:36:08 | 0.2949 | 0.0768 | 0.2949 | 0.1471 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-15 17:10:29 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-16 18:08:33 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-16 17:48:27 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-15 16:41:15 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 256 | - | mean | jsd | 21-01-16 17:55:24 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 256 | [256, 256] | mean | jsd | 21-01-16 18:49:54 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:47:01 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 09:52:44 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 17:33:27 | 0.2949 | 0.0651 | 0.2949 | 0.1344 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 22:16:14 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.001 | 20 | 256 | [256, 256, 256] | mean | jsd | 21-01-16 17:35:32 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:46:56 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:47:13 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 17:38:40 | 0.2949 | 0.0651 | 0.2949 | 0.1344 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:46:50 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-15 23:25:52 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 18:24:37 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | [256, 256] | mean | jsd | 21-01-15 21:55:32 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-16 17:49:41 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 256 | - | mean | jsd | 21-01-16 17:43:09 | 0.2949 | 0.0651 | 0.2949 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:12 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 21:46:06 | 0.2944 | 0.0978 | 0.2944 | 0.169 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:41 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:44:15 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:44:20 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:44:09 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 64 | [64, 64] | mean | jsd | 21-01-16 17:32:56 | 0.2944 | 0.0651 | 0.2944 | 0.1343 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 512 | [512, 512, 512] | mean | jsd | 21-01-15 21:46:38 | 0.2944 | 0.0978 | 0.2944 | 0.169 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:43:57 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:30 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:44:27 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | - | mean | jsd | 21-01-15 21:58:01 | 0.2944 | 0.0978 | 0.2944 | 0.169 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:43:51 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:44:39 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:02 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:21:28 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 21:59:54 | 0.2944 | 0.0978 | 0.2944 | 0.169 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:21:34 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:36 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:43:45 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:18 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:48 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-15 20:20:21 | 0.2944 | 0.0667 | 0.2944 | 0.1361 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64] | mean | jsd | 21-01-16 17:32:44 | 0.2944 | 0.0652 | 0.2944 | 0.1345 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:42:05 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:07 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:44:04 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:44:44 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.03 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-16 17:33:37 | 0.2944 | 0.0652 | 0.2944 | 0.1345 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 16:52:48 | 0.2944 | 0.0667 | 0.2944 | 0.1361 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:43:40 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:21:22 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:42:00 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:24 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:41:54 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 1 | 0.001 | 20 | 16 | - | mean | jsd | 21-01-15 20:44:33 | 0.2944 | 0.065 | 0.2944 | 0.1341 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-16 17:38:59 | 0.2912 | 0.0731 | 0.2912 | 0.1432 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 17:54:50 | 0.2907 | 0.0692 | 0.2907 | 0.1386 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.03 | 20 | 128 | - | mean | jsd | 21-01-16 17:52:57 | 0.2907 | 0.0692 | 0.2907 | 0.1386 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.03 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 18:39:19 | 0.2907 | 0.0692 | 0.2907 | 0.1386 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.01 | 20 | 128 | [128] | mean | jsd | 21-01-16 17:53:33 | 0.2903 | 0.0684 | 0.2903 | 0.1377 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.03 | 20 | 64 | - | mean | jsd | 21-01-15 21:39:18 | 0.2903 | 0.0824 | 0.2903 | 0.1537 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-random | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-15 23:20:42 | 0.2903 | 0.0684 | 0.2903 | 0.1376 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-16 00:45:25 | 0.2903 | 0.0684 | 0.2903 | 0.1376 | 
| ss_nodemodel | cora | none | bilinear | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 00:52:35 | 0.2903 | 0.0684 | 0.2903 | 0.1376 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-random | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-16 02:37:40 | 0.2903 | 0.0686 | 0.2903 | 0.1382 | 
| ss_nodemodel | cora | none | bilinear | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 09:58:52 | 0.2903 | 0.0686 | 0.2903 | 0.1382 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 18:35:25 | 0.2903 | 0.0684 | 0.2903 | 0.1377 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-15 21:48:32 | 0.2898 | 0.0676 | 0.2898 | 0.1366 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-15 21:50:17 | 0.2898 | 0.0676 | 0.2898 | 0.1366 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-15 21:41:11 | 0.2898 | 0.0676 | 0.2898 | 0.1366 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-random | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-16 17:52:17 | 0.2893 | 0.0669 | 0.2893 | 0.136 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 18:33:34 | 0.2893 | 0.0669 | 0.2893 | 0.136 | 
| ss_nodemodel | cora | none | mlp | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 128 | - | mean | jsd | 21-01-16 18:31:37 | 0.2893 | 0.0669 | 0.2893 | 0.136 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128, 128, 128] | mean | jsd | 21-01-16 17:42:22 | 0.2889 | 0.0714 | 0.2889 | 0.1411 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-random | 500 | 0.02 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 17:33:47 | 0.2889 | 0.0714 | 0.2889 | 0.1411 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.02 | 20 | 128 | [128] | mean | jsd | 21-01-16 17:40:37 | 0.2889 | 0.0714 | 0.2889 | 0.1411 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 128 | [128, 128] | mean | jsd | 21-01-16 17:41:22 | 0.2889 | 0.072 | 0.2889 | 0.1417 | 
| ss_nodemodel | cora | none | mlp | node-neighbor-except_neighbor | 500 | 0.001 | 20 | 128 | [128] | mean | jsd | 21-01-16 17:39:50 | 0.2884 | 0.0681 | 0.2884 | 0.1371 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512, 512] | mean | jsd | 21-01-15 21:45:33 | 0.288 | 0.0992 | 0.288 | 0.1694 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.02 | 20 | 512 | [512] | mean | jsd | 21-01-15 21:44:32 | 0.288 | 0.0992 | 0.288 | 0.1694 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64, 64] | mean | jsd | 21-01-15 21:40:57 | 0.2866 | 0.0814 | 0.2866 | 0.1522 | 
| ss_nodemodel | cora | none | inner | node-neighbor-except_neighbor | 500 | 0.01 | 20 | 64 | - | mean | jsd | 21-01-15 21:47:10 | 0.2866 | 0.0814 | 0.2866 | 0.1522 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64] | mean | jsd | 21-01-15 21:40:33 | 0.2866 | 0.0814 | 0.2866 | 0.1522 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 21:40:46 | 0.2866 | 0.0814 | 0.2866 | 0.1522 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 64 | [64, 64] | mean | jsd | 21-01-15 22:03:25 | 0.2787 | 0.0808 | 0.2787 | 0.1507 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-except_neighbor | 500 | 0.001 | 20 | 64 | [64] | mean | jsd | 21-01-15 22:21:34 | 0.2787 | 0.0808 | 0.2787 | 0.1507 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 500 | 0.001 | 20 | 64 | - | mean | jsd | 21-01-15 22:01:43 | 0.2787 | 0.0808 | 0.2787 | 0.1507 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 500 | 0.01 | 2000 | 128 | - | mean | jsd | 21-01-15 10:30:12 | 0.2252 | 0.1793 | 0.2252 | 0.2148 | 
| ss_nodemodel | cora | none | inner | node-rand_walk-random | 300 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-15 10:41:34 | 0.2118 | 0.1669 | 0.2118 | 0.2039 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-14 23:38:07 | 0.1947 | 0.1565 | 0.1947 | 0.1903 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-14 23:25:22 | 0.1947 | 0.1565 | 0.1947 | 0.1903 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 300 | - | - | 128 | - | mean | jsd | 21-01-14 23:36:57 | 0.1947 | 0.1565 | 0.1947 | 0.1903 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 300 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-15 10:10:51 | 0.1947 | 0.1565 | 0.1947 | 0.1903 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 300 | 0.01 | 2000 | 128 | - | mean | jsd | 21-01-15 10:29:27 | 0.1943 | 0.1509 | 0.1943 | 0.1868 | 
| ss_nodemodel | cora | none | inner | node-neighbor-random | 300 | 0.01 | 20 | 128 | - | mean | jsd | 21-01-15 10:27:47 | 0.1887 | 0.1442 | 0.1887 | 0.182 | 

