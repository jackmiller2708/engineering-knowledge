// Fuel, exploration 5: exploration 4 finished, plus running many programs on threads.
// Programs are text files, assembled into instructions. See asm.rs.

use std::fmt;

mod asm;

use std::thread;

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

impl fmt::Display for Op {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            Op::Push(n) => write!(f, "push {n}"),
            Op::Add => write!(f, "add"),
            Op::Sub => write!(f, "sub"),
            Op::Mul => write!(f, "mul"),
            Op::Div => write!(f, "div"),
            Op::Dup => write!(f, "dup"),
            Op::Swap => write!(f, "swap"),
            Op::Over => write!(f, "over"),
            Op::Pop => write!(f, "pop"),
            Op::Print => write!(f, "print"),
            Op::Jmp(t) => write!(f, "jmp {t}"),
            Op::Jz(t) => write!(f, "jz {t}"),
            Op::Halt => write!(f, "halt"),
        }
    }
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

struct Vm<'p> {
    program: &'p [Op],
    stack: Vec<i64>,
    pc: usize, // program counter: index of the next instruction
    steps: u64,
    output: Vec<i64>,
}

impl<'p> Vm<'p> {
    fn new(program: &'p [Op]) -> Vm<'p> {
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

const DEFAULT_FUEL: u64 = 10_000;

/// Everything one run produced. It owns its data, so it can be sent between threads.
struct Report {
    name: String,
    output: Vec<i64>,
    steps: u64,
    result: Result<(), VmError>,
}

impl Report {
    fn print(&self) {
        println!("== {} ==", self.name);
        for n in &self.output {
            println!("{n}");
        }
        match &self.result {
            Ok(()) => println!("ok after {} steps", self.steps),
            Err(e) => println!("error: {e}"),
        }
    }
}

fn run_job(name: &str, program: &[Op], fuel: u64) -> Report {
    let mut vm = Vm::new(program);
    let result = vm.run(fuel);
    Report { name: name.to_string(), output: vm.output, steps: vm.steps, result }
}

/// Run every job on its own thread. Reports come back in the order of `jobs`.
fn run_parallel(jobs: &[(String, Vec<Op>)], fuel: u64) -> Vec<Report> {
    thread::scope(|scope| {
        let handles: Vec<_> = jobs
            .iter()
            .map(|(name, program)| scope.spawn(move || run_job(name, program, fuel)))
            .collect();
        handles.into_iter().map(|h| h.join().unwrap()).collect()
    })
}

fn run_sequential(jobs: &[(String, Vec<Op>)], fuel: u64) -> Vec<Report> {
    jobs.iter().map(|(name, program)| run_job(name, program, fuel)).collect()
}

fn load(path: &str) -> Result<Vec<Op>, Box<dyn std::error::Error>> {
    Ok(asm::assemble(&std::fs::read_to_string(path)?)?)
}

fn main() {
    // cargo run -- [list|par|seq] [--fuel=N] <file.fuel>...
    let mut args: Vec<String> = std::env::args().skip(1).collect();
    let mode = match args.first().map(|a| a.as_str()) {
        Some(m @ ("list" | "par" | "seq")) => {
            let m = m.to_string();
            args.remove(0);
            m
        }
        _ => "seq".to_string(),
    };
    let mut fuel = DEFAULT_FUEL;
    args.retain(|a| match a.strip_prefix("--fuel=") {
        Some(n) => {
            fuel = n.parse().expect("--fuel needs a number");
            false
        }
        None => true,
    });
    if args.is_empty() {
        eprintln!("usage: cargo run -- [list|par|seq] [--fuel=N] <file.fuel>...   (examples are in programs/)");
        std::process::exit(2);
    }

    let mut jobs = Vec::new();
    for path in &args {
        match load(path) {
            Ok(program) => jobs.push((path.clone(), program)),
            Err(e) => println!("== {path} ==\nerror: {e}"),
        }
    }

    if mode == "list" {
        for (name, program) in &jobs {
            println!("== {name} ==");
            for (i, op) in program.iter().enumerate() {
                println!("{i:>3}  {op}");
            }
        }
        return;
    }

    let start = std::time::Instant::now();
    let reports = if mode == "par" { run_parallel(&jobs, fuel) } else { run_sequential(&jobs, fuel) };
    let elapsed = start.elapsed();
    for report in &reports {
        report.print();
    }
    let total: u64 = reports.iter().map(|r| r.steps).sum();
    eprintln!("{} jobs, {} steps, {:.2?} ({mode})", reports.len(), total, elapsed);
}

#[cfg(test)]
mod tests {
    use super::*;

    fn run(program: &[Op], fuel: u64) -> (Vec<i64>, Result<(), VmError>) {
        let mut vm = Vm::new(program);
        let result = vm.run(fuel);
        (vm.output, result)
    }

    #[test]
    fn arithmetic_prints_42() {
        let program = [Op::Push(2), Op::Push(4), Op::Add, Op::Push(7), Op::Mul, Op::Print, Op::Halt];
        assert_eq!(run(&program, 100), (vec![42], Ok(())));
    }

    #[test]
    fn the_same_program_gives_the_same_result_every_time() {
        let program = [Op::Push(3), Op::Dup, Op::Print, Op::Push(1), Op::Sub, Op::Dup, Op::Jz(8), Op::Jmp(1), Op::Halt];
        assert_eq!(run(&program, 1_000), run(&program, 1_000));
    }

    #[test]
    fn running_out_of_fuel_is_exact() {
        let result = run(&[Op::Jmp(0)], 1_000).1;
        assert_eq!(result, Err(VmError::OutOfFuel { steps: 1_000 }));
    }

    #[test]
    fn overflow_is_an_error_not_a_wrap() {
        let program = [Op::Push(i64::MAX), Op::Push(1), Op::Add, Op::Halt];
        assert_eq!(run(&program, 100).1, Err(VmError::Overflow { at: 2 }));
    }

    #[test]
    fn underflow_names_the_instruction() {
        let result = run(&[Op::Push(1), Op::Add], 100).1;
        assert_eq!(result, Err(VmError::StackUnderflow { at: 1, op: Op::Add }));
    }
}
