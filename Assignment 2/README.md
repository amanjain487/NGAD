# Authenticator
- A sample Authentication service for learning Docker
- Authenticates using user's Google Account

# Setup
1. Open `Deploy Image` directory in terminal
2. Make sure Docker is installed.
3. Build image from dockerfile using the below command.
   
   sudo docker build -t deploy_image .
4. Start container from image created in above step

    ```docker run --name demo_image -p8000:9000 -d deploy_image 0.0.0.0:9000```
   1. If port 8000 is not available in host machine, use some other port and replace `p8000` with available port in above command.
