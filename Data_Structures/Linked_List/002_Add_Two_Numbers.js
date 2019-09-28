class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}


class LinkedList {
  constructor(){
    this.head = null;
    this.size = 0;
  }

  addNode(x){
    var node = new Node(x);
    var cur;

    if (this.head === null)
      this.head = node;
    else {
      cur = this.head;
      while(cur.next){
        cur = cur.next;
      }
      cur.next = node(x);
    }
    this.size++;
  }

  printNode(){
    let cur = this.head;
    while(cur !== null){
      console.log(cur.data);
      cur = cur.next;
    }
  }
}

ll = new LinkedList();
for (var i = 0; i < 5 ; i++){
  ll.addNode(i);
}
printNode();
