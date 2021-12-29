# Create Chatbot using Rasa 🤖

## Install Rasa:
```
conda install python=3.6
conda create -n rasa python=3.6
source activate rasa
```



## Create a new Project in Rasa:
Open Terminal and activate Conda Virtual Environment. Now go-to one directory and do “rasa init”, it will create a Rasa Project at that location.

> source activate rasa
> rasa init


## Play with Sample Chatbot:
Rasa created a sample Bot for you with default data. So now you can start using it from Shell/Terminal. As a starting point let’s test your Chatbot from a terminal (remember to do this in Terminal)

>  rasa shell


##Training Model:
>  rasa train


A Chat widget easy to connect to RASA bot through [Rest]

## Instructions
*Before you start your bot server, make sure you have added `rest` channel in the `credentials.yml` file*

**Step_1**: Start your Rasa bot server & action server(if you have custom actions) using the below command
> rasa run -m models --enable-api --cors "*" --debug

> rasa run actions 
