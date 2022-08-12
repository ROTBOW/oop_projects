'''
example queries = [
    ["APPEND", "Hey"],               //| "" -> "Hey"
    ["APPEND", " there"],            //| "Hey" -> "Hey there"
    ["APPEND", "!"]                  //| "Hey there" -> "Hey there!"
]
// returns: [ "Hey",
//            "Hey there",
//            "Hey there!" ]

let queries2 = [
    ["APPEND", "Hey you"],           //| "" -> "Hey you"
    ["MOVE", "3"],                   //| moves the cursor after the first "y"
    ["APPEND", ","]                  //| "Hey you" -> "Hey, you"
]

// returns: [ "Hey you",
//            "Hey you",
//            "Hey, you" ]

let queries3 = [
    ["APPEND", "Hello! world!"],      //| "" -> "Hello! world!"
    ["MOVE", "5"],                   //| moves the cursor before the first "!"
    ["DELETE"],                      //| "Hello! world!" -> "Hello world!"
    ["APPEND", ","]                  //| "Hello world!" -> "Hello, world!"
]
'''

class LinkedList:
    def __init__(self, val=0, next=None, back=None) -> None:
        self.val = val
        self.next = next
        self.back = back

    @classmethod
    def copy(self, root):
        dummy = LinkedList()
        curr = dummy
        while root:
            curr.next = LinkedList(root.val, None, curr)
            curr = curr.next
            root = root.next

        return dummy.next

    @classmethod
    def to_str(self, root):
        res = ''
        while root:
            res += root.val
            root = root.next
        return res


class TextEditor:

    def __init__(self) -> None:
        self.head = LinkedList()
        self.cursor = self.head
        self.selection = [None, None]
        self.copy_text = ''
        self.undo_stack = []
        self.redo_stack = []
        self.actions = {
            'APPEND': self.append,
            'MOVE': self.move,
            'UNDO': self.undo,
            'REDO': self.redo,
            'SELECT': self.select,
            'COPY': self.copy,
            'PASTE': self.paste,
            'DELETE': self.backspace
        }
        

    def __str__(self) -> str:
        return LinkedList.to_str(self.head.next)

    def __save_state(self, undo=True) -> tuple:
        if undo:
            self.undo_stack.append(LinkedList.copy(self.head.next))
        else:
            self.redo_stack.append(LinkedList.copy(self.head.next))

    def __get_tail(self):
        curr = self.head.next
        while curr.next: curr = curr.next
        return curr

    def undo(self) -> None:
        new_state = self.undo_stack.pop()
        self.__save_state(False)
        # self.redo_stack.append(new_state)
        self.head.next = new_state
        self.cursor = self.__get_tail()

    def redo(self) -> None:
        self.__save_state()
        new_state = self.redo_stack.pop()
        self.head.next = new_state
        self.cursor = self.__get_tail()

    def select(self, start: int, end: int) -> None:
        curr = self.head.next
        for i in range(end):
            if i == start: self.selection[0] = curr
            curr = curr.next
        self.selection[1] = curr

    def append(self, text: str) -> None:
        self.__save_state()
        if self.selection != [None, None]:
            self.backspace()
        after = self.cursor.next
        for char in text:
            self.cursor.next = LinkedList(char, None, self.cursor)
            self.cursor = self.cursor.next
        self.cursor.next = after
        

    def move(self, idx) -> None:
        curr = self.head.next
        for _ in range(idx-1): curr = curr.next
        self.cursor = curr

    def backspace(self, null=None) -> None:
        self.__save_state()
        if self.selection == [None, None]:
            temp = self.cursor.back
            self.cursor.back.next = self.cursor.next
            self.cursor = temp
            self.cursor.next.back = self.cursor
        else:
          self.selection[0].back.next = self.selection[1].next
          self.selection[1].back = self.selection[0].back
          self.cursor = self.selection[0].back
          self.selection = [None, None]

    def copy(self) -> None:
        curr = self.selection[0]
        while curr != self.selection[1]:
            self.copy_text += str(curr.val)
            curr = curr.next
        self.selection = [None, None]

    def paste(self) -> None:
        self.__save_state()
        self.append(self.copy_text)


    def output_answer(self, queries):
        res = []
        for command in queries:
            if len(command) > 1:
                self.actions[command[0]](*command[1:])
            else:
                self.actions[command[0]]()
            res.append(LinkedList.to_str(self.head.next))
        return res



text = TextEditor()
queries = [
    ['APPEND', 'Hello, world!'],
    ['MOVE', 6],
    ['DELETE'],
    ['APPEND', 'CAT'],
    ['SELECT', 5, 8],
    ['DELETE'],
    ['APPEND', ' ']
]
print(text.output_answer(queries))