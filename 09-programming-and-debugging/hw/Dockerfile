# Define python version 
FROM python:3.6.7

# Set the working directory to /hw
WORKDIR /hw

# Copy the current directory contents into the container /hw
ADD . /hw

# Write in /var/flag file variable
RUN echo "bytes=b'\x10\x23\x44\x61\89'" > /var/flag

# Make port 80 avaible to the world outside for check5
EXPOSE 80

# Run hw.py when the container launches
CMD ["python3", "./hw.py"]
