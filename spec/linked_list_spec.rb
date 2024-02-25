require "linked_list"

RSpec.describe LinkedList do
  describe ".initialize" do
    it "makes a new empty LinkedList" do
      eepy_list = LinkedList.new
      expect(eepy_list.length).to eq 0
    end
    it "raises error if provided init value" do
      expect{not_a_list = LinkedList.new([1, 2])}.to raise_error(ArgumentError)
    end
  end
  describe ".fromArray" do
    it "creates a prepopulated LinkedList of values" do
      poppied = LinkedList.fromArray [1, 2, 3]
      expect([poppied[0], poppied[1], poppied[2]]).to eq [1, 2, 3]
    end
  end

  describe "#to_s" do
    it "returns the right string rep of the LinkedList" do
      listarooni = LinkedList.fromArray [10, 20, "thirty", :forty, 50.0, 60]
      expect(listarooni.to_s).to eq("<LinkedList: H → 10 → 20 → thirty → forty → 50.0 → 60 → T>")
    end
  end
  describe "#to_a" do
    it "returns an equivalent array to the one we put in" do
      arr = [1, 2, 3, "Car4"]
      listy = LinkedList.fromArray(arr)
      expect(listy.to_a).to eq arr
    end
  end

  describe "#insert" do
  it "inserts a value into first index of empty list" do
      listangular = LinkedList.new
      listangular.insert(index: 0, value: 12)
      expect(listangular[0]).to eq 12
    end
    it "inserts a value between nodes" do
      listangularMkII = LinkedList.fromArray ["c", "t"]
      listangularMkII.insert(index: 1, value: "a")
      expect(listangularMkII.to_a).to eq ["c", "a", "t"]
    end
    it "inserts a value at end of list" do
      listangular3 = LinkedList.fromArray [3, 2, 1, 0, -1, "f", "u", "c"]
      listangular3 << "k"
      listangular3.insert(index: 9, value: " ")
      expect(listangular3[9]).to eq " "
    end
  end

  describe "#append" do
    it "adds to the back of empty list" do
      eepy_list_The_Second = LinkedList.new
      eepy_list_The_Second.append(0)
      expect(eepy_list_The_Second[0]).to eq 0
    end
    it "appends (adds to the back) some value to the LinkedList" do
      aprendí = LinkedList.fromArray ["h", "e"]
      aprendí << "l"
      aprendí << "p"
      aprendí << "!"
      expect(aprendí.to_a.join("")).to eq "help!"
    end
  end

  describe "#[]=" do
    it "assigns the value of node at index to a new value" do
      flight_checklist = LinkedList.fromArray [
        "exist",
        "have a flying license",
        "make sure engine is attached to aircraft",
        "make sure aircraft is still attached to aircraft",
        "fly",
      ]
      flight_checklist[4] = "attempt to " + flight_checklist[4]
      expect(flight_checklist[4]).to eq "attempt to fly"
    end
  end

  death_is_my_purpose = LinkedList.fromArray ["h", "e", "l", "p"]
  describe "#delete_at" do
    it "removes the node at first index of list" do
      death_is_my_purpose.delete_at(0)
      expect(death_is_my_purpose.to_a).to eq ["e", "l", "p"]
    end
    it "removes a node between 2 nodes" do
      death_is_my_purpose.delete_at(1)
      expect(death_is_my_purpose.to_a).to eq ["e", "p"]
    end
    it "removes the tail node of the list" do
      death_is_my_purpose.delete_at(1)
      expect(death_is_my_purpose.to_a).to eq ["e"]
    end
  end

  describe "#pop" do
    it "removes and returns the final node of list" do
      a = death_is_my_purpose.pop
      expect(a).to eq "e"
      expect(death_is_my_purpose.length).to eq 0
      expect(death_is_my_purpose.to_a).to eq []
    end
  end

  describe "#each" do
    it "calls a provided block with each value v in the list" do
      b = [:m, "b", 3, 1/3r]
      beach = LinkedList.fromArray(b)
      i = 0
      beach.each do |v|
        expect(v).to eq b[i]
        i += 1
      end
    end
  end

  describe "#each_with_index" do
    it "does the same thing as each except also passes a second argument i" do
      eeeray = ["eee", "eeee", "eeeee"]
      eee = LinkedList.fromArray eeeray
      eee.each_with_index {|e, i| expect(e).to eq(eeeray[i])}
    end
  end

  describe "#[]" do
    it "returns the value at index" do
      expect(LinkedList.fromArray([1, 2])[1]).to eq 2
    end
  end

  # get_node has been implicitly tested in like every single other test

  describe "#includes?" do
    it "sees if includes? or not" do
      expect(LinkedList.new.includes? 3).to be false
      expect(LinkedList.fromArray([1]).includes?(1)).to be true
    end
  end

  describe "#empty?" do
    it "list empty?" do
      expect(LinkedList.new.empty?).to be true
      expect(LinkedList.fromArray([1]).empty?).to be false
    end
  end
end
