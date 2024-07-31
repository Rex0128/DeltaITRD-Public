import tkinter as tk

class Controller:
    def __init__(self):
        """
        Hint: Implement some codes here
        """

        self.last_operator = None
        self.memory = 0

class View:
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.root = tk.Tk()
        self.root.wm_title("Calculator")
        self.output_textvariable = tk.StringVar()
        self.output_text = tk.Entry(self.root, textvariable=self.output_textvariable, width = 50, justify='right')
        
        self.buttons = {}
        self.operators = {}

        for i in range(0,10):
            self.buttons.update({f"num_{i}":tk.Button(self.root, text=i, width = 10, command=lambda num=i:self.show_on_panel(num))})
        self.operators.update({f"num_AC": tk.Button(self.root, text='AC', width = 5, command=self.clear)})
        self.operators.update({f"num_+":tk.Button(self.root, text='+', width = 5, command=self.add)})
        self.operators.update({f"num_-":tk.Button(self.root, text='-', width = 5, command=self.subtract)})
        self.operators.update({f"num_*":tk.Button(self.root, text='*', width = 5, command=self.multiply)})
        self.operators.update({f"num_/":tk.Button(self.root, text='/', width = 5, command=self.divide)})
        self.operators.update({f"num_=":tk.Button(self.root, text='=', width = 5, command=self.equal)})

        self.output_text.pack()
        for key in self.buttons.keys():
            self.buttons[key].pack(side='left')
        for key in self.operators.keys():
            self.operators[key].pack()

    def add(self):
        """
        Hint: Implement some codes here
        """
        pass

    def subtract(self):
        pass

    def multiply(self):
        pass

    def divide(self):
        pass

    def equal(self):
        pass

    def clear(self):
        pass

    def show_on_panel(self, number:float):
        self.output_textvariable.set(self.output_textvariable.get()+str(number))

class Model:
    # You don't have to implement these methods
    def __init__(self, ctrl):
        self.ctrl = ctrl

    def add(self, input):
        print("Hi, I am Rex.")
        print("add")

    def subtract(self, input):
        print("subtract")

    def multiply(self, input):
        print("multiply")

    def divide(self, input):
        print("divide")

    def equal(self, num):
        print("equal")

if __name__ == '__main__':
    # Please create an instance of Controller and bind button event from View to methods in Model.
    """
    Hint: Implement some codes here
    """
    pass
