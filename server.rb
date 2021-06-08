require 'json'
require 'sinatra'

post '/payload' do
  push = JSON.parse(request.body.read)
  puts "\n\n #{push} \n\n"
  # from = push.pull_request.head.ref
  # to = push.pull_request.ref
  # puts "I got some JSON: #{push.inspect}"
  # puts "from #{from} to #{to}"
end
