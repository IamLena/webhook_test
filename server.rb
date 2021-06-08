require 'json'
require 'sinatra'

post '/payload' do
  push = JSON.parse(request.body.read)
  from = push.inspect.head.ref
  to = push.inspect.ref
  # puts "I got some JSON: #{push.inspect}"
  puts "from #{from} to #{to}"
end
