# PEP-8 Conventions

## Indentataion

- Use 4 spaces per indentation level.<br>
- Align with opening delimiter.

  ```Python
  foo = long_function_name(var_one, var_two,
  .........................var_three, var_four)
  ```

- More indentation is required to distinguish this from the rest.

  ```Python
  def long_function_name(
  ........var_one, var_two, var_three,
  ........var_four):
  ....print(var_one)
  )
  ```

- No extra indentation for <b>if</b>-statement if it is long enough to require multiple lines.

  ```Python
   if (this_is_one_thing and
   ....this_is_another_thing):
   ....do_something()
  ```

- The closing brace/bracket/parenthesis on multi-line construction may either line up under the first not-whitespace character or the last line of the list.

  ```Python
  my_list = [
  ....1, 2, 3,
  ....4, 5, 6,
  ....]
  ```

<br>

## Naming Convention

- Class should be in PascalCase

  ```Python
   class HelloWorld():
   ....Pass
  ```

- Function should be snake_case

  ```Python
  def hello_world():
  ....pass
  ```

<br>

## Comments

### Inline comments

- Inline comments are unnecessary and in fact distracting if the state the obvoius. So, don't do this

  ```Python
  x = x + 1..........# increment x
  ```

- But sometimes, this is useful

  ```Python
  x = x + 1 .......# compensate for border
  ```

### Documentation String

- Write documentation string for all public modules, funcion, classes, and methods.

  ```Python
  """Return a foobang

  Optional plotz says to frobincate the  bizbaz first.
  """
  ```

<br>

## Imports

- Yes

  ```Python
  import os
  import sys
  ```

- No

  ```Python
  import os, sys
  ```

- Imports should be grouped in following order.

  1. standard library imports.
  2. related third party imports.
  3. local application/ library specific imports
