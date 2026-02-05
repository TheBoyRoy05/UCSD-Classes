#!/bin/bash

# Check AWS credentials
if [[ -z "$AWS_ACCESS_KEY_ID" || -z "$AWS_SECRET_ACCESS_KEY" || -z "$AWS_SESSION_TOKEN" ]]; then
    echo "❌ Please export AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_SESSION_TOKEN first."
    exit 1
fi

KEY_PATH="~/DSC102_PA1_Key.pem"
SCHEDULER_PUBLIC_IP="35.93.224.163"
SCHEDULER_PRIVATE_IP="172.31.35.53"
WORKER_IPS=("35.88.190.13")

# ----- Scheduler Setup -----
echo "🔧 Setting up Scheduler ($SCHEDULER_PUBLIC_IP)..."

ssh -i "$KEY_PATH" ubuntu@"$SCHEDULER_PUBLIC_IP" <<EOF
export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
export AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN
aws s3 sync s3://dsc102-pa1-public . > /dev/null 2>&1
source dask_env/bin/activate > /dev/null 2>&1
nohup jupyter-notebook --port 8888 --no-browser > jupyter.log 2>&1 &
nohup dask scheduler --host 0.0.0.0 > scheduler.log 2>&1 &
EOF

# Port forward Jupyter (8888) and Dask dashboard (8787)
echo "🔌 Forwarding Jupyter and Dask dashboard..."
ssh -f -N -i "$KEY_PATH" -L 8888:localhost:8888 ubuntu@"$SCHEDULER_PUBLIC_IP" > /dev/null 2>&1
ssh -f -N -i "$KEY_PATH" -L 8787:localhost:8787 ubuntu@"$SCHEDULER_PUBLIC_IP" > /dev/null 2>&1

# ----- Worker Setup -----
for ip in "${WORKER_IPS[@]}"; do
    echo "⚙️ Setting up Worker ($ip)..."
    ssh -i "$KEY_PATH" ubuntu@"$ip" <<EOF
export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
export AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN
aws s3 sync s3://dsc102-pa1-public . > /dev/null 2>&1
source dask_env/bin/activate > /dev/null 2>&1
nohup dask worker tcp://$SCHEDULER_PRIVATE_IP:8786 --nworkers 4 > worker.log 2>&1 &
EOF
done

ssh -i "~/DSC102_PA1_Key.pem" ubuntu@$SCHEDULER_PUBLIC_IP "cat jupyter.log"
echo "✅ All set! Open http://localhost:8787 to see your Dask cluster."