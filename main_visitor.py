from antlr4 import *
from gen.grammar.SailingCommandsLexer import SailingCommandsLexer
from gen.grammar.SailingCommandsParser import SailingCommandsParser
from gen.grammar.SailingCommandsVisitor import SailingCommandsVisitor


class CommandVisitor(SailingCommandsVisitor):
    def visitCommand(self, ctx):
        direction = ctx.direction().getText()
        amount = ctx.amount().getText()
        if amount == 'pół':
            amount = '40%'
        elif amount == 'cała':
            amount = '100%'
        return f"{amount} {direction}"


def main():
    try:
        with open("input.txt", 'r') as file:
            for line in file:
                input_stream = InputStream(line.strip())
                lexer = SailingCommandsLexer(input_stream)
                stream = CommonTokenStream(lexer)
                parser = SailingCommandsParser(stream)
                tree = parser.command()
                visitor = CommandVisitor()
                commands = visitor.visit(tree)
                print("Commands:", commands)
    except FileNotFoundError:
        return Exception


if __name__ == "__main__":
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
