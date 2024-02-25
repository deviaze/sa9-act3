# linked_list.rb
#   by dev chrysalis!
# The COMP 2150 assignment was to modify Top's LinkedList implementation
# I have rewritten the whole LinkedList from scratch
# but it's not a 1:1 port of the old assignment's LinkedList, it's just making a new LinkedList
# and this one has tail for O(1) append operation

require_relative 'node'

# linked list implementation (with tail).
class LinkedList
  attr_reader :length

  ### Constructors

  def initialize(v = nil)
    # returns empty LinkedList, custom exception if v not nil
    @length = 0
    @head = nil
    @tail = nil

    if v then
      raise ArgumentError.new("Attempt to pass value to LinkedList.new\nUse LinkedList.fromArray to create prepopulated LinkedList.")
    end
  end

  def self.fromArray(arr)
    # prefer explicit constructor for prepopulated LinkedList
    new = self.new()
    arr.each() {|v| new << v}
    return new
  end

  ### Conversions

  def to_s
    vals = ""
    self.each{|v| vals << " #{v} →"}
    return "<LinkedList: H →#{vals} T>"
  end

  def to_a
    arr = []
    self.each do |v|
      arr << v
    end
    return arr
  end

  ### Insertions

  def insert(index: @length, value: nil)
    new_node = Node.new(value)
    if index == 0
      new_node.next = @head # this works even if @head == nil
      @head = new_node
    else
      prev = self.get_node(index - 1)
      succ = prev.next
      prev.next = new_node
      new_node.next = succ
      if index == @length
        @tail = new_node
      end
    end
    @length += 1
    return value
  end

  def append(val)
    new_node = Node.new(val)
    if @tail
      @tail.next = new_node
      @tail = new_node
    else
      # list empty
      @head = new_node
      @tail = new_node
    end
    @length += 1
    return val
  end
  def <<(val)
    return self.append(val)
  end

  # reassign val at index
  def []=(index, val)
    node = self.get_node(index)
    node.val = val
    return val
  end

  ### Deletions

  def delete_at(index)
    self._assertindex!(index)
    removed_val = self[index]
    case index
    when 0
      if @length > 1
        @head = @head.next
      else
        @head = nil
      end
    when @length - 1
      prev = self.get_node(index - 1)
      prev.next = nil
      @tail = prev
    else
      prev = self.get_node(index - 1)
      succ = self.get_node(index).next
      prev.next = succ
    end
    @length -= 1
    return removed_val
  end

  def pop
    return self.delete_at(@length - 1)
  end

  ### Iteration

  def each(&block)
    @length.times do |i|
      block.call(self[i])
    end
  end

  def each_with_index(&block)
    @length.times do |i|
      block.call(self[i], i)
    end
  end

  ### Index

  def [](index = @length - 1)
    node = self.get_node(index)
    return node.val
  end

  def get_node(target_index = nil)
    self._assertindex!(target_index)

    current_index = 0
    current_node = @head

    until current_index == @length
      return current_node if current_index == target_index
      current_index += 1
      current_node = current_node.next
    end

    return current_node
  end

  ## Queries

  def includes?(target)
    self.each {|val| return true if val == target}
    return false
  end

  def empty?
    return true if @length == 0
    return false
  end

  private

  def _assertindex!(target, between:0..@length)
    if target and !target.between?(between.begin, between.end)
      raise IndexError.new("LinkedList index out-of-bounds.\n    Attempt to index LinkedList[#{@length}] with [#{target}]")
    end
  end

end
