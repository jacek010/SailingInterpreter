from antlr4 import *
from gen.grammar.SailingCommandsLexer import SailingCommandsLexer
from gen.grammar.SailingCommandsParser import SailingCommandsParser
from gen.grammar.SailingCommandsVisitor import SailingCommandsVisitor
import pandas as pd
import datetime

group_cnt = 0
ingroup_cnt = 0
row_cnt = 0
df = pd.DataFrame({'COMMAND_GROUP_NR': [], 'INGROUP_NR': [], 'COMMAND': [], 'UNTIL':[]})


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


def insert_command_to_df(dataframe: pd.DataFrame, df_row: int, ingroup_number: int, command: str):
    new_row = {'COMMAND_GROUP_NR': '', 'INGROUP_NR': ingroup_number, 'COMMAND': command, 'UNTIL': ''}
    dataframe.loc[df_row] = new_row


class CommandVisitor(SailingCommandsVisitor):

    def visitSpeedCommand(self, ctx):
        global ingroup_cnt
        global df, row_cnt
        direction = ctx.direction().getText()
        amount = ctx.speed().getText()
        converted_amount = get_amount(amount)
        ingroup_cnt = ingroup_cnt + 1
        insert_command_to_df(df, row_cnt, ingroup_cnt,f'Silnik {converted_amount} {direction}')
        return f"\t{ingroup_cnt}. - Silnik {converted_amount} {direction}"

    def visitStereCommand(self, ctx):
        global ingroup_cnt
        global df, row_cnt
        stere = ctx.stere().getText()
        converted_stere = get_stere(stere)
        ingroup_cnt = ingroup_cnt + 1
        insert_command_to_df(df, row_cnt, ingroup_cnt,f'Przekręć ster o {converted_stere}')
        return f"\t{ingroup_cnt}. - Przekręć ster o {converted_stere}"

    def visitGroupCommand(self, ctx):
        global ingroup_cnt, group_cnt
        global df, row_cnt
        ingroup_cnt = 0
        group_cnt = group_cnt + 1
        new_row = {'COMMAND_GROUP_NR': group_cnt, 'INGROUP_NR': '', 'COMMAND': '', 'UNTIL': ''}
        df.loc[row_cnt] = new_row
        return f'\n{group_cnt}. - Nowy zestaw komend:'

    def visitTimeCommand(self, ctx):
        global ingroup_cnt
        global df, row_cnt
        commands = self.visitChildren(ctx)
        if commands:
            print(commands)
        time_command = ''

        if ctx.TO() is not None:
            landmark = ctx.landmarks().getText()
            ingroup_cnt = ingroup_cnt + 1
            time_command = f" - do {landmark}"

        elif ctx.BY() is not None:
            time_value = ctx.INT().getText() if ctx.INT() else ""
            time_unit = ctx.time_units().getText()

            time_command = f" - przez {time_value} {time_unit}"

        elif ctx.FOR_NEXT() is not None:
            time_value = ctx.INT().getText() if ctx.INT() else ''
            time_unit = ctx.time_units().getText()

            time_command = f" - na następne {time_value} {time_unit}"

        df.loc[row_cnt, 'UNTIL'] = time_command
        return time_command

    def visitCommand(self, ctx):
        global row_cnt
        command = ''
        if ctx.speedCommand():
            command += self.visitSpeedCommand(ctx.speedCommand())
        if ctx.stereCommand():
            command += self.visitStereCommand(ctx.stereCommand())
        if ctx.groupCommand():
            command += self.visitGroupCommand(ctx.groupCommand())
        if ctx.timeCommand():
            command += self.visitTimeCommand(ctx.timeCommand())
        row_cnt = row_cnt + 1
        return command


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
                commands = visitor.visitCommand(tree)
                print(commands)

                timestamp = datetime.datetime.now().strftime("%H_%M_%S-%d_%m_%Y")
                filename = f"output/commands_{timestamp}.csv"
                df.to_csv(filename, index=False, encoding="utf-8", sep=',')

    except FileNotFoundError:
        return Exception


if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
