FROM ubuntu:20.04

RUN bash /app/image_qa_tool/scripts/install.bash /app
ENTRYPOINT [ "/bin/bash", "/app/image_qa_tool/scripts/start.bash", "/app" ]