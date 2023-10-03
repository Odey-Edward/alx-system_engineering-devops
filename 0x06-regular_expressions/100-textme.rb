#!/usr/bin/env ruby
puts ARGV[0].scan(/from:(?=([a-zA-Z0-9+]+))/).join + "," + 
ARGV[0].scan(/to:(?=([a-zA-Z0-9+]+))/).join + "," + 
ARGV[0].scan(/flags:(?=([a-zA-Z0-9+:-]+))/).join
