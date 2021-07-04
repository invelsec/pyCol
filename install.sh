echo "pyCol Installing!"
if [["$OSTYPE" == "linux-gnu"* ]];then
    echo "OS -> Linux"
    sudo apt-get update && sudo apt-get upgrade -y
    sudo apt-get install python3
    sudo apt-get install python3-pip
    echo "Install Complete!"
    echo "Usage -> use -p parameter for listen requests on selected port (python3 col.py -p 8080)"
elif [["$OSTYPE" == "Darwin"* ]];then
    echo "OS -> Mac OS X Not supported!"
    exit
fi
