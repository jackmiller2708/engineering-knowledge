// Fuel, exploration 3 (starting point): exploration 2 finished.
// Errors are values, the machine runs on a fuel budget, output is collected.

use std::fmt;

#[derive(Debug, Clone, Copy, PartialEq)]
enum Op {
    Push(i64),  // put a number on the stack
    Add,        // pop b, pop a, push a + b
    Sub,        // pop b, pop a, push a - b
    Mul,        // pop b, pop a, push a * b
    Div,        // pop b, pop a, push a / b
    Dup,        // copy the top of the stack
    Swap,       // swap the top two
    Over,       // copy the second item to the top
    Pop,        // discard the top
    Print,      // pop the top and record it as output
    Jmp(usize), // continue at this instruction index
    Jz(usize),  // pop; if it was zero, continue at this index
    Halt,
}

#[derive(Debug, PartialEq)]
enum VmError {
    StackUnderflow { at: usize, op: Op },
    DivideByZero { at: usize },
    Overflow { at: usize },
    RanOffEnd { at: usize },
    OutOfFuel { steps: u64 },
}

impl fmt::Display for VmError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            VmError::StackUnderflow { at, op } => {
                write!(f, "stack underflow: {op:?} at instruction {at} needs more values")
            }
            VmError::DivideByZero { at } => write!(f, "division by zero at instruction {at}"),
            VmError::Overflow { at } => write!(f, "arithmetic overflow at instruction {at}"),
            VmError::RanOffEnd { at } => write!(f, "no instruction at index {at}"),
            VmError::OutOfFuel { steps } => write!(f, "out of fuel after {steps} steps"),
        }
    }
}

impl std::error::Error for VmError {}

struct Vm {
    program: Vec<Op>,
    stack: Vec<i64>,
    pc: usize, // program counter: index of the next instruction
    steps: u64,
    output: Vec<i64>,
}

impl Vm {
    fn new(program: Vec<Op>) -> Vm {
        Vm { program, stack: Vec::new(), pc: 0, steps: 0, output: Vec::new() }
    }

    fn pop(&mut self, at: usize) -> Result<i64, VmError> {
        self.stack
            .pop()
            .ok_or(VmError::StackUnderflow { at, op: self.program[at] })
    }

    /// Pop b, pop a, push f(a, b). `f` returns None when the result does not fit.
    fn arith(&mut self, at: usize, f: fn(i64, i64) -> Option<i64>) -> Result<(), VmError> {
        let b = self.pop(at)?;
        let a = self.pop(at)?;
        self.stack.push(f(a, b).ok_or(VmError::Overflow { at })?);
        Ok(())
    }

    /// Run until Halt, an error, or `fuel` steps.
    fn run(&mut self, fuel: u64) -> Result<(), VmError> {
        loop {
            if self.steps == fuel {
                return Err(VmError::OutOfFuel { steps: self.steps });
            }
            let at = self.pc;
            let op = *self.program.get(at).ok_or(VmError::RanOffEnd { at })?;
            self.steps += 1;
            self.pc += 1;
            match op {
                Op::Push(n) => self.stack.push(n),
                Op::Add => self.arith(at, i64::checked_add)?,
                Op::Sub => self.arith(at, i64::checked_sub)?,
                Op::Mul => self.arith(at, i64::checked_mul)?,
                Op::Div => {
                    let b = self.pop(at)?;
                    let a = self.pop(at)?;
                    if b == 0 {
                        return Err(VmError::DivideByZero { at });
                    }
                    self.stack.push(a.checked_div(b).ok_or(VmError::Overflow { at })?);
                }
                Op::Dup => {
                    let a = self.pop(at)?;
                    self.stack.push(a);
                    self.stack.push(a);
                }
                Op::Swap => {
                    let b = self.pop(at)?;
                    let a = self.pop(at)?;
                    self.stack.push(b);
                    self.stack.push(a);
                }
                Op::Over => {
                    let b = self.pop(at)?;
                    let a = self.pop(at)?;
                    self.stack.push(a);
                    self.stack.push(b);
                    self.stack.push(a);
                }
                Op::Pop => {
                    self.pop(at)?;
                }
                Op::Print => {
                    let n = self.pop(at)?;
                    self.output.push(n);
                }
                Op::Jmp(target) => self.pc = target,
                Op::Jz(target) => {
                    if self.pop(at)? == 0 {
                        self.pc = target;
                    }
                }
                Op::Halt => return Ok(()),
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

/// Print the Fibonacci numbers 0 1 1 2 3 5 ... until the next one no longer fits in an i64.
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

/// Programs that go wrong on purpose.
fn overflow() -> Vec<Op> {
    vec![Op::Push(i64::MAX), Op::Push(1), Op::Add, Op::Print, Op::Halt]
}
fn underflow() -> Vec<Op> {
    vec![Op::Push(1), Op::Add, Op::Halt]
}
fn divide_by_zero() -> Vec<Op> {
    vec![Op::Push(1), Op::Push(0), Op::Div, Op::Halt]
}
fn forever() -> Vec<Op> {
    vec![Op::Jmp(0)]
}
fn wild_jump() -> Vec<Op> {
    vec![Op::Jmp(99)]
}

const FUEL: u64 = 10_000;

fn report(name: &str, vm: &Vm, result: Result<(), VmError>) {
    println!("== {name} ==");
    for n in &vm.output {
        println!("{n}");
    }
    match result {
        Ok(()) => println!("ok after {} steps", vm.steps),
        Err(e) => println!("error: {e}"),
    }
}

fn main() {
    let programs: Vec<(&str, Vec<Op>)> = vec![
        ("arithmetic", arithmetic()),
        ("countdown", countdown()),
        ("stack-tricks", stack_tricks()),
        ("fib", fibonacci()),
        ("overflow", overflow()),
        ("underflow", underflow()),
        ("divide-by-zero", divide_by_zero()),
        ("forever", forever()),
        ("wild-jump", wild_jump()),
    ];

    // `cargo run -- countdown` runs the programs you name; with no arguments, all of them.
    let wanted: Vec<String> = std::env::args().skip(1).collect();
    for (name, program) in programs {
        if !wanted.is_empty() && !wanted.iter().any(|w| w == name) {
            continue;
        }
        let mut vm = Vm::new(program);
        let result = vm.run(FUEL);
        report(name, &vm, result);
    }

    // The same program under three different fuel budgets.
    if wanted.is_empty() {
        let program = countdown();
        for fuel in [10, 30, 100] {
            let mut vm = Vm::new(program.clone());
            let result = vm.run(fuel);
            report(&format!("countdown, fuel {fuel}"), &vm, result);
        }
    }
}
