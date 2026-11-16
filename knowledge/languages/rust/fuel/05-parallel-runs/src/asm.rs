// The assembler: text -> Vec<Op>.
//
//     # comments start with a hash
//     push 5
//     loop:           <- a label names the next instruction
//       dup
//       jz done       <- jump operands are labels or plain numbers
//       jmp loop
//     done:
//       halt

use crate::Op;
use std::collections::HashMap;
use std::fmt;

#[derive(Debug, PartialEq)]
pub enum AsmErrorKind {
    UnknownInstruction(String),
    MissingOperand,
    UnexpectedOperand(String),
    BadNumber(String),
    UnknownLabel(String),
    DuplicateLabel(String),
}

/// An error plus the (1-based) line it happened on.
/// It owns its text (`String`), so it can outlive the source it came from.
#[derive(Debug, PartialEq)]
pub struct AsmError {
    pub line: usize,
    pub kind: AsmErrorKind,
}

impl fmt::Display for AsmError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "line {}: ", self.line)?;
        match &self.kind {
            AsmErrorKind::UnknownInstruction(s) => write!(f, "unknown instruction `{s}`"),
            AsmErrorKind::MissingOperand => write!(f, "missing operand"),
            AsmErrorKind::UnexpectedOperand(s) => write!(f, "unexpected operand `{s}`"),
            AsmErrorKind::BadNumber(s) => write!(f, "`{s}` is not a number"),
            AsmErrorKind::UnknownLabel(s) => write!(f, "unknown label `{s}`"),
            AsmErrorKind::DuplicateLabel(s) => write!(f, "label `{s}` is defined twice"),
        }
    }
}

impl std::error::Error for AsmError {}

pub fn assemble(source: &str) -> Result<Vec<Op>, AsmError> {
    // Pass 1: find labels and collect instruction lines.
    // Both borrow from `source`; nothing is copied.
    let mut labels: HashMap<&str, usize> = HashMap::new();
    let mut lines: Vec<(usize, &str)> = Vec::new();
    for (i, raw) in source.lines().enumerate() {
        let line_no = i + 1;
        let text = raw.split('#').next().unwrap_or("").trim();
        if text.is_empty() {
            continue;
        }
        if let Some(name) = text.strip_suffix(':') {
            let name = name.trim();
            if labels.insert(name, lines.len()).is_some() {
                let kind = AsmErrorKind::DuplicateLabel(name.to_string());
                return Err(AsmError { line: line_no, kind });
            }
        } else {
            lines.push((line_no, text));
        }
    }

    // Pass 2: turn each line into an instruction.
    lines
        .into_iter()
        .map(|(line, text)| parse_line(text, &labels).map_err(|kind| AsmError { line, kind }))
        .collect() // Vec<Result<Op, _>> becomes Result<Vec<Op>, _>: the first error wins
}

fn parse_line(text: &str, labels: &HashMap<&str, usize>) -> Result<Op, AsmErrorKind> {
    use AsmErrorKind::*;

    let mut parts = text.split_whitespace();
    let mnemonic = parts.next().unwrap_or("");
    let operand = parts.next();
    if let Some(extra) = parts.next() {
        return Err(UnexpectedOperand(extra.to_string()));
    }

    let plain = |op: Op| match operand {
        None => Ok(op),
        Some(x) => Err(UnexpectedOperand(x.to_string())),
    };
    let target = || -> Result<usize, AsmErrorKind> {
        let x = operand.ok_or(MissingOperand)?;
        match x.parse::<usize>() {
            Ok(n) => Ok(n),
            Err(_) => labels.get(x).copied().ok_or_else(|| UnknownLabel(x.to_string())),
        }
    };

    match mnemonic {
        "push" => {
            let x = operand.ok_or(MissingOperand)?;
            Ok(Op::Push(x.parse().map_err(|_| BadNumber(x.to_string()))?))
        }
        "jmp" => Ok(Op::Jmp(target()?)),
        "jz" => Ok(Op::Jz(target()?)),
        "add" => plain(Op::Add),
        "sub" => plain(Op::Sub),
        "mul" => plain(Op::Mul),
        "div" => plain(Op::Div),
        "dup" => plain(Op::Dup),
        "swap" => plain(Op::Swap),
        "over" => plain(Op::Over),
        "pop" => plain(Op::Pop),
        "print" => plain(Op::Print),
        "halt" => plain(Op::Halt),
        other => Err(UnknownInstruction(other.to_string())),
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use AsmErrorKind::*;

    const COUNTDOWN: &str = "
        push 3
        loop:             # the loop starts here
          dup
          print
          push 1
          sub
          dup
          jz done
          jmp loop
        done:
          halt
    ";

    fn err(source: &str) -> AsmError {
        assemble(source).unwrap_err()
    }

    #[test]
    fn labels_become_instruction_indexes() {
        let program = assemble(COUNTDOWN).unwrap();
        assert_eq!(program[0], Op::Push(3));
        assert_eq!(program[6], Op::Jz(8));
        assert_eq!(program[7], Op::Jmp(1));
        assert_eq!(program.len(), 9);
    }

    #[test]
    fn numbers_work_as_jump_targets_too() {
        assert_eq!(assemble("jmp 7").unwrap(), vec![Op::Jmp(7)]);
    }

    #[test]
    fn errors_carry_the_line_number() {
        assert_eq!(err("push 1\n\nfrobnicate"), AsmError { line: 3, kind: UnknownInstruction("frobnicate".into()) });
        assert_eq!(err("push x"), AsmError { line: 1, kind: BadNumber("x".into()) });
        assert_eq!(err("push"), AsmError { line: 1, kind: MissingOperand });
        assert_eq!(err("add 1"), AsmError { line: 1, kind: UnexpectedOperand("1".into()) });
        assert_eq!(err("jmp nowhere"), AsmError { line: 1, kind: UnknownLabel("nowhere".into()) });
        assert_eq!(err("a:\na:"), AsmError { line: 2, kind: DuplicateLabel("a".into()) });
    }

    #[test]
    fn listing_then_assembling_gives_the_same_program() {
        let program = assemble(COUNTDOWN).unwrap();
        let listing: Vec<String> = program.iter().map(|op| op.to_string()).collect();
        assert_eq!(assemble(&listing.join("\n")).unwrap(), program);
    }
}
