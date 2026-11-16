// Fuel, exploration 2 (starting point): exploration 1 plus `Over` and a Fibonacci program.
// A program is a list of instructions. The machine runs them one at a time.

#[derive(Debug, Clone, Copy, PartialEq)]
enum Op {
    Push(i64),  // put a number on the stack
    Add,        // pop b, pop a, push a + b
    Sub,        // pop b, pop a, push a - b
    Mul,        // pop b, pop a, push a * b
    Dup,        // copy the top of the stack
    Swap,       // swap the top two
    Over,       // copy the second item to the top
    Pop,        // discard the top
    Print,      // pop the top and print it
    Jmp(usize), // continue at this instruction index
    Jz(usize),  // pop; if it was zero, continue at this index
    Halt,
}

struct Vm {
    program: Vec<Op>,
    stack: Vec<i64>,
    pc: usize, // program counter: index of the next instruction
}

impl Vm {
    fn new(program: Vec<Op>) -> Vm {
        Vm { program, stack: Vec::new(), pc: 0 }
    }

    fn pop(&mut self) -> i64 {
        self.stack.pop().unwrap()
    }

    /// Run until a Halt instruction.
    fn run(&mut self, trace: bool) {
        loop {
            let op = self.program[self.pc];
            if trace {
                println!("  pc={:<2} {:<10} stack={:?}", self.pc, format!("{:?}", op), self.stack);
            }
            self.pc += 1;
            match op {
                Op::Push(n) => self.stack.push(n),
                Op::Add => {
                    let b = self.pop();
                    let a = self.pop();
                    self.stack.push(a + b);
                }
                Op::Sub => {
                    let b = self.pop();
                    let a = self.pop();
                    self.stack.push(a - b);
                }
                Op::Mul => {
                    let b = self.pop();
                    let a = self.pop();
                    self.stack.push(a * b);
                }
                Op::Dup => {
                    let a = self.pop();
                    self.stack.push(a);
                    self.stack.push(a);
                }
                Op::Swap => {
                    let b = self.pop();
                    let a = self.pop();
                    self.stack.push(b);
                    self.stack.push(a);
                }
                Op::Over => {
                    let b = self.pop();
                    let a = self.pop();
                    self.stack.push(a);
                    self.stack.push(b);
                    self.stack.push(a);
                }
                Op::Pop => {
                    self.pop();
                }
                Op::Print => println!("{}", self.pop()),
                Op::Jmp(target) => self.pc = target,
                Op::Jz(target) => {
                    if self.pop() == 0 {
                        self.pc = target;
                    }
                }
                Op::Halt => return,
            }
        }
    }
}

/// (2 + 4) * 7
fn arithmetic() -> Vec<Op> {
    vec![Op::Push(2), Op::Push(4), Op::Add, Op::Push(7), Op::Mul, Op::Print, Op::Halt]
}

/// Print 5 4 3 2 1.
fn countdown() -> Vec<Op> {
    vec![
        Op::Push(5), // 0
        Op::Dup,     // 1  <- loop start
        Op::Print,   // 2
        Op::Push(1), // 3
        Op::Sub,     // 4
        Op::Dup,     // 5
        Op::Jz(8),   // 6  leave the loop when the counter reaches 0
        Op::Jmp(1),  // 7
        Op::Halt,    // 8
    ]
}

/// Swap, Sub and Pop in one place: prints -7, then 1.
fn stack_tricks() -> Vec<Op> {
    vec![
        Op::Push(10),
        Op::Push(3),
        Op::Swap, // stack: 3 10
        Op::Sub,  // 3 - 10
        Op::Print,
        Op::Push(1),
        Op::Push(2),
        Op::Pop, // discard the 2
        Op::Print,
        Op::Halt,
    ]
}

/// Print the Fibonacci numbers 0 1 1 2 3 5 ... and never stop (on purpose).
fn fibonacci() -> Vec<Op> {
    vec![
        Op::Push(0), // 0  stack: a
        Op::Push(1), // 1  stack: a b
        Op::Over,    // 2  <- loop start: a b a
        Op::Print,   // 3  prints a; stack: a b
        Op::Swap,    // 4  b a
        Op::Over,    // 5  b a b
        Op::Add,     // 6  b (a+b)
        Op::Jmp(2),  // 7
    ]
}

fn main() {
    let programs: Vec<(&str, Vec<Op>)> = vec![
        ("arithmetic", arithmetic()),
        ("countdown", countdown()),
        ("stack-tricks", stack_tricks()),
        ("fib", fibonacci()),
    ];

    // `cargo run -- countdown` runs the programs you name.
    // With no arguments, it runs the ones in `by_default`.
    let by_default = ["arithmetic", "countdown", "stack-tricks"];
    let wanted: Vec<String> = std::env::args().skip(1).collect();
    for (name, program) in programs {
        let selected = if wanted.is_empty() {
            by_default.contains(&name)
        } else {
            wanted.iter().any(|w| w == name)
        };
        if !selected {
            continue;
        }
        println!("== {name} ==");
        Vm::new(program).run(false);
    }
}
