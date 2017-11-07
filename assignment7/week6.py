import pronouncing

def generate_filename(filename):
  if "." not in filename:
    return filename + "_nonblank"
  # See https://stackoverflow.com/a/35844166/4587312
  return filename[::-1].replace(".", "_nonblank."[::-1], 1)[::-1]

def remove_empty(filename):
  new_filename = generate_filename(filename)
  blank_line_counter = 0
  with open(filename) as original_f:
    with open(new_filename, "w") as new_f:
      for line in original_f:
        if line.strip():
          new_f.write(line)
        else:
          blank_line_counter += 1
  print("Deleted {} blank lines.".format(blank_line_counter))

