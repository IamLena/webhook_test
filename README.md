# webhook_test
repo for setting a github webhook

link to info and tutorial

https://docs.github.com/en/developers/webhooks-and-events/webhooks/about-webhooks

used ```gem install sinatra-contrib``` to solve require: cannot load such file -- sinatra (LoadError)

both server and ngrok should be launched

lalala - new line


docker build -t pyserver .
docker run -p 127.0.0.1:80:4567 pyserver
