FROM eyevinntechnology/ffmpeg-base:0.3.0

COPY streamgateway_aws/stream_gateway.py .
CMD ["python3", "./stream_gateway.py"]
