ALL Docker commands

#----------------------------------------

List images
 -> docker images
Delete images
 -> docker rmi <image name>
List Container
 -> docker ps
Stop Container
 -> docker stop <id>
Delete Container
 -> docker rm <id>


#------------------------------------------

Build Image
-> docker build -t <name> <dir>

Run Container
-> docker run -p <3000:3000> --name=<name> <image name>