```bash
cd /opt/intel/openvino/deployment_tools/open_model_zoo/tools/downloader
sudo ./downloader.py --name human-pose-estimation-0001 -o /home/workspace
sudo ./downloader.py --name text-detection-0004 --precisions FP16 -o /home/workspace
sudo ./downloader.py --name vehicle-attributes-recognition-barrier-0039 --precisions INT8 -o /home/workspace

```