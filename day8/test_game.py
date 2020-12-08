import unittest

from day8 import game
from day8.game import NoopInstruction, AccumulatorInstruction, JumpInstruction, BreakInstruction


class MyTestCase(unittest.TestCase):
    def test_no_op_instruction(self):
        game.accumulator = 0
        game.instruction_index = 0
        instruction = NoopInstruction()
        instruction.execute(0)
        self.assertEqual(0, game.accumulator)
        self.assertEqual(1, game.instruction_index)

    def test_accumulator_instruction(self):
        game.accumulator = 0
        game.instruction_index = 0
        instruction = AccumulatorInstruction()
        instruction.execute(1)
        self.assertEqual(1, game.accumulator)
        self.assertEqual(1, game.instruction_index)

    def test_jump_instruction(self):
        game.accumulator = 0
        game.instruction_index = 0
        instruction = JumpInstruction()
        instruction.execute(4)
        self.assertEqual(0, game.accumulator)
        self.assertEqual(4, game.instruction_index)

    def test_break_instruction(self):
        game.accumulator = 0
        game.instruction_index = 0
        instruction = BreakInstruction()
        instruction.execute(0)
        self.assertTrue(game.end)


    def test_parse(self):
        instructions = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
        expected_parsed_instructions = [('nop', 0),
                                        ('acc', 1),
                                        ('jmp', 4),
                                        ('acc', 3),
                                        ('jmp', -3),
                                        ('acc', -99),
                                        ('acc', 1),
                                        ('jmp', -4),
                                        ('acc', 6)]
        parsed_instructions = game.parse(instructions)
        self.assertEqual(expected_parsed_instructions, parsed_instructions)

    def test_boot(self):
        instructions = [('nop', 0),
                                        ('acc', 1),
                                        ('jmp', 4),
                                        ('acc', 3),
                                        ('jmp', -3),
                                        ('acc', -99),
                                        ('acc', 1),
                                        ('jmp', -4),
                                        ('acc', 6)]
        game.boot(instructions)
        self.assertEqual(5, game.accumulator)


if __name__ == '__main__':
    unittest.main()
