import torch
import mlflow

print(torch.cuda.is_available())
x = torch.rand(5, 3)
print(x)

mlflow.start_run()
mlflow.log_param("my", "param")
mlflow.log_metric("score", 100)
run = mlflow.active_run()
print("Active run_id: {}".format(run.info.run_id))
mlflow.end_run()