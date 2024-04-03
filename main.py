class Interpreter:
  def __init__(self, name, program):
      self.name = name
      self.program = program
      self.cache = ''
      self.variables = {}

  def interpret(self):
      script = ''
      tokens = self.program.split('\n')

      for token in tokens:
          token = token.lstrip()
          if token.startswith('say'):
              self.print_statement(token)
              script += self.cache
              self.cache = ''
          elif token.startswith('at') and token.endswith(':'):
              self.at_statement(token)
          elif token.startswith('as') and token.endswith(':'):
              self.as_statement(token)
          elif token.startswith('set '):
              self.set_variable(token)
          else:
              print(f"ERROR {token}")

      with open(f'{self.name}.mcfunction', 'w') as f:
          f.write(script)

  def print_statement(self, statement):
      arguments = statement.split()[1:]
      if 'execute' in self.cache: self.cache += 'run '
      self.cache += 'say ' + ' '.join(arguments) + '\n'

  def at_statement(self, statement):
      arguments = statement[0:-1]
      arguments = arguments.split()[1:]
      if not self.cache: self.cache += 'execute '
      self.cache += 'at ' + arguments[0] + ' '

  def as_statement(self, statement):
      arguments = statement[0:-1]
      arguments = arguments.split()[1:]
      if not self.cache: self.cache += 'execute '
      self.cache += 'as ' + arguments[0] + ' '

  def set_variable(self, statement):
      parts = statement.split()
      variable_name = parts[1]
      value = int(parts[2])
      self.variables[variable_name] = value

def main():
  with open('main.mcf', 'r') as f:
      program = f.read()
  Interpreter('main', program).interpret()

if __name__ == "__main__":
  main()
