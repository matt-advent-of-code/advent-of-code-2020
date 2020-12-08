global instruction_index
instruction_index = 0

global accumulator
accumulator = 0

global end
end = False

instruction_stack = []


def parse(data: str) -> list:
    return [[instruction.split(" ")[0], int(instruction.split(" ")[1])] for instruction in data.splitlines()]


class Game:
    def __init__(self):
        self.accumulator = 0
        self.instruction_index = 0
        self.instruction_stack = []

    def boot(self, instructions: list):
        while self.instruction_index < len(instructions):
            instruction = instructions[self.instruction_index]
            bi = self.build_instruction(instruction[0])
            self.instruction_stack.append(self.instruction_index)
            bi.execute(instruction[1])

    class NoopInstruction:
        def __init__(self, game):
            self.game = game

        def execute(self, arg: int):
            self.game.instruction_index += 1

    class AccumulatorInstruction:
        def __init__(self, game):
            self.game = game

        def execute(self, arg: int):
            self.game.accumulator += arg
            self.game.instruction_index += 1

    class JumpInstruction(NoopInstruction):
        def __init__(self, game):
            self.game = game

        def execute(self, arg: int):
            self.game.instruction_index += arg

    def build_instruction(self, name: str):
        if self.instruction_index in self.instruction_stack:
            raise Exception
        elif name == 'nop':
            return Game.NoopInstruction(self)
        elif name == 'acc':
            return Game.AccumulatorInstruction(self)
        elif name == 'jmp':
            return Game.JumpInstruction(self)
        else:
            raise Exception


class AlteringGame(Game):
    def boot(self, instructions: list):
        while self.instruction_index < len(instructions):
            instruction = instructions[self.instruction_index]
            if instruction[0] == 'nop' or instruction[0] == 'jmp':
                new_game = Game()
                new_game.accumulator = self.accumulator
                new_game.instruction_index = self.instruction_index
                new_game.instruction_stack = self.instruction_stack.copy()
                if instruction[0] == 'nop':
                    instructions[self.instruction_index][0] = 'jmp'
                    old_instruction = 'nop'
                else:
                    instructions[self.instruction_index][0] = 'nop'
                    old_instruction = 'jmp'

                try:
                    new_game.boot(instructions)
                    print(new_game.accumulator)
                    exit()
                except Exception as e:
                    instructions[self.instruction_index][0] = old_instruction

            instruction = instructions[self.instruction_index]
            bi = self.build_instruction(instruction[0])
            self.instruction_stack.append(self.instruction_index)
            bi.execute(instruction[1])


if __name__ == '__main__':
    with open('input.txt') as data:
        instructions = parse(data.read())
        game = AlteringGame()
        try:
            game.boot(instructions)
        except Exception as e:
            print(game.accumulator)
            raise e
