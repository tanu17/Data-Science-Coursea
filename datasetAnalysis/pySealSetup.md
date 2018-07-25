For ubuntu/linux-

the library is shared on github: https://github.com/Lab41/PySEAL:
1) sudo apt-get install docker.io               
2) git clone https://github.com/Lab41/PySEAL.git            
Under the downloaded folder
3) sudo sh build-docker.sh
4) sudo sh run-docker.sh

The new pySeal has error so changes should b =e made in line 185 of wrapper.cpp and remove " ; ". Additional error is in run-docker.sh, the code should be changed from "seal-io" to "seal-save"
