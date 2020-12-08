global instruction_index
instruction_index = 0

global accumulator
accumulator = 0

global end
end = False

instruction_stack = []


def parse(data: str) -> list:
    return [(instruction.split(" ")[0], int(instruction.split(" ")[1])) for instruction in data.splitlines()]


class NoopInstruction:
    def execute(self, arg: int):
        global instruction_index
        instruction_index += 1


class AccumulatorInstruction(NoopInstruction):
    def execute(self, arg: int):
        super(AccumulatorInstruction, self).execute(arg)
        global accumulator
        accumulator += arg


class JumpInstruction(NoopInstruction):
    def execute(self, arg: int):
        global instruction_index
        instruction_index += arg


class BreakInstruction(NoopInstruction):
    def execute(self, arg: int):
        global end
        end = True


def boot(instructions: list):
    while not end:
        instruction = instructions[instruction_index]
        bi = build_instruction(instruction[0])
        instruction_stack.append(instruction_index)
        bi.execute(instruction[1])


def build_instruction(name: str):
    if instruction_index in instruction_stack and len(instruction_stack) != 1:
        return BreakInstruction()
    elif name == 'nop':
        return NoopInstruction()
    elif name == 'acc':
        return AccumulatorInstruction()
    elif name == 'jmp':
        return JumpInstruction()
    else:
        raise Exception


if __name__ == '__main__':
    with open('input.txt') as data:
        instructions = parse(data.read())
        boot(instructions)
        print(accumulator)
