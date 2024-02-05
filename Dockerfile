# Use the official Python image. This is not specific to AWS Lambda.
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt ./ 

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local directory files into the container at /app
COPY . .

# Expose the port Streamlit will run on (Streamlit applications default to running on port 8501)
EXPOSE 8501

# Run streamlit.py when the container launches
CMD ["streamlit", "run", "streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]