FROM eyevinntechnology/ffmpeg-base:0.3.0

COPY streamgateway_aws/stream_gateway.py /root/stream_gateway.py
ENTRYPOINT ["/root/stream_gateway.py"]
CMD []
