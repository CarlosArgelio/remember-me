# Base image for Ubuntu
FROM ubuntu:22.04

# Update package lists
RUN apt-get update && apt-get upgrade -y

# Install prerequisites for building Python from source
RUN apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev

# Download and install Python 3.10
RUN wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz && \
    tar -xvf Python-3.10.8.tgz && \
    cd Python-3.10.8 && \
    ./configure --enable-optimizations && \
    make -j $(nproc) && \
    make altinstall

# Set Python 3.10 as default
ENV PATH="/usr/local/bin:$PATH"

# Install Node version 20 with NVM (Node Version Manager)
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash

# Set up nvm for current user
RUN echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.bashrc
RUN echo '[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm' >> ~/.bashrc

# Install Node version 20 and Npm version 10
RUN source ~/.bashrc && nvm install 20
RUN nvm alias default 20

# Clean up
RUN apt-get autoremove -y && apt-get clean -y

# Set working directory
WORKDIR /app

CMD [ "bash" ]
