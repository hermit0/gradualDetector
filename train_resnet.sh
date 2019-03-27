log_dir=results_resnet_v2

#从头开始训练模型或者从最近的检查点恢复训练
nohup python -u  main.py \
--root_dir ~/gradualDetector/data \
--train_list_path train_samples_c3 \
--result_path $log_dir \
--pretrain_path pretrain_models/cut_model_epoch6.pth \
--sample_size 112 \
--sample_duration 21 \
--batch_size 32 \
--n_epochs 50 \
--auto_resume \
--train_subdir train \
--model resnet_talnn \
--model_depth 50 \
--n_threads 20 \
--learning_rate 0.001 \
--weight_decay 1e-5 \
--lr_step 3 \
--checkpoint 1 2>error.log |tee  data/$log_dir/screen.log & 
