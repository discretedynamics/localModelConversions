# Fill files in algorun_info folder and put your source code in src folder
FROM algorun/algorun

# Install any algorithm dependencies here
RUN apt-get update && apt-get install -y python3 

# [Don't change the next two lines] Add source files to the Docker image
ADD ./algorun_info /home/algorithm/web/algorun_info/
ADD ./src /home/algorithm/src/

# [Optional] Compile/build your source code
#

# [Optional] Sign your image
LABEL maintainer 'Matt Macauley <macaule@clemson.edu>'
