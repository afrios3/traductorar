from translate import Translator
import click

@click.command()
@click.argument('cadena_en')
def main(cadena_en):
  print(cadena_en)
if __name__ == '__main__':
  main()