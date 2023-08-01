#!/usr/bin/env ruby
line = 0
sender = ARGV[line].scan(/from:(\S+)\]/).flatten.first
receiver = ARGV[line].scan(/to:(\S+)\]/).flatten.first
flags = ARGV[line].scan(/flags:(\S+)\]/).flatten.first
puts "#{sender},#{receiver},#{flags}"
