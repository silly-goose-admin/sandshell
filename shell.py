from settings import *
from classes import *

commands=[
    ('clr', 'Clear the screen'),
    ('--help', 'Display this help page'),
    ('--version', 'Display the current version of the shell'),
    ('--update', 'Update the shell'),
    ('--exit', 'Exit the shell')
]

def help_page():
    print('Usage: [command] \n')
    print('Commands:')
    for cmd, desc in commands:
        print(f'  {cmd:<11} {desc}')

    print('For more information on a specific command, type:')
    print('  [command] --help\n')

    print('The shell is a work in progress. If you have any suggestions or')
    print('feedback, please send an email to the developer at: 51lly.g0o53a@gmail.com\n')
    print('Repo: https://github.com/silly-goose-admin/sandshell\n')

def get_input():
    return input(f'{user}@{host} ~\n$ ')

def main():
    cmd=get_input()
    if cmd=='--help':
        help_page()
        main()
    elif cmd=='clr':
        Shell.clear()
        main()
    elif cmd=='--version':
        print(f'Shell version {vers}\n')
        main()
    elif cmd=='--update':
        Shell.update()
    elif cmd=='--exit':
        Shell.close()
    else:
        print(f'Command not found: {cmd}')
        print('Type --help for a list of commands\n')
        main()

if __name__=='__main__':
    main()
