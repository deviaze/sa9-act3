# node.rb
#   by dev chrysalis!
# helper class for linked_list and derivatives
# wanted to keep the node outside main file for readibility

class Node
  attr_accessor :next
  def initialize(val = nil, dict: {}, name: nil, next_node: nil)
    @next = next_node
    @name = name
    @val = val
    @dict = dict
  end

  def val
    return @dict if @dict.length > 0
    return @val
  end

  def val=(v)
    @val = v if @dict.length == 0
  end

  def to_s
    "<Node #{@name}: #{@val.to_s}>"
  end
end
