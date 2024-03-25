from antlr4 import *
from gen.grammar.SailingCommandsLexer import SailingCommandsLexer
from gen.grammar.SailingCommandsParser import SailingCommandsParser
from gen.grammar.SailingCommandsVisitor import SailingCommandsVisitor

group_cnt = 0
ingroup_cnt = 0

def get_amount(amount: str) -> str:
    match amount:
        case 'awaryjna':
            return '100%'
        case 'cała':
            return '80%'
        case 'manewrowa':
            return '60%'
        case 'pół':
            return '40%'
        case 'wolna':
            return '20%'
        case _:
            return '0%'


def get_stere(stere: str) -> str:
    match stere:
        case 'lewo':
            return '-45 stopni'
        case 'lewo na burt':
            return '-90 stopni'
        case 'prawo':
            return '45 stopni'
        case 'prawo na burt':
            return '90 stopni'
        case _:
            return '0 stopni'


class CommandVisitor(SailingCommandsVisitor):

    def visitSpeedCommand(self, ctx):
        global ingroup_cnt
        direction = ctx.direction().getText()
        amount = ctx.speed().getText()
        converted_amount = get_amount(amount)
        ingroup_cnt = ingroup_cnt+1
        return f"\t{ingroup_cnt}. - Silnik {converted_amount} {direction}"

    def visitStereCommand(self, ctx):
        global ingroup_cnt
        stere = ctx.stere().getText()
        converted_stere = get_stere(stere)
        ingroup_cnt = ingroup_cnt+1
        return f"\t{ingroup_cnt}. - Przekręć ster o {converted_stere}"

    def visitGroupCommand(self, ctx):
        global ingroup_cnt, group_cnt
        ingroup_cnt = 0
        group_cnt = group_cnt+1
        return f'\n{group_cnt}. - Nowy zestaw komend:'


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
                print(commands)
    except FileNotFoundError:
        return Exception


if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
