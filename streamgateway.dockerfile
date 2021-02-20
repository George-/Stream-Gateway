FROM eyevinntechnology/ffmpeg-base:0.3.0

COPY stream_gateway/stream_gateway.py /root/stream_gateway.py
ENTRYPOINT ["/root/stream_gateway.py"]
CMD []
