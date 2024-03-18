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
    input_str = "cała wstecz"  # Przykładowe polecenia do przetworzenia
    input_stream = InputStream(input_str)
    lexer = SailingCommandsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SailingCommandsParser(stream)
    tree = parser.command()
    visitor = CommandVisitor()
    commands = visitor.visit(tree)
    print("Commands:", commands)


if __name__ == "__main__":
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
